---
layout: page
title: My Software Estimation Method, Where Every Task Is Estimated At Infinite Time
---

When I estimate software projects at work, I conform to the way we do it at work. But I can do software estimates the way I want to for my own projects, so I do them in this strange way. Despite the confounding premise, it is blisteringly simple.

Estimation
===

Set a minimum time for an issue. I usually use 1 day. Call that _t0_.

At the end of that time is a decision. I decide whether to do the task or to not do the task, given the time already taken.

If I don't do it, I don't do it.

If I will take more time and do it, I have _t\_(i + 1) = t\_i / (alpha - 1)_ more time until I make the decision again of whether to do the task or to not do the task. The expectation of how much more time I am going to take takes into account the amount of time I've already taken.

Usually that parameter _alpha_ is 2, in which case every decision time is a doubling: that is, I decide after 1 day, and then 2 more days after that, then 4 more days after that, and so on. Between 1 and 3 is a reasonable value for _alpha_.

So at every stage I am guessing, "is this going to take the increased time or not?". Really, I am answering the question, "is this worth the effort if it takes that increased time or not?", which gets to the heart of the actual question of software project estimation anyways. The question is now the same each time, and the answer must be crisply binary.

This is getting the expectation of the formal Pareto distribution, if you model my decision as to whether to do the thing or not as a Bernoulli variable with stable distribution, which it ends up being in practice: there are lots of other fat-tailled distributions which behave reasonably differently and can be gotten with other mechanisms, like the lognormal distribution or the gamma distributions.

Those are much less funny distributions, tho. Why? With certain values of alpha and certain probabilities of taking the increased amount of time, the probabilistic expectation - and in fact, any distributional moment you'd like - of time taken is infinite. Hence the title.

In effect you're taking the other side of [Bernoulli's Paradox of the St. Petersburg Game](https://en.wikipedia.org/wiki/St._Petersburg_paradox): all these decision points, all these coin flips are double or nothing and the expectation is infinite, but the resources expended increase exponentially while the whole universe of resources is quite finite, so it doesn't feel quite as awful as all that.

See also [Samuelson's discussion of Bernoulli's paradox](https://www.jstor.org/stable/2722712).

I often think to myself that power laws are an expression of Nature sitting in a probability distribution giving us humans an obscene gesture. Like, one of the really obscene ones. Perhaps you might think it less abominable, or the distributional ansatz of it being a power law wrong, but at least any serious software practitioner will agree with the mere statement that it is often a miracle that software gets made at all. Be glad of it. Enjoy the booping and beeping.

See also [this one](https://www.johndcook.com/blog/2015/12/21/power-law-projects/).

Arcane Justification
===

So the amount of time that tasks take in a software project has a radical inequality to it. You see the 4-hour tasks, you see the 2-month tasks. I am currently working on whacking a 7-year-old task that they were thinking about getting done 6 years ago, then 5 years ago, then someone asked about it 2 years ago and my coworker got folks to use a workaround 2 years ago. And coworkers repeatedly thought about it and wrote multiple design documents years ago and now I'm doing it. A basically funny but utterly mundane happening, in software.

My job is working on an open source thing, so it is actually easier to point out that direct example from that work project than a personal project. You can see me working on [issue #708 here](https://github.com/metabase/metabase/issues/708) now that we got to issue / PR number #20,000 a bit ago at Metabase, where I work, and it's going to get in when I'm done with it, almost surely before the next release.

Any method of estimation that doesn't conceive of this possible great delay as a thing that happens I do not really respect. It doesn't happen often but it happens. This statement has more to it than it seems: really, you cannot respect a system of estimation that puts a "typical scale" to things, you cannot respect a system of estimation that starts off with some addition of factors to form some underlying Gaussian, imagining issues like the above as monstrosities.

Why? They are not monstrosities if you see them on every significant software project. I've just never dealt with a software project above some trivial age that doesn't have some issue that's been lying around for an amount of time proportional to the entire lifetime of the project. It's not a special thing, either, that there are vast gaps in the lifetime of that issue where nobody ever thinks about the issue. That is also omnipresent.

Of course the [Fibonacci points system](https://www.lucidchart.com/blog/fibonacci-scale-for-agile-estimation) tries to get at this. It mostly fails because management doesn't let folks use the bigger point numbers or, oftentimes, the smaller point numbers. (Addition stalks the mind of the manager, even as multiplication leaves its tracks in the tickets.) Even though I do not do my personal projects in the presence of management, to make a durable system of estimation, you must make a system that makes that kind of meddling infeasible or at least impracticable. Also, often I end up having a sort of homunculus manager in my head even for personal projects, driving my own self towards thinking of tasks as having a characteristic scale.

Even the existing estimation models which partially do this, like the ancient COCOMO model, often dismiss the ultimate distributional uniformity of the 2-hour task and the 5-year task. I believe that they're as different as the fractal image with 2 iterations versus the fractal image with 10 iterations. Gigantic differences in scale and seeming complexity they may have, but it should be the same model for both.

There is even a pretty decent putative argument for why an underlying process for why software task times might ultimately be a fat-tailled distribution. Software is basically creating valid statements in a language with respect to a specification, in part enforced by the compiler or interpreter and in part fiddly or indistinct or only well-defined in retrospect. But this is merely dual to setting a great number of variables which satisfy a big gnarly satisfiability formula. Often the statement is made that if satisfiability was tractable (if P = NP) then the entire industry of software could just put up the chairs on the tables and turn off the lights as we go out and eat ice cream or something.

But satisfiability [is a condensed matter lattice](https://web.stanford.edu/~montanar/RESEARCH/book.html) in addition to being a computer-science NP-complete problem, despite not being matter, and they proved a second-order phase transition with criticality and abominably annoying phase structure to express certain kinds of _random_ satisfiability a long time ago. That's a second order phase transition, like ferromagnetism, not like water into ice. The phase transition is according to a measure of difficulty: very easy, it finishes quickly. Very hard, you recognize you can't solve it quickly. In the transition, everything gets doubtful.

You see a second-order phase transition, you expect the fractals and fat-tailled distribution to pop up in the transition like fungus in rotting wood. And there's a selection argument of software where it tends to get at that difficulty frontier because easier software-writing just gets folded into parts of other software projects as parts of them. You used to be able to sell HTTP servers for money to people who weren't utterly clueless, but now you can get one in one line in python or golang and there's apache or nginx if you need something for production: now you have to sell the SaaS contracts for money.
