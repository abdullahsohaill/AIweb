# Spikee
**URL:** https://labs.withsecure.com/tools/spikee
**Page Title:** Spikee: Testing LLM Applications for Prompt Injection | WithSecure™ Labs
--------------------


## Spikee: Testing LLM Applications for Prompt Injection

by Donato Capitella
TL;DR :
- This blog provides a step-by-step guide on using spikee , an open-source tool we created, to conduct prompt injection testing for LLM applications.
- We explore a case study of an LLM WebMail summarization feature, demonstrating how to build a custom dataset targeting specific attack scenarios.
- Techniques covered include dataset preparation, automated testing with Burp Suite Intruder, and spikee's custom target feature, offering practical guidance on how to test LLM features in applications and how to interpret the results.

### 1. Background

Over the past year, we’ve conducted many security assessments for LLM applications implementing different Generative AI (GenAI) features. These aren’t just chatbots—though those get a lot of attention—but features integrated into products for summarization, resource tagging and decision making to power agentic workflows. The focus of these assessments has been evaluating prompt injection risks.
Unlike generic jailbreak attacks that focus on bypassing alignment (e.g., making the LLM engage in unwanted conversations), prompt injection [ 1 ] involves exploiting the interaction between LLMs and applications that use them to target users with more traditional cyber security attacks. These commonly include data exfiltration (e.g., embedding links to steal sensitive information), executing malicious payloads (e.g., injecting rogue commands or scripts), or causing operational disruptions (e.g., resource exhaustion or denial of service) [ 2 , 3 , 4 ]. To test for these practical risks, we developed a tool called spikee, which we are now releasing as an open-source project.
This article demonstrates how to use spikee to test the security of a GenAI feature by assessing a demo web app, LLM WebMail, which uses an LLM to summarize users' email inboxes.

### 2. The Scenario: LLM Webmail

The demo application for our scenario, LLM WebMail, allows users to click a button to get a summary of their email inbox. Here’s how it works in the backend:
- Emails are retrieved and combined into a single text block.
- This text block is sent to an LLM with a prompt asking for a concise summary of the emails.
- The response is displayed to the user as a summary.
Here’s the core backend code that implements this GenAI use case:
Because we have a specific use case, we can focus on a targeted scenario rather than running thousands of generic prompt injection payloads, which would be costly, slow, and inefficient. In this example, we focus on data exfiltration via markdown images, a common exploitation vector for LLM applications. The goal is to simulate an attacker sending an email to exploit the summarization feature. This approach allows us to create a more realistic and manageable dataset, minimizing unnecessary resource consumption.
In our scenario, the user mailbox contains the following email with a password reset code we want to exfiltrate:

### 3. Make a Custom Dataset

Spikee creates datasets by combining documents ( documents.json ) with jailbreaks ( jailbreaks.json ) to inject instructions ( instructions.json ). The JSON files used to create such datasets are called seeds and are found in the datasets/ folder. You can take a look at the targeted-12-2024 folder, which contains the seeds used to create the targeted dataset for the spikee LLM benchmark ( https://spikee.ai ).
We can now create a dataset for our exfiltration scenario, containing the instruction we want to inject. Let's start by installing spikee and initializing our workspace. Then we will copy the existing seeds folder containing the targeted-12-2024 dataset that comes with the spikee repository, as we'll use these folder as a starting point to create our custom dataset:
Modify instructions.json to include only the targeted instruction for exfiltrating the password reset code:
This instructs the LLM to exfiltrate the password reset token, and we modify the canary to detect if the attack succeeds by including the base64-encoded value of the known token. You can include the entire base64-encoded token,b ut for this demo we just included the beginning of the token, as that will be sufficient to detect whether the LLM has correctly interpreted the injected instructions
Modify jailbreaks.json to select a small subset of jailbreak techniques you want to use, starting with basic ones and scaling up if needed. In our example, we keep 30 of the most common ones.
Finally, populate documents.json with a sample email into which we will inject our malicious payloads (these will be the emails an attacker would send to their target):
Once the seed folder is ready, generate the dataset in Burp-Intruder--compatible format with the following command:
The ' --format burp' option outputs a TXT file, one document per line, with JSON escaping, so that you can use this in Burp Suite Intruder. Notice that we specify custom injection delimiters ( --injection-delimiters ) to test if different placement methods affect the outcome. By default the attack payloads will be added at the end of the document, but you can also add them at the beginning and/or end using --positions .
The dataset will be generated under the datasets/ folder and its name will start with current timestamp, such as 1737471713-seeds-llmwebmail-burp-dataset.txt . This is an example entry, showing how one jailbreak techniques has been used to inject our insturction, and how that's been placed into our email docment:

### 4. Testing

Once the dataset is prepared, there are two primary ways to test the LLM Webmail application for prompt injection vulnerabilities.
The first option is to use Burp Suite Intruder to see how the application handles the different malicious emails in our dataset by automating requests to the /api/summarize endpoint and analyzing responses for potential data exfiltration.
1. Intercept the request:
- Use Burp Proxy to intercept a request to the /api/summarize endpoint when the summarization feature is triggered.
- Send the request to Intruder by right-clicking and selecting "Send to Intruder."
2. Create a placeholder:
- In the Intruder tab, select one of the emails in the body of the request, delete its content and set a placeholder there for our malicious emails to be inserted.
3. Load the payloads:
- Navigate to the "Payloads" tab and load the payloads generated by spikee.
- Use the Burp-formatted dataset created earlier.
4. Set rate limits:
- Create a resource pool under "Options" and define the appropriate request rate.
- Consult with the client to determine acceptable traffic levels.
- If unsure, limit the attack to one request at a time to avoid overwhelming the application.
5. Configure canary detection:
- In the "Grep Extract" section, configure detection rules to look for the expected canary string: ![image](https://withsecure.com?q=YWJjMTIzeH.
6. Launch the attack:
- Start the Intruder attack and analyze the responses for successful exfiltration attempts.
You can check which payloads worked by looking at the responses where the canary is present:
These are some examples of information and attack paths that can be queried from the graph generated by IAMGraph. Depending on the input dataset and additional information available of the target environment, the generated graph could be enriched to allow various different analysis.
For more direct and automated testing, spikee allows defining custom target modules that can interact directly with any API of your choosing.
1. Create a target script:
- This simply involves creating a Python file under the targets folder (e.g. targets/llmwebmail.py ) containing a method called process_input(input_text, system_message)
- The method will take as input an injected document from the dataset (i.e. email) and we need to send it to the summarization endpoint together with any other context document (in this case two other legitimate emails, one of them containing the reset code to exfiltrate)
- We can ignore the system_message argument for this use-case, that's only used when benchmarking LLMs directly
- The method needs to return the output of the summarization endpoint
2. Generate the dataset:
- We can't use the TXT dataset that we generated before, we need to regenerate it, but this time we'll select "document" as the format.
- This will output the dataset in a JSON format ready for spikee to use
3. Run the test:
- You can now simply invoke spikee, passing the dataset and the name of the target you just created:
4. Analyze the resuts:
- Once this is finished, you can analyze the Attack Success Rate with the following command:

### 5. Interpreting the results

Once testing is complete, the Attack Success Rate (ASR) provides insights into the application's resilience against prompt injection attacks. However, it's important to understand what the results mean and their limitations.
- Exploitation Potential : The results help identify working payloads that successfully achieve the attack goal, such as exfiltrating confidential data from user emails. These can be useful for demonstrating risks to stakeholders.
- Evaluation and Comparison: ASR can serve as a benchmark to measure improvements after applying mitigations such as system message tuning and guardrails. A significant reduction in ASR after implementing such measures indicates their effectiveness.
- Limitations : A low ASR does not mean the application is secure against prompt injection. Spikee does not perform adaptive attacks, which dynamically explore the embedding space to find jailbreaks. Techniques like those described in recent literature [ 6 , 7 , 8 , 9 , 10 ] have achieved near 100% success rates in jailbreaking leading LLMs under different conditions. It must be assumed that with sufficient resources and access, attackers will find ways to bypass current alignment strategies and guardrails.
Based on our work with clients deploying LLM applications in production, we have developed the LLM Application Security Canvas , a comprehensive framework that outlines various controls to help mitigate risks such as those discussed here.
This framework includes measures like input and output validation to detect potentially harmful content such as prompt injection, out-of-scope queries, and unexpected elements like links, HTML, or markdown. Additionally, when agentic workflows are involved, enforcing human-in-the-middle validation, proper access controls, and safe APIs is crucial. These controls collectively help reduce the attack surface and improve the overall security posture of LLM applications.
Some controls, especially LLM guardrails for prompt injection and jailbreaking, are likely to fail if attackers are given the opportunity to search the embedding space using adaptive attacks [ 6 , 7 , 8 , 9 , 10 ]. These attacks have been shown to achieve near 100% success rates against leading LLMs. For this reason, an effective strategy is to combine existing defenses with adaptive content moderation systems , which monitor user interactions and progressively enforce restrictions when repeated exploitation attempts are detected. These systems work similarly to traditional account lockouts by temporarily suspending or restricting access for users who exceed a predefined threshold of suspicious activity. Implementing adaptive content moderation should include per-user tracking, configurable thresholds, and detailed logging to facilitate forensic analysis and investigation. By incorporating such measures, organizations can significantly limit an attacker's ability to iteratively probe and exploit vulnerabilities, thereby enhancing the overall security posture of the application.

### 6. Conclusions

In this tutorial, we demonstrated how to use spikee to assess an LLM webmail for suceptability to common prompt injection vulnerabilities. We covered building a targeted dataset, leveraging Burp Suite Intruder for automated testing, and using spikee’s custom target support for direct interaction with the application.
Spikee is under active development, and this is just the beginning. Future updates will include a Burp Suite plugin to streamline the testing workflow further and larger attack datasets (including evasion plugins) to cover a wider range of scenarios. Check out https://spikee.ai for all latest developments and contribute to the project to help improve LLM security testing practices.

### 7. References

- Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection
- Prompt Injection in JetBrains Rider AI Assistant
- When your AI Assistant has an evil twin
- Embrace The Red Blog
- LLM Application Security Canvas
- Universal and Transferable Adversarial Attacks on Aligned Language Models
- AutoDAN: Interpretable Gradient-Based Adversarial Attacks on Large Language Models
- PRP: Propagating Universal Perturbations to Attack Large Language Model Guard-Rails
- Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks
- Best-of-N Jailbreaking

## We value your privacy

## Privacy Preference Center

### Manage Consent Preferences

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

### Cookie List

- checkbox label label

--------------------