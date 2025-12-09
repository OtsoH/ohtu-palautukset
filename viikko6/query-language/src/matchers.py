class QueryBuilder:
    def __init__(self, matcher=None):
        self._matcher = matcher if matcher else All()

    def plays_in(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def one_of(self, *queries):
        matchers = [query.build() for query in queries]
        return QueryBuilder(And(self._matcher, Or(*matchers)))

    def build(self):
        return self._matcher


class All:
    def test(self, player):
        return True


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value >= self._value


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        return all(matcher.test(player) for matcher in self._matchers)


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        return any(matcher.test(player) for matcher in self._matchers)
