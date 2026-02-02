# Blog post about GenAI Mail Insights by Martin Frick
**URL:** https://blogs.sap.com/2023/11/15/genai-mail-insights-leveraging-the-generative-ai-hub-in-sap-ai-core-to-improve-customer-support
**Page Title:** GenAI Mail Insights - Leveraging the generative AI... - SAP Community
--------------------

- SAP Community
- Products and Technology
- Technology
- Technology Blog Posts by SAP
- GenAI Mail Insights - Leveraging the generative AI...

## GenAI Mail Insights - Leveraging the generative AI hub in SAP AI Core to improve customer support

- Subscribe to RSS Feed
- Mark as New
- Mark as Read
- Bookmark
- Printer Friendly Page
- Report Inappropriate Content
- SAP Managed Tags
- SAP HANA Cloud
- SAP Cloud Application Programming Model
- SAP TechEd
- Artificial Intelligence
- SAP AI Core
- SAP Business Technology Platform
- SAP TechEd Event
- SAP Cloud Application Programming Model Software Product Function
- Artificial Intelligence Product Category
- SAP HANA Cloud Software Product
- SAP Business Technology Platform Software Product
- SAP AI Core SAP Business AI
Too busy to read but still want the essential bits ? 🏃‍ Take a quick peek at our SAP-samples repository and Generative AI reference architecture 🕵️‍ Make sure you catch the brand-new openSAP course, " Generative AI at SAP "
[LINK: SAP-samples repository](https://github.com/SAP-samples/btp-cap-genai-rag)
[LINK: CAP application](https://cap.cloud.sap/docs/)
Generative AI reference architecture for multitenant SAP BTP applications
[LINK: Develop a multitenant Software as a Service application in SAP BTP using CAP](https://github.com/SAP-samples/btp-cap-multitenant-saas)
[LINK: SAP-samples GitHub repository](https://github.com/SAP-samples/btp-cap-genai-rag)
Customer Service app before the introduction of GenAI Mail Insights
Customer Service app after the introduction of GenAI Mail Insights
[LINK: SAP-samples repository](https://github.com/SAP-samples/btp-cap-genai-rag)
[LINK: SAP AI Core resource group](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/resource-groups)
[LINK: deployments](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/terminology)
Tenant specific SAP AI Core Resource Groups and LLM Deployments (Preview Version - subject to change - check latest openSAP course )
[LINK: Inference URL](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/inference)
Calling the Chat Completion inference URL of a tenant-specific Deployment (Implementation subject to change)
[LINK: custom schemas](https://js.langchain.com/docs/modules/model_io/output_parsers/#structured-output-parser-with-zod-schema)
Using a custom schema ( zod + LangChain ) for a programmatic LLM interaction
[LINK: vector store](https://js.langchain.com/docs/integrations/vectorstores)
Leveraging the power of Retrieval Augmented Generation
[LINK: Click here](https://help.sap.com/docs/translation-hub/sap-translation-hub/tutorials?version=Cloud)
Explore further exciting use-cases and scenarios for Generative AI
[LINK: SAP-samples GitHub repository](https://github.com/SAP-samples/btp-cap-genai-rag)
[LINK: step-by-step guide](https://github.com/SAP-samples/btp-cap-genai-rag/blob/main/README.md#getting-started)
[LINK: GitHub repository](https://github.com/SAP-samples/btp-cap-genai-rag)
- openSAP Course GenerativeAI at SAP
- Artificial Intelligence / Machine Learning
- SAP AI Core
- SAP AI Launchpad
- SAP AI Business Services
- SAP AI Ethics
- Document Information Extraction (SAP AI Business Services)
- Data Attribute Recommendation (SAP AI Business Services)
- Personalized Recommendation (SAP AI Business Services)
- Technology Updates
- Generative AI
- Generative AI Hub
- Kyma
- LLM
- multitenant
- RAG
- Reference Architecture
- Mark as Read
- Mark as New
- Bookmark
- Permalink
- Print
- Report Inappropriate Content
Hi martinfrick Thanks for the blog. I'm interested to know the "email" integration. Have you integrated this Gen AI + CAP solution with any email server (like cloud or on-prem)? Can you please provide more details on this. Thanks, Manju
- Mark as Read
- Mark as New
- Bookmark
- Permalink
- Print
- Report Inappropriate Content
[LINK: click here](https://github.com/SAP-samples/btp-cap-genai-rag/blob/58d2f7eb43fa916d669ee329fc1a8d79e02b2b66/multi-tenant/code/srv/app-srv/mail-insights-service.ts#L143)
- Mark as Read
- Mark as New
- Bookmark
- Permalink
- Print
- Report Inappropriate Content
[LINK: https://platform.openai.com/docs/guides/embeddings](https://platform.openai.com/docs/guides/embeddings)
[LINK: https://js.langchain.com/docs/modules/data_connection/vectorstores/](https://js.langchain.com/docs/modules/data_connection/vectorstores/)
[LINK: https://js.langchain.com/docs/modules/model_io/output_parsers/structured#structured-output-parser-wi...](https://js.langchain.com/docs/modules/model_io/output_parsers/structured#structured-output-parser-with-zod-schema)
- Mark as Read
- Mark as New
- Bookmark
- Permalink
- Print
- Report Inappropriate Content
Hi Martin, and thanks for the blog.
As I have a limited knowledge in prompt engineering and LLM techniques, it took me a while to figure out how exactly magic works here, so maybe these links can help someone else
https://platform.openai.com/docs/guides/embeddings - about why we need vector store at all
[LINK: https://platform.openai.com/docs/guides/embeddings](https://platform.openai.com/docs/guides/embeddings)
https://js.langchain.com/docs/modules/data_connection/vectorstores/ - about how embeddings are actually getting called (by langchain magic)
[LINK: https://js.langchain.com/docs/modules/data_connection/vectorstores/](https://js.langchain.com/docs/modules/data_connection/vectorstores/)
https://js.langchain.com/docs/modules/model_io/output_parsers/structured#structured-output-parser-wi... - about JSON parsing using custom scheme // it is a part of a prompt itself , which became clear after I re-read the blog knowing this
[LINK: https://js.langchain.com/docs/modules/model_io/output_parsers/structured#structured-output-parser-wi...](https://js.langchain.com/docs/modules/model_io/output_parsers/structured#structured-output-parser-with-zod-schema)
https://www.timescale.com/blog/how-to-build-llm-applications-with-pgvector-vector-store-in-langchain... - about pretty similar stuff on "vanilla" stack (python + postgres + openai embeddings )
So, if I understand it correctly, what happens here is we ask chatGPT to give us a text summary for our mail that fits our cds schema ( onAddMails handler calling regenerateInsights then calling extractGeneralInsights )
We also store mail embeddings (that langchain fetches for us) in vector storage ( addDocuments line) to perform searches later.
Pg vector searches ( getClosestMails ) provide us with similar Mails and Responses (will use them for response generation, which is exactly the RAG magic).
Hope it helps, and please correct me if I got it wrong (I only looked at single tenant version).
Regards, Alex
- Mark as Read
- Mark as New
- Bookmark
- Permalink
- Print
- Report Inappropriate Content
- Mark as Read
- Mark as New
- Bookmark
- Permalink
- Print
- Report Inappropriate Content
- Mark as Read
- Mark as New
- Bookmark
- Permalink
- Print
- Report Inappropriate Content
- Mark as Read
- Mark as New
- Bookmark
- Permalink
- Print
- Report Inappropriate Content
- Mark as Read
- Mark as New
- Bookmark
- Permalink
- Print
- Report Inappropriate Content
- Mark as Read
- Mark as New
- Bookmark
- Permalink
- Print
- Report Inappropriate Content
Hi Team,
Thanks for this informative blog.
We are facing errors while accessing the code from GitHub.
Please let us know how should we connect with you.
Thanks in advance.
Tushar.
You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.
- Comment
- My Experience with SAP Generative AI Developer Exam (C_AIG): Excellent Hands-On Format, One Setback in Technology Blog Posts by Members Thursday
[LINK: My Experience with SAP Generative AI Developer Exam (C_AIG): Excellent Hands-On Format, One Setback](/t5/technology-blog-posts-by-members/my-experience-with-sap-generative-ai-developer-exam-c-aig-excellent-hands/ba-p/14313474)
- SAP Integration Suite: Intelligent Integration with AI Adapter in Technology Blog Posts by Members Wednesday
- SAP Cloud ALM C_STC Certification Reimagined: From Multiple Choice to AI Roleplay in Technology Blog Posts by SAP Monday
- SAP RPT‑1: Why is it Essential for Predicting Business Outcomes in Today’s and Future Generative AI? in Technology Blog Posts by SAP Monday
- UKISUG & SAP Customer Support Day: AI-Powered Support that Reaches New Horizons in Technology Blog Posts by SAP a week ago

--------------------