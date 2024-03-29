"""Výpočet seznamu prvočísel až do zadaného limitu."""


# originální kód lze nalézt na adrese:
# http://www.rosettacode.org/wiki/Sieve_of_Eratosthenes#Using_array_lookup
def primes2_(limit):
    """Výpočet seznamu prvočísel až do zadaného limitu."""
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit ** 0.5 + 1.5)):  # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n * n, limit + 1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


# originální kód lze nalézt na adrese:
# http://www.rosettacode.org/wiki/Sieve_of_Eratosthenes#Odds-only_version_of_the_array_sieve_above
def primes2(limit):
    """Výpočet seznamu prvočísel až do zadaného limitu."""
    # okrajový případ
    if limit < 2:
        return []

    # druhý případ - 2 je speciálním prvočíslem
    if limit < 3:
        return [2]

    lmtbf = (limit - 3) // 2

    # naplnění tabulky, která se bude prosívat
    buf = [True] * (lmtbf + 1)

    # vlastní prosívání
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)

    # vytvoření seznamu prvočísel
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]
