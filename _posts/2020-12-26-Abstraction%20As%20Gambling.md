---
layout: page
title: Program Abstraction as Gambling
---

<sub><sup>Note: I hope I don't insult any gambling folks by the comparison or offend anyone with real gambling problems. Those are of course much more serious.</sup></sub>

Abstraction exists, even if folks don't always agree about what it is. It is a stable term, if not a stable thing, which can be talked about.

Abstraction also has benefits. Lots of people disagree on the nature and the distribution of the benefits, but most folks agree it has benefits.

However, a depressing commonality to folks who embrace abstraction too much is that they deal with the benefits themselves in an abstract manner. They don't say explicitly that the new domain vocabulary will make things clearer to newcomers, or that the new adoption of \_\_\_-style programming will speed up development.

I tend to believe that this is a mistake. Instances of abstraction have brutally concrete benefits, and sometimes they lack those benefits in an equally brutally concrete way. Your new domain vocabulary might be worse at everything it does and confuse everyone, or your new adoption of \_\_\_ programming might slow everyone down.

Even if the benefits and detriments seem deterministic, they have the determinism of the logistic function: a brutal deterministic chaos that makes prediction a hopeless muddle. Like the determinism of the physical laws of nature being obeyed in the dealer's shuffle of the deck, or the determinism of the physical laws obeyed in the bounce and jiggle of the roulette wheel. 

That lived uncertainty has a rawness to it which led me to the titular comparison.

If you think of the act of abstraction as gambling, moreover, it properly seems more dangerous. It often comes to pass with many of the folks who deal with the benefits of abstraction in an abstract manner that they can ignore the concrete losses for too long.

This situation is often like that of a slot machine addict or gacha addict, or some desperate gambler at the stock markets, pulling levers or clicking buttons to fulfill the promise for concrete gains while only achieving concrete losses. They pull the lever of abstraction and beggar themselves in doing so.

I'd like to say that abstraction addiction does less economic damage, but I don't actually know that, especially with salaries nowadays being so high.

The benefits of abstraction do not and never will include the destruction of all uncertainty, and they definitely never will include the destruction of uncertainty about the benefits of the abstraction itself.

So in that domain we are all gamblers, and we might as well think of some rules to benefit ourselves. We all know an addict to abstraction.

### List out the odds and payoffs, even if they're estimates. Actual numbers, on actual paper or excel or something.

They made it illegal to have casino games without these for a great reason. If you are creating an abstraction - what are you trying to gain from this? Developer time? Maintainability (developer time, but much later)? Developer understandability?

Your poker game is also uncertain, but the uncertainties are perfectly measured - but most folks making abstractions will not even try to list the odds of outcomes, or to try to do a full enumeration.

The abstraction wouldn't have occurred to you if you thought that there weren't good odds of this benefit. But it helps still to write down at least the subjective opinion you have of those odds and the payoffs, to face them if you are wrong and so others can look and think about them.

The problem of not having concrete odds and payoffs is usually not as big a problem with large refactorings and big changes in the way folks do things. But you can still go bankrupt from penny slots. You should list the odds for small putative abstractions too, because there's a lot more of those.

### Don't play a martingale, and don't chase losses

A martingale is an 18th-century betting system that consists of increasing the bet after any loss in order to make up for it in any subsequent wins. In order for the trick to work, you need infinite wealth, because there is some point (and a quick point, because the bets must exponentially increase) where one runs out of money.

The way bad abstractions make a project's time balloon, I wouldn't be surprised if it had some exponential structure to it. And nobody has infinite time.

If you continuously double down on an abstraction even if you keep losing by it, it will turn bad in this way. If you don't go into the making of an abstraction without being honest to you that you might lose and not gain whatever benefit to be had, you have precluded the opportunity for winning from that abstraction.

The underlying proof for why martingales don't work is based upon the non-correlational nature of gambling, which is where this metaphor breaks down a little here. Streaks can occur, and do occur, in abstractions - but your time resolutely remains finite, and bad abstractions will remain resolutely bad.

> The odds of the above helping you are pretty remarkably high, I'd put it at over 90%, depending upon the adjustments you wish to make for the correlational structure of making abstractions in your domain. If you follow it, you can theoretically avoid infinite losses - but these in practice are merely fairly large losses before it becomes obvious to everyone that something is terrible.

### Wins can be as treacherous as losses

It seems to me that someone whose first night at a casino entailed a \$1000 loss is a fair shot less likely to start ignoring their losses than someone whose first night at a casino is suffused with some aura of magic because they won \$1000.

A surprisingly common case of abstraction works that way - the early win which is not consolidated and the benefits taken out and abused until the magic falls apart from overapplication.

> I would say the main payoff of the above is trying to avoid the state of being addicted to abstraction - that is the abstraction itself becoming an end, just like how gambling becomes an end to itself. The actual change of the way one goes about abstracting I consider more of a fringe benefit. The odds I would not say are incredible, but they're not zero, call it 40%.
