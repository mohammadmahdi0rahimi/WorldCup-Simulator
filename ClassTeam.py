# ================================================
# Daneshjoo: Mohammad Mahdi Rahimi Tabalvandani
# Shomare-ye daneshjooei: [Vared nashode]
# Onvan-e proje: Shabih-saz-e Jam-e Jahani
# Tarikh-e tahvil: 1405/05/01
# ================================================

"""Sazmandehi-e moshakhasat va raftar-e har tim-e melli.

Class-e Team dadehaye sabet, amar-e jam, lambda-ye gol, vaght-e ezafe va penalty ra zakhire mikonad va natije-ye kham-e didar ra pas midahad."""

import random

from Poisson import poisson_simple


class Team:
    """Kar-e in bakhsh: Ettelaat va amar-e yek tim-e melli-e football ra zakhire mikonad."""

    def __init__(self, name, attack, defense, rank):
        """Kar-e in bakhsh: Yek team ba amar-e avalie-ye sefr dorost mikonad.
        Daryafti-ha: name, attack, defense va rank-e team.
        Natije: Nadarad.
        """
        # Ravesh-e ejra: Moshakhasat-e sabet-e team az file-e CSV daryaft mishavand.
        self.name = name
        self.attack = attack
        self.defense = defense
        self.rank = rank

        # Ravesh-e ejra: Amar-e motaghayer dar ebteda sefr ast.
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0
        self.group = ''
        self.last_penalty_score = None

    def goal_difference(self):
        """Kar-e in bakhsh: Tafazol-e gol-e team ra mohasebe mikonad.
        Daryafti-ha: Nadarad.
        Natije: Gol-e zade menhaye gol-e khorde (int).
        """
        return self.goals_for - self.goals_against

    def reset_stats(self):
        """Kar-e in bakhsh: Amar-e team ra jahat-e shabih-sazi-e badi sefr mikonad.
        Daryafti-ha: Nadarad.
        Natije: Nadarad.
        """
        # Ravesh-e ejra: Moshakhasat-e sabet taghir nemikonand; tanha amar-e jam reset mishavad.
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0
        self.last_penalty_score = None

    def _calculate_goal_lambda(self, opponent):
        # Ravesh-e ejra: Ghodrat-e hamle-ye team va defa-e harif lambda ra misazand.
        attack_part = (self.attack / 100) * 1.5
        defense_part = (1 - opponent.defense / 100) * 0.8
        return attack_part + defense_part

    def _penalty_probability(self, opponent):
        # Ravesh-e ejra: Ehtemal-e penalty tebghe formule file-e proje mohasebe mishavad.
        success_chance = 0.75 + (self.attack - opponent.defense) / 250

        # Ravesh-e ejra: Ehtemal bayad hatman dar bazeye 0.6 ta 0.9 bemanad.
        if success_chance < 0.6:
            success_chance = 0.6
        elif success_chance > 0.9:
            success_chance = 0.9

        return success_chance

    def _simulate_penalty_shootout(self, opponent):
        self_probability = self._penalty_probability(opponent)
        opponent_probability = opponent._penalty_probability(self)
        self_penalties = 0
        opponent_penalties = 0

        # Ravesh-e ejra: Har team panj zarbeye avalie ra mizand.
        for kick_number in range(5):
            if random.random() < self_probability:
                self_penalties += 1
            if random.random() < opponent_probability:
                opponent_penalties += 1

        # Ravesh-e ejra: Dar har dor-e nagahani, har do team yek zarbeye kamel mizanand.
        while self_penalties == opponent_penalties:
            if random.random() < self_probability:
                self_penalties += 1
            if random.random() < opponent_probability:
                opponent_penalties += 1

        return self_penalties, opponent_penalties

    def simulate_match(self, opponent, is_knockout=False):
        """Kar-e in bakhsh: Natije-ye bazi ba harif ra shabih-sazi mikonad.
        Daryafti-ha: opponent (Team) va is_knockout (bool).
        Natije: Gol-e do team va tim-e barande ya None (tuple).
        """
        # Ravesh-e ejra: Lambda va gol-haye 90 daghighe jahat-e har do team mohasebe mishavand.
        home_lambda = self._calculate_goal_lambda(opponent)
        away_lambda = opponent._calculate_goal_lambda(self)
        home_goals = poisson_simple(home_lambda)
        away_goals = poisson_simple(away_lambda)
        self.last_penalty_score = None

        # Ravesh-e ejra: Vaght-e ezafe tanha jahat-e tasavi-e marhale-ye hazfi ast.
        if is_knockout and home_goals == away_goals:
            home_goals += poisson_simple(home_lambda * 0.33)
            away_goals += poisson_simple(away_lambda * 0.33)

        # Ravesh-e ejra: Barande az gol-ha ya dar nahayat az penalty taein mishavad.
        if home_goals > away_goals:
            winner = self
        elif away_goals > home_goals:
            winner = opponent
        elif is_knockout:
            self.last_penalty_score = self._simulate_penalty_shootout(opponent)
            if self.last_penalty_score[0] > self.last_penalty_score[1]:
                winner = self
            else:
                winner = opponent
        else:
            winner = None

        return home_goals, away_goals, winner
