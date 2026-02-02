# https://engineering.berkeley.edu/news/2025/03/brain-to-voice-neuroprosthesis-restores-naturalistic-speech/
**URL:** https://engineering.berkeley.edu/news/2025/03/brain-to-voice-neuroprosthesis-restores-naturalistic-speech
**Page Title:** Brain-to-voice neuroprosthesis restores naturalistic speech - Berkeley Engineering
--------------------


## Brain-to-voice neuroprosthesis restores naturalistic speech

Marking a breakthrough in the field of brain-computer interfaces (BCIs), a team of researchers from UC Berkeley and UC San Francisco has unlocked a way to restore naturalistic speech for people with severe paralysis.
This work solves the long-standing challenge of latency in speech neuroprostheses, the time lag between when a subject attempts to speak and when sound is produced. Using recent advances in artificial intelligence-based modeling, the researchers developed a streaming method that synthesizes brain signals into audible speech in near-real time.
As reported today in Nature Neuroscience , this technology represents a critical step toward enabling communication for people who have lost the ability to speak. The study is supported by the National Institute on Deafness and Other Communication Disorders (NIDCD) of the National Institutes of Health.
“Our streaming approach brings the same rapid speech decoding capacity of devices like Alexa and Siri to neuroprostheses,” said Gopala Anumanchipalli, Robert E. and Beverly A. Brooks Assistant Professor of Electrical Engineering and Computer Sciences at UC Berkeley and co-principal investigator of the study. “Using a similar type of algorithm, we found that we could decode neural data and, for the first time, enable near-synchronous voice streaming. The result is more naturalistic, fluent speech synthesis.”
“This new technology has tremendous potential for improving quality of life for people living with severe paralysis affecting speech,” said UCSF neurosurgeon Edward Chang, senior co-principal investigator of the study. Chang leads a clinical trial at UCSF that aims to develop speech neuroprosthesis technology using high-density electrode arrays that record neural activity directly from the brain surface. “It is exciting that the latest AI advances are greatly accelerating BCIs for practical real-world use in the near future,” he said.
The researchers also showed that their approach can work well with a variety of other brain sensing interfaces, including microelectrode arrays (MEAs) in which electrodes penetrate the brain’s surface, or non-invasive recordings (sEMG) that use sensors on the face to measure muscle activity.
“By demonstrating accurate brain-to-voice synthesis on other silent-speech datasets, we showed that this technique is not limited to one specific type of device,” said Kaylo Littlejohn, Ph.D. student at UC Berkeley’s Department of Electrical Engineering and Computer Sciences and co-lead author of the study. “The same algorithm can be used across different modalities provided a good signal is there.”
Decoding neural data into speech
According to study co-lead author Cheol Jun Cho, who is also a UC Berkeley Ph.D. student in electrical engineering and computer sciences, the neuroprosthesis works by sampling neural data from the motor cortex, the part of the brain that controls speech production, then uses AI to decode brain function into speech.
“We are essentially intercepting signals where the thought is translated into articulation and in the middle of that motor control,” he said. “So what we’re decoding is after a thought has happened, after we’ve decided what to say, after we’ve decided what words to use and how to move our vocal-tract muscles.”
To collect the data needed to train their algorithm, the researchers first had Ann, their subject, look at a prompt on the screen — like the phrase: “Hey, how are you?” — and then silently attempt to speak that sentence.
“This gave us a mapping between the chunked windows of neural activity that she generates and the target sentence that she’s trying to say, without her needing to vocalize at any point,” said Littlejohn.
Because Ann does not have any residual vocalization, the researchers did not have target audio, or output, to which they could map the neural data, the input. They solved this challenge by using AI to fill in the missing details.
“We used a pretrained text-to-speech model to generate audio and simulate a target,” said Cho. “And we also used Ann’s pre-injury voice, so when we decode the output, it sounds more like her.”
Streaming speech in near real time
In their previous BCI study , the researchers had a long latency for decoding, about an 8-second delay for a single sentence. With the new streaming approach, audible output can be generated in near-real time, as the subject is attempting to speak.
To measure latency, the researchers employed speech detection methods, which allowed them to identify the brain signals indicating the start of a speech attempt.
“We can see relative to that intent signal, within 1 second, we are getting the first sound out,” said Anumanchipalli. “And the device can continuously decode speech, so Ann can keep speaking without interruption.”
This greater speed did not come at the cost of precision. The faster interface delivered the same high level of decoding accuracy as their previous, non-streaming approach.
“That’s promising to see,” said Littlejohn. “Previously, it was not known if intelligible speech could be streamed from the brain in real time.”
Anumanchipalli added that researchers don’t always know whether large-scale AI systems are learning and adapting, or simply pattern-matching and repeating parts of the training data. So the researchers also tested the real-time model’s ability to synthesize words that were not part of the training dataset vocabulary — in this case, 26 rare words taken from the NATO phonetic alphabet, such as “Alpha,” “Bravo,” “Charlie” and so on.
“We wanted to see if we could generalize to the unseen words and really decode Ann’s patterns of speaking,” he said. “We found that our model does this well, which shows that it is indeed learning the building blocks of sound or voice.”
Ann, who also participated in the 2023 study, shared with researchers how her experience with the new streaming synthesis approach compared to the earlier study’s text-to-speech decoding method.
“She conveyed that streaming synthesis was a more volitionally controlled modality,” said Anumanchipalli. “Hearing her own voice in near-real time increased her sense of embodiment.”
Future directions
This latest work brings researchers a step closer to achieving naturalistic speech with BCI devices, while laying the groundwork for future advances.
“This proof-of-concept framework is quite a breakthrough,” said Cho. “We are optimistic that we can now make advances at every level. On the engineering side, for example, we will continue to push the algorithm to see how we can generate speech better and faster.”
The researchers also remain focused on building expressivity into the output voice to reflect the changes in tone, pitch or loudness that occur during speech, such as when someone is excited.
“That’s ongoing work, to try to see how well we can actually decode these paralinguistic features from brain activity,” said Littlejohn. “This is a longstanding problem even in classical audio synthesis fields and would bridge the gap to full and complete naturalism.”
In addition to the NIDCD, support for this research was provided by the Japan Science and Technology Agency’s Moonshot Research and Development Program, the Joan and Sandy Weill Foundation, Susan and Bill Oberndorf, Ron Conway, Graham and Christina Spencer, the William K. Bowes, Jr. Foundation, the Rose Hills Innovator and UC Noyce Investigator programs, and the National Science Foundation.
View the study for additional details and a complete list of co-authors.
For more information
- Novel brain implant helps paralyzed woman speak using a digital avatar
- How artificial intelligence gave a paralyzed woman her voice back

--------------------