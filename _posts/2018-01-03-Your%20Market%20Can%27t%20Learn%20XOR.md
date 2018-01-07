---
layout: page
title: Your Market Can't Learn XOR
---

Summary: The mathematics we use for neural nets and the mathematics we use for simulation of markets is very often the same maths, but due to the feedback loop being hours in neural nets and years in markets and the many orders of magnitude more money in neural networks, the neural network mathematic and algorithms are much more advanced. The advancements in neural networks should be, therefore, be subject to wholesale adoption in simulated economies. The progression of the field in neural networks has gotten to the point where wide acceptance of shipping products is possible: perhaps the same could be true of simulated planned economies. An example of a possible low-hanging fruit is given.

I noticed one day that there was a surprisingly close mapping possible between Walrasian auctions and perceptrons.

A perceptron is a purported model of neural networks. Extremely complicated versions of them are among the forums for the best models of neurons which we have, not because they are particularly realistic, but because they have the remarkable ability to simulate a wide range of tasks previously purported to be solely the domain of humans. However, perceptrons are subject to a comparatively easy and comparatively straightforward reduction. We will mostly talk about linear perceptrons, a remarkably simple form.

At basis, a perceptron and the 'learning' algorithm that comes with it, is a way to choose from among a large ensemble of functions. The structural form of the function is held constant while the weights are mutated by a linear, convex or nonconvex optimization. Usually, the case is nonconvex and there is an optimization target for which is derived a gradient with respect to an error, and the parameters are adjusted to minimize the error. At the end of "training" or "learning" comes a function that has "learned" from a ataset of putative inputs and outputs: the function is a function of both its parameters and its inputs, the parameters only having been changed.

My contention is that many of the formal models of markets which have been developed and which can equilibriate (clear), most importantly the Walrasian model without production (or the Arrow-Debreu exchange economy), map remarkably well to this perceptronic formalism. Moreover, I contend that this has far-reaching consequences for those who wish to simulate and plan economies. In the Arrow-Debreu exchange economy model, every agent has an initial endowment of goods and a utility function over sets of goods. Goods are divisible and completely commoditized, and the market clears, or equilibrates, if each agent spends its entire budget with max utility and the goods are sold.

That is, a market and the purported method by which it equilibrates is a way to choose from among a large ensemble of functions, where each function represents a certain state of the market. The initial endowment of goods is remarkably analogous to the input section of a pattern in a perceptron (a datum presented to the perceptron). The utility of the money spent is a remarkably apt analogue to the output (the functional form of the utlity, the functional form of the functions which relate the parameter and input to the output), and a natural error signal is found in the gradient towards Pareto-optimality (the excess of the market). Prices, here, would then correspond to parameters in a perceptron.

Remarkably, there are even remarkably similar proofs which prove that the linear perceptron converges and the exchange economy equilibrates, which both in turn bolstered the theoretical importance of the models despite assuming quite unrealistic strong preconditions on the structure of the functions being learned. Both the proofs depend on their crux on the existence of a separating hyperplane that define a well-behaved inner product that the error gradient moves with respect to: in the case of the linear perceptron, there is assumed to be a separating hyperplane(s) between the classifications possible of the data, and for the exchange economy, there is an assumption that the goods in the economy satisfy weak gross substitutibility, a concept which directly leads to a separating hyperplane in the utility space. The methods which are presumed for optimization in those proofs are even remarkably similar: tantonnement and gradient descent, although one is in continuous time and one in discrete time.

So if you buy that this remarkable correspondence exists, what does that give you, why would that matter?

Unlike the Arrow-Debreu exchange economy, people actually use perceptrons and actually have practical experience with the whole perceptrons, although not the linear perceptrons that people actually have proofs for. People actually use these things for systems of credit assignment: Google Search, Facebook recommendations. In large part, this is because the empirical testing cycle of model neural networks is usually on the order of a few days, and the empirical testing cycle, if there is anything that could be called that, for simulated economies tends to be in the decades. People also saw the engineering and capitalistic opportunities in neural networks very soon after inventing them, but there are few corresponding opportunities for simulated economies. Therefore, despite being 80 years older than the theory of neural networks, the theory of simulated economies of this specific kind is comparatively much further behind, because there is no industrial practice.

If you like economic planning, then, and doing it in a non-awful way, that developed existing theory should be of interest to you. Especially of note is Lange, who suggested in 1936 that a planned economy should have inputs and outputs according to a linearly optimized Walrasian economic model. Kantorovich also suggested a similar plan for organization of the Soviet economy with linear programming methods. Note that both were quite stymied: Lange, by Friedman, who criticized it for having a state-backed economy, and Kantorovich, by the Soviet economic consensus of the time, for having a supposedly-bourgeoise price system.

Looking at the economic model thus, and seeing comparisons between the economic models and the perceptron, should give us some ripe low-hanging fruit. For example, XOR is the function where the inputs are two binary-valued variables and the output (also binary-valued, a single variable) is whether the sum of those two variables is 1 or not. It is not a linear function, and Marvin Minsky (the connectionist, not the economist) noted that it was a good proving ground for supposed neural models, because it had the property that the result requires cooperation between agents in the function that is learned. That is, the result cannot be divined by just looking at one input: both inputs need to be learned. But if the equilibration of the perceptron (or the exchange economy) requires linear separability, then the function cannot be learned. And so it cannot be, in practice as well as theory: a linear perceptron will oscillate in trying to learn it, or equilibriate on a wrong answer, depending on the dynamics of the gradient descent. The solution of the problem is decades old (add more layers) and should be able to imported wholesale into the planned economy domain. I could list off 15 more claims that would be of interest to the economic planner, all of them with remarkably durable, if sometimes ad hoc, solutions in neural network land.

A planned economic system existing with that system in mind would have some large advantages over other proposed economic systems. Despite being feasibly calculable, it is centralized and compatible with other basically centralized or basically decentralized, planned or unplanned economic systems. No permission would really be needed from other economic actors, as you could set one up with the agreement of 25-100 economic actors or so and grow it from there. It would be surprisingly hard to kill, in the same way that perceptrons, especially multilayered ones, are surprisingly hard to disrupt. The weak points, as in many other machine learning pursuits, lie in data collection and adversarial dynamics.

If there's demand for it, I will add a technical addendum with actual proofs and things. If not, either way, I will try to have a small prototype in a few months.

Objections
====

The Arrow-Debreu model is a simulation only and has never been used for planning real economies.
----

This has already been materially tried before with Beer et al's Cybersyn project.
----
There are many easy ways that one could argue against the claim that the Cybersyn project exercised their idea properly: they didn't have computers or a general suffusion of computation into society at nearly a requisite level of refinement, the CIA sabotaged them, et cetera, et cetera. But two less trivial points also come to mind. The Cybersyn project depended heavily on Bayesian filtering of summary statistics, a fundamentally-statistical approach of the kind which have had remarkable success in tasks closer to the linear regime but remarkable comparative failure in natural language processing, computer vision and other AI-adjacent tasks. The AI component of the Cybersyn project (the algedonic feedback system) had the essential problem common to many of the other good-old-fashioned AI in consisting of an ensemble of variables with various colorings which were claimed to have various properties and were interrelated in various ways, the numerics of which were almost entirely ignored. It is hard-won modern neural network knowledge that numerics are everything, the coloring of variables almost nothing.

If neural networks replace the capitalist class, won't we have a small important class anyhow?
----

Arriving at everyone's distributions assuming a utility function in closed form is easy. Getting the utility functions in the first place is difficult.
---

There is no such thing as a resting Walrasian equilibrium.
---
In nonlinear perceptrons, which without exception are the neural network models used in practical industrial efforts, there is no resting equilibrium either: the optimization settles at a "good-enough" equilibrium that nevertheless generalizes remarkably well and outperforms other families of models. The goal would be to accept metastable equilibria and get to an excellent if non-perfect point in price space.

How could this predict irrational human action? What about behavioral economics?
---

Existing shipped neural network products are imperfect.
---
This is true. However, the point is that they are better than everything else for the highly nonlinear AI-adjacent tasks that people use them for and, moreover, are improving at a much, much faster rate than the theory and practice of planned economies (at the same time where the practice runs far ahead of the theory).

Why don't people already use neural nets in markets?
---

Doesn't neoliberal capitalism already do this in being similar to the optimization models that it uses in operations research? Why wouldn't people coopt this in existing firms already?
---

Don't corporations already do AI things?
---

Aren't there adversarial perturbations?
---
There's adversarial perturbations in existing markets, plain as you can see. Do you really think 40 tulip bulbs in 1635 were really worth the labor of 500 skilled men for a year? Or at least, there are fundamentally awful numerical problems in existing markets.

More importantly, there is a viable theory of adversarial perturbations, and active research on attacking and eliminating them, whereas the many numerically unsophisticated attempts to prevent numerical derangements in markets have not borne great fruit.

Citations
===
