/*
 * http://github.com/dusty-nv/jetson-inference
 */

#include "gstCamera.h"

#include "std_msgs/String.h"
#include "ros/ros.h"
#include "glDisplay.h"
#include "glTexture.h"

#include <stdio.h>
#include <signal.h>
#include <unistd.h>

#include "cudaNormalize.h"
#include "cudaFont.h"
#include "imageNet.h"


#define DEFAULT_CAMERA 1	// -1 for onboard camera, or change to index of /dev/video V4L2 camera (>=0)

using namespace std;

bool signal_recieved = false;

void sig_handler(int signo)
{
	if( signo == SIGINT )
	{
		printf("received SIGINT\n");
		signal_recieved = true;
	}
}


int main( int argc, char** argv )
{
	printf("imagenet-camera\n  args (%i):  ", argc);

	for( int i=0; i < argc; i++ )
		printf("%i [%s]  ", i, argv[i]);

	printf("\n\n");


	/*
	 * attach signal handler
	 */
	if( signal(SIGINT, sig_handler) == SIG_ERR )
		printf("\ncan't catch SIGINT\n");


	/*
	 * create the camera device
	 */
	gstCamera* camera = gstCamera::Create(DEFAULT_CAMERA);

	if( !camera )
	{
		printf("\nimagenet-camera:  failed to initialize video device\n");
		return 0;
	}

	printf("\nimagenet-camera:  successfully initialized video device\n");
	printf("    width:  %u\n", camera->GetWidth());
	printf("   height:  %u\n", camera->GetHeight());
	printf("    depth:  %u (bpp)\n\n", camera->GetPixelDepth());


	/*
	 * create imageNet
	 */

	//imageNet* net = imageNet::Create("networks/ItemNet2/deploy.prototxt", "networks/ItemNet2/snapshot_iter_31659.caffemodel", NULL, "networks/classes1.txt", "data", "softmax");
	imageNet* net = imageNet::Create("networks/ItemNetFinal/googlenet.prototxt", "networks/ItemNetFinal/model.caffemodel", NULL, "networks/ItemNetFinal/ilsvrc12_synset_words.txt");
	
	if( !net )
	{
		printf("imagenet-console:   failed to initialize imageNet\n");
		return 0;
	}


	/*
	 * create openGL window
	 */
	glDisplay* display = glDisplay::Create();
	glTexture* texture = NULL;

	if( !display ) {
		printf("\nimagenet-camera:  failed to create openGL display\n");
	}
	else
	{
		texture = glTexture::Create(camera->GetWidth(), camera->GetHeight(), GL_RGBA32F_ARB/*GL_RGBA8*/);

		if( !texture )
			printf("imagenet-camera:  failed to create openGL texture\n");
	}


	/*
	 * create font
	 */
	cudaFont* font = cudaFont::Create();


	/*
	 * start streaming
	 */
	if( !camera->Open() )
	{
		printf("\nimagenet-camera:  failed to open camera for streaming\n");
		return 0;
	}

	printf("\nimagenet-camera:  camera open for streaming\n");


	/*
	 * processing loop
	 */
	float confidence = 0.0f;
	bool lastFrameThere = false;
	string lastTaken = "";
	string last = "";
	ros::init(argc, argv, "imagenet");
	ros::NodeHandle n;	
	ros::Publisher chatter_pub = n.advertise<std_msgs::String>("item", 10);
	ros::Rate loop_rate(10);
	int count = 0;
	while( !signal_recieved )
	{
		void* imgCPU  = NULL;
		void* imgCUDA = NULL;

		// get the latest frame
		if( !camera->Capture(&imgCPU, &imgCUDA, 1000) )
			printf("\nimagenet-camera:  failed to capture frame\n");
		//else
		//	printf("imagenet-camera:  recieved new frame  CPU=0x%p  GPU=0x%p\n", imgCPU, imgCUDA);

		// convert from YUV to RGBA
		void* imgRGBA = NULL;

		if( !camera->ConvertRGBA(imgCUDA, &imgRGBA) )
			printf("imagenet-camera:  failed to convert from NV12 to RGBA\n");

		// classify image
		const int img_class = net->Classify((float*)imgRGBA, camera->GetWidth(), camera->GetHeight(), &confidence);
		string desc = net->GetClassDesc(img_class);
		if( img_class >= 0 )
		{
			if(count%30==0) {
				//printf("imagenet-camera:  %2.5f%% class #%i (%s)\n", confidence * 100.0f, img_class, net->GetClassDesc(img_class));
					//lastFrameThere = true;
					//last = desc;
				if((desc.compare("ballpoint, ballpoint pen, ballpen, Biro") == 0) || (desc.compare("notebook, notebook computer") == 0)
					|| (desc.compare("orange") == 0) || (desc.compare("laptop, laptop computer") == 0)
					|| (desc.compare("water bottle") == 0) || (desc.compare("Granny Smith") == 0)
					|| (desc.compare("fountain pen") == 0) || (desc.compare("quill, quill pen") == 0)
					|| (desc.compare("mouse, computer mouse") == 0) || (desc.compare("screwdriver") == 0)
					|| (desc.compare("screw") == 0)){
					printf("(%s) present\n", net->GetClassDesc(img_class));
					lastFrameThere = true;
					last = desc;
					std_msgs::String msg;
					std::stringstream ss;
					ss << net->GetClassDesc(img_class);
					ss << " 1";
					msg.data = ss.str();
					ROS_INFO("%s", msg.data.c_str());
					chatter_pub.publish(msg);
					ros::spinOnce();
					loop_rate.sleep();
	    				//chatter_pub.publish(net->GetClassDesc(img_class));


	   				//loop_rate.sleep();
				} else {
					lastFrameThere = false;
				}
				if (lastFrameThere == false) {
					lastTaken = last;
					printf("(%s) taken\n", lastTaken.c_str());
					std_msgs::String msg;
					std::stringstream ss;
					ss << lastTaken.c_str();
					ss << " 0";
					msg.data = ss.str();
					ROS_INFO("%s", msg.data.c_str());
					chatter_pub.publish(msg);
					ros::spinOnce();
					loop_rate.sleep();
				}

				if( font != NULL )
				{
					char str[256];
					sprintf(str, "%05.2f%% %s", confidence * 100.0f, net->GetClassDesc(img_class));

					font->RenderOverlay((float4*)imgRGBA, (float4*)imgRGBA, camera->GetWidth(), camera->GetHeight(),
									    str, 0, 0, make_float4(255.0f, 255.0f, 255.0f, 255.0f));
				}

				if( display != NULL )
				{
					char str[256];
					sprintf(str, "TensorRT build %x | %s | %s | %04.1f FPS", NV_GIE_VERSION, net->GetNetworkName(), net->HasFP16() ? "FP16" : "FP32", display->GetFPS());
					//sprintf(str, "TensorRT build %x | %s | %04.1f FPS | %05.2f%% %s", NV_GIE_VERSION, net->GetNetworkName(), display->GetFPS(), confidence * 100.0f, net->GetClassDesc(img_class));
					display->SetTitle(str);
				}
			}/* else {
				lastFrameThere = false;
				if (lastFrameThere == false) {
					lastTaken = last;
					printf("imagenet-camera: (%s) taken\n", lastTaken.c_str());
				}
			}*/


			// update display
			if( display != NULL )
			{
				display->UserEvents();
				display->BeginRender();

				if( texture != NULL )
				{
					// rescale image pixel intensities for display
					CUDA(cudaNormalizeRGBA((float4*)imgRGBA, make_float2(0.0f, 255.0f),
									   (float4*)imgRGBA, make_float2(0.0f, 1.0f),
			 						   camera->GetWidth(), camera->GetHeight()));

					// map from CUDA to openGL using GL interop
					void* tex_map = texture->MapCUDA();

					if( tex_map != NULL )
					{
						cudaMemcpy(tex_map, imgRGBA, texture->GetSize(), cudaMemcpyDeviceToDevice);
						texture->Unmap();
					}

					// draw the texture
					texture->Render(100,100);
				}

				display->EndRender();
			}
		}
	}

	printf("\nimagenet-camera:  un-initializing video device\n");


	/*
	 * shutdown the camera device
	 */
	if( camera != NULL )
	{
		delete camera;
		camera = NULL;
	}

	if( display != NULL )
	{
		delete display;
		display = NULL;
	}

	printf("imagenet-camera:  video device has been un-initialized.\n");
	printf("imagenet-camera:  this concludes the test of the video device.\n");
	return 0;
}
