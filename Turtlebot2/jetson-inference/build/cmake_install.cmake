# Install script for directory: /home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/detectNet.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/tensorNet.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/imageNet.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/loadImage.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/commandLine.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/camera/gstUtility.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/camera/v4l2Camera.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/camera/gstCamera.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/cuda/cudaFont.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/cuda/cudaUtility.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/cuda/cudaNormalize.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/cuda/cudaMappedMemory.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/cuda/cudaResize.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/cuda/cudaYUV.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/cuda/cudaRGB.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/cuda/cudaOverlay.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/display/glTexture.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/display/glDisplay.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/jetson-inference" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/util/display/glUtility.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/jetson-inference/libjetson-inference.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/jetson-inference/libjetson-inference.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/jetson-inference/libjetson-inference.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/jetson-inference" TYPE SHARED_LIBRARY FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/build/aarch64/lib/libjetson-inference.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/jetson-inference/libjetson-inference.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/jetson-inference/libjetson-inference.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/jetson-inference/libjetson-inference.so")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/jetson-inference/cmake/jetson-inferenceConfig.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/jetson-inference/cmake/jetson-inferenceConfig.cmake"
         "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/build/CMakeFiles/Export/share/jetson-inference/cmake/jetson-inferenceConfig.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/jetson-inference/cmake/jetson-inferenceConfig-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/jetson-inference/cmake/jetson-inferenceConfig.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/jetson-inference/cmake" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/build/CMakeFiles/Export/share/jetson-inference/cmake/jetson-inferenceConfig.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/jetson-inference/cmake" TYPE FILE FILES "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/build/CMakeFiles/Export/share/jetson-inference/cmake/jetson-inferenceConfig-noconfig.cmake")
  endif()
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/build/detectnet-camera/cmake_install.cmake")
  include("/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/build/imagenet-camera/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/nvidia/catkin_ws/src/beginner_tutorials/Electron/ItemDetect/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
