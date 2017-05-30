---
layout: page
title: Poking At Causation 2c / 3
---

Poking at Causation 2c / 3: Backpropagation for Literal Credit Assignment, in the Firm
--

There is much talk about the economic aspects of neural nets. There is also little talk about the economic aspects of neural nets. That is, this little section of artificial intelligence is often a philosophical object when talking about economics but scarcely ever a philosophical subject. What I mean by that is that we mostly think that AI in general will change the state of the economic world as we already envision it, but we do not expect it to change the vision itself. I believe that that will change. There will be significant contributions from the AI literature to economics. I do not have the hubris to claim that this is such a contribution. However, a thought came to me one day about backpropagation neural networks that I thought worth sharing.

People use neural networks to simulate the market and make trades based upon the simulation. They have done so for decades without thinking too hard about the reasons why neural networks simulate the market and other economic quantities so well. I will not think too hard about the market either, even though I believe that there are important claims to be made. This post exists to note something that is less noted but just as notable: that backpropagation could be a powerful attack on a class of problems dealing with the firm.

In 1991, Herbert Simon, who was the first and the greatest to define economics as one of the sciences of the artificial, told [this story](http://people.ds.cam.ac.uk/mb65/mst-ir/documents/simon-1991.pdf):

>A mythical visitor from Mars, not having been apprised of the centrality of markets and contracts, might find the new institutional economics rather astonishing. Suppose that it (the visitor I’ll avoid the question of its sex) approaches the Earth from space, equipped with a telescope that reveals social structures. The firms reveal themselves, say, as solid green areas with faint interior contours marking out divisions and departments. Market transactions show as red lines connecting firms, forming a network in the spaces between them. Within firms (and perhaps even between them) the approaching visitor also sees pale blue lines, the lines of authority connecting bosses with various levels of workers. As our visitor looked more carefully at the scene beneath, it might see one of the green masses divide, as a firm divested itself of one of its divisions. Or it might see one green object gobble up another. At this distance, the departing golden parachutes would probably not be visible.

>No matter whether our visitor approached the United States or the Soviet Union, urban China or the European Community, the greater part of the space below it would be within the green areas, for almost all of the inhabitants would be employees, hence inside the firm boundaries. Organizations would be the dominant feature of the landscape. A message sent back home, describing the scene, would speak of “large green areas interconnected by red lines.” It would not likely speak of “a network of red lines connecting green spots.”

So, to Simon, there exists this set of green blobs that lay hidden from the market economist's view, like the hidden layers that bedeviled Werbos and the other neural network folks before backpropagation. These green blobs are the central agents in the economy. At the edges of each of these vast things, salespeople and buyers interact, and that is the market. They are directly exposed at the surface areas, but the average HR person or in-house counsel or software developer or manager is inside the blob. They mostly interact with other people inside of the firm.

Backpropagation and the study of backpropagation might be of use in illuminating the innards of these green blobs. This is because they provide a fundamental attack on analogous problems with functions with many layers that do credit assignment. Literal credit assignment, in this case.

I assume familiarity with the usual usage of backpropagation, because there are so many introductions to backpropagation online. [Here](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/) is a solid simple one. As is usual with neural networks, you could stretch or break many of these stated assumptions and representations and keep on backpropagating successfully. Extensions are pretty obvious for the recurrent net, recursive net, weight sharing, and all sorts of other things.

Thought experiment with parts listing and batteries
===

A corporation is staffed by however so many people. They are organized according to a corporate hierarchy, Simon's pale blue lines. You are familiar with those, with the CEO on the top and so on. But there could also be a different hierarchical vision of what the corporation is. It could be a function that describes the world, or at least the credit-assigning parts of it, in terms of money. Like all functions that actually describe the world, it would describe the world poorly, but in a way that might be serviceable.

The input to the function should not be the cash flow in to the firm. This is because it is less easy to determine the cash flow in than the cash flow out, so the predicted cash flow in is the output of the function. One can tell a causal story: the firm is spending money in order to create this causal cascade so that the firm will earn money, so at the beginning of the chain of causation is the money the firm spends, and at the end of that chain of causation is the money the firm earns.

Doing it in this manner also will also have a benefit later on. You could follow the gradient all the way to the input units or the money spent. That is, you could adjust how much folks are paid. You could also of course add nonmonetary input and output targets and constraints, although we will not deal with those in this example.

![fig a](http://i.imgur.com/ji9N5ir.png)

One of the more important tasks for the firm is to decide on where the credit for changes in income is due. Does the credit lie in the executives' actions? If so, which executives? Lower ranked management, the rank and file? Who knows?

This question is actually pretty easy to answer in one specific place: the sales force. You know who is closing deals. You know who is not. So commission as remuneration for salespeople really often actually works. Not so for, say, executives or engineers or lawyers, where attempts at comparable schemes are all basically nonstarters. Even in the sales force, there are difficulties with the non-sales parts of the actual sales job. Many salespeople actively make life for other salespeople difficult. They fail to fill in paperwork. They fail to manage customer accounts. They grab all the good deal flow and leave nothing for everyone else. But for that one specific part of one specific job, credit assignment according to deal flow works and makes sense.

Usually, this assignment of credit and responsibility in the _hidden agents_ of the money flow, the parts of the flow that do not have a direct connection to the output of the function, goes through only an informal process. That process can be informally stated as, "Whatever good happens is because of us, if it does not strain creduility. Whatever bad happens is because of some other bastards, if it cannot be definitively pinned on us." But note that you cannot get away with this in the direct sales of the sales force. Sales managers can always know who closes the most deals or moves the most product.

From the machine learning person's point of view, this already describes a system of credit assignment. Unfortunately, it describes a bad and informal system. One done laboriously by intuition and gut feeling. One with plenty of room for classism, racism, sexism, megalomania, grudges, hidden incompetence, cronyism and other derangements. One that cannot learn hidden representations where there is no direct feedback from the output of the function. There is one decent formal algorithm that has been noted to work with some success at determining credit assignment for large and complex systems with hidden members: backpropagation. Why not just try backpropagation for this system?

It is a bit foolish to have talked so long without an example. The example firm has five people. You can see that two directly are in the front-office closing deals from four sources, and three are in support. Each person takes compensation, and there are also some other cash outflows. Suppose also that $600,000 is spent in order to earn $900,000 in this time period, split into the various accounts. For the representation in the net, divide figures by 100,000 for convenience.

![fig b](http://i.imgur.com/5olyPrv.png)

As we mentioned, _inputs_ of the model correspond closely to cash flow _out_. _Outputs_ of the model correspond in turn to cash flow _in_.

Agents correspond closely to individual units in the neural net. You could also have different nodes for groupings of agents. You could also have nodes for a subagentic representation, having a node for one aspect of A's job and another node for another aspect of A's job, or a superagentic representation, representing A, B, C at once for whatever reason.

There are relations of credit assignment between one agent in our imagined firm and another. You can see easily that these relations might correspond to edges in a network. You can also see that there is an inequality in most such relations of credit assignment. Therefore, you might imagine them to be weighted, directed edges.

You might initialize the weights with any arbitrary initialization, or you might hand-initialize them according to existing salaries, spending and judgment of who is responsible for what. There might be recurrences, which is not a problem either, as mentioned before. We actually even already make rudimentary determinations of the weight of credit that is ascribed to agents in firms, in paying people salary or setting their wages.

Then, forward propagation. I use leaky ReLU nonlinearities with alpha as 0.3, but the dynamical behavior is mostly the same without nonlinearities. Since we care about the identities of the agents and not much else, the model might still be useful in the linear regime, a la [Saxe, McClelland, Ganguli 2013](https://arxiv.org/abs/1312.6120). However, that means that this function could not represent anything more than linearly separable functions of the inputs. It would not be able to calculate XOR.

An easy loss function is squared error.

![fig c](http://i.imgur.com/MXq19PT.png)

You could then backpropagate, adjusting the initial credit assignment couplings. In fact, as I mentioned before, you could even backpropagate all the way into the input units, adjusting folks' pay and the spending on other inputs.

![fig d](http://i.imgur.com/rsK7oQY.png)

Such a process of backpropagating into the inputs would be somewhat like in the Inceptionism DeepDream networks, which usually hold the weights steady. You could also adjust the weights.

Neither adjustment is easy to do with only the sales data, given the hidden agents. If you did not have backpropagation, the thing to do would be to fold up the representation so that the sales force's salaries are the only input nodes, remove the hidden representation, and do something like a delta rule. That would make dealing with the non-salespeople, agents A, B, and C, impossible.

Amazing bullshit
===

To my knowledge, the use of backpropagation in this way for this subject has not yet been suggested. Although neural networks have been used before in statistical modelling for econonomic quantities, the representation they create in and of itself is usually not held to be of use or meaning. Their modelling capacity is usually never really quite explored, in the economics literature and also specifically the operations research literature where I expected to find such an exploration. There are also agent-based models, but I have not seen one that dealt with credit assignment. There are some good reviews of all those uses, though. [Here](http://www.smartquant.com/references/NeuralNetworks/neural7.pdf) is a solid one. There are some folks who you would expect to study this sort of thing who are called neuroeconomists. However, those folks tend to run actual fMRIs and do behavioral experiments instead of doing this sort of thing.

I do not expect anyone to actually go through with this. Doubtless in the real adversarial conditions of real credit assignment in real companies an actual implementation would be more difficult than this fairytale. But even a fairytale can yield dividends, if it admits of analogical thinking. Rather fortunately, the debug cycle on this fairytale is on the order of minutes to days, much unlike that of the firm.

There are many analogical low-hanging fruit in this case.

For example, long-term dynamical backpropagation and many-layer backpropagation is difficult, but the cause of the difficulty is not unknown. There is a well-defined, if not incredibly well-understood, set of conditions that futzes up the gradients and makes learning untractable for such networks. Is an analogous phenomenon true for organizations that try to have many layers of internal agents between money inflows and money outflows? Would some sort of analogous gating help, as it does in highway net, GRU and LSTM for backpropagation? If an apparatus was to be actually made, what would it look like? Would there be analogous apparatuses for other arcane tricks that neural network folks use, like stochastic depth and exotic nonlinearities?

Ill-conditioning of various quantities related to the gradient is an important consideration to the modern backpropagator, but to few theorists of the firm. There is a pretty easy analog in the ill-conditioning of quantities related to the changes in credit in the credit assignment process. That ill-conditioning can easily be seen as possible cause of or result of many optimizational derangements. In neural networks, the phenomenon motivates a host of optimization measures, from [momentum](http://dl.acm.org/citation.cfm?id=3043064) to [residual network structure](https://arxiv.org/abs/1611.01186). Is it everything to the many-layered economic organization? Certainly, the mere process of the optimization will militate for seeing the anisotropy of the agents, at least.

I will expand upon the contention that if you actually do this, you will live in adversarial conditions. The model will come under systematic and sustained attack at every level of the organization. The C-suite will attack it, the middle management will attack it, Joe in the mailroom will attack it, all as independent agents, all as a matter of course. As the agents who currently do credit assignment, the management will as a matter of course attack it with especial fervor.

But there is already a game theory on neural networks, and there have been efforts to create [new algorithms](https://arxiv.org/pdf/1511.04508.pdf) less vulnerable to adversarial perturbation and further efforts to [attack the new algorithms](https://pdfs.semanticscholar.org/df39/e24c3cc21dc4c79995ec2b424a37dac999c7.pdf) and show them vulnerable to different adversarial perturbations. The state of the art, which is a little further along than the linked papers, is not incredible and is not yet sufficient to the adversarial task. However, one might imagine that after a few rounds of this, some method durable towards many different and variegated kinds of adversarial perturbations might result. If you take care of the adversarial perturbation, you could probably start with bonus allotment as the initial task. The state of the art is also quite uncertain as to whether adversarial perturbation can ever be successfully defended against. There is also the adversarial reporting and production of data, for which people use Benford's law. There might have to be more cryptographic measures, against folks who are not naive to Benford's law, basically an additional adversarial scenario for which the literature is smaller.

You might relegate this whole little thought experiment to only being the contention that management, too, might be automated out of existence and sooner than one might think, another one of those breathless paeans to automation you see in the tech press. But it is uncontroversial that the managing class holds a special position in the actual practice of capitalism. They are currently the agent in the principal-agent problem that defines the firm as existing today, not the worker. And so the world that lives in adversarial conditions is also this world, and the result has been that both labor and capital have suffered fundamental attacks from management in recent decades. The damage to labor has been much greater, it is true. But it is also the case that we live in a world where you can have an IPO without any voting power in the stocks that you can buy in the IPO.

So if that principal-agent relation is better understood, then one might as well say that the firm is better understood. If the nature of the principal-agent relation is changed, then one might as well say that the nature of the firm is changed. If the anisotropy of performance is recognized and algorithmitized, then it might be possible to really pay for performance, rather than the current practice of paying for white male faces and Harvard MBAs. It might be possible to give proper credit to people outside of the scope of sales pay for performance, rather than injecting salesmanship into the technical side of things, which seems to happen at the tech majors that institute parallel tracks for management and technology.

As an aside with respect to the largest of organizations, it may also be that tax distributions and tax optimization look less like Laffer's curve and more like an awful spin glass in some intermediate phase where there is an exponential number of saddle curves, just like neural network optimization does. Difficult but not impossible to find a ground state. Great peril that the local optimum might not be the global one while at the same time there exists a large measure of those alright local optima.

One last point about connectionist attitudes towards cognition may be of interest. The representation of a task on a connectionist network is produced in the learned connections, not in the relation between preset variables. These learned connections emit patterns of activity at runtime, creating representations that are distributed. By virtue of their distributed nature, they are durable to random manipulation, vulnerable to adversarial attack, and able to spontaneously generalize to some extent. They have derangements borne out of the optimization process. It may be of use and of interest to also start from a like philosophical position with regards to the representations we hold for economic phenomena. We might eventually hold that the question of what a _firm_ is, is as complicated as the linguistic question of what a _word_ is, and there are already existing connectionist positions towards that.

I believe that if AI becomes a philosophical subject with respect to economics, this transformation of attitudes towards representation will be the method by which that will come to pass.

>To set prices, to measure values, to think up equivalencies, to exchange things - that preoccupied man's very first thinking to such a degree that in a certain sense it's what thinking itself is. Here the oldest form of astuteness was bred; here, too, we can assume are the first beginnings of man's pride, his feeling of pre-eminence in relation to other animals.

F. Nietzsche, _On the Genealogy of Morals_.

Thanks to RMO, OR, AZ, JB, JL for reading and comments.