# I learned a lot and was highly inspired by looking at the python matching library: https://github.com/daffidwilde/matching

import sys
from collections import defaultdict

preferences = defaultdict(list)
matches = defaultdict(lambda: None)


def other_preferences(partner, after):
    index = preferences[partner].index(after)
    return preferences[partner][index + 1:]


def forget(partner, other):
    if other in preferences[partner]:
        preferences[partner].remove(other)


def read_input():
    [n, _] = [int(x) for x in sys.stdin.readline().split()]
    partners = []

    for _ in range(n):
        names = sys.stdin.readline().split()
        preferences[names[0]] = names[1:]
        partners.append(names[0])

    return partners


def gale_shapley(partners):
    free = partners[:]  # Copy of partners

    while free:
        current = free.pop(0)
        currents_favourite = preferences[current][0]

        favourites_match = matches[currents_favourite]
        if favourites_match is not None:
            matches[currents_favourite] = None
            free.append(favourites_match)

        matches[currents_favourite] = current

        for partner in other_preferences(currents_favourite, current):
            forget(partner, currents_favourite)
            forget(currents_favourite, partner)

            if not preferences[partner] and partner in free:
                free.remove(partner)

    return partners


def check_nonexistence(partners):
    return any(preferences[p] == [] for p in partners)


def find_cycle(partner):
    # Finds a cycle of least-preferable and second-choice partners

    lasts = [partner]
    seconds = []

    while True:
        partners_second = preferences[partner][1]
        seconds_last = preferences[partners_second][-1]

        seconds.append(partners_second)
        lasts.append(seconds_last)

        partner = seconds_last

        if lasts.count(partner) > 2:
            break

    partner_index = lasts.index(partner)
    print(partner_index)
    print(lasts)
    print(seconds)
    print(list(zip(lasts[partner_index + 1:], seconds[partner_index:])))

    return list(zip(lasts[partner_index + 1:], seconds[partner_index:]))


def delete_cycle(cycle):
    pairs = set()
    for (i, (_, right)) in enumerate(cycle):
        left = cycle[(i - 1) % len(cycle)][0]
        op = other_preferences(right, left)
        print(i, left, right)
        for p in op:
            pairs.add((p, right))

    for (p, r) in pairs:
        forget(p, r)
        forget(r, p)


def get_next_partner(partners):
    try:
        return next(p for p in partners if len(preferences[p]) > 1)
    except StopIteration:
        return None


def second_phase(partners):
    partner = get_next_partner(partners)

    while True:
        cycle = find_cycle(partner)
        delete_cycle(cycle)

        if check_nonexistence(partners):
            break

        partner = get_next_partner(partners)
        if partner is None:
            break

    for partner in partners:
        matches[partner] = None
        if preferences[partner]:
            matches[partner] = preferences[partner][0]

    return partners


def print_out(partners):
    # TODO: This can probably be done more efficiently
    out = set()
    for a in partners:
        b = matches[a]

        if a is None or b is None:
            print("-")
            sys.exit(0)

        if a < b:
            out.add((a, b))
        else:
            out.add((b, a))

    for a, b in out:
        print(f"{a} {b}")


partners = read_input()
partners = gale_shapley(partners)

if check_nonexistence(partners):
    print("-")
    sys.exit(0)

if any(len(preferences[p]) > 1 for p in partners):
    partners = second_phase(partners)

print_out(partners)
