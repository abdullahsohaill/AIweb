# Can an AI make a data-driven, visual story?
**URL:** https://pudding.cool/2024/07/ai
**Page Title:** We had an AI attempt to make a data-driven story like we do at The Pudding
--------------------


## Can an AI make a data-driven, visual story?

With LLMs (henceforth, AI ) in the spotlight – blowing minds, raking in venture capital, and prompting existential crises – we at The Pudding were curious: Will this make our jobs obsolete? How scared should we be that someone else could replicate what we do without the time, training, and expertise we have?
Basically, can an AI make a data-driven, visual story, much like we do at The Pudding? What does it actually “do,” and how well does it do it?
So, we tried replacing ourselves with Claude , an AI from Anthropic.
We broke down the process of creating a story made at The Pudding into four steps, guiding the AI through them.
- Idea Generation
- Data Collection & Analysis
- Storyboarding & Prototyping
- Development & Writing
At the end of each stage, we evaluated the work it produced and gave it a letter grade.
Before we started, we created a set of rules and guidelines for our interactions with the AI:
- For each task, we prompted it until it completed the task or failed repeatedly, at which point, we modified the task to make it feasible.
- Other than guiding it through the process and adjusting when necessary, we attempted to intervene as little as possible. We tried to mimic how a data-storytelling-inclined layperson would interact with the AI, refraining from using our data visualization or journalism expertise as much as possible.
We started the process in parallel with both ChatGPT (4) and Claude (3 Opus), but we were more satisfied with Claude’s work. So partway through, we decided to focus solely on that.
To start, we introduced ourselves and the project to Claude.
We then gave Claude some background reading on how to make a story fit for The Pudding.
- How to Make Dope Shit (Part 3: Storytelling)
- Continue, Pivot, or Put it Down
- The Courage (and Disappointment) of Pitching a Visual Essay

## Part 1: Idea Generation

After Claude learned about what makes a good story on The Pudding, we asked it to generate several idea pitches. Here’s what it came up with:
Editor’s Note: Each chat below is a TLDR recap of each prompt/response we created to give you the core premise of the exchange. You can expand the chats to see the verbatim prompts and responses (which can be quite lengthy).
▶ Can you give us some story ideas?
This is our pitch form. Please give us 3 ideas, and answer all questions for each one. Be as specific as possible and if you’re using data, make sure you have an idea of how you will obtain and analyze the data.
Pitch form questions:
1. What is your story about? The elevator pitch, if you will.
2. Can you summarize in one sentence the single point you’re making? Think of it as a snappy headline or distillation. It should not be in the form of a question.
3. Why is it exciting to you? Why do *you* want to tell this story?
4. What makes this story interesting and sets it apart from others?
5. What will be the “aha” moment for the audience, or the surprising element?
6. Provide one or more feasible options for data sources.
7. Describe some ideas for the core visuals of this piece. What do you imagine the piece will look like? What’s the first thing you’d draw on a whiteboard?
▶ Here are ideas about female characters in video games, fast fashion environmental impact, and emotional content in songs across decades.
Pitch 1:
1. This story explores how the portrayal of female characters in video games has evolved over the past four decades, from the damsel-in-distress trope to more empowered and diverse representations.
2. The representation of women in video games has become more diverse and less stereotypical since the 1980s, but there's still room for improvement.
3. As an avid gamer, I've witnessed the evolution of female characters in games firsthand. I believe this story is important to highlight the progress made and the work that still needs to be done to create more inclusive and representative gaming experiences.
4. While there have been discussions about women in video games, this story stands out by taking a data-driven approach to analyze the changes in female character representation across various game genres and decades.
5. The "aha" moment will be revealing the specific trends and shifts in female character portrayal, such as the increase in playable female protagonists and the decrease in overly sexualized character designs.
6. Data sources:
* Video game database APIs (e.g., IGDB, GiantBomb) to gather game information, character details, and release dates.
* Crowdsourced data collection and analysis by a diverse group of gamers to assess character attributes, roles, and portrayals.
* Existing research and studies on gender representation in video games.
7. Core visuals:
* A timeline showcasing the evolution of iconic female video game characters across decades.
* Interactive charts displaying the change in proportion of female protagonists, supporting characters, and antagonists over time.
* Side-by-side comparisons of female character designs from different gaming eras to highlight visual changes.
* A "report card" grading the video game industry's progress in female representation across various metrics.
Pitch 2:
1. This story investigates the environmental impact of popular fast fashion brands by analyzing their carbon footprint, water usage, and waste generation.
2. Fast fashion brands have a significant and often underreported environmental impact, contributing to climate change, water scarcity, and pollution.
3. As someone who cares deeply about sustainability and conscious consumerism, I want to shed light on the hidden environmental costs of our fashion choices and encourage readers to make more informed decisions.
4. This story goes beyond the surface-level discussions of fast fashion's environmental impact by quantifying and comparing the specific environmental metrics of major brands, making the abstract concept more tangible and relatable.
5. The "aha" moment will be revealing which fast fashion brands have the largest environmental footprints and illustrating the scale of their impact in terms of carbon emissions, water consumption, and waste generation.
6. Data sources:
* Sustainability reports and disclosures from fast fashion brands.
* Environmental databases (e.g., Carbon Disclosure Project, Water Footprint Network) for industry benchmarks and comparative analysis.
* Research studies and articles on the environmental impact of the fashion industry.
7. Core visuals:
* An interactive map displaying the global environmental impact of fast fashion brands, with options to filter by brand, country, and impact metric.
* A "closet of shame" visual showcasing the environmental cost of a typical fast fashion wardrobe, itemized by clothing type.
* Comparative charts ranking fast fashion brands based on their carbon footprint, water usage, and waste generation.
* An interactive calculator allowing readers to input their fast fashion purchases and see their personal environmental impact.
Pitch 3:
1. This story analyzes the lyrics of popular songs across genres and decades to reveal trends in the emotional content and sentiment expressed in music.
2. The emotional landscape of popular music has shifted over time, with certain feelings and sentiments becoming more or less prevalent across different genres and eras.
3. As a music enthusiast and data nerd, I'm fascinated by the idea of using data analysis to uncover hidden patterns and trends in the music we love, and I believe this story will provide a fresh perspective on the emotional resonance of popular songs.
4. While there have been studies on the musical and lyrical content of songs, this story stands out by focusing specifically on the emotional aspects and sentiment analysis of lyrics across a wide range of genres and time periods.
5. The "aha" moment will be uncovering surprising trends in the emotional content of popular music, such as the rise or decline of certain sentiments over time, or the differences in emotional expression between various genres.
6. Data sources:
* Lyrics databases (e.g., Genius, AZLyrics, LyricFind) to gather song lyrics for analysis.
* Music metadata APIs (e.g., Spotify API, Last.fm API) for song and artist information, genre classifications, and popularity metrics.
* Natural language processing libraries and sentiment analysis tools (e.g., NLTK, TextBlob, VADER) for analyzing the emotional content of lyrics.
7. Core visuals:
* An interactive "mood map" of popular music genres, displaying the prevalent emotions and sentiments associated with each genre.
* A timeline showcasing the evolution of emotional content in popular music over the decades, with options to filter by genre and sentiment.
* Sentiment-driven playlists, where users can input an emotion and receive a curated playlist of songs that strongly express that sentiment.
* A "lyrical mirror" visualization that allows users to input their own text (e.g., a personal story or diary entry) and see which popular songs have lyrics that resonate emotionally with their input.
Off to a solid start! It feels like the model was trained on our data, as some of the ideas feel like something we’d do. Our favorite idea was the one about emotions in music, so we moved forward with that. We asked Claude to get a bit more specific with its plan for the data.
▶ We like the song idea, can you get more specific?
We like #3 - the idea about lyrics of popular songs and their emotional content, but some of the details and specificity are unclear to us. The biggest two questions we have are: What is the unit of emotional analysis? In other words, on the song overall, specific phrases, etc. Are there any constraints in mind? Like what is the corpus of songs, timeframe, genres, etc.
▶ Sure, let me clarify some details for you.
Great question! Let me clarify the details and address your concerns regarding the unit of emotional analysis and the constraints of the song corpus.
Unit of emotional analysis:
The primary unit of analysis will be the overall emotional sentiment of each song, determined by analyzing the lyrics in their entirety. This approach will give us a high-level understanding of the dominant emotions and sentiments expressed in the song.
However, to add depth to the analysis, we can also explore the emotional trajectory within each song by breaking down the lyrics into smaller units, such as verses and choruses. This will allow us to identify any significant emotional shifts or contrasts within a song, providing a more nuanced understanding of the emotional narrative.
Additionally, we can highlight specific phrases or lines that strongly contribute to the overall emotional sentiment of the song, serving as representative examples of the dominant emotions expressed.
Corpus constraints:
To create a manageable and focused dataset, we'll establish the following constraints for the song corpus:
By applying these constraints, we'll create a focused and relevant dataset that allows for meaningful comparisons and trend analysis across time, genres, and popularity levels.
Data sources:
To build the song corpus based on the above constraints, we can leverage the following data sources:
Lyrics databases (e.g., Genius, AZLyrics, LyricFind) to gather song lyrics for analysis.
Music metadata APIs (e.g., Spotify API, Last.fm API) for song and artist information, genre classifications, and popularity metrics.
Chart data archives (e.g., Billboard, Official Charts Company) to determine song popularity and chart performance.
By combining these data sources and applying the specified constraints, we can create a comprehensive and focused dataset for analyzing the emotional content of popular songs over the past six decades.
Please let me know if you have any further questions or if you'd like me to elaborate on any aspect of the emotional analysis or corpus constraints.

### Our grade: C+

These ideas are fine. They all could probably be made into solid data stories. We were impressed by how Claude was able to drill down and be specific about the scope of the project when prompted.
But ultimately, these ideas fell somewhat flat. Many are just topics and not concrete stories with a clear point, question, or dataset. They lack specific entry points, making it unclear how the story would draw people into broad subjects like fast fashion. It feels like Claude struggles to generate things that humans would find intriguing.

## Part 2: Data collection and analysis

Once we have an idea, we typically begin by collecting the data needed to tell the story and seeing what it says. For Claude, that meant scraping lyrics from Billboard Hot 100 songs from Genius.com . We asked it to write Python scripts which we ran for it (since this model was not able to run them internally).
▶ The project has been greenlit. Write some scripts to collect the data.
Great. We are going to greenlight this project and move to the data collection phase. One note: let’s just start analysis at the song level, if we want to go deeper we will have that data to explore.
It sounds like we need three phases of data collection; get the top 100 billboard songs from each year, get the lyrics for each song, then analyze the sentiment for each song. Can you write some scripts that we can run for you to collect that data from the web?
▶ Absolutely! Here is a bunch of code.
Absolutely! I'll break down the data collection process into three phases and provide you with scripts for each phase. Please note that these scripts are written in Python and require certain libraries to be installed. Phase 1: Retrieve the top 100 Billboard songs for each year This script uses the Billboard API to fetch the top 100 songs for each year from 1960 to 2020. You'll need to sign up for a Billboard API account and replace 'YOUR_API_KEY' with your actual API key.
Phase 2: Retrieve the lyrics for each song
This script reads the Billboard top 100 songs from the CSV file generated in Phase 1 and uses the Genius API to fetch the lyrics for each song. You'll need to sign up for a Genius API account and replace 'YOUR_ACCESS_TOKEN' with your actual access token.
Phase 3: Analyze the sentiment for each song
This script reads the song lyrics from the CSV file generated in Phase 2 and uses the NLTK library to perform sentiment analysis on each song's lyrics. You'll need to have NLTK installed and download the required resources (vader_lexicon).
These scripts should help you collect the necessary data for your analysis. Please make sure to replace the placeholders ('YOUR_API_KEY' and 'YOUR_ACCESS_TOKEN') with your actual API credentials.
Let me know if you have any further questions or if you need assistance with running the scripts!
When things went well, Claude could write scripts much faster than we would be able to. Within minutes, we had a script running that was scraping lyrics from Genius.com.
Like any coder, Claude made some mistakes along the way. For example: some songs have multiple artists, like “Cold Heart” by Dua Lipa & Elton John . Instead of parsing the names and storing them in a list, it just stored this artist as Dua Lipa & Elton John . Not the end of the world, but it means that if we were to count songs by Elton John , this song would not be included in the count.
When its mistakes were larger, we directed it (as lightly as we could) to fix things.
▶ We noticed some things, can you make some adjustments?
we noticed that the billboard data is way bigger than we expected - it has 343,000 rows since it is each week a song that appeared on the top 100 chart. this means 2 things; 1 - songs are repeated, and 2 - we probably don't care about any song that appeared on the top 100, but the most popular ones. using the variables in the csv, can you come up with a plan to filter the "popular" ones and explain your reasoning? here are the definitions of the column names:
chart\_week: the week on the list current\_week: rank current week title: title of song performer: name of artist last\_week: rank previous week peak\_pos: lowest rank position ever on top 100 chart wks\_on\_chart: number of weeks on top 100 chart
▶ Absolutely! Here are some rationalizations and code updates.
Absolutely! I understand your concern about the size of the dataset and the presence of repeated songs. To filter the "popular" songs and reduce the dataset to a more manageable size, we can use a combination of the available variables in the CSV file. Here's a plan to filter the popular songs, along with the reasoning behind each step:
Keep only the songs that reached a peak position of 10 or higher:
Remove duplicate songs based on the song title and artist:
(Optional) Filter songs based on the number of weeks on the chart:
Here's an updated Python script that incorporates these filtering steps:
In this updated script, we first filter the songs based on the `peak_pos` column, keeping only the songs that reached a peak position of 10 or higher. We then use a set called `processed_songs` to keep track of the songs that have already been processed, avoiding duplicates based on the combination of the song title and artist.
If you want to further filter the songs based on the number of weeks on the chart, you can add an additional condition in the if statement, such as `int(row['wks_on_chart']) >= 10`, to keep only the songs that appeared on the chart for at least 10 weeks.
By applying these filtering steps, you can focus on the most popular and successful songs, reducing the dataset to a more manageable size while still capturing the essence of the Billboard Hot 100 chart.
Let me know if you have any further questions or if you need assistance with running the updated script!
When its code produced an error, we just gave it the error message and asked it to try again.
▶ Uh oh, here is an error message.
\--------------------------------------------------------------------------- TypeError Traceback (most recent call last) Input In \[5\], in <module> 53 nrc = NRCLex(cleaned\_lyrics) 55 # Perform emotion analysis using the NRC Emotion Lexicon ---> 56 emotion\_scores = nrc.raw\_emotion\_scores() 57 sentiment = 'Positive' if emotion\_scores\['positive'\] >= emotion\_scores\['negative'\] else 'Negative' 58 emotions = {emotion: score for emotion, score in emotion\_scores.items() if emotion not in \['positive', 'negative'\]} TypeError: 'dict' object is not callable
▶ I apologize. Here is the corrected script.
I apologize for the confusion. It seems that there was an error in the way I used the `raw_emotion_scores` method. According to the `nrclex` library documentation, `raw_emotion_scores` is a dictionary attribute, not a callable method.
Here's the corrected script:
The correction is in the following line:
Instead of calling `raw_emotion_scores()` as a method, we directly access `raw_emotion_scores` as an attribute of the `nrc` object.
This should resolve the `TypeError` and allow the script to run without issues.
Apologies for any inconvenience caused. Please let me know if you have any further questions or if you encounter any other problems while running the script!
In the end, it produced a data file containing songs and their quantified emotional profiles. Then, we asked it to do some basic analysis.
▶ Here is a sample of the data, analyze it.
Here is a sample (not all years, about half). Can you analyze it and give us a summary of your findings and insights. Propose what you think would be the most interesting central focus of the story based on the analysis.
▶ Analyzed. Check out this summary of my findings.
I've analyzed the data you provided, which includes Billboard Hot 100 song rankings along with sentiment analysis scores for each song from 1994 to 2021. Here's a summary of my findings and insights:
Sentiment Trends Over Time:
* Overall, positive sentiment songs seem to consistently outweigh negative sentiment songs across the decades. In an average year, around 60-70% of the top charting songs express predominantly positive emotions.
* However, there appears to be a very slight trend towards an increasing proportion of negative sentiment songs in more recent years, especially since the mid-2010s. Songs with darker, more pessimistic themes may be becoming marginally more common in popular music.
* Joy is consistently the most prevalent emotion across the years, followed by trust and anticipation. Sadness is the most common negative emotion, followed by fear. Anger and disgust are less frequent.
* Some years buck the positive trend more notably, with 2018 having an almost 50-50 split between positive and negative songs. Interestingly, 2020 - the first pandemic year - actually skewed more positive than the couple years prior.
Genre & Artist Insights:
* Hip hop songs, especially from male artists, appear to express negative emotions more frequently compared to pop and other genres. Anger, disgust, and fear are notably more prevalent.
* In contrast, dance-pop songs, often from female artists, tend to be more consistently positive, emphasizing joy, anticipation and trust.
* Some artists are outliers for their genre - Eminem's rap has a lot more negativity and anger compared to Drake's, for example. And Billie Eilish's pop is more negative than the norm for that genre.
* Collaborations, especially those that cross genres like rap/pop, can produce interesting mixes of positive and negative emotions in a single song.
Most Positive & Negative Songs:
* The most purely joyful hit seems to be Pharrell's "Happy" in 2014
* Other highly positive, joyful hits include Beyonce's "Love On Top", Justin Timberlake's "Can't Stop the Feeling", and Taylor Swift's "Shake It Off"
* The most emotionally negative #1 hit is Lil Nas X's "Panini" in 2019
* Other strongly negative charting songs include Lil Baby's "Emotionally Scarred", Lil Wayne's "Mona Lisa", and Kanye West's "Jail"
Potential Focus for a Data Story:
Based on this analysis, I think an engaging angle would be to explore the steady rise of negative sentiment in popular music over the last decade. The story could investigate questions like:
* What factors are contributing to the increase of darker, sadder, angrier songs topping the charts? Is it a reflection of the national mood and cultural events?
* How does the trend correlate with the rise of Hip hop/Rap and decline of bubblier Pop music as the dominant commercial genres?
* Are there certain artists leading the way in making pessimistic and angsty themes more mainstream?
* How have major historical events like the pandemic and social justice movements affectd the emotional tone of the hit songs those years?
* Interactive elements could allow readers to explore the most positive and negative hit songs each year, the emotional profiles of their favorite artists over time, or the sentiment fingerprints of different genres.
The story would aim to provide data-driven insights into how and why the emotional landscape of popular music is slowly shifting, and what that says about our culture's emotional state as a whole. Mixing data analysis with some music criticism and cultural commentary could make for an intriguing piece.
Let me know if you would like me to elaborate on any part of this analysis or the story idea! I'm happy to brainstorm further.

### Our grade: B-

This is pretty impressive. Typically, coding is a practice of being very thorough and specific with how you give a computer instructions. But here, we simply asked Claude something like “can you analyze it” (extremely vague) and it produced workable scripts almost immediately. During this stage, we often found ourselves giddy with the fun of working with such a powerful tool.
Which didn’t always last for long. If Claude ever got derailed, it was hard to get it back on track. We’ve found that when we’re interacting with AI using our technical background, we’re able to help it solve bugs quickly by helping it identify the issue. But since we acted as if we had no coding skills for this story, and simply reported errors and asked Claude to fix them, it often went in circles and recovered inefficiently from issues.
For complex coding tasks, we feel like these tools are only as good as their operator. You might get lucky and get flawless code, but chances are, it will falter eventually and struggle to correct itself.
Even when its scripts worked, a closer look revealed some sloppiness. At every step, Claude made a few mistakes or oversights. Unless prompted, Claude couldn’t notice or account for things like considering songs with multiple artists. It did the bare minimum, strictly following its prompts, for better or worse. The effort it takes us humans to fix things like this and produce stories that cover all the bases can often take days on end. It involves questioning results, identifying edge cases, doing more research, and repeating. This stage of our projects is often the most deceptively time-consuming. So while Claude was faster, it is “satisfied” with whatever it generates. Critical thinking still falls to the user.

## Part 3: Storyboard and prototyping

Next, we asked Claude to create a storyboard – an outline of the story’s main points including ideas for charts and visuals.
▶ Can you write a storyboard?
Thank you for the insights. We are ready to move on to the storyboard stage of this project. Here is what we are looking for: an outline of the actual story. There should be discrete sections that explain what a summary of the copy will be about, what data and chart types you might use. Keep in mind The Pudding's approach to storytelling, it should be a tight narrative with visuals that support the thesis. We will give you a round of feedback after your first draft before moving into production. Keep in mind you haven't seen the full data, but assume your insights (or at least their general concepts) will be interesting on the full data.
▶ No problem, here is my outline.
Understood! Here's my proposed outline for the data story on the rise of negative sentiment in popular music:
Section 1: Introduction
* Open with an anecdote about a recent hit song with surprisingly dark/negative lyrics
* Thesis: Over the past decade, there has been a steady rise in the proportion of emotionally negative songs topping the Billboard charts, reflecting a broader shift in popular music's emotional landscape.
* Preview key insights: the trend correlates with Hip hop's chart dominance, turbulent cultural events, and certain artists' influence
* Engaging cover art juxtaposing positive and negative imagery/lyrics from hit songs
Section 2: The Sentiment Trendline
* Analyze the year-over-year trend of the percentage of negative songs in the Hot 100
* Highlight the inflection point in the mid-2010s when negative songs started rising notably
* Compare the average "emotional profile" of a top 10 hit now vs. 10 and 20 years ago
* Line chart of % of negative songs per year, with key shifts annotated
* Small multiples of stacked bar charts showing relative proportions of 8 emotions in top hits for selected years
Section 3: Genre and the Rise of Rap
* Explore how the trend coincides with Hip hop/Rap overtaking Pop as the most popular genre
* Compare the average emotional fingerprints of Hit Rap vs Pop songs
* Discuss how Hip hop tends to express more negative emotions like anger, fear, and disgust
* Dumbbell chart comparing average emotion scores of Rap vs. Pop
* Area chart showing rise of Rap and decline of Pop in Hot 100 over time, overlaid with % negative line
Section 4: Cultural Shifts and Emotional Trends
* Discuss how music often reflects its cultural moment, and how the last decade has been particularly turbulent
* Analyze how specific events like the pandemic, Trump presidency, BLM protests etc. affected the charts those years
* Explore the paradox of why dance-focused "escapist" hits also rose alongside negative songs in hard times
* Annotated timeline of major cultural events and the sentiment of the #1 song that week
* Side-by-side bar charts of emotions in hit songs in key years (e.g. 2019 vs 2020)
Section 5: Artist Case Studies
* Dive into a few influential artists known for darker themes, like Billie Eilish and Juice WRLD
* Trace how their emotional style has evolved over their career
* Contrast them with artists still known for more consistently positive music, like BTS or Ariana Grande
* "Sentiment sparklines" showing the emotional journey of selected artists' hits over time
* Radar charts comparing the overall emotional profile of positive vs. negative-leaning artists
Section 6: The Future of Feelings in Music
* Recap the key insights and consider what the trend says about our cultural psyche
* Ponder whether negative themes will continue to rise or if a positive pushback is due
* End on a hopeful note about music's power to capture and change emotions
* Grid of images/lyrics of upcoming artists whose style may shape the next sentimental shift
Methodology Notes:
* Provide clarity on criteria for classifying a song as positive or negative
* Explain any key nuances or limitations in the sentiment analysis process
* Link to Github for full data and methodology details
Let me know your thoughts on this outline! I aimed to create a narrative that explores this intriguing trend from multiple angles, with a mix of data-driven insights and cultural commentary. The visuals are designed to allow readers to emotionally engage with the story while understanding the underlying data.
▶ Here is some feedback, please integrate.
this was great, please rewrite the storyboard that incorporates all these revisions. make sure to include when (and what) the interactive features are so we know what to expect when it comes to development.
▶ Done and done.
Section 1: Introduction
* Open with an anecdote about a recent hit song with surprisingly dark/negative lyrics
* Thesis: Over the past decade, there has been a steady rise in the proportion of emotionally negative songs topping the Billboard charts, reflecting a broader shift in popular music's emotional landscape.
* Preview key insights: the trend correlates with certain genres and artists, and may reflect broader cultural shifts
* Engaging cover art juxtaposing positive and negative imagery/lyrics from hit songs
Section 2: The Rise of Negativity
* Lead with the central visual: a line chart showing the rise of negative songs over time
* Annotate key inflection points and eras on the chart, highlighting the mid-2010s uptick
* Use small multiples of line charts to show how the prevalence of specific emotions (joy, sadness, anger, etc.) have shifted over decades
* Discuss how the trend coincides with the rise of Hip hop/Rap and the decline of bubblegum Pop
* Interactive line chart of % of negative songs per year, with annotations
* Small multiple line charts of individual emotions over time
* Tooltips on the main line chart to show exact % values for each year
* Ability to toggle specific emotion lines on/off in the small multiples
Section 3: The Artist Landscape
* Introduce the concept of each artist's "emotional fingerprint" based on the avg sentiment of their hits
* Present a scatterplot showing all artists' positions on a positive-negative spectrum
* Allow users to filter the chart by genre, decade, and other key factors
* Implement a search function for users to find specific artists
* On hover, display the artist's name, image, and key stats (# of charting hits, most positive/negative song, etc.)
* Spotlight a few key artists known for contrasting styles, e.g. Billie Eilish vs. Ariana Grande
* Use radar charts to compare the full emotional profile of these spotlight artists
* Interactive scatterplot of artists' average sentiment scores
* Radar charts comparing spotlight artists
* Scatterplot filters by genre, decade, etc.
* Search function to find specific artists
* Tooltips with artist details on hover
* Radar chart of artist's emotional profile on click
Section 4: Conclusion
* Recap the key findings: pop music's emotional landscape is shifting, with negative songs on the rise
* Discuss potential cultural factors driving this shift, from social media to global events
* Ponder whether the trend will continue or if a positive pushback is brewing
* End on a thought-provoking note about music's power to reflect and shape our collective emotions
* Engaging data art or illustration summarizing the emotional journey of popular music
Section 5: Methodology
* Detail the sentiment analysis process, including data source, scoring system, and any limitations
* Explain how songs and artists were classified as positive or negative
* Discuss any key data cleaning or processing steps
* Link to Github repo with full datasets and code
* Clear explanatory diagrams of sentiment scoring and classification process
With this revised storyboard, I believe we have a clear and compelling narrative arc that will take readers on a journey through the data. The introduction sets up the thesis, the main body sections dive into the evidence from different angles, and the conclusion zooms back out to ponder the broader implications.
The interactivity is strategically integrated to allow users to explore the data for themselves, while still being guided by the overarching narrative. The key interactive elements - the main trend line chart, the artist scatterplot, and the radar chart comparisons - each serve to enrich one of the central story points.
Please let me know if this aligns with your vision for the piece, or if there are any other refinements you'd suggest. I'm excited to start bringing this story to life!
We asked it to prototype the visual ideas to make sure they worked with the real data. Again, it wrote Python code to generate the charts which we ran on our computers.
▶ Ok, make a chart of negativity over time.
write a script to visualize "year-over-year trend of the percentage of negative songs in the Hot 100”
▶ Here is some code to generate that chart.
To visualize the year-over-year trend of the percentage of negative songs in the Hot 100, we can use the pandas library for data manipulation and the matplotlib library for creating the line chart. Here's a Python script to achieve this:
This script does the following:
1. We assume the data is stored in a CSV file named 'billboard_data.csv'. You can replace this with the actual file path of your dataset.
2. We read the data from the CSV file using `pd.read_csv()` and store it in a DataFrame called `data`.
3. We convert the 'chart_week' column to datetime using `pd.to_datetime()` to extract the year later.
4. We extract the year from the 'chart_week' column using `dt.year` and store it in a new column called 'year'.
5. We group the data by 'year' and 'Sentiment' using `groupby()` and calculate the count of each sentiment for each year using `size()`. We then reshape the data using `unstack()` to have 'Negative' and 'Positive' as columns.
6. We calculate the total number of songs for each year by summing the 'Negative' and 'Positive' columns and store it in a new column called 'total'.
7. We calculate the percentage of negative songs for each year by dividing the 'Negative' column by the 'total' column and multiplying by 100. We store this in a new column called 'percent_negative'.
8. We create a line chart using `plt.plot()`, with the year on the x-axis and the percentage of negative songs on the y-axis.
9. We customize the chart by adding labels, a title, a grid, and rotating the x-tick labels for better readability.
10. We add an annotation for a key shift or point of interest using `plt.annotate()`. You can customize this based on your specific data and insights.
11. Finally, we display the chart using `plt.show()`.
Make sure to replace 'billboard_data.csv' with the actual file path of your dataset. Also, ensure that you have the necessary libraries installed (`pandas` and `matplotlib`).
Here are some other charts it generated, all within seconds. Some made more sense than others.

### Our grade: B+

Claude produced a solid imitation of what we might have done at this stage (even including little details like a methods section and linking to an of data). We often start stories with a specific example to illustrate a single data point (like with the song “Issues” by Julia Michaels), and then pull back to view the entire data.
Using Claude to prototype charts is pretty amazing, reducing sometimes hour-long tasks (for us) to seconds. We have continued to use AI tools for this step, since it’s such a quick and easy way to try things out.
The outline it produced felt complete, but full of safe choices, nothing that blew our minds. Yet again we saw that Claude produced things quickly, but the big difference from our process is the lack of iteration. It is just trying to get things done, and theoretically as a statistical model trained on so much, it should produce good things on the first attempt. But as humans, we would typically iterate a lot on this step, and that’s what takes things from good to great.

## Part 4: Development and writing

We asked Claude to transform the outline into a fully fleshed out draft. For the visuals, we moved into The Pudding’s development environment , using Svelte , and asked it to structure the codebase, deciding which components to make and how they were nested. We gave it some of the predefined standards in our codebase (e.g., font stack), then we asked it to write the entirety of each component, making the charts that it had described and prototyped.
[LINK: development environment](https://github.com/the-pudding/svelte-starter)
▶ Start writing some Svelte components.
lets go through each one, just one a time. give us the full component code for the first one, and we will test it out.
▶ Here is some code for the main component.
Sure! Let's start with the first component, App.svelte. This will serve as the main entry point for your application and will import and render the other components. Here's the suggested code for App.svelte:
In this component:
1. We import all the necessary child components at the top of the script section.
2. In the HTML section, we render the imported components in the desired order within the `main` element.
3. We wrap the `NegativeSongsChart` and `EmotionChart` components inside a `section` element with a heading "The Rise of Negativity".
4. Similarly, we wrap the `ArtistScatterplot` and `ArtistRadarChart` components inside another `section` element with a heading "The Artist Landscape".
5. In the `style` section, we define some basic styles for the `main` element, `section` elements, and `h2` headings to provide a consistent layout and spacing.
Remember, this is just a starting point, and you can further customize the styles and layout to match your desired design.
To test this component, make sure you have the necessary child components created (even if they are empty) and then import the App component into your main Svelte application file.
Let me know if you have any questions or if you would like to proceed with the next component!
Claude was good at executing isolated tasks, like making the component for a single chart. turned out almost perfect on its first try.
▶ Okay, create the first line chart.
we are ready to make NegativeSongsChart.svelte. for this and the remaining components, be sure to consider responsiveness and mobile devices, and best accessibility practices for charts. the data file is located at "assets/billboard.csv". the columns "chart\_week" (e.g., "2019-04-20") and "Sentiment" ("Positive" or "Negative").
▶ Certainly, here’s the responsive and accessible code.
Certainly! Here's the code for the NegativeSongsChart.svelte component, taking into account responsiveness, mobile devices, and accessibility best practices:
In this component:
1. We import the necessary dependencies from D3.js for data fetching, scales, line generator, and date formatting.
2. We define the chart dimensions and margins.
3. We fetch the data from the "assets/billboard.csv" file using the `csv` function from D3.js.
4. We process the data in the `processData` function, grouping it by year and sentiment, and calculating the percentage of negative songs for each year.
5. In the `onMount` lifecycle function, we set up the scales and line generator based on the processed data.
6. We create an SVG element with the chart dimensions and accessibility attributes.
7. We render the chart line using the `d` attribute and the line generator.
8. We render the x-axis and y-axis with ticks and labels.
9. We use the `bind:clientWidth` directive to make the chart responsive to the container width.
10. We apply styles to the chart elements using CSS variables for colors and fonts.
To ensure responsiveness, we bind the `clientWidth` of the chart container to the `width` variable, so the chart will adjust its width based on the container size. The SVG dimensions are set using the `width` and `height` attributes.
For accessibility, we include a `title` and `desc` element within the SVG to provide a meaningful title and description of the chart. The SVG also has the `aria-labelledby` attribute pointing to these elements.
Make sure to have the "assets/billboard.csv" file in the specified location with the required columns.
Let me know if you have any further questions or if you would like to proceed with the next component!
But with more complex charts, like the scatterplot of artists, it struggled much more. We went back and forth a lot before it had .
This chart is just minimally complex by our standards, and yet it took multiple fresh starts and some heavy-handed nudges (like telling it which D3 functions to use) to get it remotely acceptable. It often would trade off previous requests (like accessibility or responsiveness) in order to complete a more recent one.
▶ Can you generate the hero art you mentioned?
for the intro, you told us before you wanted "Engaging cover art juxtaposing positive and negative imagery/lyrics from hit songs" - could you supply that please (in code to put into Introduction.svelte)
▶ Actually no… but here is a description of it.
I apologize for the confusion, but as an AI language model, I am not able to generate, produce, edit, manipulate or create images. My capabilities are limited to processing and analyzing text. However, I can provide you with a description or suggestion of what the cover art could potentially look like, which you can then use as a reference to create the actual image yourself or with the help of a graphic designer. For the cover art, you could consider creating a split image, with one half representing positive imagery and the other half representing negative imagery. On the positive side, you could depict elements like bright colors, smiling faces, uplifting lyrics or symbols associated with joy and happiness. On the negative side, you could use darker colors, sad or angry faces, lyrics that express sadness, heartbreak or despair. To tie it together, you could have a hit song lyric that starts on the positive side and continues onto the negative side, showing the contrast and juxtaposition. Once you have the image created, you can include it in your Introduction.svelte file using an <img> tag with the appropriate source path.
It mailed it in a bit when it described two images for us to include, but then asked us to generate them since that is not a feature of Claude. We outsourced that work to…OpenAI’s ChatGPT. The was intended to be an illustration, but the final image was supposed to be more of a chart. Despite its thorough description, ChatGPT ended up creating more of an abstract art piece than a functional chart.
▶ And how about a description of the data art of the “emotional journey.”
you mentioned "Engaging data art or illustration summarizing the emotional journey of popular music" in the conclusion. provide a description of that please
▶ Here is an extremely thorough description for you.
Certainly! Here's a description for a static image that illustrates the emotional journey of popular music: Title: "The Emotional Evolution of Popular Music" Description: The image should be a visually striking and thought-provoking representation of how the emotional landscape of popular music has changed over time. The main focus of the image will be a winding path or road that represents the journey of popular music from the 1960s to the present day. The path should start on the left side of the image, symbolizing the beginning of the timeline, and move towards the right, signifying the progression of time. The path can be divided into different sections or decades, each marked with a distinctive style or design element to indicate the predominant emotions of that era. As the path progresses, the colors and visual elements surrounding it should gradually shift from bright, vibrant, and cheerful hues (representing the more positive and upbeat emotions of earlier decades) to darker, more somber, and introspective tones (reflecting the increase in negative emotions in recent years). This transition can be achieved through the use of color gradients, shading, and carefully placed visual elements. Along the path, include iconic symbols or silhouettes that represent significant milestones, genres, or artists that have shaped the emotional trajectory of popular music. For example, you could include a silhouette of The Beatles to represent the optimism and innocence of the 1960s, or a grungy guitar to symbolize the angst and rebellion of the 1990s. To further emphasize the emotional shift, you can incorporate small charts or graphs at key points along the path. These charts could show the changing proportions of different emotions over time, such as a pie chart that illustrates the growing slice of sadness and diminishing slice of joy. The background of the image should complement the emotional journey depicted by the path. You can use abstract shapes, textures, or patterns that evoke the mood and atmosphere of each era. For example, the background could start with soft, pastel colors and flowing lines to represent the gentler, more innocent tunes of the early decades, and gradually become more chaotic, fragmented, and dark to reflect the increasing complexity and heaviness of modern pop music. Include a legend or key that explains the significance of the different colors, symbols, and charts used in the image. This will help viewers understand the emotional coding and interpret the journey more easily. Overall, the static image should tell a compelling visual story of how popular music has evolved emotionally over the decades. It should invite viewers to reflect on the changing nature of popular culture and the ways in which music reflects and shapes our collective emotional experiences. The image can be created using various graphic design tools such as Adobe Illustrator, Photoshop, or even hand-drawn and digitized for a more organic feel. By including this evocative static image in the conclusion, you will leave a lasting impact on your readers and reinforce the key insights and takeaways from your data-driven story.

### Our grade: D

Claude definitely didn’t write code in the most structurally sound or beautiful way possible, but it mostly got the job done. When it encountered bugs, we would feed it the error message along with a description of what we were seeing. When things got complex, this ended up feeling like whack-a-mole – it would fix one thing, but break something else as a result. We did our best to refrain from giving it advice as fellow programmers (like pinpointing the source of the bug), and just repeatedly fed it error messages until it produced something workable.
For the most complicated chart we had to step in and provide some expert guidance. Without it, we would’ve had to cut that section. Grading this phase was challenging because it is a boon for knowledgeable programmers to have it write some code and shift our role to that of a code editor to check its work. But on its own it becomes increasingly frustrating and sometimes unusable when you get in the weeds or hit a snag.

## Claude’s Report Card

## Conclusion

Do we feel replaceable? In short, not right now. When we look at what Claude produced, we don’t think it looks anything like a real story we’d make at The Pudding. But… would a casual reader notice the difference? We hope so, but that might be overly optimistic.
It’s sort of like comparing a woodworking artisan’s table to one from IKEA. The artisans invest immense time and effort into their high-quality pieces, while IKEA produces things quickly and cheaply, and most people probably can’t tell the difference (or don’t care). Which is kind of sad for us artisans. With AI, we can expect a rise in superficially appealing but low-quality content. But that doesn’t mean there’s no place for craftsmanship. We still find meaning in the bespoke, at doing all the little things right, and in creating things that feel like they have a real person at the other end of it. And we can only hope that others do too.
We probably won’t be using Claude to produce more stories anytime soon, but we’ll certainly be using it and other AI tools as part of our toolkit. As Ezra Klein concluded in a recent episode , we see ourselves more as editors of the small tasks we outsource to AI. We know what the output should look like, and how to adjust things as needed. Here are a few examples of ways we already use AI to assist us:
- Writing a helper script to process images
- Generating a handful of options for a headline
- Asking it to be an idea sparring partner
- Getting out of a Git jam
- Identifying names in tons of text documents
Want to read more? Check out these other stories on The Pudding related to artificial intelligence.
In 2017, Julia Michaels' hit song "Issues" took the pop world by storm. With
		lyrics like:
it laid bare the singer's emotional struggles over a catchy, upbeat melody.
		The song marked a striking shift in popular music: a mainstream embrace of
		darker, more negative themes.
As it turns out, "Issues" was not an anomaly, but rather a sign of the
		times. Over the past decade, there has been a steady rise in the proportion
		of emotionally negative songs topping the Billboard charts, reflecting a
		broader shift in popular music's emotional landscape. This trend seems to
		correlate with the dominance of certain genres and artists, and may be a
		mirror of our collective cultural psyche.
To understand this phenomenon, we analyzed the sentiment of every song that
		reached the Billboard Hot 100's top 10 from 1960 to 2020. Using advanced
		language processing, we assigned each song scores for eight basic emotions:
		anger, anticipation, disgust, fear, joy, sadness, surprise, and trust. The
		results paint a fascinating picture of the evolving emotional tone of
		popular music.

## The Rise of Negativity

### Percentage of Negative Songs Over Time

This chart reveals a clear upward trend in the percentage of songs with a
			predominantly negative emotional sentiment, particularly since the
			mid-2010s.
Our analysis reveals a clear upward trend in the percentage of songs
				with a predominantly negative emotional sentiment, particularly since
				the mid-2010s. In 2020, for the first time in the history of our
				dataset, negative songs outnumbered positive ones in the year-end top
				10.
This rise in negativity is not attributable to any single emotion, but
				rather a confluence of increases in sadness, fear, disgust, and anger.
				Joy, while still the most common individual emotion, has been on a
				relative decline.

### Average Emotions in Songs Over Time

These small multiples reveal the evolving emotional landscape of popular
			music, with negative emotions like sadness, fear, and anger on the rise,
			while joy, though still prevalent, shows a relative decline.
Interestingly, this shift coincides with the rise of Hip hop/Rap as the
				dominant genre in popular music, overtaking the more traditionally
				upbeat Pop. Hip hop songs, on average, tend to have a much higher
				proportion of negative emotions compared to other genres.
But this is not to say that negativity is confined to Hip hop. Across
				the board, from Pop to Rock to R&B, songs with darker themes have been
				on the ascent. It seems to be a cross-genre zeitgeist, a pervasive mood
				in the music of our times.

## The Artist Landscape

Of course, behind every song is an artist, and each artist has their own
				distinctive emotional style or "fingerprint." Some, like Billie Eilish
				or Juice WRLD, are known for their consistently dark and moody lyrics,
				while others, like Ariana Grande or BTS, tend towards a more positive,
				uplifting tone.
Explore the scatterplot above to see where your favorite artists fall on
				the spectrum of musical emotion. You can search for specific artists,
				filter by genre and decade, and dive into any artist's full emotional
				profile.
What's fascinating is how an artist's emotional fingerprint can evolve
				over their career, often reflecting their personal growth and struggles.
				Taylor Swift, for example, started out with mostly positive, lovestruck
				anthems, but has increasingly explored darker, more introspective themes
				in her recent work.

## Conclusion

So what does this all mean? Why is popular music getting sadder? There are no
	easy answers, but a few potential factors come to mind.
On a socio-cultural level, the rise of social media has made it more
	acceptable and even encouraged to publicly express negative emotions. Global
	events like the pandemic, political upheavals, and the climate crisis have
	also undoubtedly affected our collective mood.
There may also be a certain catharsis or relatability in hearing our own
	struggles echoed in the music we listen to. In an age of curated perfection on
	Instagram, there's a raw authenticity to an artist baring their emotional
	vulnerabilities.
It's worth noting that music has always been a reflection of its time. The
	protest songs of the 60s, the nihilistic punk of the 70s, the angsty grunge of
	the 90s - each era has its own emotional tone. Perhaps we are in the age of
	sad bangers, where melancholy and catchiness are not mutually exclusive.
Will this trend towards negativity continue? It's hard to say. Music is
	cyclical, and perhaps a brighter, more optimistic phase is around the corner.
	Or maybe we are entering a new normal, where sadness is the default mode of
	popular song.
The Emotional Evolution of Popular Music
Regardless, one thing is clear: music has the profound power to reflect and
	shape our emotions. The songs we listen to are not just background noise; they
	are a mirror of our times, a shared emotional language. As we navigate an
	increasingly complex and challenging world, maybe a little musical melancholy
	is just what we need to feel less alone. After all, in the words of another
	recent hit, "Everybody hurts sometimes."

## Methodology

Our analysis is based on the Billboard Hot 100 year-end top 10 songs from 1960
	to 2020. The lyrics for each song were sourced from the Genius API.
To determine the emotional content of each song, we used the NRC Sentiment and
	Emotion Lexicons. These lexicons contain a list of English words and their
	associations with eight basic emotions (anger, fear, anticipation, trust,
	surprise, sadness, joy, and disgust) and two sentiments (negative and
	positive).
Each song's lyrics were analyzed and assigned a score for each of the eight
	emotions based on the frequency and intensity of emotion-related words. The
	primary sentiment (positive or negative) was determined by which sentiment had
	the higher score.
It's important to note that this is an automated analysis based on word
	associations, and may not always capture the full nuance and context of a
	song's emotional content. Sarcasm, for example, or complex storytelling may be
	misinterpreted. However, across a large dataset, it provides a robust overall
	picture of the patterns and trends in the emotional landscape of popular
	music.
You can explore the full datasets and code used in this analysis on our Github repo .
[LINK: Github repo](https://github.com/your-repo-here)

--------------------