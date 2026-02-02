# Office File API — Enhance Accessibility in Office Documents (Word & Excel) using OpenAI Models
**URL:** https://community.devexpress.com/blogs/office/archive/2024/05/08/enhance-accessibility-in-office-documents-word-and-excel-using-artificial-intelligence-system.aspx
**Page Title:** Office File API — Enhance Accessibility in Office Documents (Word & Excel) using OpenAI Models
--------------------


## Office File API — Enhance Accessibility in Office Documents (Word & Excel) using OpenAI Models

For accessibility-related reasons, certain business usage scenarios require that Office documents include meaningful descriptions/alternative text (Alt Text) for graphics content (images, charts, etc). Alt Text helps individuals with visual impairments to interpret pictures and other graphical content (screen readers cannot properly read documents that contain images without Alt Text). In addition, documents without Alt Text cannot be exported correctly as accessible PDFs (these PDFs fail accessibility validation).
The OpenAI platform offers a solution to address this particular requirement/issue (OpenAI's g enerative AI can help describe images and other graphical content within Word and Excel files). In this blog post, I'll show you how to integrate the OpenAI model into a DevExpress-powered Office File API application and add missing media descriptions and Alt Text. After processing documents, users can export files to accessible PDFs or upload them in a document viewer and read with a screen reader.
We created a sample project to help illustrate our strategy. This REST API application includes two endpoints: to describe images in Word documents and charts in Excel files. You can download this project from GitHub: Office File API – Integrate AI to Generate Accessible Descriptions
[LINK: Office File API – Integrate AI to Generate Accessible Descriptions](https://github.com/DevExpress-Examples/office-file-api-ai-implementation)

## Implement OpenAI Model API

Before you incorporate this solution in your app, please be sure to read and understand OpenAI's license agreement and terms of use.
To begin, add a reference to the Azure.AI.OpenAI package in your project. This package adapts OpenAI's REST APIs so they can be used in non-Azure OpenAI development. We will use this API to send requests and process responses.
The following code snippet sends a request to describe an image and obtain a string with a response.

### Word Processing Document API Endpoint

We can use the API described above within a DevExpress-powered Word Processing Document API application. Use the Document.Shapes collection to retrieve document images. Sort the retrieved shapes by type and check whether the image includes Alt Text. Then call the OpenAIClientImageHelper.GetImageDescription method implemented above to generate an image description.
[LINK: Document.Shapes](https://docs.devexpress.com/OfficeFileAPI/DevExpress.XtraRichEdit.API.Native.SubDocument.Shapes)

### Spreadsheet Document API Endpoint

You can also generate Alt Text for Excel Charts. Our project shows how to combine Azure OpenAI and Spreadsheet Document APIs to address this particular requirement. First, you'll need to convert Excel charts to images. Call the Shape.ExportToImage method to obtain the OfficeImage object from each chart. Then call the OpenAIClientImageHelper.GetImageDescription method implemented above to generate an image description and use it as Alt Text.
[LINK: Shape.ExportToImage](https://docs.devexpress.com/OfficeFileAPI/DevExpress.Spreadsheet.Shape.ExportToImage.overloads)
As always, your feedback is very important. Please let us know whether additional AI-related samples/solutions are of interest to you.

### This survey has expired

If you want to share your feedback or request new functionality, please submit a new support ticket via the DevExpress Support Center . We’ll be happy to follow up.

## Free DevExpress Products - Get Your Copy Today

- .NET App Security & Web API Service
[LINK: .NET App Security & Web API Service](https://www.devexpress.com/security-api-free?utm_source=DevExpress&utm_medium=Blog&utm_campaign=XAF&utm_content=footer)
- CodeRush for Visual Studio
- .NET ORM Library (XPO)
[LINK: API](https://community.devexpress.com/Tags/API)
[LINK: Excel Spreadsheet API](https://community.devexpress.com/Tags/Excel+Spreadsheet+API)
[LINK: Office File API](https://community.devexpress.com/Tags/Office+File+API)
[LINK: Rest API](https://community.devexpress.com/Tags/Rest+API)
[LINK: spreadsheet document api](https://community.devexpress.com/Tags/spreadsheet+document+api)

## Recent Posts

[LINK: File & Document Processing APIs (Office/PDF File APIs) — Year-End Roadmap (v25.2)](https://community.devexpress.com/Blogs/office/archive/2025/08/14/document-processing-libraries-office-file-api-november-2025-roadmap-v25-2.aspx)
[LINK: File & Document Processing APIs — New PowerPoint Presentation API Library](https://community.devexpress.com/Blogs/office/archive/2025/08/13/document-processing-new-powerpoint-presentation-api-library.aspx)
[LINK: Document Processing (Office File API) — Early Access Preview (v25.1) — Redaction API, Export Enhancements and More](https://community.devexpress.com/Blogs/office/archive/2025/04/25/document-processing-office-file-api-early-access-preview-v25-1-redaction-api-export-enhancements-and-more.aspx)
[LINK: Document Processing Libraries (Office File API) — June 2025 Roadmap (v25.1)](https://community.devexpress.com/Blogs/office/archive/2025/02/20/document-processing-libraries-office-file-api-june-2025-roadmap-v25-1.aspx)

## Privacy Preference Center

### Manage Consent Preferences

These cookies are necessary for the website to function properly and cannot be disabled. They are usually set in response to actions initiated by you – actions that amount to a request for services, such as setting your privacy preferences, logging onto the website, or populating website forms. You can set your browser to block or alert you about these cookies, but certain portions of the site will not work properly when these cookies are disabled. These cookies do not store any personally identifiable information.
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us understand page popularity and determine how visitors move around the site. All information collected by these cookies are aggregated and therefore anonymous. If you disallow/disable these cookies, we will not know when you have visited our site and we will not be able to monitor its performance.
These cookies allow the website to provide enhanced functionality and personalization. They may be set by us or by third party providers whose services we have added to our pages. If you disallow/disable these cookies, some or all of these services may fail to function properly.
These cookies may be set through our site by our advertising partners. They may be used by advertising partners to build a profile of your interests and display relevant advertisements on other sites. While these cookies do not store personal information, they do identify your browser and internet device. If you disallow/disable these cookies, you will experience less targeted advertising.

### Cookie List


--------------------