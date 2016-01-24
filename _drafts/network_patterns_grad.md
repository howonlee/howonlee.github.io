Social Network Patterns in Neural Network (Multilayer Perceptron) Gradients
----

A very familiar set of patterns appears when one does a strange thing to a neural network gradient. Take a gradient for any SGD step, normalize it so that the top matrix member of that gradient is 1, and then sample it like the gradient was a distribution over matrices. Construe the resulting matrix as an adjacency matrix. You get something which looks very much like a social network.
