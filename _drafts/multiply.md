Fast Multiplication in Residue Number System
---

Residue number system is the number system where every integer is represented by its value modulo coprime integers called the moduli. WLOG we can just think in terms the primorials (products of the first N primes), so each modulo in there is the first N prime numbers.

If you think of the damn representation in a seemingly-highly-inefficient way, a series of data science-style one-hot vectors (where the moduli are implicitly determined by vector lengths), you can multiply fast. Damn fast.
