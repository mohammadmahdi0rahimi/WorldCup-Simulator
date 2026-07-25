# ================================================
# Daneshjoo: Mohammad Mahdi Rahimi Tabalvandani
# Shomare-ye daneshjooei: [Vared nashode]
# Onvan-e proje: Shabih-saz-e Jam-e Jahani
# Tarikh-e tahvil: 1405/05/01
# ================================================

"""Ejra va sabt-e yek didar-e football.

Class-e Match do tim ra daryaft mikonad, gol va emtiyaz ra be-rooz mikonad va matn-e yekdast-e natije, penalty va barande ra amade mikonad."""

from ClassTeam import Team


class Match:
    """Kar-e in bakhsh: Yek didar va khorooji-e an ra sazmandehi mikonad."""

    def __init__(self, team1, team2, is_knockout=False):
        """Kar-e in bakhsh: Yek didar bein-e do team dorost mikonad.
        Daryafti-ha: team1, team2 va is_knockout.
        Natije: Nadarad.
        """
        self.team1 = team1
        self.team2 = team2
        self.goals1 = 0
        self.goals2 = 0
        self.is_knockout = is_knockout
        self.winner = None
        self.penalties1 = None
        self.penalties2 = None

    def play(self):
        """Kar-e in bakhsh: Bazi ra ejra va amar va emtiyaz-e tim-ha ra be-rooz mikonad.
        Daryafti-ha: Nadarad.
        Natije: Tim-e barande ya None.
        """
        # Ravesh-e ejra: Natije-ye penalty-e bazi-e pishin nabayad dar bazi-e taze bemanad.
        self.penalties1 = None
        self.penalties2 = None

        # Ravesh-e ejra: Class-e Team gol-ha va barande-ye didar ra taein mikonad.
        self.goals1, self.goals2, self.winner = self.team1.simulate_match(
            self.team2, self.is_knockout
        )

        # Ravesh-e ejra: Gol-haye penalty joda az gol-haye markazi negahdari mishavand.
        if self.team1.last_penalty_score is not None:
            self.penalties1 = self.team1.last_penalty_score[0]
            self.penalties2 = self.team1.last_penalty_score[1]

        # Ravesh-e ejra: Gol-haye penalty dar amar-e gol-haye bazi hesab nemishavand.
        self.team1.goals_for += self.goals1
        self.team1.goals_against += self.goals2
        self.team2.goals_for += self.goals2
        self.team2.goals_against += self.goals1

        # Ravesh-e ejra: Emtiyaz tanha dar marhale-ye groohi be tim-ha ezafe mishavad.
        if not self.is_knockout:
            if self.goals1 > self.goals2:
                self.team1.points += 3
            elif self.goals2 > self.goals1:
                self.team2.points += 3
            else:
                self.team1.points += 1
                self.team2.points += 1

        return self.winner

    def result_text(self):
        """Kar-e in bakhsh: Natije-ye bazi ra be matn-e ghabel-e chap tabdil mikonad.
        Daryafti-ha: Nadarad.
        Natije: Natije, penalty-e ehtemali va barande (str).
        """
        # Ravesh-e ejra: Natije-ye gol-haye markazi dar aval-e matn gharar migirad.
        text = (
            self.team1.name + ' ' + str(self.goals1) + ' - '
            + str(self.goals2) + ' ' + self.team2.name
        )

        # Ravesh-e ejra: Agar bazi be penalty reside bashad, khorooji-e penalty ezafe mishavad.
        if self.penalties1 is not None:
            text += (
                ' (Penalty: ' + str(self.penalties1) + ' - '
                + str(self.penalties2) + ')'
            )

        if self.winner is not None:
            text += ' -> Barande: ' + self.winner.name

        return text
