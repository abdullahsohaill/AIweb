# Pabbly Connect MCP
**URL:** https://forum.pabbly.com/threads/pabbly-connect-mcp-server-beta.28381
**Page Title:** Pabbly Connect MCP Server (Beta) | Pabbly Support
--------------------

- New posts
- New profile posts
- Latest activity
- Instructions to Ask a Question For any assistance, please click the "Ask a Question" button and select the Pabbly product for which you require support. We offer seven comprehensive applications designed to help you efficiently manage and grow your business: Pabbly Connect Pabbly Subscription Billing Pabbly Email Marketing Pabbly Form Builder Pabbly Email Verification Pabbly Hook Pabbly Chatflow Our support team endeavors to respond within 24 business hours (Monday to Friday, 10:00 AM to 6:00 PM IST). We appreciate your understanding and patience.
Instructions to Ask a Question
For any assistance, please click the "Ask a Question" button and select the Pabbly product for which you require support.
We offer seven comprehensive applications designed to help you efficiently manage and grow your business:
- Pabbly Connect
- Pabbly Subscription Billing
- Pabbly Email Marketing
- Pabbly Form Builder
- Pabbly Email Verification
- Pabbly Hook
- Pabbly Chatflow
Our support team endeavors to respond within 24 business hours (Monday to Friday, 10:00 AM to 6:00 PM IST). We appreciate your understanding and patience.
- Home
- What's new
- All Application Help and Troubleshooting 💡

## Pabbly Connect MCP Server (Beta)

- Thread starter Gaurang Sharma
- Start date Apr 14, 2025

## Setting Up an MCP Tool ​

- Navigate to your desired action in the Pabbly Connect workflow
- Click the dropdown menu for the action and select "Add to MCP server"
- A popup window will appear to configure your MCP tool
- Enter a MCP Server Tool Name (Required) Must start with alphabets. Cannot contain spaces or special characters. Maximum 64 characters. Use kebab-case format (e.g., add-lead-to-crm or send-email-notification).
- Must start with alphabets.
- Cannot contain spaces or special characters.
- Maximum 64 characters.
- Use kebab-case format (e.g., add-lead-to-crm or send-email-notification).
- Enter a MCP Tool Description (Required) Provide a clear, concise explanation of what the tool does. Must contain a minimum of 25 character.s Be specific about the tool's functionality and purpose. Click the Add button to create your MCP tool.
- Provide a clear, concise explanation of what the tool does.
- Must contain a minimum of 25 character.s
- Be specific about the tool's functionality and purpose.
- Click the Add button to create your MCP tool.
- Go to https://connect.pabbly.com/v2/app/setting/mcp-server
- Locate your MCP Server URL.
- This URL is your secure connection key - do not share it publicly.

## Connecting Claude Desktop to Pabbly MCP Server ​

- Make sure that node.js is installed on the computer.
- Check the node installation by running the following command -
- Bash: node -v

//or

node --version
- Open Claude Desktop application.
- Navigate to the Developer Settings.
- Open the configuration file for editing.
- Add the following JSON configuration:
- Replace YOUR_MCP_SERVER_URL with your actual MCP Server URL (e.g., https://connect.pabbly.com/mcp/your-unique-id/sse )
- Save the configuration file.
- Restart the Claude Desktop application.
- Your Pabbly Connect tools should now appear in the Claude Desktop client.

## Using MCP Tools with Claude ​

- Interact with your tools using natural language.
- Provide necessary data as prompted by Claude.
- Execute workflow actions directly through the Claude interface.
- Security: Your MCP Server URL functions like a password - keep it secure.
- URL Validity: Generating a new API token will invalidate your current MCP Server URL.
- Tool Naming: Choose clear, descriptive names for your tools to improve usability.
- Tool Description: Write detailed descriptions to help Claude understand each tool's purpose.
- Data Format: Ensure you provide data in the format expected by your workflow actions.
- Verify your MCP Server URL is correct.
- Ensure the configuration file is properly formatted.
- Check that Claude Desktop has been restarted after configuration.
- Confirm your tools have been correctly added to the MCP server.
- Replace YOUR_MCP_SERVER_URL with your actual MCP Server URL (e.g., https://connect.pabbly.com/mcp/your-unique-id/sse )

### Similar threads

- Moeen
- Oct 1, 2025
- General Discussions 🎙️
[LINK: Pabbly MCP - OpenAI agent builder [500 errors from OpenAI Agent Builder when invoking Pabbly MCP custom API/webhook tools]](/threads/pabbly-mcp-openai-agent-builder-500-errors-from-openai-agent-builder-when-invoking-pabbly-mcp-custom-api-webhook-tools.32933/)
- FabeeoBreen
- Oct 13, 2025
[LINK: Oct 13, 2025](/threads/pabbly-mcp-openai-agent-builder-500-errors-from-openai-agent-builder-when-invoking-pabbly-mcp-custom-api-webhook-tools.32933/)
- General Discussions 🎙️
[LINK: Oct 30, 2025](/threads/pabbly-mcp-openai-agent-builder-500-errors-from-openai-agent-builder-when-invoking-pabbly-mcp-custom-api-webhook-tools.32933/latest)
- Locked
- Article
- Rounak Kumar
- Dec 29, 2025
- All Application Help and Troubleshooting 💡
- Locked
- Article
- Rounak Kumar
- Dec 26, 2025
- Help Guide 📘
- Article
- Shambhavi Pandey
- Sep 29, 2025
- Help Guide 📘
- Home
- What's new
- All Application Help and Troubleshooting 💡
- This site uses cookies to help personalise content, tailor your experience and to keep you logged in if you register. By continuing to use this site, you are consenting to our use of cookies. Accept Learn more…

--------------------