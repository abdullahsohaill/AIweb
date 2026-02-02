# Playing with Artificial Intelligence in the browser using TensorFlow
**URL:** https://www.coforge.com/resource-library/white-papers/playing-with-artificial-intelligence-in-the-browser-using-tensorflow-part-2
**Page Title:** Playing with Artificial Intelligence in the browser using TensorFlow (Part 2) | Coforge
--------------------


## Playing with Artificial Intelligence in the browser using TensorFlow (Part 2)

Artificial intelligence (AI) is rapidly transforming our world, from the call centers we call to the chatbots we interact with on websites. AI is already having a significant impact on our daily lives, whether we're shopping, studying, or working.
Technological advancements are supporting the growth of AI production. Large-scale research is making computer technology cheaper and more efficient, and access to more powerful hardware is making it easier and more affordable to train and develop AI systems. As a result, more sophisticated AI systems are being developed to solve increasingly complex problems.
AI is basically machine software that imitates human intelligence. AI based programs can see, read and understand pictures, text, video, emotion, audio. It can also smell, touch, move after it has been developed using various algorithms and machine learning modules. Machine learning is an artificial intelligence-based method for creating intelligent computer systems. Artificial intelligence and machine learning technologies are also used in self-driving cars, medical care, forensics, and also other industries like education, internet security, business, supply chain, and logistics.
This blog provides a comprehensive overview of how we use artificial intelligence in our daily lives, even though we may not be aware of it. It also explores how AI is likely to change our future in dramatic ways.
The outcome of this blog is a single-page web application where we can experience how artificial intelligence works in the browser (e.g object detection and image classification). To develop this web app popular deep neural networks that are trained with large-scale data sets, single shot multibox detector, and other important tools like HTML, CSS, Javascript, React, TensorFlow.js, ML5.js were used.

## What are the different technologies used?

This section contains a description of all the technologies used during the process of making the web application.
- HTML HyperText Markup Language which is also called HTML is a markup language for documents that are expected to be displayed in a web browser. It makes use of tags to describe an element that can be used to organize data in a particular format, retaining the data's original form.
- CSS CSS is a design sheet language for constructing the visual display and configure of a document written in a markup language like HTML, XML, or other markup languages. CSS is commonly used to design a web page's layout, colors, fonts, border, padding, and margin of HTML elements.
- Javascript One of the most common scripting languages for web pages is JavaScript, also known as ECMA Script. It is a first-class object-oriented language that's lightweight and interpreted. In a web development project, it’s very easy to use for multifunctionality features. It can be used in the frontend architecture as well as the backend to manage server-side operations.
- React React which is also known as Reactjs, is an open-source library based on javascript that is very useful for building a web application's interactive UI (user interface). It enables the development of reusable user interface components so that components can be reused without having to rewrite the code. React uses JSX, which is an XML-like language to construct an element for a component.
- TensorFlow.js Initially, running machine learning in the browser was incredibly difficult. This was due to some factors, including the need for hosting on cloud servers, the developer's expertise with programming languages like Python, and the high cost of hardware components. As Tensorflow.js was added, this changed. TensorFlow.js is a fully accessible library that uses JavaScript and a high-level layer API to describe, train, and run various ML models exclusively in the browser.
- ML5.js ML5.js is a JavaScript library that is developed on top of TensorFlow.js and provides browser-based access to algorithms, tasks, and models of Machine learning. Machine Learning in the browser eliminates the need to obtain libraries or other resources from the perspective of the end-user. Users must visit a website before the application can run and It also ensures that this technology can be used on a mobile device if there any browser available. Finally, all data remains on the front-end, which makes it less afflicted to latency problems and also ensures privacy and protection.

## How to develop a Web Application using TensorFlow.js?

This part of the blog covers the entire web application development process, conceptualizing the architecture of the web app and from coding to deployment.
Implementation: The project's goal was to create a single-page web app that could classify objects based on their category and make segmentation of an image. Many of the tools were downloaded prior to the actual implementation. The used text editor for this project was VSCode (Visual Studio). This is a small and powerful source code editor that runs on a PC and all major operating systems supported (Windows, Linux, and Mac OS). VSCode editor has integrated support for JavaScript and receives extra features for React, making it ideal for this application. GitBash was used as the primary terminal and it's a Windows framework that offers work flexibility. During the development process, the development server was also run using GitBash.
Figure 1. Screenshot for importing libraries
Line 1 is for loading react to the document file, line 2 is for loading the coco-ssd model. This model detects objects defined in the COCO dataset. Line 3 load TensorFlow.js (Figure 1).
Figure 2. Screenshot for video and canvas reference
Create references for video and canvas. This is to be able to manipulate the video and the canvas which is responsible for showing the information from the webcam to the webpage (Figure 2).
Figure 3. Screenshot for componentDidMount
componentDidMount is a feature called after a component has been assembled (inserted into the tree). This is where we can put any initialization that includes DOM nodes. This is a good place to start a network request from a remote endpoint if data need to be loaded. This lifecycle is used to load the webcam and start the stream in this case (Figure 3).
Figure 4. Screenshot for componentWillUnmont
componentWillUnmount is a function invoked immediately before a component is unmounted and destroyed. We perform this lifecycle for cleaning up any subscriptions that were created in componentDidMount(). In this case, we need to destroy the detectFrame so it doesn't run all the time (Figure 4).
Figure 5. Screenshot for detectFrame
This function is responsible for making predictions based on what the webcam/camera is seeing. It compares it to the coco-SSD model to make predictions (Figure 5).
Figure 6. Screenshot for package.json
Every npm package includes a package file, which is typically located in the project root. JSON file contains various project-related metadata. It is used to provide information to npm so that it can define the project and manage its requirements (Figure 6).
Figure 7. Screenshot for renderPredictions
This function creates a box for the detected object and shows the prediction based on the model (Figure 7).
Figure 8. Screenshot for CSS
Styling the object detection class and canvas, which are CSS code (Figure 8).
Figure 9. Screenshot for classifyImg
ml5.imageClassifier() is a method for creating an object that uses a pre-trained model to identify the content of an image. It's worth noting that the example uses a pre-trained model that was trained on a database of around 15 million images. The cloud model is accessed using the ml5 library. What is included, omitted, and how those images are labeled or mislabeled, are all entirely dependent on the training data (Figure 9).
Figure10. Screenshot of image recognition
The Image Classification part can be seen in the screenshot above (Figure 10). The user can upload a picture from their device to the web app, and the application will predict the object in the image they uploaded. It analyzes images only in the browser and does not save them in the archive. This page showcases image classification in the web app that highlighted browser-based deep learning (or ML) where MobileNet and ImageNet were used which are CNN and image dataset respectively.
Figure 11. Screenshot of object detection
The screenshot in Figure 11 shown is browser-based machine learning which can detect objects using the COCO-SSD model.

## Author

## Alin Bhattacharyya

Alin Bhattacharyya is a certified Enterprise Architect, heading the Omnichannel Practice and working as "Associate Vice President" in Coforge. He has over 20 years of experience in Software Engineering, Web and Mobile Application Development, Product Development, Architecture Design, Media Analysis, AI\ML and Technology Management. His vast experience in Designing Solutions, creating Accelerators using Artificial Intelligence, Client Interactions, Onsite-Offshore Model Management, Research & Development and developing POC’s in new technologies allow him to have a well-rounded perspective of the industry.

## Cookies Policy

This site uses cookies to enhance your browsing experience, show you personalized content, and help us improve our website. Some cookies are essential for the site to function; others help us understand how you use the site. Click 'Allow all' to accept all cookies, or 'Cookie settings' to manage your preferences. For more details, click on "Learn More"
Learn more

--------------------