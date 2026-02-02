# FactSet Developer Portal | Developer
**URL:** https://developer.factset.com/api-catalog/natural-language-processing-api
**Page Title:** Natural Language Processing API | FactSet Developer
--------------------


## Natural Language Processing API

- SECTIONS
- Overview
- API Definition
- API Documentation
- Code Snippet
- Changelog
- Sample Use Case
The Natural Language Processing API is a collection of services that analyze and add value to unstructured text.  These APIs leverage Artificial Intelligence, Machine Learning, Deep Learning, Natural Language Processing, and Natural Language Generation techniques.

### AI Text Summarization

The AI Text Summarization service takes text as an input and returns a computer-generated summary that represents the most important information in the original content.

### AI Themes

The AI Themes service identifies significant concepts in unstructured text.  AI Themes can be used to quickly understand the contents of a document, as a first step in determining the sentiment of a document, or to discover when new ideas emerge. Every theme is paired with a numeric value to indicate its significance within the document, and can additionally be paired with a sentiment score.

### Named Entity Recognition

The FactSet NER (Named Entity Recognition) service identifies companies, people, locations, health conditions, drug names, numbers, monetary values, and dates from unstructured or semi-structured documents. In addition to providing the text and type of the entity names, along with their start and end offsets in the document, this service also provides the best matching FactSet identifiers for companies and people found in the text. This unique FactSet identifier allows you to link any document with other FactSet content sets, such as historical prices or fundamental data.

### Question & Answer

The Question & Answer API is a machine learning service that provides the ability to ask questions about the information contained in text documents. The service will return answer(s) based on the information contained in the text.
[LINK: Download Spec](//assets.ctfassets.net/lmz2w5z92b9u/11kBh8sKon5fgDCf8ZnSSl/b0b44b11b48996bb8f9829aa941406dd/natural_language_processing_api-v1.yaml)

## Natural Language Processing API 1.3.0 OAS 3.0

[LINK: //assets.ctfassets.net/lmz2w5z92b9u/11kBh8sKon5fgDCf8ZnSSl/b0b44b11b48996bb8f9829aa941406dd/natural_language_processing_api-v1.yaml](https://assets.ctfassets.net/lmz2w5z92b9u/11kBh8sKon5fgDCf8ZnSSl/b0b44b11b48996bb8f9829aa941406dd/natural_language_processing_api-v1.yaml)
APIs that leverage Natural Language Processing to help extract meaningful data from unstructured text
[LINK: FactSet Research Systems - Website](https://developer.factset.com/contact)
[LINK: Send email to FactSet Research Systems](mailto:api@factset.com)

### AI Text Summarization

### AI Themes

### Named Entity Recognition

### Question & Answer

- AI Themes.pdf 449.27 KB
- AI Text Summarization.pdf 432.20 KB
- Named Entity Recognition.pdf 491.05 KB
- Q&A.pdf 389.48 KB

## 1.4

## Summary

Version 1.4 - AI Themes Sentiment Added 7/21/2023

## Functionality Additions

- AI Themes "includeSentiments" parameter added to extract sentiments from themes. ID and Status endpoints added.
- "includeSentiments" parameter added to extract sentiments from themes.
- ID and Status endpoints added.

## 1.3

## Summary

Version 1.3 - Question & Answer Added 1/27/2023

## Functionality Additions

- Question & Answer Supports English language text. Input should be in plain text. Minimum input length is 100 characters. Maximum input length is 10,000 characters per request. Any text beyond the maximum length will not be considered for output. The first request made to the Q&A API may take 10-15 seconds longer to generate a response than subsequent requests as the service needs to start up.
- Supports English language text.
- Input should be in plain text.
- Minimum input length is 100 characters.
- Maximum input length is 10,000 characters per request. Any text beyond the maximum length will not be considered for output.
- The first request made to the Q&A API may take 10-15 seconds longer to generate a response than subsequent requests as the service needs to start up.

## 1.2

## Summary

Version 1.2 - Named Entity Recognition Added 11/7/2022

## Functionality Additions

- Named Entity Recognition - originally released separately from the NLP library Supports English Language text Detect entities (people/places/organizations etc.) within the text
- Supports English Language text
- Detect entities (people/places/organizations etc.) within the text

## 1.1

## Summary

Version 1.1 – AI Text Summarization Added 9/6/2022

## Functionality Additions

- AI Text Summarization  – Originally Released 03/31/2022 Supports English language text. Input should be in plain text. Minimum input length is 100 words. Maximum input length is 1,024 words. Any text beyond the maximum length will not be considered for summarized output.
- Supports English language text.
- Input should be in plain text.
- Minimum input length is 100 words.
- Maximum input length is 1,024 words. Any text beyond the maximum length will not be considered for summarized output.

## 1.0

## Summary

Version 1.0 – Released AI Themes 6/1/2022

## Functionality Additions

- AI Themes Supports English language text. Input should be in plain text. Minimum input length is 100 characters. Maximum input length is 15,000 characters per request. Any text beyond the maximum length will not be considered for output.
- Supports English language text.
- Input should be in plain text.
- Minimum input length is 100 characters.
- Maximum input length is 15,000 characters per request. Any text beyond the maximum length will not be considered for output.

## AI Text Summarization

- Reduce large bodies of text: Quickly consolidate information focusing on document highlights
- Enhance prioritization and focus: Quickly decide document priority based on the main ideas in a body of text
- Populate News Applications: Developers and engineers can use Summarization to create headlines and story snippets to populate news applications

## AI Themes

- This service is used inside FactSet to extract themes from earnings call transcripts
- This service can be used on any unstructured text such as news stories, company filings, or research reports
- When used on multiple historical versions of a document, this API can be used to differentiate themes over time

## Named Entity Recognition

- When filtering content before sending it to analysts at your firm, use the NER service to identify people, companies, and geographic locations specific to user needs and interests.
- You can use NER to enrich unstructured text from filings or other documents before storing it in your firm’s internal data stores.
- Media firms can use NER to identify companies, people, and geographic locations on web pages during the editorial process, and then create hyperlinks from those entities to other relevant data.
- You can use NER to tag companies mentioned in tweets, press releases, or social media posts for your own data gathering or sentiment analysis.
- Within FactSet, when you create a research note using e-mail or the IRN Chrome extension, NER identifies which company the note is about.

## Question & Answer

- This service can be used to find the same type of information across multiple documents. For example, you may query several documents with questions such as "what are new products?", "what are new plant-based products?", or "what does this company make?"
- This service can be used on any unstructured text such as news stories, company filings, or research reports
We use cookies to improve user experience and site performance. For more information on the cookies we use, see our Cookie Policy . We may also share information about your use of our site with our advertising and analytics partners. Please see our Privacy Policy for more information. Visit Cookie Preference Manager to customize your preferences.

## Cookie Preference Center

### Manage Consent Preferences

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance. Examples of performance cookies we may use include but are not limited to: Google Analytics, Microsoft Clarity , Salesforce Pardot, Swiftype Search, Navattic, Vidyard.
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising. Examples of targeting cookies we may use include but are not limited to: Google Advertising, Linkedin Advertising, Microsoft Advertising, Reddit.
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

### Cookie List


--------------------