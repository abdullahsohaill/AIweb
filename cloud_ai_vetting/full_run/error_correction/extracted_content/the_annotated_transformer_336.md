# The Annotated Transformer
**URL:** https://nlp.seas.harvard.edu/annotated-transformer
**Page Title:** The Annotated Transformer
--------------------


## The Annotated Transformer

Attention is All You Need
- v2022: Austin Huang, Suraj Subramanian, Jonathan Sum, Khalid Almubarak, and Stella Biderman.
- Original : Sasha Rush .
The Transformer has been on a lot of people’s minds over the last year five years. This post presents an annotated version of the paper in the form of a line-by-line implementation. It reorders and deletes some sections from the original paper and adds comments throughout. This document itself is a working notebook, and should be a completely usable implementation. Code is available here .
[LINK: here](https://github.com/harvardnlp/annotated-transformer/)

### Table of Contents

- Prelims
- Background
- Part 1: Model Architecture
- Model Architecture Encoder and Decoder Stacks Position-wise Feed-Forward Networks Embeddings and Softmax Positional Encoding Full Model Inference:
- Encoder and Decoder Stacks
- Position-wise Feed-Forward Networks
- Embeddings and Softmax
- Positional Encoding
- Full Model
- Inference:
- Part 2: Model Training
- Training Batches and Masking Training Loop Training Data and Batching Hardware and Schedule Optimizer Regularization
- Batches and Masking
- Training Loop
- Training Data and Batching
- Hardware and Schedule
- Optimizer
- Regularization
- A First Example Synthetic Data Loss Computation Greedy Decoding
- Synthetic Data
- Loss Computation
- Greedy Decoding
- Part 3: A Real World Example Data Loading Iterators Training the System
- Data Loading
- Iterators
- Training the System
- Additional Components: BPE, Search, Averaging
- Results Attention Visualization Encoder Self Attention Decoder Self Attention Decoder Src Attention
- Attention Visualization
- Encoder Self Attention
- Decoder Self Attention
- Decoder Src Attention
- Conclusion

## Prelims

Skip
My comments are blockquoted. The main text is all from the paper itself.

## Background

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU, ByteNet and ConvS2S, all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention.
Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations. End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks.
To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequence aligned RNNs or convolution.

## Part 1: Model Architecture

## Model Architecture

Most competitive neural sequence transduction models have an encoder-decoder structure (cite) . Here, the encoder maps an input sequence of symbol representations ( x 1 , . . . , x n ) (x_1, ..., x_n) ( x 1 ​ , ... , x n ​ ) to a sequence of continuous representations z = ( z 1 , . . . , z n ) \mathbf{z} = (z_1, ..., z_n) z = ( z 1 ​ , ... , z n ​ ) . Given z \mathbf{z} z , the decoder then generates an output sequence ( y 1 , . . . , y m ) (y_1,...,y_m) ( y 1 ​ , ... , y m ​ ) of symbols one element at a time. At each step the model is auto-regressive (cite) , consuming the previously generated symbols as additional input when generating the next.
The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively.

## Encoder and Decoder Stacks

### Encoder

The encoder is composed of a stack of N = 6 N=6 N = 6 identical layers.
We employ a residual connection (cite) around each of the two sub-layers, followed by layer normalization (cite) .
That is, the output of each sub-layer is L a y e r N o r m ( x + S u b l a y e r ( x ) ) \mathrm{LayerNorm}(x + \mathrm{Sublayer}(x)) LayerNorm ( x + Sublayer ( x )) , where S u b l a y e r ( x ) \mathrm{Sublayer}(x) Sublayer ( x ) is the function implemented by the sub-layer itself. We apply dropout (cite) to the output of each sub-layer, before it is added to the sub-layer input and normalized.
To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension d model = 512 d_{\text{model}}=512 d model ​ = 512 .
Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected feed-forward network.

### Decoder

The decoder is also composed of a stack of N = 6 N=6 N = 6 identical layers.
In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization.
We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position i i i can depend only on the known outputs at positions less than i i i .
Below the attention mask shows the position each tgt word (row) is allowed to look at (column). Words are blocked for attending to future words during training.

### Attention

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.
We call our particular attention “Scaled Dot-Product Attention”. The input consists of queries and keys of dimension d k d_k d k ​ , and values of dimension d v d_v d v ​ . We compute the dot products of the query with all keys, divide each by d k \sqrt{d_k} d k ​ ​ , and apply a softmax function to obtain the weights on the values.
In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix Q Q Q . The keys and values are also packed together into matrices K K K and V V V . We compute the matrix of outputs as:
A t t e n t i o n ( Q , K , V ) = s o f t m a x ( Q K T d k ) V \mathrm{Attention}(Q, K, V) = \mathrm{softmax}(\frac{QK^T}{\sqrt{d_k}})V Attention ( Q , K , V ) = softmax ( d k ​ ​ Q K T ​ ) V
The two most commonly used attention functions are additive attention (cite) , and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of 1 d k \frac{1}{\sqrt{d_k}} d k ​ ​ 1 ​ . Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code.
While for small values of d k d_k d k ​ the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of d k d_k d k ​ (cite) . We suspect that for large values of d k d_k d k ​ , the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients (To illustrate why the dot products get large, assume that the components of q q q and k k k are independent random variables with mean 0 0 0 and variance 1 1 1 . Then their dot product, q ⋅ k = ∑ i = 1 d k q i k i q \cdot k = \sum_{i=1}^{d_k} q_ik_i q ⋅ k = ∑ i = 1 d k ​ ​ q i ​ k i ​ , has mean 0 0 0 and variance d k d_k d k ​ .). To counteract this effect, we scale the dot products by 1 d k \frac{1}{\sqrt{d_k}} d k ​ ​ 1 ​ .
Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this.
M u l t i H e a d ( Q , K , V ) = C o n c a t ( h e a d 1 , . . . , h e a d h ) W O where h e a d i = A t t e n t i o n ( Q W i Q , K W i K , V W i V ) \mathrm{MultiHead}(Q, K, V) =
    \mathrm{Concat}(\mathrm{head_1}, ..., \mathrm{head_h})W^O \\
    \text{where}~\mathrm{head_i} = \mathrm{Attention}(QW^Q_i, KW^K_i, VW^V_i) MultiHead ( Q , K , V ) = Concat ( hea d 1 ​ , ... , hea d h ​ ) W O where hea d i ​ = Attention ( Q W i Q ​ , K W i K ​ , V W i V ​ )
Where the projections are parameter matrices W i Q ∈ R d model × d k W^Q_i \in \mathbb{R}^{d_{\text{model}} \times d_k} W i Q ​ ∈ R d model ​ × d k ​ , W i K ∈ R d model × d k W^K_i \in \mathbb{R}^{d_{\text{model}} \times d_k} W i K ​ ∈ R d model ​ × d k ​ , W i V ∈ R d model × d v W^V_i \in \mathbb{R}^{d_{\text{model}} \times d_v} W i V ​ ∈ R d model ​ × d v ​ and W O ∈ R h d v × d model W^O \in \mathbb{R}^{hd_v \times d_{\text{model}}} W O ∈ R h d v ​ × d model ​ .
In this work we employ h = 8 h=8 h = 8 parallel attention layers, or heads. For each of these we use d k = d v = d model / h = 64 d_k=d_v=d_{\text{model}}/h=64 d k ​ = d v ​ = d model ​ / h = 64 . Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality.

### Applications of Attention in our Model

The Transformer uses multi-head attention in three different ways: 1) In “encoder-decoder attention” layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as (cite) .
- The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder.
The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder.
- Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to − ∞ -\infty − ∞ ) all values in the input of the softmax which correspond to illegal connections.
Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to − ∞ -\infty − ∞ ) all values in the input of the softmax which correspond to illegal connections.

## Position-wise Feed-Forward Networks

In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied to each position separately and identically. This consists of two linear transformations with a ReLU activation in between.
F F N ( x ) = max ⁡ ( 0 , x W 1 + b 1 ) W 2 + b 2 \mathrm{FFN}(x)=\max(0, xW_1 + b_1) W_2 + b_2 FFN ( x ) = max ( 0 , x W 1 ​ + b 1 ​ ) W 2 ​ + b 2 ​
While the linear transformations are the same across different positions, they use different parameters from layer to layer. Another way of describing this is as two convolutions with kernel size 1. The dimensionality of input and output is d model = 512 d_{\text{model}}=512 d model ​ = 512 , and the inner-layer has dimensionality d f f = 2048 d_{ff}=2048 d ff ​ = 2048 .

## Embeddings and Softmax

Similarly to other sequence transduction models, we use learned embeddings to convert the input tokens and output tokens to vectors of dimension d model d_{\text{model}} d model ​ . We also use the usual learned linear transformation and softmax function to convert the decoder output to predicted next-token probabilities. In our model, we share the same weight matrix between the two embedding layers and the pre-softmax linear transformation, similar to (cite) . In the embedding layers, we multiply those weights by d model \sqrt{d_{\text{model}}} d model ​ ​ .

## Positional Encoding

Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add “positional encodings” to the input embeddings at the bottoms of the encoder and decoder stacks. The positional encodings have the same dimension d model d_{\text{model}} d model ​ as the embeddings, so that the two can be summed. There are many choices of positional encodings, learned and fixed (cite) .
In this work, we use sine and cosine functions of different frequencies:
P E ( p o s , 2 i ) = sin ⁡ ( p o s / 1000 0 2 i / d model ) PE_{(pos,2i)} = \sin(pos / 10000^{2i/d_{\text{model}}}) P E ( p os , 2 i ) ​ = sin ( p os /1000 0 2 i / d model ​ )
P E ( p o s , 2 i + 1 ) = cos ⁡ ( p o s / 1000 0 2 i / d model ) PE_{(pos,2i+1)} = \cos(pos / 10000^{2i/d_{\text{model}}}) P E ( p os , 2 i + 1 ) ​ = cos ( p os /1000 0 2 i / d model ​ )
where p o s pos p os is the position and i i i is the dimension. That is, each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from 2 π 2\pi 2 π to 10000 ⋅ 2 π 10000 \cdot 2\pi 10000 ⋅ 2 π . We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset k k k , P E p o s + k PE_{pos+k} P E p os + k ​ can be represented as a linear function of P E p o s PE_{pos} P E p os ​ .
In addition, we apply dropout to the sums of the embeddings and the positional encodings in both the encoder and decoder stacks. For the base model, we use a rate of P d r o p = 0.1 P_{drop}=0.1 P d ro p ​ = 0.1 .
Below the positional encoding will add in a sine wave based on position. The frequency and offset of the wave is different for each dimension.
We also experimented with using learned positional embeddings (cite) instead, and found that the two versions produced nearly identical results. We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.

## Full Model

Here we define a function from hyperparameters to a full model.

## Inference:

Here we make a forward step to generate a prediction of the model. We try to use our transformer to memorize the input. As you will see the output is randomly generated due to the fact that the model is not trained yet. In the next tutorial we will build the training function and try to train our model to memorize the numbers from 1 to 10.

## Part 2: Model Training

## Training

This section describes the training regime for our models.
We stop for a quick interlude to introduce some of the tools needed to train a standard encoder decoder model. First we define a batch object that holds the src and target sentences for training, as well as constructing the masks.

## Batches and Masking

Next we create a generic training and scoring function to keep track of loss. We pass in a generic loss compute function that also handles parameter updates.

## Training Loop

## Training Data and Batching

We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair encoding, which has a shared source-target vocabulary of about 37000 tokens. For English-French, we used the significantly larger WMT 2014 English-French dataset consisting of 36M sentences and split tokens into a 32000 word-piece vocabulary.
Sentence pairs were batched together by approximate sequence length. Each training batch contained a set of sentence pairs containing approximately 25000 source tokens and 25000 target tokens.

## Hardware and Schedule

We trained our models on one machine with 8 NVIDIA P100 GPUs. For our base models using the hyperparameters described throughout the paper, each training step took about 0.4 seconds. We trained the base models for a total of 100,000 steps or 12 hours. For our big models, step time was 1.0 seconds. The big models were trained for 300,000 steps (3.5 days).

## Optimizer

We used the Adam optimizer (cite) with β 1 = 0.9 \beta_1=0.9 β 1 ​ = 0.9 , β 2 = 0.98 \beta_2=0.98 β 2 ​ = 0.98 and ϵ = 1 0 − 9 \epsilon=10^{-9} ϵ = 1 0 − 9 . We varied the learning rate over the course of training, according to the formula:
l r a t e = d model − 0.5 ⋅ min ⁡ ( s t e p _ n u m − 0.5 , s t e p _ n u m ⋅ w a r m u p _ s t e p s − 1.5 ) lrate = d_{\text{model}}^{-0.5} \cdot
  \min({step\_num}^{-0.5},
    {step\_num} \cdot {warmup\_steps}^{-1.5}) l r a t e = d model − 0.5 ​ ⋅ min ( s t e p _ n u m − 0.5 , s t e p _ n u m ⋅ w a r m u p _ s t e p s − 1.5 )
This corresponds to increasing the learning rate linearly for the first w a r m u p _ s t e p s warmup\_steps w a r m u p _ s t e p s training steps, and decreasing it thereafter proportionally to the inverse square root of the step number. We used w a r m u p _ s t e p s = 4000 warmup\_steps=4000 w a r m u p _ s t e p s = 4000 .
Note: This part is very important. Need to train with this setup of the model.
Example of the curves of this model for different model sizes and for optimization hyperparameters.

## Regularization

### Label Smoothing

During training, we employed label smoothing of value ϵ l s = 0.1 \epsilon_{ls}=0.1 ϵ l s ​ = 0.1 (cite) . This hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU score.
We implement label smoothing using the KL div loss. Instead of using a one-hot target distribution, we create a distribution that has confidence of the correct word and the rest of the smoothing mass distributed throughout the vocabulary.
Here we can see an example of how the mass is distributed to the words based on confidence.
Label smoothing actually starts to penalize the model if it gets very confident about a given choice.

## A First Example

We can begin by trying out a simple copy-task. Given a random set of input symbols from a small vocabulary, the goal is to generate back those same symbols.

## Synthetic Data

## Loss Computation

## Greedy Decoding

This code predicts a translation using greedy decoding for simplicity.

## Part 3: A Real World Example

Now we consider a real-world example using the Multi30k German-English Translation task. This task is much smaller than the WMT task considered in the paper, but it illustrates the whole system. We also show how to use multi-gpu processing to make it really fast.

## Data Loading

We will load the dataset using torchtext and spacy for tokenization.
Batching matters a ton for speed. We want to have very evenly divided batches, with absolutely minimal padding. To do this we have to hack a bit around the default torchtext batching. This code patches their default batching to make sure we search over enough sentences to find tight batches.

## Iterators

## Training the System

Once trained we can decode the model to produce a set of translations. Here we simply translate the first sentence in the validation set. This dataset is pretty small so the translations with greedy search are reasonably accurate.

## Additional Components: BPE, Search, Averaging

So this mostly covers the transformer model itself. There are four aspects that we didn’t cover explicitly. We also have all these additional features implemented in OpenNMT-py .
[LINK: OpenNMT-py](https://github.com/opennmt/opennmt-py)
- BPE/ Word-piece: We can use a library to first preprocess the data into subword units. See Rico Sennrich’s subword-nmt implementation. These models will transform the training data to look like this:
[LINK: subword-nmt](https://github.com/rsennrich/subword-nmt)
▁Die ▁Protokoll datei ▁kann ▁ heimlich ▁per ▁E - Mail ▁oder ▁FTP ▁an ▁einen ▁bestimmte n ▁Empfänger ▁gesendet ▁werden .
- Shared Embeddings: When using BPE with shared vocabulary we can share the same weight vectors between the source / target / generator. See the (cite) for details. To add this to the model simply do this:
- Beam Search: This is a bit too complicated to cover here. See the OpenNMT-py for a pytorch implementation.
[LINK: OpenNMT-py](https://github.com/OpenNMT/OpenNMT-py/)
- Model Averaging: The paper averages the last k checkpoints to create an ensembling effect. We can do this after the fact if we have a bunch of models:

## Results

On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported models (including ensembles) by more than 2.0 BLEU, establishing a new state-of-the-art BLEU score of 28.4. The configuration of this model is listed in the bottom line of Table 3. Training took 3.5 days on 8 P100 GPUs. Even our base model surpasses all previously published models and ensembles, at a fraction of the training cost of any of the competitive models.
On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 the training cost of the previous state-of-the-art model. The Transformer (big) model trained for English-to-French used dropout rate Pdrop = 0.1, instead of 0.3.
With the addtional extensions in the last section, the OpenNMT-py replication gets to 26.9 on EN-DE WMT. Here I have loaded in those parameters to our reimplemenation.

## Attention Visualization

Even with a greedy decoder the translation looks pretty good. We can further visualize it to see what is happening at each layer of the attention

## Encoder Self Attention

## Decoder Self Attention

## Decoder Src Attention

## Conclusion

Hopefully this code is useful for future research. Please reach out if you have any issues.
Cheers, Sasha Rush, Austin Huang, Suraj Subramanian, Jonathan Sum, Khalid Almubarak, Stella Biderman

--------------------