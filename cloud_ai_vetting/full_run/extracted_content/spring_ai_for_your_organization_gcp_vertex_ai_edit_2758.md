# "Spring AI for Your Organization - GCP Vertex AI Edition" by Muthukumaran Navaneethakrishnan (Leanpub)
**URL:** https://leanpub.com/springai
**Page Title:** Spring AI for Your Organization [Leanpub PDF/iPad/Kindle]
--------------------

- About
- Packages
- Author
- Contents
- Sample

## About

About the Book
This book is for Spring developers who want to explore GCP Vertex AI. It's perfect if you're looking to:
- Learn Google Vertex AI
- Understand vector databases
- Help your company become AI-driven
The guide is designed for developers who want to quickly start with generative AI.
By the end, you'll be able to:
- Build chatbots that can handle any type of company data (PDFs, logs, emails, audio, video, images)
- Use the newest features of Spring AI
- Create and launch an API for interacting with these chatbots
This will help make your organization's data more accessible and useful.

### Share this book

### Categories

### Feedback

## Team Discounts

Team Discounts
Get a team discount on this book!
- Up to 3 members Minimum price $47.00 Suggested price $47.00
Up to 3 members
- Up to 5 members Minimum price $75.00 Suggested price $75.00
Up to 5 members
- Up to 10 members Minimum price $132.00 Suggested price $132.00
Up to 10 members
- Up to 15 members Minimum price $189.00 Suggested price $189.00
Up to 15 members
- Up to 25 members Minimum price $284.00 Suggested price $284.00
Up to 25 members

## Author

About the Author
Muthukumaran Navaneethakrishnan has over 20 years of experience as a software developer, working with languages such as Java, JavaScript, Clojure, and Golang. Even as he serves in roles such as engineering manager and architect, he continues to engage daily in coding, demonstrating his enduring passion for hands-on software development. His work has been featured by prominent publishers like Leanpub, O'Reilly, and Manning.
In the open-source community, Muthukumaran is highly active, contributing to projects like Spring AI and developing numerous other libraries. He is dedicated to creating proof of concepts, reviewing codebases to enhance scalability, performance, and security, and building tools that improve the developer experience. He specializes in quickly resolving urgent issues, ensuring systems are both robust and efficient.

## Contents

Table of Contents
- 1: 1 Introduction 1.1 Evolution of AI Frameworks in Java 1.2 Emergence of Spring AI 1.3 Introduction to Generative AI 1.4 Overview of Spring AI 1.5 Introduction to Google Cloud’s Vertex AI 1.6 Goals of the Book (What You Will Learn) 1.7 Who Should Read This Book 1.8 Prerequisites 1.9 What’s Next 2: Creating ChatBot with Spring AI 2.1 Chapter Highlights: 2.2 How to Initialize the project 2.3 Creating a RESTful Chat Endpoint 2.4 Connecting to Vertex AI Gemini 2.5 Implementing the Chat Endpoint 2.6 How to Test the Application 2.7 Configuring Chat Options for Vertex AI 2.8 How to Test the Application 2.9 Understanding API Interaction with Vertex AI 2.10 How to Deploy in GCP Cloud Run 2.11 Review Questions 2.12 Answers to Review Questions 2.13 What We Learned 3: Building Context-Aware Chatbots with Spring AI: Memory Management and Conversational Continuity 3.1 Chapter Highlights 3.2 The Challenge of Contextual Conversation 3.3 Understanding LLMs and Contextual Conversations 3.4 Implementing Conversation History in Spring AI 3.5 Managing ChatBot Conversations with Session IDs 3.6 Updating the ChatBot Endpoint for Conversational Context 3.7 Testing the Enhanced ChatBot with Session History 3.8 Simplifying Chat History Management with Advisors 3.9 Creating a DELETE Endpoint to Reset Chat Session History 3.10 Understanding System Prompts in Chatbot Responses 3.11 What We Learned 4: Creating Structural Data Bots 4.1 Chapter Highlights: 4.2 Make Inventory to be queried by Natural Language 4.3 Update Dependencies 4.4 Setting up an SQL database in GCP Cloud SQL 4.6 Getting Ready for Natural Language Processing 4.7 From Natural Queries to SQL 4.8 JSON Conversion of SQL Results 4.9 SQL to Natural Language Response 4.10 Bringing It All Together: The Endpoint 4.11 Testing the Endpoint 4.12 Exercise: Implement it using CSV instead of JSON 4.13 Improving SQL Query Flexibility for User Queries 4.14 Handling multiple questions 4.15 What We Learned 5: LLM Tool Calling with Spring AI 5.1 Chapter Highlights: 5.2 Understanding LLM Tool Calls 5.3 Implementing Tool Calling with REST API 5.4 Java Implementation with Direct API Calls 5.5 Handling Multiple Tool Calls 5.6 Simplifying with Spring AI 5.7 Advanced Tool Calling: Sequential Tool Routing 5.8 Few Words 5.9 What We Learned 6: Building Chatbots with Text and PDF Files 6.1 Chapter Highlights: 6.2 Use Case: Answering Questions About Vacuum Cleaners based on text file 6.3 Use Case: Answering Questions About Laptop based on pdf manual 7: Building Chatbots with Multimedia Capabilities 7.1 Chapter Highlights: 7.2 Use Case: Answering Questions About Coupons from an Image 7.3 Invoking the Chatbot with Image Data 7.4 Testing 7.5 Use Case: Answering Questions based on a Customer Care Audio 7.6 Testing 7.7 Use Case: Answering Questions from a Vaccum Cleaner Advertisement video 7.8 Invoking the Chatbot with Video Data 7.9 Testing 8: Using RAG to Make LLMs Smarter with Internal Data 8.1 Integrating Internal Data with LLM 8.2 Chapter Highlights: 8.3 How to Create Embeddings 8.4 Vector Database 8.5 Making Similar Documents as Conversational 8.6 Exercise: Modify Chatbot to Search All Records When Department Is Not Specified 9: Building Internal Knowledge based assistant 9.1 Chapter Highlights: 9.2 Integrating Google Cloud Storage Bucket 9.3 Building a Chatbot with Internal Documents 9.4 Adding File References on Chat 10: PDF Documents & Image Embeddings 10.1 Chapter Highlights: 10.1 Saving PDF Document Pages as Image Embeddings 10.2 Updating Chat Endpoint to use Image embeddings 11: Accessing other models in GCP Model Garden 11.1 Chapter Highlights: 11.1 Setting Up GCP 11.2 Setting Up Gradle and Configuration 11.3 Setting Up Authentication Tokens for Llama Requests 12: Whats Next
- 1: 1 Introduction 1.1 Evolution of AI Frameworks in Java 1.2 Emergence of Spring AI 1.3 Introduction to Generative AI 1.4 Overview of Spring AI 1.5 Introduction to Google Cloud’s Vertex AI 1.6 Goals of the Book (What You Will Learn) 1.7 Who Should Read This Book 1.8 Prerequisites 1.9 What’s Next
- 1.1 Evolution of AI Frameworks in Java
- 1.2 Emergence of Spring AI
- 1.3 Introduction to Generative AI
- 1.4 Overview of Spring AI
- 1.5 Introduction to Google Cloud’s Vertex AI
- 1.6 Goals of the Book (What You Will Learn)
- 1.7 Who Should Read This Book
- 1.8 Prerequisites
- 1.9 What’s Next
- 2: Creating ChatBot with Spring AI 2.1 Chapter Highlights: 2.2 How to Initialize the project 2.3 Creating a RESTful Chat Endpoint 2.4 Connecting to Vertex AI Gemini 2.5 Implementing the Chat Endpoint 2.6 How to Test the Application 2.7 Configuring Chat Options for Vertex AI 2.8 How to Test the Application 2.9 Understanding API Interaction with Vertex AI 2.10 How to Deploy in GCP Cloud Run 2.11 Review Questions 2.12 Answers to Review Questions 2.13 What We Learned
- 2.1 Chapter Highlights:
- 2.2 How to Initialize the project
- 2.3 Creating a RESTful Chat Endpoint
- 2.4 Connecting to Vertex AI Gemini
- 2.5 Implementing the Chat Endpoint
- 2.6 How to Test the Application
- 2.7 Configuring Chat Options for Vertex AI
- 2.8 How to Test the Application
- 2.9 Understanding API Interaction with Vertex AI
- 2.10 How to Deploy in GCP Cloud Run
- 2.11 Review Questions
- 2.12 Answers to Review Questions
- 2.13 What We Learned
- 3: Building Context-Aware Chatbots with Spring AI: Memory Management and Conversational Continuity 3.1 Chapter Highlights 3.2 The Challenge of Contextual Conversation 3.3 Understanding LLMs and Contextual Conversations 3.4 Implementing Conversation History in Spring AI 3.5 Managing ChatBot Conversations with Session IDs 3.6 Updating the ChatBot Endpoint for Conversational Context 3.7 Testing the Enhanced ChatBot with Session History 3.8 Simplifying Chat History Management with Advisors 3.9 Creating a DELETE Endpoint to Reset Chat Session History 3.10 Understanding System Prompts in Chatbot Responses 3.11 What We Learned
- 3.1 Chapter Highlights
- 3.2 The Challenge of Contextual Conversation
- 3.3 Understanding LLMs and Contextual Conversations
- 3.4 Implementing Conversation History in Spring AI
- 3.5 Managing ChatBot Conversations with Session IDs
- 3.6 Updating the ChatBot Endpoint for Conversational Context
- 3.7 Testing the Enhanced ChatBot with Session History
- 3.8 Simplifying Chat History Management with Advisors
- 3.9 Creating a DELETE Endpoint to Reset Chat Session History
- 3.10 Understanding System Prompts in Chatbot Responses
- 3.11 What We Learned
- 4: Creating Structural Data Bots 4.1 Chapter Highlights: 4.2 Make Inventory to be queried by Natural Language 4.3 Update Dependencies 4.4 Setting up an SQL database in GCP Cloud SQL 4.6 Getting Ready for Natural Language Processing 4.7 From Natural Queries to SQL 4.8 JSON Conversion of SQL Results 4.9 SQL to Natural Language Response 4.10 Bringing It All Together: The Endpoint 4.11 Testing the Endpoint 4.12 Exercise: Implement it using CSV instead of JSON 4.13 Improving SQL Query Flexibility for User Queries 4.14 Handling multiple questions 4.15 What We Learned
- 4.1 Chapter Highlights:
- 4.2 Make Inventory to be queried by Natural Language
- 4.3 Update Dependencies
- 4.4 Setting up an SQL database in GCP Cloud SQL
- 4.6 Getting Ready for Natural Language Processing
- 4.7 From Natural Queries to SQL
- 4.8 JSON Conversion of SQL Results
- 4.9 SQL to Natural Language Response
- 4.10 Bringing It All Together: The Endpoint
- 4.11 Testing the Endpoint
- 4.12 Exercise: Implement it using CSV instead of JSON
- 4.13 Improving SQL Query Flexibility for User Queries
- 4.14 Handling multiple questions
- 4.15 What We Learned
- 5: LLM Tool Calling with Spring AI 5.1 Chapter Highlights: 5.2 Understanding LLM Tool Calls 5.3 Implementing Tool Calling with REST API 5.4 Java Implementation with Direct API Calls 5.5 Handling Multiple Tool Calls 5.6 Simplifying with Spring AI 5.7 Advanced Tool Calling: Sequential Tool Routing 5.8 Few Words 5.9 What We Learned
- 5.1 Chapter Highlights:
- 5.2 Understanding LLM Tool Calls
- 5.3 Implementing Tool Calling with REST API
- 5.4 Java Implementation with Direct API Calls
- 5.5 Handling Multiple Tool Calls
- 5.6 Simplifying with Spring AI
- 5.7 Advanced Tool Calling: Sequential Tool Routing
- 5.8 Few Words
- 5.9 What We Learned
- 6: Building Chatbots with Text and PDF Files 6.1 Chapter Highlights: 6.2 Use Case: Answering Questions About Vacuum Cleaners based on text file 6.3 Use Case: Answering Questions About Laptop based on pdf manual
- 6.1 Chapter Highlights:
- 6.2 Use Case: Answering Questions About Vacuum Cleaners based on text file
- 6.3 Use Case: Answering Questions About Laptop based on pdf manual
- 7: Building Chatbots with Multimedia Capabilities 7.1 Chapter Highlights: 7.2 Use Case: Answering Questions About Coupons from an Image 7.3 Invoking the Chatbot with Image Data 7.4 Testing 7.5 Use Case: Answering Questions based on a Customer Care Audio 7.6 Testing 7.7 Use Case: Answering Questions from a Vaccum Cleaner Advertisement video 7.8 Invoking the Chatbot with Video Data 7.9 Testing
- 7.1 Chapter Highlights:
- 7.2 Use Case: Answering Questions About Coupons from an Image
- 7.3 Invoking the Chatbot with Image Data
- 7.4 Testing
- 7.5 Use Case: Answering Questions based on a Customer Care Audio
- 7.6 Testing
- 7.7 Use Case: Answering Questions from a Vaccum Cleaner Advertisement video
- 7.8 Invoking the Chatbot with Video Data
- 7.9 Testing
- 8: Using RAG to Make LLMs Smarter with Internal Data 8.1 Integrating Internal Data with LLM 8.2 Chapter Highlights: 8.3 How to Create Embeddings 8.4 Vector Database 8.5 Making Similar Documents as Conversational 8.6 Exercise: Modify Chatbot to Search All Records When Department Is Not Specified
- 8.1 Integrating Internal Data with LLM
- 8.2 Chapter Highlights:
- 8.3 How to Create Embeddings
- 8.4 Vector Database
- 8.5 Making Similar Documents as Conversational
- 8.6 Exercise: Modify Chatbot to Search All Records When Department Is Not Specified
- 9: Building Internal Knowledge based assistant 9.1 Chapter Highlights: 9.2 Integrating Google Cloud Storage Bucket 9.3 Building a Chatbot with Internal Documents 9.4 Adding File References on Chat
- 9.1 Chapter Highlights:
- 9.2 Integrating Google Cloud Storage Bucket
- 9.3 Building a Chatbot with Internal Documents
- 9.4 Adding File References on Chat
- 10: PDF Documents & Image Embeddings 10.1 Chapter Highlights: 10.1 Saving PDF Document Pages as Image Embeddings 10.2 Updating Chat Endpoint to use Image embeddings
- 10.1 Chapter Highlights:
- 10.1 Saving PDF Document Pages as Image Embeddings
- 10.2 Updating Chat Endpoint to use Image embeddings
- 11: Accessing other models in GCP Model Garden 11.1 Chapter Highlights: 11.1 Setting Up GCP 11.2 Setting Up Gradle and Configuration 11.3 Setting Up Authentication Tokens for Llama Requests
- 11.1 Chapter Highlights:
- 11.1 Setting Up GCP
- 11.2 Setting Up Gradle and Configuration
- 11.3 Setting Up Authentication Tokens for Llama Requests
- 12: Whats Next

## Get the free sample chapters

Click the buttons to get the free sample in PDF or EPUB, or read the sample online here

## The Leanpub 60 Day 100% Happiness Guarantee

Within 60 days of purchase you can get a 100% refund on any Leanpub purchase, in two clicks . Now, this is technically risky for us, since you'll have the book or course files either way. But we're so confident in our products and services, and in our authors and readers, that we're happy to offer a full money back guarantee for everything we sell. You can only find out how good something is by trying it, and because of our 100% money back guarantee there's literally no risk to do so! So, there's no reason not to click the Add to Cart button, is there? See full terms...

## Earn $8 on a $10 Purchase, and $16 on a $20 Purchase

We pay 80% royalties on purchases of $7.99 or more , and 80% royalties minus a 50 cent flat fee on purchases between $0.99 and $7.98 . You earn $8 on a $10 sale, and $16 on a $20 sale . So, if we sell 5000 non-refunded copies of your book for $20 , you'll earn $80,000 . (Yes, some authors have already earned much more than that on Leanpub.) In fact, authors have earned over $14 million writing, publishing and selling on Leanpub. Learn more about writing on Leanpub

## Free Updates. DRM Free.

If you buy a Leanpub book, you get free updates for as long as the author updates the book! Many authors use Leanpub to publish their books in-progress, while they are writing them. All readers get free updates, regardless of when they bought the book or how much they paid (including free). Most Leanpub books are available in PDF (for computers) and EPUB (for phones, tablets and Kindle). The formats that a book includes are shown at the top right corner of this page. Finally, Leanpub books don't have any DRM copy-protection nonsense, so you can easily read them on any supported device.
Learn more about Leanpub's ebook formats and where to read them

## Write and Publish on Leanpub

You can use Leanpub to easily write, publish and sell in-progress and completed ebooks and online courses! Leanpub is a powerful platform for serious authors, combining a simple, elegant writing and publishing workflow with a store focused on selling in-progress ebooks. Leanpub is a magical typewriter for authors: just write in plain text, and to publish your ebook, just click a button. (Or, if you are producing your ebook your own way, you can even upload your own PDF and/or EPUB files and then publish with one click!) It really is that easy.

--------------------