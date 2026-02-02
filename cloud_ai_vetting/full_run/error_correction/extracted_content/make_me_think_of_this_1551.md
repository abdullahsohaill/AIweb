# Make me think of this
**URL:** https://tht.fangraphs.com/mvp-2018-mookie-betts-christian-yelich-machine-learning
**Page Title:** Predicting the 2018 MVP Winners with Machine Learning | The Hardball Times
--------------------


## Predicting the 2018 MVP Winners with Machine Learning

by RyanP October 29, 2018
Will Mookie Betts be the 2018 AL MVP? Machine learning might be able to tell us. (via Keith Allison )
The 2018 American League MVP race reminds me of 2012. That year, Mike Trout led the sport in WAR but finished second to Miguel Cabrera , who had an inferior season but won the first Triple Crown in 45 years. Cabrera’s Detroit Tigers also went to the playoffs while Trout’s Los Angeles Angels finished in fourth place. Cabrera’s victory was quite controversial .
This year, Mookie Betts plays the role of Trout, while J.D. Martinez stands in for Cabrera. The Boston right fielder led the major leagues in WAR but finished behind his DH teammate in home runs and RBI, two of the Triple Crown stats. Meanwhile, Martinez came reasonably close to a Triple Crown himself, ranking second in average and home runs and first in RBI. In addition to these two, the AL race again features Trout, with 9.8 WAR to Betts’ 10.4; Cleveland’s José Ramírez with 8.1 WAR and a 30-30 season that easily could’ve been a 40-40 one; and Houston’s Alex Bregman with 31 home runs and 7.6 WAR that helped his team win a surprisingly contentious AL West.
The NL MVP race is less controversial but still interesting. Early in the season, Javier Baez of the Cubs made some noise by adding power and a touch more plate discipline to his game. After the All-Star break, Matt Carpenter hit dinger after dinger to vault the Cardinals into playoff contention and himself into the MVP race . In Colorado, Trevor Story had his anticipated breakout year, garnering MVP consideration while pushing the Rockies into a playoff spot.
But the award likely will go to Milwaukee’s Christian Yelich , who racked up a monster 5.4 WAR in the season’s second half . The Brewers’ outfielder finished two home runs and an RBI short of a Triple Crown while leading the Brewers to a surprise the NL Central title. Humans like a good story , and Yelich provided a great one.
With an interesting race in the American League and some good storylines in the National League, I wanted to predict the 2018 MVP races as objectively as possible while understanding what factors voters consider. To do this, I turned to machine learning; specifically, a popular machine learning package called xgboost .
[LINK: xgboost](https://xgboost.readthedocs.io/en/latest/)
xgboost implements gradient boosting, a powerful decision-tree-based technique for predicting outcomes and classifying samples. It’s an ensemble method known for avoiding overfitting when handling correlated inputs, which helps when understanding how data points like OPS, home runs, and batting average influence the probability of winning an MVP award.
I asked the the xgboost algorithm: Given data about 2018 players’ seasons, what’s the probability of each player winning his league’s MVP award?

### Approaching the Problem

I ran many iterations of the model while playing around with lots of inputs. Does OPS matter in determining the MVP? The team he plays for? His defensive ranking ? Do voters treat players differently whether they’re in the American League or National League?
I also had to choose how to model the inputs. Do raw measurements of stats like OPS or home run totals produce the best results? How about park-adjusted stats?
One key insight was converting most raw stats to rankings in that year’s respective leagues. It seems MVP voters think in terms of “Mike Trout leads the American League in OPS” instead of “Mike Trout has a 1.088 OPS in the American League.” Ranked data also better captures the competitive aspect of the MVP award and smooths out comparisons across seasons. We know a .300 batting average in 2007 means something different than a .300 batting average in 2018, but No. 1 is always No. 1.
To avoid rewarding league-leading performances in a small sample, I analyzed only players with at least 2.93 plate appearances per team game. Why this threshold? Because it’s the fewest PA per team game of any MVP award winner ( Willie Stargell , 1979). I didn’t want to miss anyone.
I didn’t analyze pitchers. With possible apologies to Jacob deGrom this year, pitcher MVP seasons are rare. I didn’t see enough value in spending the computational or thought time in modeling their chances. There’s no reason I can’t, though. Consider it part of what will be included in the next version of the model.
I classified players by their primary defensive position by seeing where they played the most innings in the field. Thus, Baez in 2018 is classified as a second baseman. If a player wasn’t on the field for at least 50 percent of the games he played in, I classified him as a DH.
I looked at data for the 10 seasons prior to the year I was predicting. Meaning, to predict 2018’s MVPs, I looked at data from 2007 through 2017. This approach captures voters’ tendencies at the time of the vote.
In the end, I used the following data points about each player who met the PA/G threshold:
- Season (to understand whether voting criteria change over time)
- League (to understand whether MVP voters weight AL performance differently from NL performance)
- OPS rank (within the player’s season-league, where 1 is the highest)
- AVG rank
- Team winning percentage. I used raw percentage here because I found  ranking the teams in order of their finish in the division detracted from the model’s results.
- RBI rank
- HR rank
- SB rank. I know voters appreciate a speedy player; in particular, voters love players with a combination of power and speed.
- WAR rank
- Primary defensive position
- DEF Rank
I examined all of these elements with respect to whether the player won the MVP award. Here are five random rows from the training data set so you can see what xgboost had to work with.

### Evaluating the Model

I found the best model by removing 2011 AL and 2014 NL data (when Justin Verlander and Clayton Kershaw , respectively, won MVPs), since my dataset doesn’t contain pitchers, and repeating 10-fold cross-validation five times across a range of tuning parameters for the xgboost algorithm. The caret package helped tremendously. I then set the predicted MVP as the player in each league whose season had the highest probability of winning the MVP award.
[LINK: caret](http://topepo.github.io/caret/index.html)
I evaluated the models using precision, recall , and the F1 score. I chose these metrics instead of sensitivity, specificity , and accuracy because the data set is wildly imbalanced. Out of 1,517 player-seasons, only 20 (1.3 percent) are classified as having won the MVP. With so little data about what makes an MVP, precision and recall represent the model’s performance better than sensitivity and specificity do. This choice of metrics also means I paid attention to the area under the precision-recall curve instead of the area under the receiver operating characteristics (ROC) curve.
The final model resulted in the following confusion matrix .
In plain English:
- Of the 20 MVP winners: The model correctly labeled 13 winners as winners The model incorrectly labeled seven winners as non-winners
- The model correctly labeled 13 winners as winners
- The model incorrectly labeled seven winners as non-winners
- Of the 1,497 non-winners: The model correctly labeled 1,490 non-winners as non-winners The model incorrectly labeled seven non-winners as winners
- The model correctly labeled 1,490 non-winners as non-winners
- The model incorrectly labeled seven non-winners as winners
The precision and recall here are both 0.65. The F1 score is the same. Could this be improved? Yes, but given the subjective nature of MVP voting, I think these results are good.
The following graph shows the precision-recall curve and the area under it:
An area under this curve of 1.0 would indicate perfect precision and perfect recall. Compared to that unattainable perfection, the area under this curve above is 0.745. Conversely, the area under the ROC curve (not shown here) is 0.82. The latter number is misleadingly high because of how easy it is to identify true negatives in this dataset: 98.6 percent of the time, just predict someone won’t win the MVP, and you’ll be right.

### Show Me the Winners!

Numbers are great, but looking at names is even more fun. The following table shows the 13 correct predictions and the seven incorrect ones.
Most of the incorrect predictions placed in the top 10 in their league’s voting that year. The one exception is Votto in 2012, who placed 14th. (Behind Jay Bruce ? Really?!!??!)

### Who Wins in 2018?

The true test of any model is how it performs on data it hasn’t seen before. We don’t know the 2018 voting results yet, but the model’s predictions are reasonable. The following graphs show the players in each league with the ten highest probabilities of winning the MVP award:
In the AL, seasons like the ones belonging to Betts and Martinez have high probabilities of winning the award. Betts had an historic all-around year and would be an excellent choice for the award. But don’t forget about Martinez, whose home run and RBI totals will get him more consideration than many might think. Meanwhile, Ramírez will get some stray votes for his outstanding season, and Trout continues to make voters look past the “playoff team” criterion. Bregman’s presence on the list shows that chants of “MVP! MVP!” during his playoff at-bats were not undeserved. It would not surprise me if these players finished ranked 1–5 in the order listed above.
Yelich dominates the NL field, and no one else is close. Arenado and Story will get some support on the backs of strong seasons that pushed their team into the NL Wild Card game. The model thinks the same of Baez, and Max Muncy ’s presence reminds us how strong his season was even though he didn’t qualify for the batting title. Carpenter is nowhere to be found. I suspect he would be if the Cardinals had finished higher in the NL Central.
Speaking of Arenado and Story, this is a good time to note that I found no “team bias” effect when modeling. Voters didn’t punish Rockies players for playing at altitude, nor did voters reward Red Sox and Yankees players with an “East Coast bias.”
Aside from Trout and Juan Soto , all the names above come from playoff teams. While the MVP ballot states  the award winner “need not come from a division winner or other playoff qualifier,” voters clearly have difficulty voting for players on just-okay or losing teams.
Speaking of winning teams, the following graph shows what the model thinks are the most important criteria in determining the MVP winner:
Today’s MVPs must hit well, as measured by OPS and batting average. Voters clearly want their MVPs to come from winning teams. And despite RBI falling out of favor as a metric for evaluating hitters, MVP voters still prefer players who drive in runs. This fact hurts Trout, who ranked 24th in the AL in RBI among the players examined. Consider also that Martinez ranks first in RBI, whereas Betts ranks 22nd.
Further down the list, home runs and stolen base prowess come into play. It seems voters do love a good power-speed story. The “Season” factor shows voting criteria change over time. Finally, voters give a bit of consideration to the league the players are in, as well as whether they’re catchers or designated hitters.
The remaining factors had little to no influence on voters’ minds, at least not in this data set. I was surprised to see defensive position wasn’t more of a factor in the voting. Perhaps for this reason, and also because players’ defensive ranking isn’t that important, WAR by itself doesn’t mean as much as pure hitting talent for a good team.
Despite some limitations, this model is a good first step at identifying MVP-caliber seasons and understanding the criteria voters use to decide on the award. In future versions, I’d like to incorporate pitchers, implement techniques to better handle the imbalanced training data, and identify more relevant metrics for position players. I’d also like to separate OPS into OBP and SLG to see which is more important. Finally, instead of predicting a pure winner, I would like to predict MVP voting placement. These changes should result in a more usable and interesting model.
Really interesting to see the 2012 result from your model, which shows Trout was not its predicted MVP.  It does seem like past vote biases are too strong. Thanks for this article and putting in so much work!
it’s really difficult to say winning team matters when last year’s NL MVP voting top 2 guys were from losing teams.
Why is “Is National League?” an important factor?
It would be a co-variate in the model allowing the model to control for differences in the voting patterns between AL and NL.
Makes sense!
You should read that as “which league is a player in?” But the model can’t use “NL” or “AL” as inputs. So you have a binary variable instead. If you call it “Is American League” then Betts gets a 1 and Yellich gets a zero; if you call it “Is National League” then the values are switched. Either convention is arbitrary; what’s important is that you’re capturing which league a player is in so that if (as there seems to be) there’s some difference in how voters evaluate the MVP candidates in each league, the model can account for that.
Really appreciate all of the technical detail here – looking forward to playing around with replication and learning xgboost in the process!
A question on your “Season” variable – does that work like a fixed effect for each year?  If so, I’m guessing it [necessarily, because it’s only quantifiable after the vote is taken] hasn’t been accounted for in the 2018 projections?
Did you consider building in a variable for “past MVP finishes”? There has been a possible tendency to find reasons to give the MVP to someone “new”, such as Pujols, Trout, and Bonds, most recently.
I assume based on your descriptions you used a tree method for the predictive model as well. This likely explains why “NL” was important – the model found a difference in the importance of at least one variable as it applies to a particular league. Can you share which one(s)?
It’s fun that WAR ranking came out as completely “unimportant”. Given the strong co-linearity of something link WAR rank with OPS rank, I guess it’s just not quite as useful when predicting voting.
I didn’t consider that, but in the next revision I can!
Great article!
Ryan,
For the 2018 Player-Seasons With the Highest MVP Chances, should the total of all players in each league not total 100%?  For example, not sure how combined Betts and Martinez total more 160%?
Was confused about this as well. My guess is it means % of time that they would win the MVP given their stats alone.
So Mookie and JD both had seasons that would win the MVP in most years, and it’s not taking into account that only one of them can win the MVP this year.
I agree that’s a little confusing. The answer is that xgboost doesn’t treat the MVP probability like a winner-take-all competition that is really is. It is designed to classify the probability that a sample falls into one of two buckets, for example, is a given pitch more likely to be a ball or a strike? That question isn’t a contest like the MVP award is. So I had to classify each player-season as “more likely to be an MVP or non-MVP?” to make it work inside the way xgboost thinks.
Think of it like this. The model asks “given these stats about JD Martinez, what is the probability he wins the MVP?” The answer is something like 92%.
Then the algorithm discards what it knows about Martinez and asks: “given these stats about Mookie Betts, what is the probability _he_ wins the MVP?” The answer is something like 97%. But the algorithm has no knowledge about the stats compiled by Martinez. So it can’t say that 97% is higher than 92%. You and I have to apply our intelligence to say “of all the players measured, which has the highest chance of winning?”
I did some research but couldn’t find a way to predict the winner of a competition in the sense the MVP award is, without going through these steps.
2 thoughts:
Mookie had no real chance to amass a high RBI total-because he was a leadoff hitter.  He did lead the league in runs scored, tho (1 less run than the 130 RBI of Martinez).  JD was of course a cleanup hitter.  To say that voters would have zero understanding of this factor does them a disservice, even if it is just your model “saying” that.
It is clear that defense-1st positions (other than catcher) now seem to have virtually no weight and is pretty surprising, if one were to take a larger historical view.  Altuve was the 1st 2B to win since Pedroia in ’08: there hasn’t been a SS for MVP since Jimmy Rollins ’07 (and he was one of the weaker winners of course).  Posey and Mauer 1st catchers since Pudge in ’99. Trout 1st CF since Junior in ’97.
Contrast that with the 50’s/60’s, where I see the following:
C	4     [doesn’t include w/ my endpoints Bench in ’70 & ’72] 2B	1 SS	6 CF	5
Since 1999 inclusive:
C	3 2B	2 SS	3 CF	3
2009 inclusive:
C	1 2B	1 SS	0 CF	2
“To say that voters would have zero understanding of this factor does them a disservice, even if it is just your model “saying” that.”
Well, I never said voters would have zero understanding of this factor In fact it would be pretty straightforward to model ‘primary lineup position’ in a future run of the model, to see if voters give weight to that. I could do ‘runs scored’ in the same manner.
I’m more interested in the failures. I think you may be onto something when you mention “Humans like a good story” and that’s precisely what happened in at least some of the years where the model didn’t predict the actual winner: there was a story attached to those players which existed outside the inputs you used.  Posey was back from a serious leg injury, Bryant was on a Cubs “team of destiny”, etc.
You are officially a 3 ring binder nerd… mookie plays amazing defense, covers crazy ground in the hardest right field in baseball… he has a cannon for an arm and has plenty of extra base hits and homeruns, plus a .346 batting average… he also leads the league in your little WAR stat on the best team in baseball….  get that Mike Trout out of your pants and stop being a nerd… plus a triple crown on a 1st place team is not a dinosaur… it means you can freaking Rake! Your Angels are horrible, and while mike trout is probably the best player in the game, he wasn’t the best player in either of the single years you’re bitching about
Its interesting to see that OPS matters over WAR. I wonder if that has anything to do with the fact that they may be largely correlated or the fact that you are using rank.  I approached this problem using the scaled actual values of performance thinking that larger leads in categories would matter. Of course my goal was a bit different, I was trying to predict the overall order of the top 5 finishers. Posted it on FG a while back but here is a link https://sharpestats.com/thinking-like-an-mlb-mvp-voter/
Nice article man! I was also thinking that the magnitude of difference between players’ stat rankings would also make a difference. I’ll have to try that out next.
Care to share your work?

--------------------