# https://docs.frigate.video/configuration/object\_detectors/
**URL:** https://docs.frigate.video/configuration/object_detectors
**Page Title:** Object Detectors | Frigate
--------------------

Frigate supports multiple different detectors that work on different types of hardware:
Most Hardware
- Coral EdgeTPU : The Google Coral EdgeTPU is available in USB and m.2 format allowing for a wide range of compatibility with devices.
- Hailo : The Hailo8 and Hailo8L AI Acceleration module is available in m.2 format with a HAT for RPi devices, offering a wide range of compatibility with devices.
AMD
- ROCm : ROCm can run on AMD Discrete GPUs to provide efficient object detection.
- ONNX : ROCm will automatically be detected and used as a detector in the -rocm Frigate image when a supported ONNX model is configured.
Intel
- OpenVino : OpenVino can run on Intel Arc GPUs, Intel integrated GPUs, and Intel CPUs to provide efficient object detection.
- ONNX : OpenVINO will automatically be detected and used as a detector in the default Frigate image when a supported ONNX model is configured.
Nvidia GPU
- ONNX : TensorRT will automatically be detected and used as a detector in the -tensorrt Frigate image when a supported ONNX model is configured.
Nvidia Jetson
- TensortRT : TensorRT can run on Jetson devices, using one of many default models.
- ONNX : TensorRT will automatically be detected and used as a detector in the -tensorrt-jp6 Frigate image when a supported ONNX model is configured.
Rockchip
- RKNN : RKNN models can run on Rockchip devices with included NPUs.
For Testing
- CPU Detector (not recommended for actual use : Use a CPU to run tflite model, this is not recommended and in most cases OpenVINO can be used in CPU mode with better results.
Multiple detectors can not be mixed for object detection (ex: OpenVINO and Coral EdgeTPU can not be used for object detection at the same time).
This does not affect using hardware for accelerating other tasks such as semantic search

## Officially Supported Detectors

Frigate provides the following builtin detector types: cpu , edgetpu , hailo8l , onnx , openvino , rknn , and tensorrt . By default, Frigate will use a single CPU detector. Other detectors may require additional configuration as described below. When using multiple detectors they will run in dedicated processes, but pull from a common queue of detection requests from across all cameras.

## Edge TPU Detector ​

The Edge TPU detector type runs a TensorFlow Lite model utilizing the Google Coral delegate for hardware acceleration. To configure an Edge TPU detector, set the "type" attribute to "edgetpu" .
The Edge TPU device can be specified using the "device" attribute according to the Documentation for the TensorFlow Lite Python API . If not set, the delegate will use the first device it finds.
[LINK: Documentation for the TensorFlow Lite Python API](https://coral.ai/docs/edgetpu/multiple-edgetpu/#using-the-tensorflow-lite-python-api)
A TensorFlow Lite model is provided in the container at /edgetpu_model.tflite and is used by this detector type by default. To provide your own model, bind mount the file into the container and provide the path with model.path .
See common Edge TPU troubleshooting steps if the Edge TPU is not detected.

### Single USB Coral ​

### Multiple USB Corals ​

### Native Coral (Dev Board) ​

warning: may have compatibility issues after v0.9.x
[LINK: compatibility issues](https://github.com/blakeblackshear/frigate/issues/1706)

### Single PCIE/M.2 Coral ​

### Multiple PCIE/M.2 Corals ​

### Mixing Corals ​

## Hailo-8 ​

This detector is available for use with both Hailo-8 and Hailo-8L AI Acceleration Modules. The integration automatically detects your hardware architecture via the Hailo CLI and selects the appropriate default model if no custom model is specified.
See the installation docs for information on configuring the Hailo hardware.

### Configuration ​

When configuring the Hailo detector, you have two options to specify the model: a local path or a URL .
If both are provided, the detector will first check for the model at the given local path. If the file is not found, it will download the model from the specified URL. The model file is cached under /config/model_cache/hailo .
Use this configuration for YOLO-based models. When no custom model path or URL is provided, the detector automatically downloads the default model based on the detected hardware:
- Hailo-8 hardware: Uses YOLOv6n (default: yolov6n.hef )
- Hailo-8L hardware: Uses YOLOv6n (default: yolov6n.hef )
For SSD-based models, provide either a model path or URL to your compiled SSD model. The integration will first check the local path before downloading if necessary.
The Hailo detector supports all YOLO models compiled for Hailo hardware that include post-processing. You can specify a custom URL or a local path to download or use your model directly. If both are provided, the detector checks the local path first.
For additional ready-to-use models, please visit: https://github.com/hailo-ai/hailo_model_zoo
[LINK: https://github.com/hailo-ai/hailo_model_zoo](https://github.com/hailo-ai/hailo_model_zoo)
Hailo8 supports all models in the Hailo Model Zoo that include HailoRT post-processing. You're welcome to choose any of these pre-configured models for your implementation.
Note: The config.path parameter can accept either a local file path or a URL ending with .hef. When provided, the detector will first check if the path is a local file path. If the file exists locally, it will use it directly. If the file is not found locally or if a URL was provided, it will attempt to download the model from the specified URL.

## OpenVINO Detector ​

The OpenVINO detector type runs an OpenVINO IR model on AMD and Intel CPUs, Intel GPUs and Intel VPU hardware. To configure an OpenVINO detector, set the "type" attribute to "openvino" .
The OpenVINO device to be used is specified using the "device" attribute according to the naming conventions in the Device Documentation . The most common devices are CPU and GPU . Currently, there is a known issue with using AUTO . For backwards compatibility, Frigate will attempt to use GPU if AUTO is set in your configuration.
[LINK: Device Documentation](https://docs.openvino.ai/2024/openvino-workflow/running-inference/inference-devices-and-modes.html)
OpenVINO is supported on 6th Gen Intel platforms (Skylake) and newer. It will also run on AMD CPUs despite having no official support for it. A supported Intel platform is required to use the GPU device with OpenVINO. For detailed system requirements, see OpenVINO System Requirements
[LINK: OpenVINO System Requirements](https://docs.openvino.ai/2024/about-openvino/release-notes-openvino/system-requirements.html)
When using many cameras one detector may not be enough to keep up. Multiple detectors can be defined assuming GPU resources are available. An example configuration would be:

### Supported Models ​

An OpenVINO model is provided in the container at /openvino-model/ssdlite_mobilenet_v2.xml and is used by this detector type by default. The model comes from Intel's Open Model Zoo SSDLite MobileNet V2 and is converted to an FP16 precision IR model.
[LINK: SSDLite MobileNet V2](https://github.com/openvinotoolkit/open_model_zoo/tree/master/models/public/ssdlite_mobilenet_v2)
Use the model configuration shown below when using the OpenVINO detector with the default OpenVINO model:
This detector also supports YOLOX. Frigate does not come with any YOLOX models preloaded, so you will need to supply your own models.
YOLO-NAS models are supported, but not included by default. See the models section for more information on downloading the YOLO-NAS model for use in Frigate.
[LINK: YOLO-NAS](https://github.com/Deci-AI/super-gradients/blob/master/YOLONAS.md)
After placing the downloaded onnx model in your config folder, you can use the following configuration:
Note that the labelmap uses a subset of the complete COCO label set that has only 80 objects.
YOLOv3, YOLOv4, YOLOv7, and YOLOv9 models are supported, but not included by default.
[LINK: YOLOv9](https://github.com/WongKinYiu/yolov9)
The YOLO detector has been designed to support YOLOv3, YOLOv4, YOLOv7, and YOLOv9 models, but may support other YOLO model architectures as well.
If you are using a Frigate+ YOLOv9 model, you should not define any of the below model parameters in your config except for path . See the Frigate+ model docs for more information on setting up your model.
After placing the downloaded onnx model in your config folder, you can use the following configuration:
Note that the labelmap uses a subset of the complete COCO label set that has only 80 objects.
RF-DETR is a DETR based model. The ONNX exported models are supported, but not included by default. See the models section for more informatoin on downloading the RF-DETR model for use in Frigate.
[LINK: RF-DETR](https://github.com/roboflow/rf-detr)
Due to the size and complexity of the RF-DETR model, it is only recommended to be run with discrete Arc Graphics Cards.
After placing the downloaded onnx model in your config/model_cache folder, you can use the following configuration:
D-FINE is a DETR based model. The ONNX exported models are supported, but not included by default. See the models section for more information on downloading the D-FINE model for use in Frigate.
[LINK: D-FINE](https://github.com/Peterande/D-FINE)
Currently D-FINE models only run on OpenVINO in CPU mode, GPUs currently fail to compile the model
After placing the downloaded onnx model in your config/model_cache folder, you can use the following configuration:
Note that the labelmap uses a subset of the complete COCO label set that has only 80 objects.

## AMD/ROCm GPU detector ​

### Setup ​

Support for AMD GPUs is provided using the ONNX detector . In order to utilize the AMD GPU for object detection use a frigate docker image with -rocm suffix, for example ghcr.io/blakeblackshear/frigate:stable-rocm .

### Docker settings for GPU access ​

ROCm needs access to the /dev/kfd and /dev/dri devices. When docker or frigate is not run under root then also video (and possibly render and ssl/_ssl ) groups should be added.
When running docker directly the following flags should be added for device access:
When using Docker Compose:
For reference on recommended settings see running ROCm/pytorch in Docker .
[LINK: running ROCm/pytorch in Docker](https://rocm.docs.amd.com/projects/install-on-linux/en/develop/how-to/3rd-party/pytorch-install.html#using-docker-with-pytorch-pre-installed)

### Docker settings for overriding the GPU chipset ​

Your GPU might work just fine without any special configuration but in many cases they need manual settings. AMD/ROCm software stack comes with a limited set of GPU drivers and for newer or missing models you will have to override the chipset version to an older/generic version to get things working.
Also AMD/ROCm does not "officially" support integrated GPUs. It still does work with most of them just fine but requires special settings. One has to configure the HSA_OVERRIDE_GFX_VERSION environment variable. See the ROCm bug report for context and examples.
[LINK: ROCm bug report](https://github.com/ROCm/ROCm/issues/1743)
For the rocm frigate build there is some automatic detection:
- gfx1031 -> 10.3.0
- gfx1103 -> 11.0.0
If you have something else you might need to override the HSA_OVERRIDE_GFX_VERSION at Docker launch. Suppose the version you want is 10.0.0 , then you should configure it from command line as:
When using Docker Compose:
Figuring out what version you need can be complicated as you can't tell the chipset name and driver from the AMD brand name.
- first make sure that rocm environment is running properly by running /opt/rocm/bin/rocminfo in the frigate container -- it should list both the CPU and the GPU with their properties
- find the chipset version you have (gfxNNN) from the output of the rocminfo (see below)
- use a search engine to query what HSA_OVERRIDE_GFX_VERSION you need for the given gfx name ("gfxNNN ROCm HSA_OVERRIDE_GFX_VERSION")
- override the HSA_OVERRIDE_GFX_VERSION with relevant value
- if things are not working check the frigate docker logs
We unset the HSA_OVERRIDE_GFX_VERSION to prevent an existing override from messing up the result:

### Supported Models ​

See ONNX supported models for supported models, there are some caveats:
- D-FINE models are not supported
- YOLO-NAS models are known to not run well on integrated GPUs

## ONNX ​

ONNX is an open format for building machine learning models, Frigate supports running ONNX models on CPU, OpenVINO, ROCm, and TensorRT. On startup Frigate will automatically try to use a GPU if one is available.
If the correct build is used for your GPU then the GPU will be detected and used automatically.
- AMD ROCm will automatically be detected and used with the ONNX detector in the -rocm Frigate image.
AMD
- ROCm will automatically be detected and used with the ONNX detector in the -rocm Frigate image.
- Intel OpenVINO will automatically be detected and used with the ONNX detector in the default Frigate image.
Intel
- OpenVINO will automatically be detected and used with the ONNX detector in the default Frigate image.
- Nvidia Nvidia GPUs will automatically be detected and used with the ONNX detector in the -tensorrt Frigate image. Jetson devices will automatically be detected and used with the ONNX detector in the -tensorrt-jp6 Frigate image.
Nvidia
- Nvidia GPUs will automatically be detected and used with the ONNX detector in the -tensorrt Frigate image.
- Jetson devices will automatically be detected and used with the ONNX detector in the -tensorrt-jp6 Frigate image.
When using many cameras one detector may not be enough to keep up. Multiple detectors can be defined assuming GPU resources are available. An example configuration would be:

### Supported Models ​

There is no default model provided, the following formats are supported:
YOLO-NAS models are supported, but not included by default. See the models section for more information on downloading the YOLO-NAS model for use in Frigate.
[LINK: YOLO-NAS](https://github.com/Deci-AI/super-gradients/blob/master/YOLONAS.md)
If you are using a Frigate+ YOLO-NAS model, you should not define any of the below model parameters in your config except for path . See the Frigate+ model docs for more information on setting up your model.
After placing the downloaded onnx model in your config folder, you can use the following configuration:
YOLOv3, YOLOv4, YOLOv7, and YOLOv9 models are supported, but not included by default.
[LINK: YOLOv9](https://github.com/WongKinYiu/yolov9)
The YOLO detector has been designed to support YOLOv3, YOLOv4, YOLOv7, and YOLOv9 models, but may support other YOLO model architectures as well. See the models section for more information on downloading YOLO models for use in Frigate.
If you are using a Frigate+ YOLOv9 model, you should not define any of the below model parameters in your config except for path . See the Frigate+ model docs for more information on setting up your model.
After placing the downloaded onnx model in your config folder, you can use the following configuration:
Note that the labelmap uses a subset of the complete COCO label set that has only 80 objects.
YOLOx models are supported, but not included by default. See the models section for more information on downloading the YOLOx model for use in Frigate.
[LINK: YOLOx](https://github.com/Megvii-BaseDetection/YOLOX)
After placing the downloaded onnx model in your config folder, you can use the following configuration:
Note that the labelmap uses a subset of the complete COCO label set that has only 80 objects.
RF-DETR is a DETR based model. The ONNX exported models are supported, but not included by default. See the models section for more information on downloading the RF-DETR model for use in Frigate.
[LINK: RF-DETR](https://github.com/roboflow/rf-detr)
After placing the downloaded onnx model in your config/model_cache folder, you can use the following configuration:
D-FINE is a DETR based model. The ONNX exported models are supported, but not included by default. See the models section for more information on downloading the D-FINE model for use in Frigate.
[LINK: D-FINE](https://github.com/Peterande/D-FINE)
After placing the downloaded onnx model in your config/model_cache folder, you can use the following configuration:
Note that the labelmap uses a subset of the complete COCO label set that has only 80 objects.

## CPU Detector (not recommended) ​

The CPU detector type runs a TensorFlow Lite model utilizing the CPU without hardware acceleration. It is recommended to use a hardware accelerated detector type instead for better performance. To configure a CPU based detector, set the "type" attribute to "cpu" .
The CPU detector is not recommended for general use. If you do not have GPU or Edge TPU hardware, using the OpenVINO Detector in CPU mode is often more efficient than using the CPU detector.
The number of threads used by the interpreter can be specified using the "num_threads" attribute, and defaults to 3.
A TensorFlow Lite model is provided in the container at /cpu_model.tflite and is used by this detector type by default. To provide your own model, bind mount the file into the container and provide the path with model.path .
When using CPU detectors, you can add one CPU detector per camera. Adding more detectors than the number of cameras should not improve performance.

## Deepstack / CodeProject.AI Server Detector ​

The Deepstack / CodeProject.AI Server detector for Frigate allows you to integrate Deepstack and CodeProject.AI object detection capabilities into Frigate. CodeProject.AI and DeepStack are open-source AI platforms that can be run on various devices such as the Raspberry Pi, Nvidia Jetson, and other compatible hardware. It is important to note that the integration is performed over the network, so the inference times may not be as fast as native Frigate detectors, but it still provides an efficient and reliable solution for object detection and tracking.

### Setup ​

To get started with CodeProject.AI, visit their official website to follow the instructions to download and install the AI server on your preferred device. Detailed setup instructions for CodeProject.AI are outside the scope of the Frigate documentation.
To integrate CodeProject.AI into Frigate, you'll need to make the following changes to your Frigate configuration file:
Replace <your_codeproject_ai_server_ip> and <port> with the IP address and port of your CodeProject.AI server.
To verify that the integration is working correctly, start Frigate and observe the logs for any error messages related to CodeProject.AI. Additionally, you can check the Frigate web interface to see if the objects detected by CodeProject.AI are being displayed and tracked properly.

## Community Supported Detectors

## NVidia TensorRT Detector ​

Nvidia Jetson devices may be used for object detection using the TensorRT libraries. Due to the size of the additional libraries, this detector is only provided in images with the -tensorrt-jp6 tag suffix, e.g. ghcr.io/blakeblackshear/frigate:stable-tensorrt-jp6 . This detector is designed to work with Yolo models for object detection.

### Generate Models ​

The model used for TensorRT must be preprocessed on the same hardware platform that they will run on. This means that each user must run additional setup to generate a model file for the TensorRT library. A script is included that will build several common models.
The Frigate image will generate model files during startup if the specified model is not found. Processed models are stored in the /config/model_cache folder. Typically the /config path is mapped to a directory on the host already and the model_cache does not need to be mapped separately unless the user wants to store it in a different location on the host.
By default, no models will be generated, but this can be overridden by specifying the YOLO_MODELS environment variable in Docker. One or more models may be listed in a comma-separated format, and each one will be generated. Models will only be generated if the corresponding {model}.trt file is not present in the model_cache folder, so you can force a model to be regenerated by deleting it from your Frigate data folder.
If you have a Jetson device with DLAs (Xavier or Orin), you can generate a model that will run on the DLA by appending -dla to your model name, e.g. specify YOLO_MODELS=yolov7-320-dla . The model will run on DLA0 (Frigate does not currently support DLA1). DLA-incompatible layers will fall back to running on the GPU.
If your GPU does not support FP16 operations, you can pass the environment variable USE_FP16=False to disable it.
Specific models can be selected by passing an environment variable to the docker run command or in your docker-compose.yml file. Use the form -e YOLO_MODELS=yolov4-416,yolov4-tiny-416 to select one or more model names. The models available are shown below.
An example docker-compose.yml fragment that converts the yolov4-608 and yolov7x-640 models would look something like this:

### Configuration Parameters ​

The TensorRT detector can be selected by specifying tensorrt as the model type. The GPU will need to be passed through to the docker container using the same methods described in the Hardware Acceleration section. If you pass through multiple GPUs, you can select which GPU is used for a detector with the device configuration parameter. The device parameter is an integer value of the GPU index, as shown by nvidia-smi within the container.
The TensorRT detector uses .trt model files that are located in /config/model_cache/tensorrt by default. These model path and dimensions used will depend on which model you have generated.
Use the config below to work with generated TRT models:

## Rockchip platform ​

Hardware accelerated object detection is supported on the following SoCs:
- RK3562
- RK3566
- RK3568
- RK3576
- RK3588
This implementation uses the Rockchip's RKNN-Toolkit2 , version v2.3.2.
[LINK: Rockchip's RKNN-Toolkit2](https://github.com/airockchip/rknn-toolkit2/)
When using many cameras one detector may not be enough to keep up. Multiple detectors can be defined assuming NPU resources are available. An example configuration would be:

### Prerequisites ​

Make sure to follow the Rockchip specific installation instructions .
You can get the load of your NPU with the following command:

### Supported Models ​

This config.yml shows all relevant options to configure the detector and explains them. All values shown are the default values (except for two). Lines that are required at least to use the detector are labeled as required, all other lines are optional.
The inference time was determined on a rk3588 with 3 NPU cores.
- All models are automatically downloaded and stored in the folder config/model_cache/rknn_cache . After upgrading Frigate, you should remove older models to free up space.
- You can also provide your own .rknn model. You should not save your own models in the rknn_cache folder, store them directly in the model_cache folder or another subfolder. To convert a model to .rknn format see the rknn-toolkit2 (requires a x86 machine). Note, that there is only post-processing for the supported models.
The pre-trained YOLO-NAS weights from DeciAI are subject to their license and can't be used commercially. For more information, see: https://docs.deci.ai/super-gradients/latest/LICENSE.YOLONAS.html
[LINK: https://docs.deci.ai/super-gradients/latest/LICENSE.YOLONAS.html](https://docs.deci.ai/super-gradients/latest/LICENSE.YOLONAS.html)

### Converting your own onnx model to rknn format ​

To convert a onnx model to the rknn format using the rknn-toolkit2 you have to:
[LINK: rknn-toolkit2](https://github.com/airockchip/rknn-toolkit2/)
- Place one ore more models in onnx format in the directory config/model_cache/rknn_cache/onnx on your docker host (this might require sudo privileges).
- Save the configuration file under config/conv2rknn.yaml (see below for details).
- Run docker exec <frigate_container_id> python3 /opt/conv2rknn.py . If the conversion was successful, the rknn models will be placed in config/model_cache/rknn_cache .
This is an example configuration file that you need to adjust to your specific onnx model:
Explanation of the paramters:
- soc : A list of all SoCs you want to build the rknn model for. If you don't specify this parameter, the script tries to find out your SoC and builds the rknn model for this one.
- quantization : true: 8 bit integer (i8) quantization, false: 16 bit float (fp16). Default: false.
- output_name : The output name of the model. The following variables are available: quant : "i8" or "fp16" depending on the config input_basename : the basename of the input model (e.g. "my_model" if the input model is calles "my_model.onnx") soc : the SoC this model was build for (e.g. "rk3588") tk_version : Version of rknn-toolkit2 (e.g. "2.3.0") example : Specifying output_name = "frigate-{quant}-{input_basename}-{soc}-v{tk_version}" could result in a model called frigate-i8-my_model-rk3588-v2.3.0.rknn .
- quant : "i8" or "fp16" depending on the config
- input_basename : the basename of the input model (e.g. "my_model" if the input model is calles "my_model.onnx")
- soc : the SoC this model was build for (e.g. "rk3588")
- tk_version : Version of rknn-toolkit2 (e.g. "2.3.0")
- example : Specifying output_name = "frigate-{quant}-{input_basename}-{soc}-v{tk_version}" could result in a model called frigate-i8-my_model-rk3588-v2.3.0.rknn .
- config : Configuration passed to rknn-toolkit2 for model conversion. For an explanation of all available parameters have a look at section "2.2. Model configuration" of this manual .
[LINK: this manual](https://github.com/MarcA711/rknn-toolkit2/releases/download/v2.3.2/03_Rockchip_RKNPU_API_Reference_RKNN_Toolkit2_V2.3.2_EN.pdf)

## Models

Some model types are not included in Frigate by default.

## Downloading Models ​

Here are some tips for getting different model types

### Downloading D-FINE Model ​

D-FINE can be exported as ONNX by running the command below. You can copy and paste the whole thing to your terminal and execute, altering MODEL_SIZE=s in the first line to s , m , or l size.

### Downloading RF-DETR Model ​

RF-DETR can be exported as ONNX by running the command below. You can copy and paste the whole thing to your terminal and execute, altering MODEL_SIZE=Nano in the first line to Nano , Small , or Medium size.

### Downloading YOLO-NAS Model ​

You can build and download a compatible model with pre-trained weights using this notebook which can be run directly in Google Colab .
[LINK: this notebook](https://github.com/blakeblackshear/frigate/blob/dev/notebooks/YOLO_NAS_Pretrained_Export.ipynb)
[LINK: Google Colab](https://colab.research.google.com/github/blakeblackshear/frigate/blob/dev/notebooks/YOLO_NAS_Pretrained_Export.ipynb)
The pre-trained YOLO-NAS weights from DeciAI are subject to their license and can't be used commercially. For more information, see: https://docs.deci.ai/super-gradients/latest/LICENSE.YOLONAS.html
[LINK: https://docs.deci.ai/super-gradients/latest/LICENSE.YOLONAS.html](https://docs.deci.ai/super-gradients/latest/LICENSE.YOLONAS.html)
The input image size in this notebook is set to 320x320. This results in lower CPU usage and faster inference times without impacting performance in most cases due to the way Frigate crops video frames to areas of interest before running detection. The notebook and config can be updated to 640x640 if desired.

### Downloading YOLO Models ​

YOLOx models can be downloaded from the YOLOx repo .
[LINK: from the YOLOx repo](https://github.com/Megvii-BaseDetection/YOLOX/tree/main/demo/ONNXRuntime)
To export as ONNX:
YOLOv9 model can be exported as ONNX using the command below. You can copy and paste the whole thing to your terminal and execute, altering MODEL_SIZE=t and IMG_SIZE=320 in the first line to the model size you would like to convert (available model sizes are t , s , m , c , and e , common image sizes are 320 and 640 ).
[LINK: model size](https://github.com/WongKinYiu/yolov9#performance)
- Edge TPU Detector Single USB Coral Multiple USB Corals Native Coral (Dev Board) Single PCIE/M.2 Coral Multiple PCIE/M.2 Corals Mixing Corals
- Single USB Coral
- Multiple USB Corals
- Native Coral (Dev Board)
- Single PCIE/M.2 Coral
- Multiple PCIE/M.2 Corals
- Mixing Corals
- Hailo-8 Configuration
- Configuration
- OpenVINO Detector Supported Models
- Supported Models
- AMD/ROCm GPU detector Setup Docker settings for GPU access Docker settings for overriding the GPU chipset Supported Models
- Setup
- Docker settings for GPU access
- Docker settings for overriding the GPU chipset
- Supported Models
- ONNX Supported Models
- Supported Models
- CPU Detector (not recommended)
- Deepstack / CodeProject.AI Server Detector Setup
- Setup
- NVidia TensorRT Detector Generate Models Configuration Parameters
- Generate Models
- Configuration Parameters
- Rockchip platform Prerequisites Supported Models Converting your own onnx model to rknn format
- Prerequisites
- Supported Models
- Converting your own onnx model to rknn format
- Downloading Models Downloading D-FINE Model Downloading RF-DETR Model Downloading YOLO-NAS Model Downloading YOLO Models
- Downloading D-FINE Model
- Downloading RF-DETR Model
- Downloading YOLO-NAS Model
- Downloading YOLO Models

--------------------