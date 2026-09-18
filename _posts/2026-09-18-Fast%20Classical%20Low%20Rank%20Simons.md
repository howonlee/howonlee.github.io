---
layout: page
title: Fast Classical Low-Rank Simon's
---

_Butlerian Notice:_ The code and its comments was done by LLM, I had the ideas, verified the LLM output and wrote the actual words here myself.

[Simon's problem](https://en.wikipedia.org/wiki/Simon%27s_problem) is a basically-useless problem introduced by D. R. Simon to prove that there is an oracle separation between BQP and BPP. There is a sort of sleight of hand in that there is then the implicature that the problems we care about in BQP, namely factoring, discrete logarithm, HHL and messing with Hamiltonians, are putatively in the given BQP \ BPP.

However, it is an _oracle_ separation: the function that we're doing the Simon's algorithm of must be a black box. Black boxes exist only with respect to our knowledge, not with respect to reality, which always have as much detail as it has.

Given is an implementation of a fast (polylog time) classical solution to Simon's problem with respect to Simon's problems posed for functions given that their actual implementations are given and representable in low tensor (CP) rank. The main thrust of it is to just keep the tensor factorization as you go along, and have the Hadamard operator factorized also as you go along.

[https://github.com/howonlee/simons](https://github.com/howonlee/simons)
