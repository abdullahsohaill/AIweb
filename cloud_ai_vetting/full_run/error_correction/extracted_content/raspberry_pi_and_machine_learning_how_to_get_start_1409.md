# Raspberry Pi and machine learning: How to get started
**URL:** https://www.techrepublic.com/article/raspberry-pi-and-machine-learning-how-to-get-started
**Page Title:** Raspberry Pi and machine learning: How to get started - TechRepublic
--------------------


## Account Information

If you want to dabble with machine learning on the $35 Raspberry Pi you’ve never had more options.
Google offers several kits for carrying out speech and image recognition on the Pi and is readying a USB stick that will turbo charge the Pi’s machine-learning capabilities .
The tech giant recently boosted the Pi’s machine-learning credentials even further by officially supporting its machine learning software framework TensorFlow on the board .
If you want to get started with machine learning on the Pi, here’s everything you need to know.

### How to get started?

Google’s Artificial Intelligence Yourself (AIY) kits provide a great introduction to machine learning on the Pi.
You can choose between two kits, allowing you to experiment with either speech or image recognition . The kits includes all the hardware you need — the cameras, microphones etc — and detailed tutorials on how to set up the Pi.
While the voice AIY kit offloads speech recognition to Google Cloud, the vision AIY kit actually performs the image recognition on the board, albeit with the aid of an Intel Movidius AI accelerator.
Once you’ve completed the tutorials, there are other trained machine-learning models you can run on the Pi and AIY kits, including face/dog/cat/human detectors and a general-purpose image classifier.

### What other options are available?

Those with more machine learning experience can install Google’s TensorFlow software library on the Pi, a process that recently got much easier .
TensorFlow is a software framework used to build machine-learning models, and is used for a wide range of deep learning tasks, such as image and speech recognition.
To install TensorFlow on the Pi follow these instructions , and then follow the tutorials under the Learn and use ML section on this page , which detail how to train and test models for simple text and image classification.
One fact worth bearing in mind is that the Pi’s modest specs will constrain its performance.

### What are the limits of the Pi when it comes to machine learning?

Although the relatively low-specced Pi isn’t an obvious choice for machine learning, the board’s compact size and low power consumption mean it’s well suited to building mobile homemade gadgets and robots. Machine learning can help these devices handle new tasks, using image recognition to “see” and speech recognition to “hear”. However, there are definite limits to the Pi’s ML capabilities.
There are two main stages to machine learning, training, during which the model learns how to perform a given task, and inference, when the trained model is used to perform that task.
The Pi’s limited processing power means it’s not suitable for training anything but the simplest machine-learning models. Instead this stage is typically carried on a machine with at least a mid- to high-end GPU.
However, the Pi is capable of performing inference, of actually running the trained machine learning model, albeit rather slowly.
In one test, the Pi’s estimated performance when using image recognition to spot cars in dashcam footage was about 1 – 4 frames per second , obviously far slower than real time. And while Google’s AIY vision kit runs trained models on the Pi , it does so using an AI accelerator.
These constraints are why computer vision tasks on the Pi are often handled using the OpenCV software library, which uses non-ML techniques that perform better on the Pi.

### How can I improve machine learning performance on the Pi?

If you’re running up against the limits of what the Pi can do there are add-ons that accelerate the Pi’s ability to run trained machine-learning models.
Intel’s Movidius Compute Stick boosts the rate at which the Pi carries out vision-related tasks such as facial and object recognition, using its 12-core Myriad 2 Vision Processing Unit.
The $79 USB stick is capable of 100 gigaflops (one thousand-million, floating-point operations per second) and consumes a single watt, although the power draw occasionally rises to 2.5W. Rough estimates of performance online say the stick’s VPU can do 10 inferences per second using a GoogLeNet convolutional neural network, a machine-learning model commonly used for image recognition. That’s compared to about 2 inferences per second using Google’s Inception convolutional neural network architecture on an unaided Raspberry Pi.
You can see the sort of performance boost the Movidius Stick gives the Pi in this video of an accelerated Pi carrying out real-time identification of vehicles .
Google has also revealed its own USB stick that it says will dramatically accelerate the rate at which the Pi runs trained machine-learning models.
Google’s says the Edge TPU Accelerator will allow devices to run multiple state-of-the-art computer vision models on high-resolution video at more than 30 frames per second .
That level of performance would be far beyond what an unaided Pi is capable of, and seemingly above the levels of performance reported using Intel’s Movidius Neural Compute Stick .
[LINK: levels of performance reported using Intel’s Movidius Neural Compute Stick](https://movidius.github.io/blog/ncs-rpi3-mobilenets/)
The device is due out this fall, and those interested can sign up to be notified about its release .

### What are people doing with machine learning on the Pi?

There are various examples, such as this automated cucumber sorter used at a Japanese cucumber farm through to this AI train spotter .

### Subscribe to the Daily Tech Insider Newsletter

Stay up to date on the latest in technology with Daily Tech Insider. We bring you news on industry-leading companies, products, and people, as well as highlighted articles, downloads, and top resources. You’ll receive primers on hot tech topics that will help you stay ahead of the game. Delivered Weekdays
- Account Information Share with Your Friends Raspberry Pi and machine learning: How to get started

## Account Information

## Share with Your Friends

Raspberry Pi and machine learning: How to get started

### Subscribe to the Daily Tech Insider Newsletter

Stay up to date on the latest in technology with Daily Tech Insider. We bring you news on industry-leading companies, products, and people, as well as highlighted articles, downloads, and top resources. You’ll receive primers on hot tech topics that will help you stay ahead of the game. Delivered Weekdays

--------------------