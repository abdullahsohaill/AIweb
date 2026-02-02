# Night Shade
**URL:** https://nightshade.cs.uchicago.edu/whatis.html
**Page Title:** Nightshade: Protecting Copyright
--------------------

- Glaze and Nightshade About Us What is Nightshade Glaze WebGlaze
- About Us
- What is Nightshade
- Glaze
- WebGlaze
- Q & A
- Download
- User's Guide
- Email
- Papers/Media

## What Is Nightshade?

Since their arrival, generative AI models and their trainers have demonstrated their ability to download 
            any online content for model training. For content owners and creators, few tools can prevent their content 
            from being fed into a generative AI model against their will. Opt-out lists have been disregarded by model 
            trainers in the past, and can be easily ignored with zero consequences. They are unverifiable and 
            unenforceable, and those who violate opt-out lists and do-not-scrape directives can not be identified with 
            high confidence.
In an effort to address this power asymmetry, we have designed and implemented Nightshade, a tool that 
	    turns any image into a data sample that is unsuitable for model training. More precisely, Nightshade 
	    transforms images into "poison" samples, so that models training on them without consent will see their 
	    models learn unpredictable behaviors that deviate from expected norms, e.g. a prompt that asks for an image 
	    of a cow flying in space might instead get an image of a handbag floating in space.
Used responsibly, Nightshade can help deter model trainers who disregard copyrights, opt-out lists, and 
	    do-not-scrape/robots.txt directives. It does not rely on the kindness of model trainers, but instead 
	    associates a small incremental price on each piece of data scraped and trained without authorization. 
	    Nightshade's goal is not to break models, but to increase the cost of training on unlicensed data, such that 
	    licensing images from their creators becomes a viable alternative.
Nightshade works similarly as Glaze, but instead of a defense against style mimicry, it is 
	    designed as an offense tool to distort feature representations inside generative AI image models. Like 
	    Glaze, Nightshade is computed as a multi-objective optimization that minimizes visible changes to the 
	    original image. While human eyes see a shaded image that is largely unchanged from the original, the AI 
	    model sees a dramatically different composition in the image. For example, human eyes might see a shaded image of a cow in a green field largely unchanged, but an AI model might see a large leather 
	    purse lying in the grass. Trained on a sufficient number of shaded images that include a cow, a model will 
	    become increasingly convinced cows have nice brown leathery handles and smooth side pockets with a zipper, 
	    and perhaps a lovely brand logo.
As with Glaze, Nightshade effects are robust to normal changes one might apply to an image. You can crop 
	    it, resample it, compress it, smooth out pixels, or add noise, and the effects of the poison will remain. 
	    You can take screenshots, or even photos of an image displayed on a monitor, and the shade effects remain. 
	    Again, this is because it is not a watermark or hidden message (steganography), and it is not brittle.
Nightshade vs. Glaze. A common question is, what is the difference between Nightshade and 
	    Glaze. The answer is that Glaze is a defensive tool that individual artists can use to protect 
	    themselves against style mimicry attacks, while Nightshade is an offensive tool that artists can use as 
	    a group to disrupt models that scrape their images without consent (thus protecting all artists against 
	    these models). Glaze should be used on every piece of artwork artists post online to protect themselves, 
	    while Nightshade is an entirely optional feature that can be used to deter unscrupulous model trainers. 
	    Artists who post their own art online should ideally have both Glaze AND Nightshade applied to their 
	    artwork. We are working on an integrated release of these tools.
Risks and Limitations.
- Changes made by Nightshade are more visible on art with flat colors and smooth backgrounds. Because Nightshade is 
  about disrupting models, lower levels of intensity/poison do not have negative consequences for the image owner. Thus 
  we have included a low intensity setting for those interested in prioritizing the visual quality of the original image.
- As with any security attack or defense, Nightshade is unlikely to stay future proof over long periods of time. But 
	as an attack, Nightshade can easily evolve to continue to keep pace with any potential countermeasures/defenses.
Our goals. As with Glaze, our primary goals are to discover and learn new things through our research, and to 
make a positive impact on the world. I (Ben) speak for myself (but I think the team as well) when I say that we are not 
interested in profit. Like Glaze, Nightshade is designed to run without a network, so there is no data (or art) sent 
back to us or anyone else.
Nightshade and WebGlaze. Nightshade v1.0 is designed as a standalone tool. It does not provide mimicry 
protection like Glaze, so please be cautious in how you use it. Do not post shaded images of your art if you are at all 
concerned about style mimicry. We are testing how Nightshade co-exists with Glaze, and when ready, we will release 
Nightshade as an add-on to Webglaze, so that Webglaze users can apply Nightshade and Glaze together in one pass on a 
single image.
For more info on Nightshade, please take a look at the User guide on installing, 
  running/configuring, and uninstalling Nightshade. You can also read Nightshade's technical paper: Nightshade: Prompt-Specific Poisoning Attacks on Text-to-Image Generative Models Shawn Shan, Wenxin Ding, Josephine Passananti, Haitao Zheng, Ben Y. Zhao To Appear: Proceedings of 45th IEEE Symposium on Security and Privacy, San Francisco CA, May 2024. Preprint: arxiv/2310.13828 , February 2024.
Samples . These are posted with permission from the respective artists.
Background Image: Dive , Jingna Zhang

--------------------