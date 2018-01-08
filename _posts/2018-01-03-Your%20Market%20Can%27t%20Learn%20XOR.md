---
layout: page
title: Your Market Can't Learn XOR
---

Summary: The mathematics we use for neural nets and the mathematics we use for simulation of markets is very often the same maths, but due to the feedback loop being hours in neural nets and years in markets and the many orders of magnitude more money in neural networks, the neural network mathematics and algorithms are much more advanced. The advancements in neural networks should be, therefore, be subject to wholesale adoption in simulated economies. The progression of the field in neural networks has gotten to the point where wide acceptance of shipping products is possible: perhaps the same could be true of simulated planned economies. An example of a possible low-hanging fruit is given.

NB: I can be reached at hleehowon at the Google email service, if you want to harangue me

I noticed one day that there was a surprisingly close mapping possible between Walrasian auctions and perceptrons.

A perceptron is a purported model of neural networks. Extremely complicated versions of them are among the forums for the best models of neurons which we have, not because they are particularly realistic, but because they have the remarkable ability to simulate a wide range of tasks previously purported to be solely the domain of humans. However, perceptrons are subject to a comparatively easy and comparatively straightforward reduction. We will mostly talk about linear perceptrons, a remarkably simple form.

At basis, a perceptron and the 'learning' algorithm that comes with it, is a way to choose from among a large ensemble of functions. The structural form of the function is held constant while the weights are mutated by a linear, convex or nonconvex optimization. Usually, the case is nonconvex and there is an optimization target for which is derived a gradient with respect to an error, and the parameters are adjusted to minimize the error. At the end of "training" or "learning" comes a function that has "learned" from a dataset of putative inputs and outputs: the function is a function of both its parameters and its inputs, the parameters only having been changed.

My contention is that many of the formal models of markets which have been developed and which can equilibrate (clear), most importantly the Walrasian model without production (or the Arrow-Debreu exchange economy), map remarkably well to this perceptronic formalism. Moreover, I contend that this has far-reaching consequences for those who wish to simulate and plan economies. In the Arrow-Debreu exchange economy model, every agent has an initial endowment of goods and a utility function over sets of goods. Goods are divisible and completely commoditized, and the market clears, or equilibrates, if each agent spends its entire budget with max utility and the goods are sold.

That is, a market and the purported method by which it equilibrates is a way to choose from among a large ensemble of functions, where each function represents a certain state of the market. The initial endowment of goods is remarkably analogous to the input section of a pattern in a perceptron (a datum presented to the perceptron). The utility of the money spent is a remarkably apt analogue to the output (the functional form of the utility, the functional form of the functions which relate the parameter and input to the output), and a natural error signal is found in the gradient towards Pareto-optimality (the excess of the market). Prices, here, would then correspond to parameters in a perceptron.

Remarkably, there are even remarkably similar proofs which prove that the linear perceptron converges and the exchange economy equilibrates, which both in turn bolstered the theoretical importance of the models despite assuming quite unrealistic strong preconditions on the structure of the functions being learned. Both the proofs depend on their crux on the existence of a separating hyperplane that define a well-behaved inner product that the error gradient moves with respect to: in the case of the linear perceptron, there is assumed to be a separating hyperplane(s) between the classifications possible of the data, and for the exchange economy, there is an assumption that the goods in the economy satisfy weak gross substitutability, a concept which directly leads to a separating hyperplane in the utility space. The methods which are presumed for optimization in those proofs are even remarkably similar: tantonnement and gradient descent, although one is in continuous time and one in discrete time.

So if you buy that this remarkable correspondence exists, what does that give you, why would that matter?

Unlike the Arrow-Debreu exchange economy, people actually use perceptrons and actually have practical experience with the whole perceptrons, although not the linear perceptrons that people actually have proofs for. People actually use these things for systems of credit assignment: Google Search, Facebook recommendations. In large part, this is because the empirical testing cycle of model neural networks is usually on the order of a few days, and the empirical testing cycle, if there is anything that could be called that, for simulated economies tends to be in the decades. People also saw the engineering and capitalistic opportunities in neural networks very soon after inventing them, but there are few corresponding opportunities for simulated economies. Therefore, despite being 80 years older than the theory of neural networks, the theory of simulated economies of this specific kind is comparatively much further behind, because there is no industrial practice.

If you like economic planning, then, and doing it in a non-awful way, that developed existing theory should be of interest to you. Especially of note is Lange, who suggested in 1936 that a planned economy should have inputs and outputs according to a linearly optimized Walrasian economic model. Kantorovich also suggested a similar plan for organization of the Soviet economy with linear programming methods. Note that both were quite stymied: Lange, by Friedman, who criticized it for having a state-backed economy, and Kantorovich, by the Soviet economic consensus of the time, for having a supposedly-bourgeois price system.

Looking at the economic model thus, and seeing comparisons between the economic models and the perceptron, should give us some ripe low-hanging fruit. For example, XOR is the function where the inputs are two binary-valued variables and the output (also binary-valued, a single variable) is whether the sum of those two variables is 1 or not. It is not a linear function, and Marvin Minsky (the connectionist, not the economist) noted that it was a good proving ground for supposed neural models, because it had the property that the result requires cooperation between agents in the function that is learned. That is, the result cannot be divined by just looking at one input: both inputs need to be learned. But if the equilibration of the perceptron (or the exchange economy) requires linear separability, then the function cannot be learned. And so it cannot be, in practice as well as theory: a linear perceptron will oscillate in trying to learn it, or equilibrate on a wrong answer, depending on the dynamics of the gradient descent. The solution of the problem is decades old (add more layers) and should be able to imported wholesale into the planned economy domain. I could list off 15 more claims that would be of interest to the economic planner, all of them with remarkably durable, if sometimes ad hoc, solutions in neural network land.

A planned economic system existing with that system in mind would have some large advantages over other proposed economic systems. Despite being feasibly calculable, it is centralized and compatible with other basically centralized or basically decentralized, planned or unplanned economic systems. No permission would really be needed from other economic actors, as you could set one up with the agreement of 25-100 economic actors or so and grow it from there. It would be surprisingly hard to kill by attacking the members, in the same way that perceptrons, especially multilayered ones, are surprisingly hard to disrupt, but it would be vulnerable to attack in the actual apparatus hosting the network. The weak points, as in many other machine learning pursuits, lie in data collection and adversarial dynamics.

If there's demand for it, I will add a technical addendum with actual proofs and things. The like is true with citations. If not, either way, I will try to have a small prototype in half a year or two-thirds of a year or so.

Objections
====

The Arrow-Debreu model is a simulation only and has never been used for planning real economies.
----
Of course, the linear perceptron doesn't get used for many real machine learning tasks anymore, but people ship perceptrons anyhow, more complicated ones, convolution ones, recurrent ones. This refinement of modelling hasn't happened in the economic models and it seems to me this lack of refinement, rather than a general un-simulatability, which leads to the lack of viable practical real-world application of the models. So the argument is really if the models are of the same class and if the advances in neural models can be forwarded to the economic models, not if the current existing Arrow-Debreu models are fit for current usage.

Does this have anything to do with cryptocurrency?
----
No. These systems will have to be relatively centralized implemented inside of a condition of trust to work more than marginally (indeed, the parts of the crypto ecosystem that work more than marginally are the trusted ones).

This has already been materially tried before with Beer et al's Cybersyn project.
----
There are many easy ways that one could argue against the claim that the Cybersyn project exercised their idea properly: they didn't have computers or a general suffusion of computation into society at nearly a requisite level of refinement, the CIA replaced the leader backing it with a crazy person, et cetera, et cetera. But two less trivial points also come to mind. The Cybersyn project depended heavily on Bayesian filtering of summary statistics, a fundamentally-statistical approach of the kind which have had remarkable success in tasks closer to the linear regime but remarkable comparative failure in natural language processing, computer vision and other AI-adjacent tasks.

The AI component of the Cybersyn project (the algedonic feedback system) had the essential problem common to many of the other good-old-fashioned AI in consisting of an ensemble of variables with various colorings which were claimed to have various properties and were interrelated in various ways, the numerics of which were almost entirely ignored. It is hard-won modern neural network knowledge that numerics are everything, the coloring of variables almost nothing.

If neural networks replace the capitalist class, won't we have a small important class anyhow?
----
Yes. Some people will still have to determine hyperparameters, take care of the implementation, and so on.

The important fact, however, is that having an implementation which can be forked allows for the implosion of profit in the whole endeavor. The hope (it is a small hope, but nevertheless a hope), is some structure more akin to the open source movement, where people do it either as a very small and volunteer part of the course of normal employment or for the hell of it. Strong concentrations of power can be had in open source at the same time as completely negligible amounts of profit, because forks are possible. If there is a formal computational representation of the market, the market is also then forkable. So even if a class of people exist who take care of the market, the rents they can extract could become miniscule.

If one such network is used to represent a capital market, many more exotic things can be done with the capital distribution and other distributions given in the market. Of note is the fact that there is a comparatively-developed theory and practice of clamping certain weights of the network towards a value and not adjusting them, such as in the echo state network.

Arriving at everyone's distributions assuming a utility function in closed form is easy. Getting the utility functions in the first place is difficult.
---
If you walked up to an optimization professor today and said "linear optimization is a solved problem", they would agree with you. If you said, "nonlinear optimization is a solved problem", they would laugh you out of the building. Neural nets after 1980, because of the XOR example, are all nonlinear in less principled but much, much, much better working ways than the "weak" nonlinearities people use for economic models. That was the actual empirical goad that Marvin Minsky gave to the connectionist folks.

Now, the problem of lack of access and lack of data is much much more relevant to the essential neural network approach than one might imagine at first glance, because we have no real introspection into brains but we can get neural nets (and only neural nets, if you want them done comparatively well, although not to human level yet) to display the behavior that brains display. This is why I said that perceptrons (and multilayer perceptrons, and convolutional perceptrons, recurrent ones, recursive ones, etc etc) are not a good model for being realistic, they're a good model for displaying that behavior. One of the behaviors, the most important of the behaviors, is a starkly reduced data requirement. One example is the MNIST digits (classification of a bunch of pictures of numerals collected by the post office: trivial to a human, but involves solution of 2^784 space nonlinear optimization for the computer to get to human parity, which people did in 2002 or 2006 depending on how you look at it). Linear and gaussian mixture and that kind of model can actually get to human parity on them, if you allow like 2 to 3 orders of magnitude more data: but that, in turns, means that neural nets (nonlinear ones only) and only neural nets can save all that data complexity. We don't really understand why.

There is no such thing as a resting Walrasian equilibrium.
---
In nonlinear perceptrons, which without exception are the neural network models used in practical industrial efforts, there is no resting equilibrium either: the optimization settles at a "good-enough" equilibrium that nevertheless generalizes remarkably well and outperforms other families of models. The goal would be to accept metastable equilibria and get to an excellent if non-perfect point in price space.

Existing shipped neural network products are imperfect.
---
This is true. However, the point is that they are better than everything else for the highly nonlinear AI-adjacent tasks that people use them for and, moreover, are improving at a much, much faster rate than the theory and practice of planned economies (at the same time where the practice runs far ahead of the theory).

Why isn't this just the existing usage of neural networks in markets for trading?
---
A neural network algorithm in trading attempts to forecast the future in order to help a trade in a market which has all the appurtenances of a general market and, importantly, where the attempted clearing equilibrium is not calculated at all, but derived from the order book. If the neural network comprises the market, the market itself is cleared by the gradient descent algorithm.

Doesn't neoliberal capitalism already do this in being similar to the optimization models that it uses in operations research? Why wouldn't people coopt this in existing firms? Don't corporations already do AI things?
---
Of course, this is an instance of automation. However, the specific skill that this automation would de-skill and the specific people this would impact would be of the financial and management workers of the world. Notwithstanding alleged fiduciary duty, much of the activity of this group consists in enriching themselves by legal and usually ethical means. In nearly all firms, those two groups of people are the main decision makers. Why would they impoverish themselves as a class or as individuals for the alleged fiduciary duty they have towards others? So this is I suspect it wouldn't be used for operation of the firm.

Corporations who declare that they use sophisticated statistics for decisionmaking, as a rule, either have products which have in them sophisticated statistics or use statistics to rationalize decisionmaking, not to actually make the decisions. This is seen in the general statistical unsophistication of the actual decision makers at a firm. It's surprisingly rare to even find a CEO who can explain to you what, say, kurtosis is.

The same arguments hold forth for the apparatchiki of the allegedly socialist enterprises existing. If he really wants to, Brezhnev can indeed shut down a factory to get his own custom-made denim jacket buttons. They certainly wouldn't opt to destroy their own positions in society by adopting such a system.

Aren't there adversarial perturbations?
---
There's adversarial perturbations in existing markets, plain as you can see. Do you really think 40 tulip bulbs in 1635 were really worth the labor of 500 skilled men for a year? Or at least, there are fundamentally awful numerical problems in existing markets.

More importantly, there is a viable theory of adversarial perturbations, and active research on attacking and eliminating them, whereas the many numerically unsophisticated attempts to prevent numerical derangements in markets have not borne great fruit.

Of course, fraud will be a factor. I do not think the job of accountants and auditors will necessarily go away as quickly, although they may mostly implement fraud detection algorithms instead of make spreadsheets on Excel.

What matter of political orientation are you?
---
I am a pessimist.
