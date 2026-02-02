# pullpush.io
**URL:** http://pullpush.io
**Page Title:** Pull Push Reddit API
--------------------


## PullPush Reddit API Documentation

[LINK: Documentation](https://pullpush.io/#docs)

## Special Thanks

I would like to extend special thanks to Reddit user Watchful1 for compiling Bittorrent data for Reddit. Without him this service would not be possible.

## Removal requests

Unfortunately Pushshift team has not removed any posts for which there are legitimate removal requests from the bittorrent files. PullPush has no power to remove them from there.
If you have submitted a removal request to Pushshift and you would like to remove the data from PullPush too, you will need to file a separate removal request.
If you would like your data to be removed from PullPush please submit a request by submitting a ticket in our ticket system removals.pullpush.io .

## Using the legacy https://api.pullpush.io endpoints

[LINK: https://api.pullpush.io](https://api.pullpush.io)
There are two main endpoints used to search all publicly available comments and submissions on Reddit:
- /reddit/search/comment
- /reddit/search/submission
In the next section, we will explore how to perform more effective searches using the comment search endpoint.

## Searching Comments

To search for comments, use the https://api.pullpush.io/reddit/search/comment/ endpoint. Let's start with a few examples and then go over the various parameters available when using this endpoint. One of the simplest searches is using just the q parameter. The q parameter is used to search for a specific word or phrase. Here is an example:
[LINK: https://api.pullpush.io/reddit/search/comment/](https://api.pullpush.io/reddit/search/comment/)
Search for the most recent comments mentioning the word "science"
https://api.pullpush.io/reddit/search/comment/?q=science
[LINK: https://api.pullpush.io/reddit/search/comment/?q=science](https://api.pullpush.io/reddit/search/comment/?q=science)
This will search the most recent comments with the term "science" in the body of the comment. This search is not case-sensitive, so it will find any occurence of the term "science" regardless of capitalization. The API defaults to sorting by recently made comments first. After performing this search, 100 results are returned. This is the default size for searches and can be adjusted using the size parameter. This will be discussed in further detail in the parameters section. Data is returned in JSON format and actual search results are included in the "data" key. There is also a "metadata" key that gives additional information about the search including total number of results found, how long the search took to process, etc.

## Search parameters for comments

There are numerous additional parameters that can be used when performing a comment search. Let's go over them and provide examples for each.

## Getting comments based on id

You can retrieve comments directly by using the ids parameter. To get a batch of comments by their id, use the following example:
Retrieve three comments using their base 36 id values
https://api.pullpush.io/reddit/comment/search?ids=dlrezc8,dlrawgw,dlrhbkq
[LINK: https://api.pullpush.io/reddit/comment/search?ids=dlrezc8,dlrawgw,dlrhbkq](https://api.pullpush.io/reddit/comment/search?ids=dlrezc8,dlrawgw,dlrhbkq)

## Using the subreddit parameter

There are quite a few parameters to review, so let's start by providing some more complex examples and how to use the parameters above. Let's continue with the previous example above and expand on our "science" keyword search. What if we wanted to search for the term "science" but restrict it to a specific subreddit? By using the subreddit parameter, we can do that:
Search for the most recent comments mentioning the word "science" within the subreddit /r/askscience
https://api.pullpush.io/reddit/search/comment/?q=science&subreddit=askscience
[LINK: https://api.pullpush.io/reddit/search/comment/?q=science&subreddit=askscience](https://api.pullpush.io/reddit/search/comment/?q=science&subreddit=askscience)

## Using the sort and size parameters

This will return 100 comments containing the term "science" but only from the /r/askscience subreddit. Since we didn't ask for a specific sort method, the most recent comments are returned (the sort parameter defaults to "desc"). What if we wanted the first comment ever to /r/askscience that mentioned the word "science"? We could use the sort and size parameters to handle that.
Search for the most recent comments mentioning the word "science" within the subreddit /r/askscience
https://api.pullpush.io/reddit/search/comment/?q=science&subreddit=askscience&sort=asc&size=1
[LINK: https://api.pullpush.io/reddit/search/comment/?q=science&subreddit=askscience&sort=asc&size=1](https://api.pullpush.io/reddit/search/comment/?q=science&subreddit=askscience&sort=asc&size=1)
This is the result:
From the result returned, we can see that the first comment ever made to /r/askscience mentioning "science" happened on epoch date 1270637661, which translates to Wednesday, April 7, 2010 10:54:21 AM (GMT). Let's quickly go over the metadata pieces. We can see that the execution time for this search was around 30 milliseconds. There were a total of 36 shards searched and all were successful. The search did not time out (timed_out parameter) which is good. This is an attribute you may want to check if you use the API programmatically as some searches that are more complicated may sometimes time out. The total_results value is 134,785. This tells us the total number of comments in /r/askscience that mention the word science. Since we did not use the before or after parameters, this number represents the entirety of the comments made to /r/askscience.

## Using the before and after parameters

Let's continue by using additional parameters to highlight the power of the search API. The before and after parameters allow you to restrict the time-frame for the search by giving an epoch timestamp for both. However, the API also understands more human-like values for the before and after parameters. You can use a number followed by the characters s,m,h,d (which stand for second, minute, hour and day) to limit the time-frame as well. Let's run through some examples.
If you wanted to do a search for "Rome" in the subreddit /r/askhistorians but limit it only to the past 30 days, you could use the after parameter with the value 30d (30 days).
Search the subreddit /r/askhistorians for comments mentioning Rome within the past 30 days
https://api.pullpush.io/reddit/search/comment/?q=rome&subreddit=askhistorians&after=30d
[LINK: https://api.pullpush.io/reddit/search/comment/?q=rome&subreddit=askhistorians&after=30d](https://api.pullpush.io/reddit/search/comment/?q=rome&subreddit=askhistorians&after=30d)
What if there was a recent news story three days ago, but we wanted to limit the search window between 4 days ago and 2 days ago? We could use both the before and after parameter to do so. In the next example, we will search for comments mentioning Trump that were made between 4 and 2 days ago and sort by ascending.
Search all subreddits for the term "Trump" and return comments made between 2 and 4 days ago
https://api.pullpush.io/reddit/search/comment/?q=trump&after=4d&before=2d&sort=asc
[LINK: https://api.pullpush.io/reddit/search/comment/?q=trump&after=4d&before=2d&sort=asc](https://api.pullpush.io/reddit/search/comment/?q=trump&after=4d&before=2d&sort=asc)

## Using the author parameter

Using one of the examples above that searched for the first occurrence of the word "science" in the subreddit /r/askscience, we saw that the author of the comment was "MockDeath." What if we wanted to get the first 100 comments that "MockDeath" made to Reddit? We can use the author parameter, along with the sort and size parameters.
Search all subreddits and get the first 100 comments ever made by the user /u/MockDeath
https://api.pullpush.io/reddit/search/comment/?author=MockDeath&sort=asc&size=100
[LINK: https://api.pullpush.io/reddit/search/comment/?author=MockDeath&sort=asc&size=100](https://api.pullpush.io/reddit/search/comment/?author=MockDeath&sort=asc&size=100)

## Searching Submissions

To search for submissions, use the endpoint https://api.pullpush.io/reddit/search/submission/ endpoint. Let's start with a few examples and then go over the various parameters available when using this endpoint. To do a simple search, the q parameter is used to search for a specific word or phrase. Here is an example:
[LINK: https://api.pullpush.io/reddit/search/submission/](https://api.pullpush.io/reddit/search/submission/)
Search for the most recent submissions mentioning the word "science"
https://api.pullpush.io/reddit/search/submission/?q=science
[LINK: https://api.pullpush.io/reddit/search/submission/?q=science](https://api.pullpush.io/reddit/search/submission/?q=science)
This will search for the most recent submissions with the word science in the title or selftext. The search is not case-sensitive, so it will find any occurrence of science regardless of capitalization. The API defaults to sorting by the most recently made submissions first. After running this search, 25 results are returned. This is the default size for searches and can be changed by using the size parameter. This will be discussed in further detail in the parameters section. Data are returned in JSON format and results are included in the "data" key.

## Search parameters for submissions

There are numerous additional parameters that can be used when performing a submission search. Let's go over each of them now and provide examples for each one.

## Get all comment ids for a particular submission

This call is very helpful when used along with Reddit's API. When there are large submissions with thousands of comments, it is often difficult to get all the comment ids for a submission. This call will return an array of comment ids when a submission id is passed to it.
This call will return a data key with an array of comment ids. You can then retrieve the actual comment information from this API or the Reddit API. If the submission is fairly new, it is better to use the Reddit API to get the most current score for the comments.
Retrieve all comment ids for a submission object
https://api.pullpush.io/reddit/search/comment/?link_id=6uey5x
[LINK: https://api.pullpush.io/reddit/search/comment/?link_id=6uey5x](https://api.pullpush.io/reddit/search/comment/?link_id=6uey5x)

--------------------