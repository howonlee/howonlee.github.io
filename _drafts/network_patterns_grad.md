Social Network Patterns in Neural Network (Multilayer Perceptron) Gradients
----

I wish to note a strange phenomenon which appears when one does a strange thing to a neural network gradient.

Take a gradient for a SGD step on a "plain" multilayer perceptron,

take the absolute value,

normalize it so that the extremal matrix member of that gradient is 1,

and then sample it as if the gradient was a distribution over matrices.

Construe the resulting matrix as an adjacency matrix.

I do not pretend to have a justification for too much of this. But you get from this process a network which looks very much like a social network, meaning that it shows a series of network patterns common to social networks among other complex networks. The phenomenon is durable to different datasets,

### different learning speeds?
### different hidden layer sizes
### other stuff
