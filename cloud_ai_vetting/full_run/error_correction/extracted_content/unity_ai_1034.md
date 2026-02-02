# Unity AI
**URL:** https://unity.com/ai
**Page Title:** Unity AI: AI Game Development Tools & RT3D Software | Unity
--------------------


## Unity AI

- Key benefits
- FAQ

## See Unity AI in action

## Contextual awareness

## Data controls

## Curated models

## Easily audit your assets

Get quick, focused help with your GameObjects, scripts, Prefabs, and more–just drop them into Assistant without having to spell out every detail.

## Locate, modify, and organize in bulk

Automate repetitive tasks in-editor, like locating lights over a set intensity or objects missing Rigidbodies, and update names, layers, or components all at once.

## Debug console errors

Ask Assistant to explain scripts or error messages directly in the Editor to better understand and resolve issues.

## Learn Unity development

Get thorough explanations and step-by-step setup guidance for complex Unity features or concepts (like Colliders or VFX Graphs) directly in the Editor.

## Quickly set up scenes

Use plain language commands to generate objects, place assets, and automate scene setup.

## Generate placeholder assets

Create sprites, textures, animations, and sounds directly in Unity—properly formatted, no extra setup or context switching required. Plus, trace their use for replacement when going to production.

## Generate code

Generate new scripts or optimize existing ones directly in your project, automating C# boilerplate and repetitive tasks to free up your focus on problem solving.

## Frequently asked questions

### What is Unity AI?

Unity AI is a suite of AI tools and capabilities that are integrated directly into the Unity Editor. Muse and Sentis will be sunset, and their functionality will be incorporated into Unity AI which provides improved features, better integration with the Unity Editor, more flexible pricing, and more choice in AI models. A few of the new features include pre-compiled code generation, running agentic actions, and new generative asset types.

### Can I use Unity AI on my existing project while it’s in beta?

Unity AI packages are in a “pre-release” state in our continued open beta. As a reminder, per our terms of service related to evaluation versions , you may only try Unity AI in test projects, and not in production projects until it becomes generally available.

### What features are in Unity AI?

Unity AI has three main components:
- Assistant : Assistant replaces Muse Chat as a contextual helper in Unity. It can answer questions about your project and guide you through implementing new features more productively. Project assets can be dragged to your prompt to provide heightened context to the Assistant. Assistant can also generate pre-compiled code and execute agentic actions like resolving console errors, batch renaming multiple files, creating NPC variants, placing a large number of objects in a scene. Assistant will consume Unity Points, which you can read about below.
[LINK: Assistant](https://docs.unity3d.com/Packages/com.unity.ai.assistant@1.0/manual/index.html?ampDeviceId=d47430d6-d46e-4e7c-8d6a-815bf191ba80&ampSessionId=1769962416793&ampTimestamp=1770048832974)
- Generators : Generators replace all Muse asset generation features: Animate, Sprite, and Texture. Generators are better integrated into Unity Editor workflows and inspectors and include both Unity’s own first-party AI models and third-party models (models developed and hosted independently from Unity) via APIs. Notably, we added new higher quality generative models for Sprites, introduced a video prompt to the Animation generator, and added generative Sound as a new generative asset type. Post-processing effects are available to refine generated asset styles, such as sound envelope editing, sprite background removal, pixelation, upscaling, recolor, texture map settings, animation looping, and more. The Generators will consume Unity Points (see below FAQ: How much will Unity AI cost?).
[LINK: Generators](https://docs.unity3d.com/Packages/com.unity.ai.generators@1.0/manual/index.html?ampDeviceId=d47430d6-d46e-4e7c-8d6a-815bf191ba80&ampSessionId=1769962416793&ampTimestamp=1770048832974)
- Inference Engine : Inference Engine replaces Sentis. This is a simple name change as we wanted something that fits better with existing Unity Editor naming conventions. Inference Engine continues to focus on local AI model inference performance gains for unique runtime experiences. We have built an API upgrade path for users upgrading from Sentis to Inference Engine that is simple to implement. Hugging Face models are still available here . Local inference remains free and will not consume Unity Points.
[LINK: Inference Engine](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.2/manual/index.html?ampDeviceId=d47430d6-d46e-4e7c-8d6a-815bf191ba80&ampSessionId=1769962416793&ampTimestamp=1770048832974)
[LINK: API upgrade path](https://docs.unity3d.com/Packages/com.unity.ai.inference@latest/manual/upgrade-guide.html?ampDeviceId=d47430d6-d46e-4e7c-8d6a-815bf191ba80&ampSessionId=1769962416793&ampTimestamp=1770048832974)

### How do I get access to Unity AI?

When you download the Unity 6.2 beta, you will see a new “AI” button persistent at the top of the Editor window for easy installation and access to Unity AI. During the beta period, all users who install Unity 6.2 and choose to install the Unity AI features (packages) will receive free Unity Points to try the features. Unity AI will enter GA (general availability) along with Unity 6.2 later this year. The free points will expire at the end of the beta, and paid Unity Points will be required going forward.

### What are the system requirements for Unity AI?

- You must install Unity 6.2.
- You must agree and accept the terms on the AI button in the Unity Editor, and install the AI packages.
- Your project must be linked to a Unity Cloud project per the documentation .
[LINK: documentation](https://docs.unity3d.com/6000.2/Documentation/Manual/ai-menu.html?ampDeviceId=d47430d6-d46e-4e7c-8d6a-815bf191ba80&ampSessionId=1769962416793&ampTimestamp=1770048832974)

### How much will Unity AI cost?

During the Unity 6.2 beta, Unity AI is free for all users. When Unity 6.2 enters GA (general availability), we will introduce Unity Points which can be used for various AI actions within the Assistant and Generators. Unity Points will be included in Unity Pro, Unity Enterprise, and Unity Industry plans. All users will also be able to purchase Unity Points bundles separately. Pricing will be available when Unity 6.2 enters GA.

### What is happening to Muse?

Muse will be sunset shortly after Unity 6.2 enters GA (general availability). Muse will remain available for users through the Unity 6.2 beta period.

### As a current Muse user what do these changes mean for me?

You can continue to use Muse until Unity 6.2 enters GA (general availability) later this year. After that, your monthly subscription will not renew and your credit card will not be charged. You will lose access to create new Muse generations and chats once your monthly subscription automatically ends. You can cancel your Muse subscription any time before then.
You will have access to Muse Chat history and local Muse asset generated assets (ie. Sprites, Textures, Animations) as long as you keep the Muse packages installed, but will lose them if you uninstall the Muse packages. All Muse generated assets that are imported in the project will remain in your project. There is no migration of Muse points, assets, or user data to Unity AI.

### Do terms for Unity Muse apply to Unity AI?

No. Unity Muse and Unity AI are separate offerings with distinct approaches and terms. Unity Muse uses only first-party AI models developed and trained by Unity, and its terms and usage policies are specific to that product. Unity AI, on the other hand, provides access to third-party generative models via API, which are developed and maintained by external partners. Unity AI terms will be published when the product becomes generally available, and Unity’s Terms of Service apply while the product remains in beta.
Unity continues to provide in-product safeguards, asset traceability tools, and opt-out controls to help developers manage content responsibly across both Muse and Unity AI.

### What is happening to Sentis?

Sentis remains the engine for running models within the Unity Runtime to improve performance and create unique experiences. You can find more information in the documentation .
[LINK: documentation](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.4/manual/index.html?ampDeviceId=d47430d6-d46e-4e7c-8d6a-815bf191ba80&ampSessionId=1769962416793&ampTimestamp=1770048832974)

### What models does Unity AI use?

You can find the full list of AI models on our Models and Partners page .

### How are AI-generated assets managed in my project?

All generated assets and scripts will contain metadata (i.e. EXIF data) that states “This asset was generated with AI”, making it easy to manage and search in your project. It is your responsibility to determine the appropriate AI-based declarations to make with app stores, distribution platforms, and end-users when you ship a commercial project that has used generative AI.
Additionally, as with any imported asset, you should always verify that you have the rights to use generated content in your final build.

### How does Unity AI use my data?

By default, data related to your use of Unity AI including prompts, responses, and interactions are only used to provide you with the service, and are not used to train AI models. For example, if you upload a reference image to generate a truck sprite, we do not use your source image to train or improve the generative image model.
Via your Unity Dashboard, you can choose to share your Unity AI data with us for model training purposes. We do not use your runtime application (the binary itself) or media assets such as your images, meshes, or audio to improve Unity AI.
Learn more here about Unity’s Developer Data Framework.
[LINK: here](https://docs.unity.com/en-us/cloud/developer-data-framework)

### What if I have more questions?

Check out our dedicated Unity AI Discussions page or contact Unity Support .

## Privacy Preference Center

## Privacy Preference Center

- Your Privacy

### Your Privacy

- Functional Cookies

### Functional Cookies

- Performance Cookies

### Performance Cookies

- Targeting Cookies

### Targeting Cookies

- Strictly Necessary Cookies

### Strictly Necessary Cookies

When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. More information
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising. Some 3rd party video providers do not allow video views without targeting cookies. If you are experiencing difficulty viewing a video, you will need to set your cookie preferences for targeting to yes if you wish to view videos from these providers. Unity does not control this.
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

### Cookie List

- checkbox label label

--------------------