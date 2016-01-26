Poking at Causation 1.3 / 3 : Social Network Patterns in Neural Network (Multilayer Perceptron) Gradients
----

All the code that I used is on [github](https://github.com/howonlee/mlp_gradient_networks).

I wish to note a strange phenomenon which appears when one does a strange thing to a neural network gradient. I do not pretend to have a justification for doing this, except that it was fun.

Take a gradient for a SGD step on a "plain" multilayer perceptron,

![gradient](http://i.imgur.com/TrMcG46.png)

take the absolute value,

![abs gradient](http://i.imgur.com/fYpj4sZ.png)

normalize it so that the extremal matrix member of that gradient is 1,

![norm gradient](http://i.imgur.com/MdzzSHM.png)

and then sample it as if the gradient was a distribution over matrices.

![sampled gradient](http://i.imgur.com/HlB8PhA.png)

Construe the resulting matrix as an adjacency matrix, so you get a network out of it. I will claim that this network looks like a social network in some ways. This is because it shows a series of network patterns common to social networks, among other complex networks.

This network shows a [degree distribution](http://users.phys.psu.edu/~ralbert/phys597_09/c03_netw_prop.pdf) with high skew and kurtosis on the outdegree. The indegrees depend solely on the data only, unfortunately, because we are looking at the input-hidden weights.

You could argue that this whole thing boils down to "hey, the histogram of cached deltas in backprop have high skew and kurtosis" and that could also be a worthwhile thing to say, I think. It would be stay a coherent statement when the number of hidden variables is not equal to the number of inputs, too, but this network theory business is funner.

![deg distribution](http://i.imgur.com/wdMh8a8.png)

It also shows a small [diameter](http://mathworld.wolfram.com/GraphDiameter.html), in this case 4, and large [average clustering coefficient](https://networkx.github.io/documentation/latest/reference/algorithms.clustering.html), in this case 0.279.

The phenomenon is durable to different datasets (the above was on an MNIST digit).

![cifar](http://i.imgur.com/zOwsTS1.png)

(Diameter is 4 and average clustering coefficient 0.215 on this CIFAR-10 SGD step.)

Different learning speeds,

# show 0.01, 1.0 degree distribution, diameter, cc
![smalllearn](http://i.imgur.com/KMQmzFq.png)
(Diameter is 5 and average clustering coefficient 0.259 for 0.01 learning rate)
![biglearn](http://i.imgur.com/jAkOjLx.png)
(Diameter is 6 and average clustering coefficient 0.08 for 1.0 learning rate)

Note that the large average  clustering coefficient thing deteriorates a little bit on learn rate 1.0, which is of course too high a learning rate.

So this induced network looks kind of like a social network. Or any of the other complex networks out there, like [linguistic networks](http://research.microsoft.com/pubs/81246/review_of_linguistic_networks.pdf) or [actual neural networks in C. Elegans](http://arxiv.org/pdf/0907.2373.pdf). Or the degree distribution looks like the [distribution of money in a market](http://online.itp.ucsb.edu/online/colloq/yakovenko1/pdf/Yakovenko.pdf), significant because many backpropagating and backpropagation-like models and economic markets solve surprisingly similar problems, that of credit assignment in a situation with hidden variables.

I don't really have too many possible explanations except possible [universality](https://terrytao.wordpress.com/2009/07/03/benfords-law-zipfs-law-and-the-pareto-distribution/). That universality is not really related to the statement that multilayer perceptrons can be [universal function approximators](https://en.wikipedia.org/wiki/Universal_approximation_theorem): it is a statement closer in spirit to Feigenbaum's discovery of [universality in chaos](https://en.wikipedia.org/wiki/Feigenbaum_constants).

I don't really have too many conclusions except that this makes me suspect that the space of possible gradients is radically smaller than is assumed by most folks, and that further optimizations on backpropagation and related algorithms may be possible based upon this fact. Convolution may be construed as one such operation, in that it is a coarse-graining like [block spin renormalization](https://en.wikipedia.org/wiki/Renormalization_group#Block_spin) (fractals are as closely related to power laws as ellipses in n-space are to Gaussians), but _there may be others_.

This is excerpted from the [other blog post](http://howonlee.github.io/2016/01/21/Poking%2520At%2520Causation1.html), because I highly suspect all the other claims in it may be a tad bullcrap, but this one is surprising and not very speculative.

Poke at me at hlee . howon at the big search engine's webmail if you have any questions, comments, etc.

RIP M. Minsky. I had the opportunity to meet Minsky only once, and he seemed like a very wise man.
