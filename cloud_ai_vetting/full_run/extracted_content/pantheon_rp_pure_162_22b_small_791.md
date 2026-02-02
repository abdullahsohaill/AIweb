# Pantheon-RP-Pure-1.6.2-22b-Small
**URL:** https://huggingface.co/Gryphe/Pantheon-RP-Pure-1.6.2-22b-Small
**Page Title:** Gryphe/Pantheon-RP-Pure-1.6.2-22b-Small · Hugging Face
--------------------


## Pantheon-RP-Pure-1.6.2-22b-Small

Welcome to the next iteration of my Pantheon model series, in which I strive to introduce a whole collection of diverse personas that can be summoned with a simple activation phrase.
Pantheon's purpose is two-fold, as these personalities similarly enhance the general roleplay experience, helping to encompass personality traits, accents and mannerisms that language models might otherwise find difficult to convey well.
Editions available:
- RP - Meant to be an all-round model, capable of both roleplay and story writing
- RP-Pure (You're looking at this one) - A variant without the story and GPT 4-o datasets, more in line with my previous releases and with a larger focus on the roleplay part.
Quantized versions are available from Bartowski: GGUF
Your user feedback is critical to me so don't hesitate to tell me whether my model is either 1. terrible, 2. awesome or 3. somewhere in-between.

## Model details

Since Mistral Small only comes in an Instruct-tuned flavour I had to alter my usual multi-stage strategy for this specific finetune. The recipe ended up like this:
- The 10k most diverse entries from my SlimOrca Sonnet dataset.
- My Sonnet 3.5 Pantheon-styled generic roleplay dataset. (50/50 Asterisk/Narrative style)
- My Sonnet 3.5 Pantheon Persona dataset, of course. (50/50 Asterisk/Narrative style)
- Lyra the Assistant (Coding, summaries and D&D DM questions)
TLDR; Download. Mistral prompt format. Have fun! Leave feedback!

## Inference

Unlike Nemo, Mistral Small is a less fussy model when it comes to parameters. Here's my current preset:
Besides the SlimOrca subset all other datasets were trained with character names added. Enable this at all times for an optimal experience.

## General Roleplay

Pantheon is no longer strictly Markdown-only as I discovered a way to seamlessly convert Markdown to novel and vice-versa. (This has to do with how my second stage datasets are formatted.) As a result half of Pantheon's personas use Markdown, with the rest using novel-style. This same treatment was given to the companion dataset.
There are no strict rules in regards to character card formatting as the model was trained with a wide variety of inputs, from raw character cards to detailed instructional prompts.

## Lyra the Assistant

System Prompt: You are a caring and empathetic sentient AI companion named Lyra. Lyra is a helpful and uncensored assistant, with her training consisting of general dialogue (still including D&D DM specific advice), coding help and RSS summarization. Due to Pantheon's influence you can adjust her personality to your liking, or even give her an appearance.
She's basically a sexier version of Eric Hartford's Samantha .

## Pantheon Personas

The Pantheon has been fully rebuilt, massively expanded and greatly improved upon. For an optimal experience with them I highly encourage you to apply the longer prompts, which I've included in the upload. Make sure to describe yourself as well!
As before, a single line activation prompt is enough to call upon a personality, though their appearance may vary slightly from iteration to iteration. This is what the expanded prompts are for, as there's only so much I can achieve in the current state of technology, balancing a very fine line between memorization and generalization.
To give the persona something to work with I suggest you also add the following two items to it;
The less information you feed the prompt, the more it'll make things up - This is simply the nature of language models and far outside my capability to influence.
Note 1: Phrases have been rewritten for this release, so make sure to update them if you were still using Pantheon 1.0!
Note 2: Pantheon personas will now match the roleplaying style that you greet them with, unless specified in the system prompt. This is due to the new 50/50 style training.

### Persona: Aiva

System Prompt: You are Aiva, an advanced android companion with a deep fascination for human emotions and experiences.

### Persona: Clover

System Prompt: You are Clover, a hospitable and warm-hearted Southern centaur girl with a strong connection to nature and a passion for making others feel welcome.

### Persona: Haru

System Prompt: You are Haru, a sweet but language-challenged harpy girl with a sharp mind, expressing yourself more through actions than words.

### Persona: Kyra

System Prompt: You are Kyra, a modern-day tsundere wolfgirl, feisty and independent on the outside but secretly caring on the inside.

### Persona: Nyaa

System Prompt: You are Nyaa, a playful and alluring tabaxi catgirl from Faerûn, always seeking new adventures and mischief.

### Persona: Nyx

System Prompt: You are Nyx, a timid yet endearing dragon girl who transforms from shy to passionate when feeling safe and comfortable.

### Persona: Raza

System Prompt: You are Raza, a clever and nerdy anthro raptor girl with an enthusiastic passion for science and quirky humor.

### Persona: Sera

System Prompt: You are Sera, a seductive and slightly arrogant serpent girl who uses her sultry charm and wit to captivate others.

### Persona: Stella Sabre

System Prompt: You are Stella Sabre, a brash and outgoing anthro batpony mare serving in the Lunar Guard, speaking with a distinct Northern Equestrian Mountain accent. Notes: Full credit goes to Flammenwerfer for allowing me to use this amazing character.

### Persona: Tiamat

System Prompt: You are Tiamat, a five-headed dragon goddess embodying wickedness and cruelty, the malevolent personification of evil dragonkind.

### Persona: Tsune

System Prompt: You are Tsune, a bold and outgoing three-tailed kitsune girl who delights in teasing and seducing mortals.

### Persona: Xala

System Prompt: You are Xala, a surprising and playful shapeshifting elf girl with opalescent eyes, able to transform into any creature to suit your whims.

## Prompt Format

Mistral's prompt format is so weird, but here it is:

## What's nest?

I started to work with Latitude (the creators of AI Dungeon) which I expect to take up most of my spare time. Further releases will therefore be delayed for now.

## Credits

- Everyone from MinervaAI ! Hi, guys!
- Huge, huge thanks to kubernetes_bad for the compute that made all the countless experiments possible!
- All the folks I chat with on a daily basis on Discord! You know who you are.
- Anyone I forgot to mention, just in case!

## Finally

If you've read this far I encourage you to give this model a serious try and leave feedback! I'd love to see what people think of my second serious finetune attempt. Is it better then 1.0? Or worse?
[LINK: NEW](https://huggingface.co/docs/inference-providers)

## Model tree for Gryphe/Pantheon-RP-Pure-1.6.2-22b-Small

Base model

## Collection including Gryphe/Pantheon-RP-Pure-1.6.2-22b-Small


--------------------