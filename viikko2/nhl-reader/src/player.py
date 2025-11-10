class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.team = player_dict['team']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} team {self.team:3}  goals {self.goals:2} assists {self.assists:2}"
