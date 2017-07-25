#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "jetson-inference" for configuration ""
set_property(TARGET jetson-inference APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(jetson-inference PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_NOCONFIG "/usr/local/cuda-8.0/lib64/libcudart_static.a;-lpthread;dl;/usr/lib/aarch64-linux-gnu/librt.so;nvcaffe_parser;nvinfer;Qt4::QtGui;GL;GLEW;gstreamer-1.0;gstapp-1.0"
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/jetson-inference/libjetson-inference.so"
  IMPORTED_SONAME_NOCONFIG "libjetson-inference.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS jetson-inference )
list(APPEND _IMPORT_CHECK_FILES_FOR_jetson-inference "${_IMPORT_PREFIX}/lib/jetson-inference/libjetson-inference.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
