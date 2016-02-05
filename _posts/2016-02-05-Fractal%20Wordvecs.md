---
layout: page
title: Fractal Structure in Word2Vec Word Embeddings
---

I like fractals. After long experience with them, I have come to the conclusion that I do not like to see them. I am completely indifferent to their beauty, although of course they are beautiful. I like them for their [statistical](http://arxiv.org/abs/cond-mat/0412004) [omnipresence](http://physics.stackexchange.com/questions/55269/why-do-fractal-systems-show-power-law-behavior), as most statisticians like the Gaussian.

I will claim that the global structure of the set of points created by word2vec in a high-dimensional vector space might have an empirical [fractal dimension](https://en.wikipedia.org/wiki/Fractal_dimension) far lower than the ordinary, everyday dimension, and buttress this claim with evidence.

I am not really satisfied with nearly any definition of fractal, but I will note that by some definitions, that set of points is a fractal set.

I will have one chart and _no other pictures_.

It is exceedingly easy to intuitively define what a fractal is if you are allowed to use pictures and exceedingly difficult if you are not allowed to use pictures. I will use one possible definition of many, promulgated by [Mandelbrot 1983](http://www.amazon.com/Fractal-Geometry-Nature-Benoit-Mandelbrot/dp/0716711869): having a fractal dimension greater than the [topological dimension](https://en.wikipedia.org/wiki/Lebesgue_covering_dimension).

This is a sufficient, but not a necessary definition. That is, although passing this test means that it's a fractal, there are fractals which are evidently fractals that do not pass this test (say, the [Peano curve](https://en.wikipedia.org/wiki/Peano_curve)).

Unfortunately, fractal dimension (Hausdorff-Besicovich dimension) can only be calculated, not empirically measured: approximations have to be made for real sets. We will use [correlation dimension](https://en.wikipedia.org/wiki/Correlation_dimension), which Wikipedia describes better than I can.

Topological dimension is more difficult. One has the intuition that a set of points which is in the shape of a circle has a sort of "empirical" topological dimension which should not necessarily be zero topological dimension which is the formal definition. To my knowledge, however, there is no procedure for empirically determining that quantity.

Anyhow, by the strict Mandelbrot 1983 definition, because the topological dimension of a set of points is zero, if we find any self-similarity at all in this set of points, this is a fractal self-similarity. (Non-fractal self-similarities are quite ordinary: lines, spheres, and other such geometric objects).

Upon inspection, you may note that the procedure for finding correlation dimension is subject to the [curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality). To ameliorate that curse, I take a comparatively low-dimensionality word2vec: only 10 dimensions.The other existing measures of dimension used for this kind of analysis ([Minkowski-Bouligand dimension](http://mathworld.wolfram.com/InformationDimension.html) and [information dimension](http://mathworld.wolfram.com/InformationDimension.html)) get it worse, though.

The algorithm to get correlation dimension is also O(n^2) with n being the number of points, so I take a 10,000 point sample of the vectors only.

Correlation dimension has more numerical problems than the Wikipedia article notes for it, especially in low dimension: it often comes to pass that a point sampling of a circle or other non-fractal 2d polygon will have an empirical correlation dimension value of something like 1.9. But correlation dimension will, for example, get the dimension for Sierpinski triangles roughly right, at about 1.54 (the analytical Hausdorff-Besicovich dimension is known for them, at log(3) / log(2), or about 1.58).

The corpus is the [Brown corpus](http://www.nltk.org/book/ch02.html#brown-corpus), from newspapers. The word2vec implementation is the [Python wrapper](https://github.com/danielfrg/word2vec) around the original implementation. The code for the analysis of the vectors is [here](https://github.com/howonlee/wordvec_fractal). And now, the chart.

![chart](http://i.imgur.com/Q93bjtd.png)

As you can see, the calculated slope (which we interpret as the embedding dimension) is about 5.7, which is a lot less than the number of dimensions that the points are situated in, and indeed greater than the topological dimension of the points.

So it is a fractal by the Mandelbrot 1983 definition, but remember that this definition is unsatisfying (I haven't really found any satisfying ones). You might think that it's a fractal because of its noninteger dimension, but remember the numerical problems with correlation dimension.

This scaling is not really an incredibly durable phenomenon: outside of the range of these epsilons, the global structure of the whole range looks far more like a logistic function (because at tiny epsilons, there are no neighbors, and at huge epsilons, all points are neighbors). So this is not like the really impressive demonstrations of self-similar structure, because there are so few orders of magnitude.

But it _is_ a self-similarity, and _that_ is an empirical statement.

I won't give any explanations for the phenomenon. Perhaps chaos is involved, given that this phenomenon could be construed as a sort of view of an attractor. I note that many dynamical analyses of neural network phenomena leave out chaotic analyses, like [Pascanu Mikolov Bengio 2013](http://www.jmlr.org/proceedings/papers/v28/pascanu13.pdf) (although Pascanu Mikolov Bengio 2013 is for recursive neural networks). But if these systems have fractal (strange) attractors, the possibility of chaos __must__ be investigated.

I would hypothesize that this is not an extraordinarily particular phenomenon with respect to neural representations, limited to word2vec. Fractal structures and power-law distributions seem to be surprisingly common in neural networks. Try training a simple backpropagation multilayer perceptron on MNIST and then [take the histograms](https://github.com/howonlee/mlp_gradient_histograms) of the absolute values of the weights - you will get a very heavy tail on that histogram (and that __is__ a pretty durable phenomenon, in a variety of ways). I am currently implementing the [Clauset Shalizi Newman 2007](http://arxiv.org/abs/0706.1062) steps to find if it's a proper power law.
 
I wish to also state a related contention. In the year 2016, if someone is told to model a random landscape, an imaginary landscape generated by computer, they would be remiss if they did not think about fractals. I believe that in modelling a different kind of imaginary landscape - the energy landscapes that gradient descent algorithms rattle about in - we should investigate whether it is also remiss in this case to not think a little about fractals. Perhaps it would be a step towards understanding their structure, including the most important and most mystifying energy landscape, that of neural networks.
