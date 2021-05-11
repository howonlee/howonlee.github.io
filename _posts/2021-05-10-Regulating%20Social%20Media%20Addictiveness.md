---
layout: page
title: Regulating Social Media Addictiveness
---
There's a lot of other terrible things about social media, but a specific material terrible thing that might be the subject of regulation is how addictive it is.

You don't get to [the usage per day that social media platforms have](https://www.statista.com/forecasts/1088803/time-spent-on-social-networks-per-day-in-the-us) without at least a little addictiveness. It's addictive! We regulate liquor and cocaine and casinos, why not regulate the addictive structure of social media?

I suggest an objective and direct avenue of regulation: make the services increase latency in server responses, by setting a minimum latency to UI loading animations (including initial page loads, infinite scroll loads, page swipes, skeletons and bouncy balls, etc).

1. [Lowering latency is proven to increase usage, increasing latency is proven to decrease usage.](https://www.thinkwithgoogle.com/marketing-strategies/app-and-mobile/mobile-page-speed-new-industry-benchmarks/) So it's already known to work.
2. It's not censorship if you just slow down every response.
3. Everyone agrees on what a UI loading animation is. It gets non-application multi-page websites, SPA-backed things, mobile apps, and so on.
4. It's like a two line implementation with respect to technical difficulty to implement, if they use any sane animation library.
5. It can be applied to any social media provider without reference to the structural form of the provider, as long as they're on the Internet, because everyone agrees what a loading animation is.
6. It can be verified objectively with a timer and it can also be verified objectively by a third party. So you can't do the Volkswagen bamboozling of the regulators because it's much less annoying to do independent testing of UI transition latency than of car emissions.
7. It's not hard to do definitional wriggling about non-abusive or abusive content: it's surprisingly difficult to do definitional wriggling to get out of being defined as social media itself.
8. I think the most viable definitional wriggling is to pretend that things are multiplayer video games with low-latency requirements. But there are already existing pretty viable regulatory attacks on MMORPG addiction pioneered by East Asian countries.
9. One hangup is differences between media forms of the services. There's probably a material difference between video content and other content because video content is comparatively longer-running. But that difference can also be articulated pretty well and maybe you would have longer latencies for video content.
10. Such a policy would be adjustable depending on how much less addictive potential folks want.

I recommend about 2.0 second minimum latencies, which seem to be noticeable and effective at reducing browsing to about 50 minutes a day in my case.

You could note that HTTP responses are even better defined, but you could do wibbly things with transitions to get around this. You could also do a mandated pre-load black screen with scary messages on it, like cigarette cartons, but this is harder to deal with infinite scrolls and other dark UI patterns.

I know I posted [a dealio](https://howonlee.github.io/2020/02/12/I-20Add-2020-20Seconds-20of-20Latency-20to-20Every-20Website-20I-20Visit.html) a bit back about how I do this personally for myself but after a few years of this I believe that there are surprisingly few material obstacles to just turning it into policy.
