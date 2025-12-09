from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # Testi 1
    print("Pelaajat, joilla ei ole vähintään 2 maalia NYR:ssä:")
    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)

    print("\n" + "="*50 + "\n")

    # Testi 2
    print("Pelaajat, joilla on alle 2 maalia NYR:ssä:")
    matcher2 = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher2):
        print(player)

    print("\n" + "="*50 + "\n")

    # Testi 3
    print("Kaikkien pelaajien määrä:")
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    print("\n" + "="*50 + "\n")

    # Testi 4
    print("Pelaajat, joilla vähintään 45 maalia tai 70 syöttöä:")
    matcher3 = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    for player in stats.matches(matcher3):
        print(player)

    print("\n" + "="*50 + "\n")

    # Testi 5
    print("Pelaajat, joilla vähintään 70 pistettä ja pelaavat COL/FLA/BOS:")
    matcher4 = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("COL"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher4):
        print(player)

if __name__ == "__main__":
    main()
