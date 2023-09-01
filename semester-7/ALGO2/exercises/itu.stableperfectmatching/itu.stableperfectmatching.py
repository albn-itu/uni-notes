# I learned a lot and was highly inspired by looking at the python matching library: https://github.com/daffidwilde/matching

import sys


class Player:
    def __init__(self, name):
        self.name = name
        self.preferences = []
        self.match = None

    def forget(self, player):
        if player in self.preferences:
            self.preferences.remove(player)

    def other_preferences(self, after):
        index = self.preferences.index(after)
        return self.preferences[index + 1:]

    def __repr__(self):
        match_name = self.match.name if self.match is not None else None
        return f"({self.name}, {match_name})"


def read_input():
    [n, m] = [int(x) for x in sys.stdin.readline().split()]

    players = []
    player_map = {}

    def get_or_create_player(name):
        if name in player_map:
            return player_map[name]
        else:
            player = Player(name)
            player_map[name] = player
            return player

    for i in range(n):
        names = sys.stdin.readline().split()
        name = names[0]

        player = get_or_create_player(name)
        players.append(player)

        for j in range(1, len(names)):
            preference = get_or_create_player(names[j])
            player.preferences.append(preference)

    return players


def gale_shapley(players):
    free = players[:]  # Copy of players

    while free:
        current = free.pop(0)
        currents_favourite = current.preferences[0]

        favourites_match = currents_favourite.match
        if favourites_match is not None:
            currents_favourite.match = None
            free.append(favourites_match)

        currents_favourite.match = current

        for player in currents_favourite.other_preferences(current):
            player.forget(currents_favourite)
            currents_favourite.forget(player)

            if not player.preferences and player in free:
                free.remove(player)

    return players


def check_nonexistence(players):
    return any(p.preferences == [] for p in players)


def find_cycle(player):
    # Finds a cycle of least-preferable and second-choice players

    lasts = [player]
    seconds = []

    while True:
        players_second = player.preferences[1]
        seconds_last = players_second.preferences[-1]

        seconds.append(players_second)
        lasts.append(seconds_last)

        player = seconds_last

        if lasts.count(player) > 2:
            break

    player_index = lasts.index(player)
    cycle = list(zip(lasts[player_index + 1:], seconds[player_index:]))

    return cycle


def delete_cycle(cycle):
    pairs = set()
    for (i, (_, right)) in enumerate(cycle):
        left = cycle[(i - 1) % len(cycle)][0]
        other_preferences = right.other_preferences(left)
        for p in other_preferences:
            pairs.add((p, right))

    for (p, r) in pairs:
        p.forget(r)
        r.forget(p)


def get_next_player(players):
    try:
        return next(p for p in players if len(p.preferences) > 1)
    except StopIteration:
        return None


def second_phase(players):
    player = get_next_player(players)

    while True:
        cycle = find_cycle(player)
        delete_cycle(cycle)

        if check_nonexistence(players):
            break

        player = get_next_player(players)
        if player is None:
            break

    for player in players:
        player.match = None
        if player.preferences:
            player.match = player.preferences[0]

    return players


def print_out(players):
    # TODO: This can probably be done more efficiently
    out = set()
    for p in players:
        a = p.name
        b = p.match

        if a is None or b is None:
            print("-")
            sys.exit(0)

        b = b.name

        if a < b:
            out.add((a, b))
        else:
            out.add((b, a))

    for a, b in out:
        print(f"{a} {b}")


players = read_input()
players = gale_shapley(players)

if check_nonexistence(players):
    print("-")
    sys.exit(0)

if any(len(p.preferences) > 1 for p in players):
    players = second_phase(players)

print_out(players)
