# Running Keras models on iOS with Core ML
**URL:** https://www.pyimagesearch.com/2018/04/23/running-keras-models-on-ios-with-coreml
**Page Title:** Running Keras models on iOS with CoreML - PyImageSearch
--------------------

- Skip to primary navigation
- Skip to main content
- Skip to primary sidebar
- Skip to footer
Deep Learning Keras and TensorFlow Tutorials
by Adrian Rosebrock on April 23, 2018
In last week’s blog post, you learned how to train a Convolutional Neural Network (CNN) with Keras.
Today, we’re going to take this trained Keras model and deploy it to an iPhone and iOS app using what Apple has dubbed “CoreML”, an easy-to-use machine learning framework for Apple applications:
While not directly requiring a dataset, using real-world data when running Keras models on iOS with CoreML can help to test and showcase the deployed model’s capabilities in realistic scenarios.
Roboflow has free tools for each stage of the computer vision pipeline that will streamline your workflows and supercharge your productivity.
Sign up or Log in to your Roboflow account to access state of the art dataset libaries and revolutionize your computer vision pipeline.
You can start by choosing your own datasets or using our PyimageSearch’s assorted library of useful datasets .
Bring data in any of 40+ formats to Roboflow , train using any state-of-the-art model architectures, deploy across multiple platforms (API, NVIDIA, browser, iOS, etc), and connect to applications or 3rd party tools.
To recap, thus far in this three-part series, we have learned how to:
- (Quickly) create a deep learning image dataset
- Train a Keras + Convolutional Neural Network on our custom dataset
- Deploy our Keras model to an iPhone app with CoreML (this post)
My goal today is to show you how simple it is to deploy your Keras model to your iPhone and iOS using CoreML.
How simple you say?
To be clear, I’m not a mobile developer by any stretch of the imagination, and if I can do it, I’m confident you can do it as well.
Feel free to use the code in today’s post as a starting point for your own application.
But personally, I’m going to continue the theme of this series and build a Pokedex . A Pokedex is a device that exists in the world of Pokemon, a popular TV show, video game, and trading card series (I was/still am a huge Pokemon nerd).
Using a Pokedex you can take a picture of a Pokemon (animal-like creatures that exist in the world of Pokemon) and the Pokedex will automatically identify the creature for for you, providing useful information and statistics, such as the Pokemon’s height, weight, and any special abilities it may have.
You can see an example of a Pokedex in action at the top of this blog post, but again, feel free to swap out my Keras model for your own — the process is quite simple and straightforward as you’ll see later in this guide.
To learn how you can deploy a trained Keras model to iOS and build a deep learning iPhone app, just keep reading.

## Running Keras models on iOS with CoreML

Today’s blog post is broken down into four parts.
First, I’ll give some background on CoreML , including what it is and why we should use it when creating iPhone and iOS apps that utilize deep learning.
[LINK: CoreML](https://developer.apple.com/documentation/coreml)
From there, we’ll write a script to convert our trained Keras model from a HDF5 file to a serialized CoreML model — it’s an extremely easy process.
Next, we’ll create a Swift project in Xcode. This step is painless for those that know their way around Xcode, but for me I had to learn as I went along using resources online (I’m not a mobile expert and it’s been a long time since I’ve needed to use Xcode).
My hope is that I’ve provided you enough detail that you don’t need to pull up a search engine unless you’re modifying the code.
At some point you’ll likely want to register for the Apple Developer Program — I’ll squeeze this in just before we test the app on our iPhone.
Finally, we’ll compile the app and deploy the Keras model to our iPhone and iOS.

### What is CoreML and who is it for?

CoreML is a machine learning framework created by Apple with the goal of making machine learning app integration easy for anyone that wants to build a machine learning mobile app for iOS/iPhone.
CoreML supports Caffe, Keras, scikit-learn, and more.
For today, you just need a trained, serialized Keras model file to convert into a CoreML (Xcode compatible) file. This could be:
- Last week’s Keras Pokedex model
- Our deep learning Santa detector model from the holiday season
- Or a deep learning model you have already trained residing on your system
If you choose to use your own custom model you’ll want to check the CoreML documentation to ensure the layers utilized inside your network are supported.
[LINK: CoreML documentation](https://developer.apple.com/documentation/coreml/converting_trained_models_to_core_ml)
From there all you need is a few short lines of code to load the model and run inferences.
Apple’s CoreML development team really couldn’t have made it any easier and they deserve some well-earned praise. Great job to you all.

### I’m a computer vision + deep learning expert, not an app developer

I’ll be totally upfront and candid:
I’m not a mobile app developer (and I don’t claim to be).
Sure, I’ve built previous apps like ID My Pill and Chic Engine , but mobile development isn’t my strong suit or interest. In fact, those apps were created with PhoneGap / Cordova using HTML, JavaScript, and CSS without any Objective-C or Swift knowledge.
Instead, I’m a computer vision guy through and through. And when it comes to mobile apps, I lean heavily on easy-to-use frameworks such as PhoneGap/Cordova and (now) CoreML.
To learn the CoreML basics for this blog post, I gleaned this project from the knowledge of other expert developers on the web. Without them, I would be lost.
One app developer in particular, Mark Mansur, shared an excellent article on how to put together a deep learning + iOS app.
Much of today’s code is based on Mark’s post and project, with only a small modification or two. Thanks to Mark, this project is possible. Thanks Mark!

### Making a Keras model compatible with iOS with CoreML and Python

In this section, we’re going to make use of the pip-installable coremltools package .
[LINK: coremltools package](https://apple.github.io/coremltools/index.html)
To install coremltools coremltools , ensure you’re in a Python virtual environment with relevant libraries (we’re using Keras) and enter the following command:
From there, grab my converter script and associated files by scrolling down to the “Downloads” section of this blog post and downloading the code.
Once you’re ready, open coremlconverter.py coremlconverter.py and follow along:
Lines 2-5 import our required packages.
If you don’t have coremltools coremltools installed, be sure to refer above this code block for installation instructions.
Then we parse our command line arguments . We have two arguments:
- --model --model : The path to the pre-trained, serialized Keras model residing on disk.
- --labelbin --labelbin : The path to our class label binarizer. This file is a scikit-learn LabelBinarizer LabelBinarizer object from our previous post where we trained the CNN. If you do not have a LabelBinarizer LabelBinarizer object you will need to modify the code to hardcode the set of class_labels class_labels .
From there, let’s load the class labels and our Keras model:
On Lines 17-19 , we load our class label pickle file, and store the class_labels class_labels as a list.
Next, we load the trained Keras model on a single line ( Line 23 ).
From there, let’s call the converter from coremltools coremltools and save the resulting model to disk:
Beginning on Line 27 , we call the coremltools.converters.keras.convert coremltools.converters.keras.convert function. Be sure to refer to the docs for the keyword parameter explanations. We are utilizing the following parameters today:
- model model : The Keras model we are converting. You can actually just put a string path + filename here, but I elected to enter the model object — the API supports both methods.
[LINK: API](https://apple.github.io/coremltools/generated/coremltools.converters.keras.convert.html#coremltools.converters.keras.convert)
- input_names= "image" input_names="image" : Quoted from the docs : “Optional name(s) that can be given to the inputs of the Keras model. These names will be used in the interface of the Core ML models to refer to the inputs of the Keras model. If not provided, the Keras inputs are named to [input1, input2, …, inputN] in the Core ML model. When multiple inputs are present, the input feature names are in the same order as the Keras inputs.”
[LINK: from the docs](https://apple.github.io/coremltools/generated/coremltools.converters.keras.convert.html#coremltools.converters.keras.convert)
- image_input_names= "image" image_input_names="image" : Quoted from the docs : “Input names to the Keras model (a subset of the input_names parameter) that can be treated as images by Core ML. All other inputs are treated as MultiArrays (N-D Arrays).”
[LINK: from the docs](https://apple.github.io/coremltools/generated/coremltools.converters.keras.convert.html#coremltools.converters.keras.convert)
- image_scale= 1 / 255.0 image_scale=1/255.0 : This parameter is very important . It’s common practice to scale the pixel intensities of your images to [0, 1] prior to training your network. If you performed this type of scaling, be sure to set the image_scale image_scale parameter to the scale factor. Double and triple-check and scaling and preprocessing you may have done during training and ensure you reflect these preprocessing steps during the conversion process.
- class_labels=class_labels class_labels=class_labels : Here we supply the set of class labels our model was trained on. We obtained our class_labels class_labels from our LabelBinarizer LabelBinarizer object. You can also hardcode the class_labels class_labels if you wish.
- is_bgr= True is_bgr=True : This parameter is easy to overlook (I found out the hard way). If your model was trained with BGR color channel ordering, then it is important to set this value to True True so that CoreML operates as intended. If your model was trained with RGB images, you can safely ignore this parameter. If your images are not BGR or RGB, refer to the docs for further instruction.
I’d also like to point out that you can add red/green/blue/gray biases via the parameters if you’re performing mean subtraction on your query image from within your iPhone app. This is required for many ImageNet models, for example. Be sure to refer to the docs if you need to perform this step. Mean subtraction is a common pre-processing step covered in Deep Learning for Computer Vision with Python .
The last step on our script is to save the output CoreML protobuf model:
Xcode expects this file to have the extension .mlmodel .mlmodel . Therefore, I elected to handle this with code rather than a command line argument to avoid possible problems down the road.
Line 35 drops the .model .model extension from the input path/filename and replaces it with .mlmodel .mlmodel storing the result as output output .
From there, Line 37 saves the file to disk using the correct filename.
That’s all there is to this script. Thanks Apple CoreML developers!

### Running the Keras to CoreML conversion script

Our script can be executed by passing two command line arguments :
- The path to the model
- The path to the label binarizer.
Each of those files was created in last week’s blog post but are included in this week’s download as well.
Once you’re ready, enter the following command in your terminal and review the output as needed:
Then, list the contents of your directory:
…and you’ll see pokedex.mlmodel pokedex.mlmodel which can be imported right into Xcode (we’ll proceed to do this in the next section in Step 4 ). Interestingly, you can see that the file is smaller than the original Keras model which likely means CoreML stripped any optimizer state status during the conversion process.
Note: In an effort to allow for my Pokedex app to recognize when the camera is aimed at an “everyday object” and not a Pokemon (with a goal of eliminating false positives of our Pokemon friends), I added a class called “background”. I then retrained the model using the exact code from last week . The background class consisted of 250 images randomly sampled from the UKBench dataset residing on my system.

### Creating a Swift + CoreML deep learning project in Xcode

Step 0: Prepare your development environment
The zeroth step for this section is to download and install Xcode on your Macintosh computer. If your version of Xcode is not at least version 9.0 , then you’ll need to upgrade. At some point my Xcode insisted that I upgrade to version 9.3 to support my iPhone iOS 11.3.
Warning : Upgrading Xcode can break other development software + environments on your machine (such as a Python virtual environment with OpenCV installed). Proceed with caution or use a service such as MacInCloud so you do not break your local development environment.
Once you’ve installed/checked for the proper version of XCode, you’ll be ready to continue on.
Step 1: Create the project
For organization purposed, I opted to create a folder called xcode xcode in my home directory to house all of my Xcode projects. I created the following directory: ~/adrian/xcode ~/adrian/xcode .
From there, launch Xcode and create a “Single View App” as shown in Figure 3 .
Next, you can name your project whatever you’d like — I named mine “pokedex” as shown below.
Step 2: Kill off the storyboard
A storyboard is a view controller (think Model/View/Controller architecture). We’re going to get rid of the view controller for today’s simple app. Our view will be created programmatically instead.
Go ahead and delete Main.storyboard Main.storyboard from the file manager on the left as in Figure 5 .
Then, click the high level app name in the tree ( “pokedex ” in my case) and scroll to “Deployment info” . Erase the contents of the text box labeled “Main Interface”
Step 3: Add an element to info.plist
Our app accesses the camera, so we need to prepare an authorization message. This can easily be done in info.plist.
Click the “+” button as is shown in Figure 7 and add the Key + Value.  The Key must match exactly to “Privacy – Camera Usage Description”, but the value can be any message you’d like.
Step 4: Create the app window and root view controller
We still need a view even though we’ve gotten rid of the storyboard. For this step, you’ll want to copy and paste the following code into AppDelegate.swift AppDelegate.swift . The function is already defined — you just need to paste the body from below:
Step 5: Drag the CoreML model file into Xcode
Using Finder on your Mac, navigate to the CoreML .mlmodel .mlmodel file that you created above (or just grab my pokedex.mlmodel pokedex.mlmodel from the “Downloads” section of this blog post) .
Then, drag and drop it into the project tree. It will import automatically and create the relative Swift classes:
Step 6: Build the ViewController
Open ViewController.swift ViewController.swift and import our required packages/frameworks:
Lines 10-12 import three required packages for this project.
The UIKit UIKit package is a common framework for developing the view of an iOS application and allows for text, buttons, table views, and navigation.
The AVFoundation AVFoundation framework is for audiovisual media on iOS — we’ll employ it to capture from the camera.
We’re going to use the Vision Vision framework for our custom CoreML model classification, but the framework allows for much more than that. With the Vision framework, you can perform face detection, facial landmark detection, barcode recognition, feature tracking, and more.
Now that we’ve imported the relevant frameworks, let’s create the ViewController ViewController class and begin with a text label:
On Line 14 the ViewController ViewController class is defined while inheriting UIViewController UIViewController and AVCaptureVideoDataOutputSampleBufferDelegate AVCaptureVideoDataOutputSampleBufferDelegate . That’s a mouthful and really brings be back to my days of coding in Java!
In this class, we’re first going to define a UILabel UILabel which will hold our class label and associated probability percentage text. Lines 16-23 handle this step.
Next, we’re going to override the viewDidLoad viewDidLoad function:
The viewDidLoad viewDidLoad function is called after the view has been loaded. For view controllers created via code, this is after loadView loadView .
On Line 25 we use the override override keyword so that the compiler knows that we’re overriding the inherited class function.
Since we’re overriding the function, we need to call the super/parent function as is shown on Line 27 .
From there, we establish the capture session ( Line 30 ) followed by adding the label label as a subview ( Lines 31 and 32 ).
I’m including this next function as a matter of completeness; however, we’re not actually going to make any changes to it:
If you are experiencing memory warnings when testing your app, you can override override the didReceiveMemoryWarning didReceiveMemoryWarning function with additional actions. We’re going to leave this as-is and move on.
Let’s try to set up camera capture access using iOS and Swift:
Now remember — I’m not an expert at iOS development , but the codeblock above is relatively easy to follow.
First, we need to create a capture session ( Line 44 ) and query for a camera + check for any errors ( Lines 47-57 ).
From there, we output the feed to the screen in a previewLayer previewLayer ( Lines 60-64 ) and start the session ( Lines 67 and 68 ).
Let’s classify the frame and draw the label text on the screen:
Nothing magic is happening in this block — it may just be a little unfamiliar to Python developers.
We load the CoreML model on Line 73 .
Then, we classify a given frame and grab the results on Lines 76-79 . We can then grab the first predicted result from the CoreML model, storing it as an object named Observation Observation ( Line 82 ).
The predicted class label can be extracted via Observation. identifier Observation.identifier ( Line 85 ). We also format the confidence to show only two places past the decimal ( Line 86 ). We set the label label text with these two components ( Lines 89-91 ).
And finally, we establish a video pixel buffer and execute the request ( Lines 97-100 ).
We’ve reached the final function where we’ll establish a location on the screen for the label:
The two settings in setupLabel setupLabel speak for themselves — essentially we constrain the label to the bottom center.
Don’t forget the final bracket to mark the end of the ViewController class!
It’s easy to make minor syntax errors if you aren’t used to Swift, so be sure to use the “Downloads” section of this blog post to grab the entire project.

### Registering for the Apple Developer Program

In order to deploy the project to your iPhone, first enroll in the Apple Developer Program .
[LINK: Apple Developer Program](https://developer.apple.com/programs/enroll/)
After you’re enrolled, accept the certificates on your iPhone. I remember this being very easy somewhere in settings but I don’t recall where.
It is a nearly instant process to enroll, wait for Xcode and your iPhone to sync, and then accept certificates. I ended up paying the $100 but I later found out that it’s possible to create a free developer account via this blog post . Don’t make my mistake if you want to save some funds (and potentially use those extra funds to purchase a copy of Deep Learning for Computer Vision with Python ).
[LINK: this blog post](https://9to5mac.com/2016/03/27/how-to-create-free-apple-developer-account-sideload-apps/)

### Testing our Keras + CoreML deep learning app on the iPhone

Now we’re ready to compile and test our Keras + iOS/iPhone deep learning app!
I recommend first deploying your app via USB. From there if you want to share it with others, you could take advantage of TestFlight before publishing in the App Store.
[LINK: TestFlight](https://developer.apple.com/testflight/)
We’re going to use USB today.
First, plug in your iPhone to your Mac via USB. You likely have to unlock your iPhone with your pin and when iTunes prompts you to trust the device, you should.
From there, in the Xcode menubar, select Product > Destination > Adrian's iPhone Product > Destination > Adrian's iPhone .
Then to build and run all in one swoop, select Product > Run Product > Run . If you have any build errors, you’ll need to resolve them and try again.
If you are successful, the app will be installed and opened automatically on your iPhone.
At this point, you can go find Pokemon in the wild (playing cards, stuffed Pokemon, or action figures). A big shoutout to GameStop, Target, and Wal-mart where I caught some Pokemon critters. You might get lucky and find a whole box for a few bucks on CraigsList or eBay. If you don’t find any, then load some photos/illustrations on your computer and aim your iPhone at your screen.
Here’s my CoreML app in action:
To watch the full video on YouTube, just press play on the video here:
It’s definitely a simple app, but I’m quite proud that I have this on my phone to show my friends, fellow Pokemon nerds, and PyImageSearch readers.
I’d like to thank Mark Mansur for his inspiring, detailed this blog post which made today’s tutorial possible.
If I had had more time, I may have placed a button on the UI so that I could take snapshots of the Pokemon I encounter in the wild. I’ll leave this to the Swift + iOS experts — with practice and determination, it could be you!
Note: Screenshots are easy on iPhone/iOS. I assume you already know how to take them. If not, Google it. Screencast videos are relatively easy too. Just add the feature via Settings > Control Center > Customize Controls Settings > Control Center > Customize Controls and then go back to the app and swipe up from the bottom ( further details here ).
Compatibility Note: This app was tested with iOS 11.3 on an iPhone 6s, iPhone 7, and iPhone X. I used xCode 9.3 to build the app.

### What about Android? Does CoreML work on Android?

CoreML is an Apple toolkit and is meant only for iPhone, iOS, and other Apple applications. CoreML does not work on Android.
I do not have any experience developing Android apps and I’ve never used Android Studio.
I also do not have an Android phone.
But if there is enough interest in the comments section I will consider borrowing an Android phone from a friend and trying to deploy a Keras model to it.

### What's next? We recommend PyImageSearch University .

I strongly believe that if you had the right teacher you could master computer vision and deep learning.
Do you think learning computer vision and deep learning has to be time-consuming, overwhelming, and complicated? Or has to involve complex mathematics and equations? Or requires a degree in computer science?
That’s not the case.
All you need to master computer vision and deep learning is for someone to explain things to you in simple, intuitive terms. And that’s exactly what I do . My mission is to change education and how complex Artificial Intelligence topics are taught.
If you're serious about learning computer vision, your next stop should be PyImageSearch University, the most comprehensive computer vision, deep learning, and OpenCV course online today. Here you’ll learn how to successfully and confidently apply computer vision to your work, research, and projects. Join me in computer vision mastery.
Inside PyImageSearch University you'll find:
- ✓ 86+ courses on essential computer vision, deep learning, and OpenCV topics
- ✓ 86 Certificates of Completion
- ✓ 115+ hours hours of on-demand video
- ✓ Brand new courses released regularly , ensuring you can keep up with state-of-the-art techniques
- ✓ Pre-configured Jupyter Notebooks in Google Colab
- ✓ Run all code examples in your web browser — works on Windows, macOS, and Linux (no dev environment configuration required!)
- ✓ Access to centralized code repos for all 540+ tutorials on PyImageSearch
- ✓ Easy one-click downloads for code, datasets, pre-trained models, etc.
- ✓ Access on mobile, laptop, desktop, etc.
Click here to join PyImageSearch University

## Summary

In today’s blog post we saw that it’s incredibly easy to leverage the CoreML framework to take (trained) Keras models and deploy them to the iPhone and iOS.
I hope you see the value in Apple’s CoreML framework — it is quite impressive and a huge testament to the Apple developers and machine learning engineers for creating a tool that can ingest a deep neural network (that could be trained via a variety of popular deep learning libraries) and output a model that is nearly drag-and-drop compatible with the iPhone and iOS.
We used Swift for today’s iPhone app. While Swift isn’t as straightforward as Python (take that statement with a grain of salt because I’m a bit biased), given how easy CoreML is, you’ll be able to take this project and build your own, polished apps in no time.

## Now, I have a challenge for you.

I used Pokemon for this series of tutorials as it was one of my favorite childhood pastimes and brought back some wonderful nostalgic memories.
Now it’s your turn to let your imagination run wild.
What deep learning vision app would you like to build? Do you want to recognize the make and model of cars, build an animal species classifier, detect fruits and vegetables? Something else?
If so, you’ll want to start by taking a look at my book, Deep Learning for Computer Vision with Python .
Inside my book you will:
- Learn the foundations of machine learning and deep learning in an accessible manner that balances both theory and implementation
- Study advanced deep learning techniques , including object detection, multi-GPU training, transfer learning, and Generative Adversarial Networks (GANs)
- Replicate the results of state-of-the-art papers , including ResNet, SqueezeNet, VGGNet, and others on the 1.2 million ImageNet dataset
I have no doubt in my mind that you’ll be able to train your own custom deep neural networks using my book.
Be sure to take a look (and while you’re at it, don’t forget to grab your free table of contents + sample chapters PDF of the book).
From there, using both (1) your newly trained deep learning model and (2) today’s lesson, you can undoubtedly create a deep learning + Keras iPhone app and deploy it to the app store (and perhaps even make some money off the app as well, if you’re so inclined).
I’ll be back next week with a special bonus “part four” to this tutorial. I’m so excited about it that I might even drop some hints on Twitter leading up to Monday. Stay tuned!
Be sure that you don’t miss out on my next blog post (and more to come) by entering your email in the form below.
Enter your email address below to get a .zip of the code and a FREE 17-page Resource Guide on Computer Vision, OpenCV, and Deep Learning. Inside you'll find my hand-picked tutorials, books, courses, and libraries to help you master CV and DL!
Hi there, I’m Adrian Rosebrock, PhD. All too often I see developers, students, and researchers wasting their time, studying the wrong things, and generally struggling to get started with Computer Vision, Deep Learning, and OpenCV. I created this website to show you what I believe is the best possible way to get your start.

### Similar articles

### You can learn Computer Vision, Deep Learning, and OpenCV.

Get your FREE 17 page Computer Vision, OpenCV, and Deep Learning Resource Guide PDF. Inside you’ll find our hand-picked tutorials, books, courses, and libraries to help you master CV and DL.

## Footer

### Topics

- Deep Learning
- Dlib Library
- Embedded/IoT and Computer Vision
- Face Applications
- Image Processing
- Interviews
- Keras & Tensorflow
- OpenCV Install Guides
- Machine Learning and Computer Vision
- Medical Computer Vision
- Optical Character Recognition (OCR)
- Object Detection
- Object Tracking
- OpenCV Tutorials
- Raspberry Pi

### Books & Courses

- PyImageSearch University
- FREE CV, DL, and OpenCV Crash Course
- Practical Python and OpenCV
- Deep Learning for Computer Vision with Python
- PyImageSearch Gurus Course
- Raspberry Pi for Computer Vision

### PyImageSearch

- Affiliates
- Get Started
- About
- Consulting
- Coaching
- FAQ
- YouTube
- Blog
- Contact
- Privacy Policy

### Access the code to this tutorial and all other 500+ tutorials on PyImageSearch

Enter your email address below to learn more about PyImageSearch University (including how you can download the source code to this post):

### What's included in PyImageSearch University?

- Easy access to the code, datasets, and pre-trained models for all 500+ tutorials on the PyImageSearch blog
- High-quality, well documented source code with line-by-line explanations (ensuring you know exactly what the code is doing)
- Jupyter Notebooks that are pre-configured to run in Google Colab with a single click
- Run all code examples in your web browser — no dev environment configuration required!
- Support for all major operating systems (Windows, macOS, Linux, and Raspbian)
- Full access to PyImageSearch University courses
- Detailed video tutorials for every lesson
- Certificates of Completion for all courses
- New courses added every month! — stay on top of state-of-the-art trends in computer vision and deep learning
PyImageSearch University is really the best Computer Visions "Masters" Degree that I wish I had when starting out. Being able to access all of Adrian's tutorials in a single indexed page and being able to start playing around with the code without going through the nightmare of setting up everything is just amazing. 10/10 would recommend.

--------------------