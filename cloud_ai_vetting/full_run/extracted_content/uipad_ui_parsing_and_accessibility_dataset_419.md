# UiPad: UI Parsing and Accessibility Dataset
**URL:** https://huggingface.co/datasets/MacPaw/uipad
**Page Title:** macpaw-research/UiPad · Datasets at Hugging Face
--------------------


## UiPad - UI Parsing and Accessibility Dataset

- Curated by: MacPaw Way Ltd.
- Language(s): Mostly EN, UA
- License: MIT
Overview UiPad is a dataset created for the IASA Champ 2024 Challenge , focusing on the accessibility and interface understanding of MacOS applications. With growing interest in AI-driven user interface analysis, the dataset aims to bridge the gap in available resources for desktop app accessibility. While mobile apps and web platforms benefit from datasets like RICO and Mind2Web, MacOS apps remain mostly underexplored, particularly regarding accessibility parsing and textual representation.

## Dataset Structure

UiPad contains 352 unique screens from 63 different MacOS applications. Of these, 68% include accessibility data in the form of JSON trees. A screenshot accompanies each app screen and, if available, a JSON file detailing the accessibility elements.
Screenshot PNG image of the app screen
Accessibility Tree Data The accessibility tree captures essential UI elements such as:
- name : Element name
- role : The role of the UI element (e.g., button, image)
- description and role_description
- value : Element state or value
- children : Nested UI components
- bbox and visible_bbox : Bounding box coordinates of elements
Questions (for evaluation)
The dataset includes several types of questions to evaluate UI understanding:
- Numeric: "How many checkboxes are checked on the screen?" (485 instances)
- Yes/No: "Is there a '+' button on the screen?" (306 instances)
- String: "What is the name of the app on the screen?" (143 instances)
- Coordinate: "Where do I click to connect Gmail?" (122 instances)
The dataset provides real-world challenges in accessibility recognition. Some screens may lack full accessibility support, with common issues like misidentifying roles (e.g., a button as an image), inaccurate bboxes or missing selected states.
Task and Objectives
UiPad's primary goal is to create an AI agent that understands and enhances UI accessibility in MacOS scenarios. The quality of the generated UI representation and the effectiveness of the AI agent are measured using Question Answering tasks related to UI understanding.
Limitations and Challenges
- Accessibility data may be incomplete, redundant or missing.
- The dataset size is limited, which may not be sufficient for training models from scratch.
- Human labelling of the Q/A introduces the potential for errors.
Dataset Card Contact
Feel free to reach out tech-research@macpaw.com if you have any questions or need further information about the dataset!

--------------------