import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from player_reader import PlayerReader
from player_stats import PlayerStats

def create_players_table(players, nationality, season):
    """Luo ja palauttaa taulukon pelaajista."""
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

    return table

def get_user_input(console):
    """Kysyy käyttäjältä kauden ja kansallisuuden."""
    console.print("\n[bold cyan]NHL Statistics Viewer[/bold cyan]\n")
    season = Prompt.ask("Select season", default="2024-25")
    nationality = Prompt.ask("Select nationality", default="FIN").upper()
    return season, nationality

def fetch_and_display_players(console, url, nationality, season):
    """Hakee ja näyttää pelaajat."""
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    if not players:
        console.print(f"\n[yellow]No players found for nationality: {nationality}[/yellow]")
        return

    table = create_players_table(players, nationality, season)
    console.print(table)

def main():
    console = Console()
    season, nationality = get_user_input(console)
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    try:
        fetch_and_display_players(console, url, nationality, season)
    except requests.RequestException as error:
        console.print(f"\n[bold red]Error:[/bold red] {str(error)}")

if __name__ == "__main__":
    main()
