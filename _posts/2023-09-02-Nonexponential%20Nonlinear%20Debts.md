---
layout: page
title: Why are there no nonexponential nonlinear debts?
---

The amount paid in simple interest is $P(1 + rt)$, where $P$ is principal, r is the interest rate and t is the time.

The main influence on the behavior of such functions is the functional form of them - the parameters can be futzed but don't fundamentally change the behavior in the typical interest domain (interest positive). This is an omnipresent situation in computer science and therefore Landau notation, invented for number theory, is omnipresent in that domain. Simple interest is therefore better seen as $O(t)$ debt ($\theta(t)$ debt).

Compound interest is $P(1 + \frac{r}{n})^{nt}$ with $n$ being the number of compounding periods. This is (in the limit) therefore $\theta((1 + r)^t)$ debt.

These two regimes of interest are the simplest ones to calculate because you don't need state to calculate them: simple interest is linear and compound interest is exponential, and exponentials are the eigenfunctions of the derivative so no computational state is needed to calculate them.

This was a material factor in ancient Sumeria when interest was invented but it must be noted that computation for the 21st century modern is, conservatively speaking, cheaper by a factor of $10^{10}$ compared to the ancient Sumerians.

Therefore I don't really think there are material computational obstacles to someone offering something $\theta(t ^ 2)$ or something. I don't have a banking license and I don't plan to get one so I recommend someone else go and do that.
