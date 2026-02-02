# Building a pet monitoring app in Android with machine learning
**URL:** https://medium.freecodecamp.org/a-guide-to-object-detection-with-fritz-build-a-pet-monitoring-app-in-android-with-machine-learning-a8ed500978e5
**Page Title:** A guide to Object Detection with Fritz: Build a pet monitoring app in Android with machine learning
--------------------

Learn to code — free 3,000-hour curriculum
By Eric Hsiao
Whether it is detecting plant damage for farmers , tracking vehicles on the road, or monitoring your pets — the applications for object detection are endless. With the rise of mobile frameworks like TensorFlow Lite and Core ML, more and more mobile apps leverage the power of machine learning to create features that leave us in awe.
In plain English, object detection identifies and locates specific items in an image or live video with a bounding box.
The middle one is a poodle dressed up as Toothless for Halloween
But creating features powered by machine learning isn’t easy. Many engineering teams cannot justify the time and resources. You need the right in-house expertise to collect data, train a model, and iterate on the performance and accuracy. Understandably, with pressure from product teams to deliver value quickly for end-users, potential features are tossed aside in a backlog abyss.
In this post, I’ll show you how any Android developer can use real-time object detection to create an app that detects and recognizes pets — all in less than 30 minutes. To do this, I’ll use the Fritz SDK (full disclosure, I work at Fritz) which makes it easier to leverage machine learning capabilities without any prior experience.

### Getting started

To start using the Fritz SDK, we’ll go through adding the necessary dependencies in a sample app that we’ve created.
Sign up here and follow the get started directions .
[LINK: get started directions](https://docs.fritz.ai/get-started.html?utm_source=medium&utm_campaign=freecodecamp)
Set up a skeleton app that includes a video feed and camera code. In this tutorial, we won’t go depth into the Camera 2 API , but if you have any questions, please leave a comment.
[LINK: Camera 2 API](https://developer.android.com/reference/android/hardware/camera2/package-summary)
You need to register your app with Fritz in order to use ML-features. When you’re adding the app to Fritz, use the same applicationId (ai.fritz.camera) as the app/build.gradle.
In your app/build.gradle, notice the applicationId field
The package ID must match the applicationId shown above for your application. In this case, the package id is ai.fritz.camera
Make sure you note the API Key for Step 5. If you need to access it again, you can go to Project Settings > Your App (Pet Monitor)> Show API Key (in the options menu).
Make sure to add the Fritz repository. This will allow you to download the necessary dependencies:
In the dependencies section, add these 2 libraries:
Call Fritz.configure in the Application or MainActivity onCreate lifecycle method with the API key you got in Step 3.
With that, you’re ready to use object detection in your app.

### Detecting dogs & cats on live video

Now let’s get to the fun stuff. We’ll jump into the MainActivity and use the object detection predictor on each frame passed in on the video stream.
The predictor takes in a FritzVisionImage and returns a list of FritzVisionObjects detected.
Use either fromBitmap or fromMediaImage static methods to create an object from a Bitmap or media.Image object. For the sample app, use fromMediaImage , which also takes in the rotation applied on the image from the camera.
The rotation depends on the device rotation and the camera orientation sensor. The cameraId identifies the active camera being used on the device (front, back, etc.), and you can get the rotation angle with the following helper method.
Finally, create a FritzVisionImage object with the Image and rotation value.
Pass the image into the predictor to detect different objects in the image.
Each FritzVisionObject comes with a label, a confidence score, and a bounding box that shows where it’s located on the original image. In this case, we only care about pets (specifically cats and dogs), so we can filter out the other items.
Finally, display the bounding boxes around your pets. FritzVisionObject has a convenient method called drawOnCanvas which makes it easy to display the detected objects.
Here’s the complete code after the render callback:
Notice the scale factor on the boxes. This is because the media.Image object we used to create the FritzVisionImage object is the same size as the preview viewport. In the camera sample app, it’s 1280 x 960. The bounding boxes will have coordinates associated with the preview size. Since we want to show this on the full screen, we need to scale the result to the phone’s viewport.
Here’s the final result:
For the finished code, take a look at the GitHub repo .
[LINK: GitHub repo](https://github.com/fritzlabs/pet-monitor-android)

### Why this is useful

With the machine learning feature behind this basic app, there are ton of different features you can create (both practical and goofy):
- Alert the owners with a text message if the dog walker hasn’t returned.
- Record a message telling your dog to “Sit down!” when they’re running around the room with no one around. I bet you could capture funny photos of your dog in this moment, too.
- Show the user a message when a cat / dog is detected (take a look at the completed code for an example)
- Sound an alarm when the camera detects cats (I’m allergic).
Of course, not many people have a spare Android tablet / phone that they can use as an expensive pet monitoring camera, but this is just a simple example among many different possibilities for how you might create an app with object detection using Fritz . I can’t wait to see what all the creative developers of the world build using object detection.
[LINK: object detection](https://docs.fritz.ai/features/object-detection/about.html?utm_source=medium&utm_campaign=freecodecamp)
Got an idea? Leave a comment!
I’m a lead developer at Fritz specializing in mobile machine learning. If you’re looking to create features powered by AI/ML, we offer prebuilt APIs ( image segmentation , image labeling , style transfer ) and custom model support.
[LINK: image segmentation](https://docs.fritz.ai/features/image-segmentation/about.html?utm_source=medium&utm_campaign=freecodecamp)
[LINK: image labeling](https://docs.fritz.ai/features/image-labeling/about.html?utm_source=medium&utm_campaign=freecodecamp)
[LINK: style transfer](https://docs.fritz.ai/features/style-transfer/about.html?utm_source=medium&utm_campaign=freecodecamp)
[LINK: custom model](https://docs.fritz.ai/custom-models/overview.html?utm_source=medium&utm_campaign=freecodecamp)
If you read this far, thank the author to show them you care.
Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. Get started

--------------------