---
layout: page
title: Proportionate-Growth Software Estimation
---

When I estimate software projects at work, I conform to the way we do it at work. But I can do software estimates the way I want to for my own projects, so I do them in this strange way. It is blisteringly simple.

Skip to the header about "Estimation" if you just want to hear about what I do instead of the thinking behind it.

Thinking
===

So the amount of time that tasks take in a software project has a radical inequality to it. You see the 4-hour tasks, you see the 2-month tasks. I am currently working on whacking a 7-year-old task that they were thinking about getting done 6 years ago, then 5 years ago, then someone asked about it 2 years ago and my coworker got folks to use a workaround 2 years ago.

My job is working on an open source thing, so it is actually easier to point out that direct example from that work project than a personal project. You can see me working on [issue #708 here](https://github.com/metabase/metabase/issues/708) now that we got to issue / PR number #20,000 a bit ago at Metabase, where I work, and it's going to get in when I'm done with it, almost surely before the next release.

Any way of estimation that doesn't conceive of this possible great delay as a thing that happens I do not really respect. It doesn't happen often but it happens. You cannot respect a system of estimation that puts a "typical scale" to things, you cannot respect a system of estimation that starts off with some addition of factors to form some underlying Gaussian, imagining issues like the above as monstrosities.

Why? They are not monstrosities if you see them on every significant software project. I've just never dealt with a software project above some trivial age that doesn't have some issue that's been lying around for an amount of time proportional to the entire lifetime of the project. It's not a special thing, either, that there are vast gaps in the lifetime of that issue where nobody ever thinks about the issue. That is also omnipresent.

Of course the Fibonacci points system tries to get at this. It mostly fails because management doesn't let folks use the bigger point numbers or, oftentimes, the smaller point numbers. (Addition stalks the mind of the manager, even as multiplication leaves its tracks in the snow.) Even though I do not do my personal projects in the presence of management, to make a durable system of estimation, you must make a system that makes that kind of meddling infeasible or at least impracticable.

Even the existing estimation models which partially do this, like the ancient COCOMO model, often dismiss the ultimate uniformity of the 2-hour task and the 5-year task. I believe that they're as different as the fractal image with 2 iterations versus the fractal image with 10 iterations. Gigantic differences in scale and seeming complexity they may have, but it should be the same model for both.

So what do you do in that sort of picture? One possible picture is proportionate growth, like Gibrat's law. The claim thus goes, "Tasks grow in multiplicative proportion in time taken without respect to their scale." The chance a 2-day task has to double in time is the same as the chance a 4-day task has to double in time. This makes a lognormal distribution of possible times. If you're one of those physics weirdoes, like Bak was, who's obsessed with power laws then there's shenanigans you can do to turn the resulting lognormal distribution into a power law (https://arxiv.org/pdf/cond-mat/0310061.pdf).

There is a pretty decent putative argument for why an underlying process for software task times might ultimately be a power law instead of just being a classic instance of physicists writing with large markers on log-log plots and seeing a power law where there isn't. Software is basically creating valid statements in a language with respect to a specification, sometimes fiddly or indistinct or only well-defined in retrospect: but this is merely dual to setting a great number of variables which satisfy a big gnarly satisfiability formula. But satisfiability is a condensed matter lattice in addition to being a computer-science NP-complete problem, and they proved a second-order phase transition with criticality and fiddly little phase transitions in it a long time ago. You see a second-order phase transition, you expect the power laws to pop up like fungus in rotting wood.

Estimation
===

Set a minimum time for an issue, I usually use 1 day. At the end of that time is a decision point as to whether to entirely not do the task or not. If you don't do it, you don't do it. If you decide to do it still despite spending that one day, then you set the next decision point at 2 * 1 = 2 days, and make that decision to give up on the issue or not again in that time. Then another decision point at 2 * 2 = 4 days, then 2 * 4 = 8 days, etc. If you use an issue tracker you should just stick it in the calendar this way.

You don't have to have an exponent or 2 or a minimum time of 1 day, but that's how I do it.

So at every stage you are guessing, "is this going to take twice the time or not?" (or, really, "is this worth the effort if it takes twice the time or not?", which gets to the heart of the actual question of software project estimation anyways) - and the question is the same each time, and the answers crisply binary.
