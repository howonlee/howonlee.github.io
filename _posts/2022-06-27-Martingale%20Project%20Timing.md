---
layout: page
title: Martingale Project Timing
---

[The previous introduction](https://howonlee.github.io/2022/03/29/A-20Software-20Estimation-20Method-20Where-20Every-20Task-20Is-20Estimated-20At-20Infinite-20Time.html) was pretty arcane, so this one should be a little less.

Suppose we start one day with one task, Bingling Zoobleybops. It's day 0.

Unlike in other methods of project timing, especially estimation, in Martingale timing we always rigidly set a next time of 1 day to look at it again.

One day passes. Day 1. We look at our progress in Bingling Zoobleybops.

Perhaps it's a trivial task after all and we're done with it: in which case, cross it off and we're done.

Perhaps it wasn't a trivial task, and we need more time. We do some kind of progress report, no matter how trivial, then we decide on whether or not to have more time.

These progress reports are going to have to be pretty trivial if we're starting a grand project and it's the 1 day mark. They don't really have to be that trivial if we're in the middle of a grand project and it's the 63 day mark.

When we need more time, we always have a rigid new amount of time where we'll look at Zoobleybops again. It's double the previous time. So 2 days from now, because we waited 1 day the previous time.

What prevents us from just doing tasks forever?

At each of these double-or-nothing decision points we always have the possible choice of deciding, consciously and soberly, that we're not going to do Zoobleybops, picking nothing. Then, we quit: we erase it from the task list.

We don't have to estimate the complexity or 'how long it's going to take' of Zoobleybops again, ever. We just keep on playing double-or-nothing, the martingale coin-flips.

Why is that a good thing?

The only time when you can estimate the complexity of a seriously complex task is when you've materially derisked it, so _estimates_ qua estimates, done at the beginning of the project, veer alarmingly between Panglossianism and bad-faith sandbagging.

But if you're doing it with double-or-nothing martingales, we always make the _fundamental_ decision of whether or not to do the task.

Sometimes estimates exist as a way to express power towards developers by management. You can still do that in the martingale way, just crisply make the decision to kill tasks.

Two more days pass. Day 3. OK, we still want to do Zoobleybops. Double the previous time, 4 days.

Four more days pass. Day 7. (You will want to count working days). Eight - day 15.

A conundrum presents itself.

You thought that Zoobleybops was a singular thing but in fact it's multiple coherent tasks which can be split up.

When we split tasks up, we always do it by halving, and it'll halve the double-or-nothing bet too.

So if you break Zoobleybops up into two, you go look at the two halved parts on day (15 + 8) = 23, instead of day (15 + 16) = 31.

Perhaps you will also halve the halved pieces in that case, and break the gigantic project into the usual greatly unequal pile of tasks, some of which are trivial and easily done and an unyielding core of really hard stuff. Perhaps one half on day (15 + 8) = 23, and four eights at day (15 + 2) = 17.

That's fine, that's ordinary - but you didn't do it by estimating, you actually recognized the hardness of hard stuff when you encountered the hardness, not from a vague foggy view of the future.

If you have a stable probability distribution over which you make the decision of double-or-nothing, the steady-state distribution of task lifetimes ends up being what's called a gamma distribution.

Which ends up not too far from empirical task lives in many issue trackers I've seen, anecdotally.

Many flips later, and now dealing with an entire ensemble of tasks, you get to day 255.

If you get to really high numbers, you also crisply get into why martingale systems don't actually work for betting: your bankroll quickly runs out.

This is an exponent, exponents are not fun to spend. But it's an honest exponent that now calls for you to kill the task underlying it - because it's not worth the cost anymore.

This system won't work for truly exogenous deadlines - GDPR and taxes where the government is setting it and won't yield, or planetary conjunctions for spacecraft where physics sets it and _really_ won't yield.

But this isn't the case for most software development - and in this case, martingale timing will allow you to avoid estimation at all.
