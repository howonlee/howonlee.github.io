---
layout: page
title: Heap Search is NP-Complete
---

I found the other day that the problem of searching for a value in the leaf nodes of binary heaps is NP-complete. I looked for a fair amount of time for any previous publication of this in the literature and couldn't find one, so I thought maybe it was worth sharing (I may be mistaken, of course). Here is the reduction, from subset sum.

Construe subset sum as the decision problem of whether a multiset of positive integers may sum to a query `Q`.

We will construct a min-heap from this problem. The construction goes like so.

- The initial heap is a single node, which corresponds to the intermediate sum of 0. This corresponds to the 0th layer of the heap.
- For every member of the multiset, create another layer of the heap.
  - Every node of the previous layer will have two children in this new layer.
  - The left child corresponds to not adding the member of the multiset and should have the intermediate sum of the parent.
  - The right child corresponds to adding the member of the multiset and should have the intemediate sum of the parent + the value of the member.

Note that the value of the left child is always lesser than that of the right child, by construction. Also this data structure remains at each layer a min-heap by construction, because each member of the multiset is a positive integer.

The bottom layer of the heap contains `O(2^N)` nodes, where `N` is the number of layers in the heap, or alternately the number of members of the multiset.

The problem of subset sum reduces to searching for `Q` in the leaf nodes of the heap, because each member of the bottom layer corresponds to a possible partition, with the value of the sum of that partition, and they enumerate the possible partitions.

This is because every left child corresponds to a decision not to include a member in the possible partition, every right child corresponds to a decision to include that member.

Therefore, an algorithm that solves searching in a heap also solves subset sum. To prove for max-heaps, repeat the construction but subtract from the whole sum of the multiset instead of adding.

If the heap were a binary search tree, we would have it trivially in polytime, because we would be able to bisect the tree without actually instantiating it and search the tree in `O(N)` steps. This happens when the set is superincreasing, remarkably enough, so that's a very interesting way to view the easy portion and hard portion of the knapsack cryptosystem. This seems to be pretty separate from the concern of the critical phase transition.
