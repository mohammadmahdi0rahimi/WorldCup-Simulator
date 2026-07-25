# ================================================
# Daneshjoo: Mohammad Mahdi Rahimi Tabalvandani
# Shomare-ye daneshjooei: [Vared nashode]
# Onvan-e proje: Shabih-saz-e Jam-e Jahani
# Tarikh-e tahvil: 1405/05/01
# ================================================

"""Sazmandehi-e didarha va jadval-e yek daste.

In module shesh didar-e chahar tim ra misazad, ranking ra ba emtiyaz va gol moratab mikonad va do tim-e aval ra pas midahad."""

import random

from ClassMatch import Match


class Group:
    """Kar-e in bakhsh: Tim-ha, bazi-ha va jadval-e yek grooh ra sazmandehi mikonad."""

    def __init__(self, name, teams):
        """Kar-e in bakhsh: Yek daste-ye taze dorost mikonad.
        Daryafti-ha: name (str) va teams (list).
        Natije: Nadarad.
        """
        self.name = name
        self.teams = teams
        self.matches = []
        self.ranking = []

    def play_all_matches(self):
        """Kar-e in bakhsh: Shesh bazi-e momken-e grooh ra yek bar ejra mikonad.
        Daryafti-ha: Nadarad.
        Natije: Nadarad.
        """
        # Ravesh-e ejra: Natayej-e pishin-e grooh pish az ejra-ye taze khali mishavand.
        self.matches = []
        self.ranking = []

        # Ravesh-e ejra: Har team daghighan yek bar ba har tim-e digar bazi mikonad.
        for left_index in range(len(self.teams)):
            for right_index in range(left_index + 1, len(self.teams)):
                match = Match(
                    self.teams[left_index], self.teams[right_index], False
                )
                match.play()
                self.matches.append(match)

        # Ravesh-e ejra: Ghore-ye tasavi yek bar zakhire mishavad ta natije sabet bemanad.
        self.ranking = self._calculate_ranking()

    def _calculate_ranking(self):
        # Ravesh-e ejra: random.sample tartib-e avalie ra jahat-e ghore-ye tasavi taein mikonad.
        return sorted(
            random.sample(self.teams, len(self.teams)),
            key=lambda team: (
                team.points,
                team.goal_difference(),
                team.goals_for
            ),
            reverse=True
        )

    def get_ranking(self):
        """Kar-e in bakhsh: Jadval-e grooh ra tebghe chahar meyar pas midahad.
        Daryafti-ha: Nadarad.
        Natije: Tim-ha az rotbe-ye aval ta chaharom (list).
        """
        # Ravesh-e ejra: Ranking-e zakhire-shode az ghore-keshi-e dobare jologiri mikonad.
        if len(self.ranking) == 0:
            self.ranking = self._calculate_ranking()
        return self.ranking

    def advance_teams(self):
        """Kar-e in bakhsh: Do tim-e aval-e grooh ra entekhab mikonad.
        Daryafti-ha: Nadarad.
        Natije: Tim-e aval va dovom (tuple).
        """
        ranking = self.get_ranking()
        return ranking[0], ranking[1]

    def display_table(self):
        """Kar-e in bakhsh: Jadval-e nahaei-e grooh ra chap mikonad.
        Daryafti-ha: Nadarad.
        Natije: Nadarad.
        """
        print('\n===== Daste ' + self.name + ' =====')
        ranking = self.get_ranking()

        # Ravesh-e ejra: Har team ba rotbe, emtiyaz, tafazol va gol-e zade chap dade mishavad.
        for index in range(len(ranking)):
            team = ranking[index]
            goal_difference = team.goal_difference()
            if goal_difference >= 0:
                goal_balance_text = '+' + str(goal_difference)
            else:
                goal_balance_text = str(goal_difference)
            print(
                str(index + 1) + '. ' + team.name
                + ': Emtiyaz ' + str(team.points)
                + ', Tafazol ' + goal_balance_text
                + ', Gol-e zade ' + str(team.goals_for)
            )
