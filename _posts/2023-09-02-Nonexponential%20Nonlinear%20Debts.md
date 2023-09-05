---
layout: page
title: Why are there no nonexponential nonlinear loans?
---

The amount paid in interest in the often-taught, rarely-used simple interest regime is $P(1 + rt)$, where $P$ is principal, $r$ is the interest rate and $t$ is the time.

The main influence on the behavior of such functions is their functional form - the parameters can be futzed with and are obviously material in practice but don't fundamentally change the behavior in the typical interest domain (interest positive).

This situation of the functional form being the important thing is an omnipresent situation in computer science. Landau notation (big O notation), invented for number theory, is omnipresent in talking about the scaling of computers for that reason.

I see no reason not to foreground that notation in this case for interest-bearing debt if you take that foregrounding of functional form seriously.

Simple interest is therefore better seen as $O(t)$ debt.

The amount paid with the actually-used compound interest is $P(1 + \frac{r}{n})^{nt}$ with $n$ being the number of compounding periods. This is (in the limit) $O(e^{rt})$ debt, where $e$ is Euler's constant.

I have found without exception that simple interest is held as synonymous to noncompound interest. But there are more functional forms than "linear" and "exponential". There's all the polynomials, for one.

The two mentioned regimes of interest are the simplest ones to calculate because you don't need memory to calculate them. Simple interest is linear, so derivative is constant, and compound interest is exponential, and exponentials are the eigenfunctions of the derivative (take a derivative of an exponential and you just get a scaled exponential) so trivial amounts of computational memory is needed to calculate them in either case.

This was a material factor in ancient Sumeria when interest was invented and inscribed in clay tablets, the compounding reasoned about in terms of the growth of herds of cows.

It must, however, be noted that memory and computation for the 21st century modern is, conservatively speaking, cheaper by a factor of $10^{10}$ compared to the ancient Sumerians. Therefore I don't really think there are material computational obstacles to someone offering something that's $O(t ^ 2)$ or $O(t \log t)$ or what-have-you, at least in this millennium.

I don't have a banking license and I don't plan to get one so this is a recommendation that someone else go and do this. Obviously loan-making is incredibly regulated for great reasons, so get those no-action letters before you try this yourself.

The history of compound interest is filled with instances of exponents doing their thing and getting unmanageably big and causing chaos while doing so. But simple interest is a nonentity outside of pawnshops and consignment stores and other niche domains because it has a structurally terrible yield. So something $O(t^2)$ might be actually useful.
