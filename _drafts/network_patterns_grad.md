Poking at Causation 1.3 / 3 : Social Network Patterns in Neural Network (Multilayer Perceptron) Gradients
----

All the code for this thing is on [github](https://github.com/howonlee/mlp_gradient_networks).

I wish to note a strange phenomenon which appears when one does a strange thing to a neural network gradient. I do not pretend to have a justification for doing this, except that it was fun.

Take a gradient for a SGD step on a "plain" multilayer perceptron,

#### pic

take the absolute value,

#### pic

normalize it so that the extremal matrix member of that gradient is 1,

#### pic

and then sample it as if the gradient was a distribution over matrices.

#### pic

Construe the resulting matrix as an adjacency matrix, so you get a network out of it. I will claim that this network looks like a social network. This is because it shows a series of network patterns common to social networks, among other complex networks.

### pic of the network

This network shows a [degree distribution](http://users.phys.psu.edu/~ralbert/phys597_09/c03_netw_prop.pdf) with high skew and kurtosis,

#### pic

It also shows a small [diameter](http://mathworld.wolfram.com/GraphDiameter.html), in this case ############################ and large [clustering coefficient](https://networkx.github.io/documentation/latest/reference/algorithms.clustering.html), in this case #################.

The phenomenon is durable to different datasets (the above was on an MNIST digit),

# show CIFAR degree distribution, diameter, cc

Different learning speeds,

# show 0.01, 1.0 degree distribution, diameter, cc

and different hidden layer sizes.

# show 100, 500, 4000 degree distribution, diameter, cc

So this induced network looks like a social network. Or any of the other complex networks out there, like linguistic networks or actual neural networks in C. Elegans. Or the degree distribution looks like the [distribution of money in a market](http://online.itp.ucsb.edu/online/colloq/yakovenko1/pdf/Yakovenko.pdf), significant because many backpropagating and backpropagation-like models and economic markets solve surprisingly similar problems, that of credit assignment in a situation with hidden variables.

I don't really have too many possible explanations except possible [universality](https://terrytao.wordpress.com/2009/07/03/benfords-law-zipfs-law-and-the-pareto-distribution/). That statement of universality is not related to the statement that multilayer perceptrons can be [universal function approximators](https://en.wikipedia.org/wiki/Universal_approximation_theorem): it is a statement closer in spirit to Feigenbaum's discovery of [universality in chaos](https://en.wikipedia.org/wiki/Feigenbaum_constants).

I don't really have too many conclusions except that this makes me suspect that the space of possible gradients is radically smaller than is assumed by most folks, and that further optimizations on backpropagation may be possible based upon this fact. Convolution may be one such operation, in that it is a coarse-graining like [block spin renormalization](https://en.wikipedia.org/wiki/Renormalization_group#Block_spin) (fractals : power laws :: ellipses in n-space : Gaussians), but there may be others.

This is excerpted from this [other blog post](http://howonlee.github.io/2016/01/21/Poking%2520At%2520Causation1.html), because I highly suspect all the other claims in it may be a tad bullcrap, but this one is surprising and not very speculative.

Poke at me at hlee . howon at the big search engine's webmail if you have any questions, comments, etc.
