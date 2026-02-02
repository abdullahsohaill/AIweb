# better format entity titles
**URL:** https://eugeneyan.com/writing/product-categorization-api-part-2-data-preparation
**Page Title:** Product Classification API Part 2: Data Preparation
--------------------


## eugeneyan

- Start Here
- Writing
- Speaking
- Prototyping
- About

## Product Classification API Part 2: Data Preparation

[ machinelearning python 🛠 ] · 8 min read
This post is part 2 of the series on building a product classification API. The API is available for demo here . Part 1 available here ; Part 3 available here . ( Github repositiory )
[LINK: here](/writing/product-categorization-api-part-1-data-acquisition-and-formatting/)
[LINK: here](/writing/product-categorization-api-part-3-creating-an-api/)
[LINK: Github repositiory](https://github.com/eugeneyan/datagene)
Update: API discontinued to save on cloud cost.
In part 1, we focused on data acquisition and formatting the categories. Here, we’ll focus on preparing the product titles (and short description, if you want) before training our model.
This is part of a series of posts on building a product classification API:
- Data acquisition and formatting (part 1)
[LINK: Data acquisition and formatting (part 1)](/writing/product-categorization-api-part-1-data-acquisition-and-formatting/)
- Data cleaning and preparation (part 2)
[LINK: Data cleaning and preparation (part 2)](/writing/product-categorization-api-part-2-data-preparation/)
- API development (part 3)
[LINK: API development (part 3)](/writing/product-categorization-api-part-3-creating-an-api/)
- Image classification demo
- Image search demo

## Measuring data purity

We’ll have products within our data that are categorized incorrectly. How do we exclude these mis-categorized products from our training set?
Here’s one approach: If two products have the same title but different category, we assume that at least one of the products is mis-categorized (and the data is dirty).
Extending on the above, as we take steps to prepare our data, we’ll be measuring data “purity” at each step. In this instance, purity is defined as:
Products with the same title and same category / Total number of products
This measures the proportion of products that have the same title and same category in our data. The higher the purity, the cleaner we can assume our data to be.
At the end of the data preparation , we’ll be able to identify which products are “impure”. Given that we’re unable to distinguish between correctly and incorrectly categorized products, we’ll exclude them from the training of the model.

## Preparing the title (and short descriptions)

The titles need a bit of cleaning and preparation before we can train our model on them. In the next steps, we’ll go through some sample data cleaning and preparation procedures.

## Encoding titles as ascii

It’s not uncommon to find non-ascii characters in data, sometimes due to sellers trying to add a touch of class to their product (e.g., Crème brûlée), or due to errors in scraping the data (e.g., & quot , & amp , & nbsp ).
Thus, before doing any further processing, we’ll ensure titles are properly encoded so that Crème brûlée -> Creme brulee, åöûëî -> aouei, and " &   -> “ & ‘.
Here’s the approach I took:
There’s quite a bit going on in the code above, so let’s examine it piece by piece:

## Lowercasing titles

Lowercasing titles is a fairly standard step in text processing. We’ll lowercase all title characters before proceeding.

## Tokenizing titles

One common way to tokenize text is via nltk.tokenize. I tried it and found it to be significantly slower than using regular regex. In addition, writing our own regex tokeniser gives us flexibility in excluding certain characters that are being used as a split character.
For example, we want to exclude the following words/phrases from being tokenised by splitting on the punctuation character in brackets. Intuitively, the punctuation characters provides essential information; empirically, keeping them led to greater accuracy during model training and validation.
- hyphen-words (-)
- 0.9 (.)
- 20% (%)
- black/red (/)
Here’s how we write our own tokeniser:

### Removing stop words

After tokenising our titles, we can proceed to remove stop words. The trick is in which stop words to remove. For the product classification API, I found a combination of the following to work well:
- Stop words: nltk.corpus.stopwords
- Colours: matplotlib.colors.cnames.keys
- Self-defined: We also define some words that come across as spam, such as “free”, “international”, etc.
At this point, after tokenising the titles, the tokens are stored in a list. We can remove stop words easy and cleanly via list comprehension, like so:

## Removing words that are solely numeric

We’ll also remove words that are solely numeric. Intuitively, an iPhone 7, iPhone 8, or iPhone 21 should all be categorized as a mobile phone, and having the numeric suffix does not add any additional useful information to categorize it better. Can you think of a product where removing the numerics would put it in different category?
Similar to above, removing numerics can be accomplished easily via list comprehension:

## Removing words with too few characters

We also remove words that have character length below a certain threshold. E.g., if the threshold is two, then single character words are removed; if the threshold is three, then words with two characters are removed.
To an untrained eye (like mine), double character words like “TX”, “AB”, “GT” doesn’t add much informational value to the title—though there are exceptions like “3M”. Via cross-validation, I found that removing these words led to increased accuracy.
Here’s how we remove these double character words—you can change the word length threshold to suit your needs:

## Removing duplicated words

Next, we exclude duplicated words in titles. Sometimes, titles have duplicate words due to sellers attempting to apply search engine optimisation (SEO) on their products to make them more findable. However, these duplicate words do not provide any additional information to categorizing products.
We can remove duplicate tokens by converting the token list to a token set—yes, this removes any sequential information in the title. However, we’re only doing this step to identify impure products that should not be used in training our model. During the actual data preparation, we will exclude this step.
Converting a list to a set shouldn’t be too difficult right? I’ve leave that for the reader.

## Removing empty titles

Lastly, after performing all the cleaning and preparation above, there may be some titles that have no text left. (This means that those titles only contained stop words, numerics, or words with < 3 character length.) We’ll exclude these products as well.

## Excluding titles that are impure

After doing the above, we’re left with titles in their most informational rich and dense form. In this case, we’re confident that products with identical titles and categories are correctly categorized, while products with identical titles but different categories have at least one error in them (i.e., impure)
Among the impure products, without having ground truth about which are correctly or incorrectly categorized, we’ll discard them and not use them to train our model.

## Conclusion

Whew! That’s a lot of work just to clean titles! Nonetheless, We’re largely done with the data preparation steps.
Next, we’re going to share about the framework to making this product classifier available online, via a simple web UI. This will involve the following:
- Writing a class to take in titles, prepare them, and categorize them.
- Writing a simple flask app
If you found this useful, please cite this write-up as:
Yan, Ziyou. (Dec 2016). Product Classification API Part 2: Data Preparation. eugeneyan.com.
        https://eugeneyan.com/writing/product-categorization-api-part-2-data-preparation/.
Join 11,800+ readers getting updates on machine learning, RecSys, LLMs, and engineering.

--------------------