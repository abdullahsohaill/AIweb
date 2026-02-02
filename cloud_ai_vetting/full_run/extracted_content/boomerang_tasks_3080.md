# Boomerang Tasks
**URL:** https://docs.roocode.com/features/boomerang-tasks
**Page Title:** Boomerang Tasks: Orchestrate Complex Workflows | Roo Code Documentation
--------------------

Boomerang Tasks (also known as subtasks or task orchestration) allow you to break down complex projects into smaller, manageable pieces using the built-in 🪃 Orchestrator Mode (aka Boomerang Mode) . Think of it like delegating parts of your work to specialized assistants. Each subtask runs in its own context, often using a different Roo Code mode tailored for that specific job (like 💻 Code , 🏗️ Architect , or 🪲 Debug ). The Orchestrator mode manages this process.
The 🪃 Orchestrator mode (previously achieved via a custom "Boomerang Mode") is now a built-in mode specifically designed to orchestrate workflows by breaking down tasks and delegating them to other modes. You no longer need to create a custom mode for this functionality.
Learn more about Built-in Modes .

## Why Use Boomerang Tasks? ​

- Tackle Complexity: Break large, multi-step projects (e.g., building a full feature) into focused subtasks (e.g., design, implementation, documentation).
- Use Specialized Modes: Automatically delegate subtasks to the mode best suited for that specific piece of work, leveraging specialized capabilities for optimal results.
- Maintain Focus & Efficiency: Each subtask operates in its own isolated context with a separate conversation history. This prevents the parent (orchestrator) task from becoming cluttered with the detailed execution steps (like code diffs or file analysis results), allowing it to focus efficiently on the high-level workflow and manage the overall process based on concise summaries from completed subtasks.
- Streamline Workflows: Results from one subtask can be automatically passed to the next, creating a smooth flow (e.g., architectural decisions feeding into the coding task).

## How It Works ​

- When in the 🪃 Orchestrator mode (aka Boomerang Mode), Roo analyzes a complex task and suggests breaking it down into a subtask 1 .
When in the 🪃 Orchestrator mode (aka Boomerang Mode), Roo analyzes a complex task and suggests breaking it down into a subtask 1 .
- The parent task (in Orchestrator mode) pauses, and the new subtask begins in a different, specialized mode 2 .
The parent task (in Orchestrator mode) pauses, and the new subtask begins in a different, specialized mode 2 .
- When the subtask's goal is achieved, Roo signals completion.
When the subtask's goal is achieved, Roo signals completion.
- The parent task resumes with only the summary 3 of the subtask. The parent uses this summary to continue the main workflow.
The parent task resumes with only the summary 3 of the subtask. The parent uses this summary to continue the main workflow.

## Key Considerations ​

- Approval Required: By default, you must approve the creation and completion of each subtask. This can be automated via the Auto-Approving Actions settings if desired.
- Context Isolation and Transfer: Each subtask operates in complete isolation with its own conversation history. It does not automatically inherit the parent's context. Information must be explicitly passed: Down: Via the initial instructions provided when the subtask is created. Up: Via the final summary provided when the subtask finishes. Be mindful that only this summary returns to the parent.
- Down: Via the initial instructions provided when the subtask is created.
- Up: Via the final summary provided when the subtask finishes. Be mindful that only this summary returns to the parent.
- Navigation: Roo's interface helps you see the hierarchy of tasks (which task is the parent, which are children). You can typically navigate between active and paused tasks.
Boomerang Tasks provide a powerful way to manage complex development workflows directly within Roo Code, leveraging specialized modes for maximum efficiency.
Use subtasks (delegated via Orchestrator mode) to maintain clarity. If a request significantly shifts focus or requires a different expertise (mode), consider creating a subtask rather than overloading the current one.

## Frequently Asked Questions ​

### Why can't Orchestrator mode read files, write files, call MCPs, or run commands? ​

The Orchestrator mode is intentionally limited to focus on high-level workflow management. Giving it the ability to read files by default causes the context to become filled with file reads, hampering its ability to remain focused on orchestration. The design philosophy is that subtasks should handle the detailed work and return only the necessary information (via their completion summaries) for the orchestrator to delegate further tasks effectively.
This limitation helps prevent context poisoning , where irrelevant or excessive information contaminates the model's active context, leading to degraded performance and task deviation.

### How can I override Orchestrator mode's limitations? ​

You can customize the Orchestrator mode to add capabilities like file reading by following the configuration precedence system:
- Open the Command Palette and select "Edit Global Modes"
- Copy and paste this configuration:
- Save the file. Your global Orchestrator mode will now have read capabilities.
Adding capabilities to the Orchestrator mode should be done thoughtfully. The limited default capabilities help maintain focus on orchestration rather than implementation details.

## Footnotes ​

- This context is passed via the message parameter of the new_task tool when the Orchestrator mode delegates the task. ↩
This context is passed via the message parameter of the new_task tool when the Orchestrator mode delegates the task. ↩
- The mode for the subtask is specified via the mode parameter of the new_task tool during initiation by the Orchestrator mode. ↩
The mode for the subtask is specified via the mode parameter of the new_task tool during initiation by the Orchestrator mode. ↩
- This summary is passed via the result parameter of the attempt_completion tool when the subtask finishes. ↩
This summary is passed via the result parameter of the attempt_completion tool when the subtask finishes. ↩
- Why Use Boomerang Tasks?
- How It Works
- Key Considerations
- Frequently Asked Questions Why can't Orchestrator mode read files, write files, call MCPs, or run commands? How can I override Orchestrator mode's limitations?
- Why can't Orchestrator mode read files, write files, call MCPs, or run commands?
- How can I override Orchestrator mode's limitations?

--------------------