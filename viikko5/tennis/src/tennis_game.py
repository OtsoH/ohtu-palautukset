class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def _get_score_name(self, points):
        """Muuntaa pistemäärän tennisterminologiaksi"""
        score_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return score_names[points]

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._get_tied_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self._get_endgame_score()
        else:
            return self._get_regular_score()

    def _get_tied_score(self):
        """Palauttaa tuloksen kun pisteet ovat tasan"""
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def _get_endgame_score(self):
        """Palauttaa tuloksen advantage/win -tilanteessa"""
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_regular_score(self):
        """Palauttaa normaalin pisteilyn tuloksen"""
        player1_score_text = self._get_score_name(self.player1_score)
        player2_score_text = self._get_score_name(self.player2_score)
        return f"{player1_score_text}-{player2_score_text}"
