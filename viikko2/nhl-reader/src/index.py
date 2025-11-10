from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

def main():
    console = Console()

    # Kysy kaudelta
    console.print("\n[bold cyan]NHL Statistics Viewer[/bold cyan]\n")
    season = Prompt.ask("Select season", default="2024-25")

    # Kysy kansallisuudelta
    nationality = Prompt.ask("Select nationality", default="FIN").upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    try:
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        if not players:
            console.print(f"\n[yellow]No players found for nationality: {nationality}[/yellow]")
            return

        # Luo taulukko
        table = Table(title=f"\n[bold]Top scorers from {nationality} season {season}[/bold]")

        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="yellow")
        table.add_column("Points", justify="right", style="bold red")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.points())
            )

        console.print(table)

    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {str(e)}")
if __name__ == "__main__":
    main()