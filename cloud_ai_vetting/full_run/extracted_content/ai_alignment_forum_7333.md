# AI Alignment Forum
**URL:** https://www.alignmentforum.org
**Page Title:** AI Alignment Forum
--------------------

This post is a not a so secret analogy for the AI Alignment problem. Via a fictional dialog, Eliezer explores and counters common questions to the Rocket Alignment Problem as approached by the Mathematics of Intentional Rocketry Institute. MIRI researchers will tell you they're worried that "right now, nobody can tell you how to point your rocket’s nose such that it goes to the moon, nor indeed any prespecified celestial destination."

## The 2024 Review Final Voting

### The 2024 Review

## Final Voting

## AI Alignment Posts

## Popular Comments

## Recent Discussion

mostly it does not match my practical experience so far
I mostly wouldn't expect it to at this point, FWIW. The people engaged right now are by and large people sincerely grappling with the idea, and particularly people who are already bought into takeover risk. Whereas one of the main mechanisms by which I expect misuse of the idea is that people who are uncomfortable with the concept of "AI takeover" can still classify themselves as part of the AI safety coalition when it suits them.
As an illustration of this happening to Paul's worldview, see this Vox ar ... (read more)
As we develop new techniques for detecting deceptive alignment, ranging from action monitoring to Chain-of-Thought (CoT) or activations monitoring, we face a dilemma: once we detect scheming behaviour or intent, should we use that signal to "train the scheming out"?
On the one hand, leaving known misaligned behaviour / intent in the model is not marginally informative and possibly unsafe. On the other hand, training against a monitor might not actually fix the model's underlying motivations; it might simply provide selection pressure that favours more sophisticated, less detectable forms of deception.
This post outlines a simple framework formalising when the generalisation benefit of training outweighs the selection risk of creating a schemer. I assume that the choice is between training and not training on the incriminating examples, e.g. we...
I don't think it's that crazy to train against examples surfaced by a scheming monitor. For example, for diffuse threats (that happen a lot, and that aren't very harmful individually - e.g. sandbagging), async monitoring + training against the examples seems like a reasonable response. There's not much use continuing to see the same failures and there are good reasons to get rid of them - e.g. being able to more confidently use the model for safety research. So I'm not sure always keeping monitors separate from training is practical, or correct.
My hope for... (read more)

## Tl;dr

AI alignment has a culture clash. On one side, the “technical-alignment-is-hard” / “rational agents” school-of-thought argues that we should expect future powerful AIs to be power-seeking ruthless consequentialists. On the other side, people observe that both humans and LLMs are obviously capable of behaving like, well, not that. The latter group accuses the former of head-in-the-clouds abstract theorizing gone off the rails, while the former accuses the latter of mindlessly assuming that the future will always be the same as the present, rather than trying to understand things. “Alas, the power-seeking ruthless consequentialist AIs are still coming,” sigh the former. “Just you wait.”
As it happens, I’m basically in that “alas, just you wait” camp, expecting ruthless future AIs. But my camp faces a real question: what exactly is it...
Like, a discussion might go:
Optimist: If you pick some random thing, there is no reason at all to expect that thing to be a ruthless sociopath. It’s an extraordinarily weird and unlikely property.
Me: Yes I happily concede that point.
O : You do? So why are you worried about ASI x-risk?
Me: Well if you show me some random thing, it’s probably, like, a rock or something. It’s not sociopathic, but only because it’s not intelligent at all.
O: Well, c’mon, you know what I mean. If you pick some random mind ,  there is no reason at all to expect it to be a ruthl... (read more)
I honestly didn't think of that at all when making the market, because I think takeover-capability-level AGI by 2028 is extremely unlikely.
I care about this market insofar as it tells us whether (people believe) this is a good research direction. So obviously it's perfectly ok to resolve YES if it is solved and a lot of the work was done by AI assistants. If AI fooms and murders everyone before 2028 then this is obviously a bad portent for this research agenda, because it means we didn't get it done soon enough, and it's little comfort if the ASI sol... (read more)
This was written for the Vignettes Workshop . [1] The goal is to write out a detailed future history (“trajectory”) that is as realistic (to me) as I can currently manage, i.e. I’m not aware of any alternative trajectory that is similarly detailed and clearly more plausible to me. The methodology is roughly: Write a future history of 2022. Condition on it, and write a future history of 2023. Repeat for 2024, 2025, etc. (I'm posting 2022-2026 now so I can get feedback that will help me write 2027+. I intend to keep writing until the story reaches singularity/extinction/utopia/etc.)
What’s the point of doing this? Well, there are a couple of reasons:
- Sometimes attempting to write down a concrete example causes you to learn things, e.g. that a possibility is more
In light of Anthropic's Constitution and xAI's attempts to be 'Based', now I wonder if my original prediction was correct after all. We'll see.
A new version of “Intro to Brain-Like-AGI Safety” is out!

## Things that have not changed

Same links as before :
- As a series of 15 blog posts on LessWrong / Alignment Forum: https://www.lesswrong.com/s/HzcM2dkCq7fwXBej8
- As a 225-page PDF (now up to version 3): https://osf.io/preprints/osf/fe36n
- Summary video: Video & transcript: Challenges for Safe & Beneficial Brain-Like AGI
…And same abstract as before :
Suppose we someday build an Artificial General Intelligence algorithm using similar principles of learning and cognition as the human brain. How would we use such an algorithm safely?
I will argue that this is an open technical problem, and my goal in this post series is to bring readers with no prior knowledge all the way up to the front-line of unsolved problems as I see them.
Post #1 contains definitions, background, and motivation. Then Posts #2 – #7

--------------------