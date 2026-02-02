# https://forums.ankiweb.net/t/casting-a-spell-on-chatgpt-let-it-write-anki-cards-for-you-a-prompt-engineering-case/27907
**URL:** https://forums.ankiweb.net/t/casting-a-spell-on-chatgpt-let-it-write-anki-cards-for-you-a-prompt-engineering-case/27907
**Page Title:** Casting a spell on ChatGPT: Let it write Anki cards for you — A Prompt Engineering Case - Anki / Add-ons - Anki Forums
--------------------

- Topics
- Anki
- AnkiDroid (Android)
- AnkiMobile (iPhone/iPad)
- All categories
Welcome! This is a place to discuss Anki, and ask any questions you may have. Before asking a question, please see these instructions .
[LINK: these instructions](https://docs.ankiweb.net/getting-help.html)

## Casting a spell on ChatGPT: Let it write Anki cards for you — A Prompt Engineering Case

You have selected 0 posts.
select all
cancel selecting

## post by L.M.Sherlock on Feb 26, 2023

I meant to take a break today, but my hands itched. It’s been a while since I produced original writing, so I want to share my lessons on tinkering with ChatGPT recently.
If you have read my Reddit post — AnkiGPT: teach ChatGPT to create cards for you , you may be impressed by the flashcards made by ChatGPT:
You may wonder how I teach ChatGPT to make flashcards. Let me show you how to instruct ChatGPT to succeed step by step with some basic techniques of Prompt Engineering.
Prompts involve instructions and context passed to a language model to achieve a desired task. Prompt engineering is the practice of developing and optimizing prompts to efficiently use language models (LMs) for a variety of applications.

## Basic Prompt

To begin with, what’s the first prompt that comes to your mind if you want to make ChatGPT create flashcards for you? As the simplest form:
Me: balabalabala (a text). I want you to create a deck of flashcards from the above text.
However, this prompt didn’t work well:
It looks like ChatGPT understands the concept of flashcards. But the flashcards it made had lengthy answers. This stands against the Minimum Information Principle and is impossible to memorize.
Let’s improve on the prompt and specify our requirements for flashcards:
The result:
Turns out the generated cards have shorter answers than before. Maybe some of you find it good enough, but I see some room for improvement. What’s next? Give ChatGPT some examples!

## Few-shot prompts

There is a classic example of writing good cards, i.e. the 20 rules proposed by SuperMemo:
Let’s try teaching ChatGPT with this example:
As expected, ChatGPT got what I wanted to do, and it created two more cards making the result well-around:
Is there any other way to improve it?

## Chain-of-Thought (CoT) Prompting

Don’t forget that there is something called the Chain of Thought ability. Given some reasoning, ChatGPT generates better results. Therefore, we can teach him how to create flashcards step by step to meet our needs (To keep the example short, I removed the few-shot examples, which helps you observe the effect of CoT on its own )
Now ChatGPT knows how to keep the answer short and easy to understand:
Could it be better? I applied Few-shot and Chain-of-Thought together and got the following results:
They feel much better than the original cards! Of course, this prompt can also be improved, so I’ll leave this task to you.

## Adjust the output format

So how do you get ChatGPT to output a table? It’s really simple, just add an extra step in Chain-of-Thought to instruct ChatGPT to output in the specified format. Or in Few-shot, change the example to the output format you want.
Then ChatGPT learned:

## Importing the cards into Anki

Although ChatGPT is so smart at making cards, you can’t just copy and paste them one by one into Anki, right? What a bummer!
In fact, many people don’t know that Anki can import .csv table files. And ChatGPT output table can be directly pasted into Excel!
Then save it in .csv format:
Open Anki and click Import:
Open the .csv file that you just saved, choose Basic template, choose what deck you want to import into, and click Import:
The final result:
I hope this tutorial will be helpful to you.

## References

Prompt engineering guides：
dair-ai/Prompt-Engineering-Guide: Guides, papers, lecture, and resources for prompt engineering (github.com)
[LINK: dair-ai/Prompt-Engineering-Guide: Guides, papers, lecture, and resources for prompt engineering (github.com)](https://github.com/dair-ai/Prompt-Engineering-Guide)
Principles of writing good cards:
20 rules of formulating knowledge in learning
How to write good prompts: using spaced repetition to create understanding (andymatuschak.org)
By the way, I have also developed a new spaced repetition algorithm for Anki:
open-spaced-repetition/fsrs4anki: A modern Anki custom scheduling based on free spaced repetition scheduler algorithm (github.com)
[LINK: open-spaced-repetition/fsrs4anki: A modern Anki custom scheduling based on free spaced repetition scheduler algorithm (github.com)](https://github.com/open-spaced-repetition/fsrs4anki)
This tutorial is posted firstly in my medium:
Casting a spell on ChatGPT: Let it write Anki cards for you — A Prompt Engineering Case | by Jarrett Ye | Feb, 2023 | Medium
- Collection of Anki Resources

## post by HerrHopster on Apr 28, 2023

## post by a_m9216 on Apr 28, 2023

## post by nilsreichardt on May 27, 2023

## post by neribr on May 27, 2023

## post by krstoevan on May 27, 2023

## post by katlylon on Mar 15, 2024

## post by krstoevan on Mar 16, 2024

## post by krstoevan on Mar 16, 2024

### Related topics


--------------------