Social Network Patterns in Neural Network (Multilayer Perceptron) Gradients
----

I wish to note a strange phenomenon which appears when one does a strange thing to a neural network gradient. I do not pretend to have a justification for doing this, except that it was fun.

Take a gradient for a SGD step on a "plain" multilayer perceptron,

#### pic

take the absolute value,

#### pic

normalize it so that the extremal matrix member of that gradient is 1,

#### pic

and then sample it as if the gradient was a distribution over matrices.

#### pic

Construe the resulting matrix as an adjacency matrix, so you get a network out of it.

### pic of the network

You get from this process a network which looks very much like a social network, meaning that it shows a series of network patterns common to social networks among other complex networks, including the [degree distribution](http://users.phys.psu.edu/~ralbert/phys597_09/c03_netw_prop.pdf),

#### pic

[diameter](http://mathworld.wolfram.com/GraphDiameter.html) and [clustering coefficient](https://networkx.github.io/documentation/latest/reference/algorithms.clustering.html). The phenomenon is durable to different datasets.

### try MNIST and CIFAR

### different learning speeds: try 0.01, 0.1, 1

### different hidden layer sizes: try 100, 500, 1000

I don't really have too many possible explanations except possible [universality](https://terrytao.wordpress.com/2009/07/03/benfords-law-zipfs-law-and-the-pareto-distribution/). I don't really have too many conclusions except that I suspect that the space of possible gradients is radically smaller than is assumed by most folks, and that optimizations may be possible based upon this fact.

This is excerpted from this [other blog post](http://howonlee.github.io/2016/01/21/Poking%2520At%2520Causation1.html), because I highly suspect all the other claims in it may be a tad bullcrap, but this one is actually empirical.
