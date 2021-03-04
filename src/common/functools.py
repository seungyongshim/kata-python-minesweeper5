from itertools import chain


def flat_map(f, xs):
    return map(f, chain.from_iterable(xs))