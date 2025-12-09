from statistics import Statistics
from player_reader import PlayerReader
from matchers import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    print("Kaikki pelaajat (määrä):")
    query = QueryBuilder()
    matcher = query.build()
    print(len(stats.matches(matcher)))

    print("\n" + "="*50 + "\n")

    # Testi 2
    print("NYR-pelaajat:")
    query = QueryBuilder()
    matcher = query.plays_in("NYR").build()

    for player in stats.matches(matcher):
        print(player)

    print("\n" + "="*50 + "\n")

    # Testi 3
    print("NYR-pelaajat, joilla 10-19 maalia:")
    query = QueryBuilder()

    matcher = (
        query
        .one_of(
            QueryBuilder().plays_in("PHI").has_at_least(10, "assists").has_fewer_than(10, "goals"),
            QueryBuilder().plays_in("EDM").has_at_least(50, "points")
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
