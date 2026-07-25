# ================================================
# Daneshjoo: Mohammad Mahdi Rahimi Tabalvandani
# Shomare-ye daneshjooei: [Vared nashode]
# Onvan-e proje: Shabih-saz-e Jam-e Jahani
# Tarikh-e tahvil: 1405/05/01
# ================================================

"""Ejra-ye yek dor az bracket-e hazfi.

Har shey nam-e dor va list-e didarha ra zakhire mikonad, didarha ra ejra mikonad va barandegan ra ba tartib-e bracket pas midahad."""


class KnockoutStage:
    """Kar-e in bakhsh: Bazi-ha va barandegan-e yek marhale-ye hazfi ra zakhire mikonad."""

    def __init__(self, round_name, matches):
        """Kar-e in bakhsh: Yek marhale-ye hazfi dorost mikonad.
        Daryafti-ha: round_name (str) va matches (list).
        Natije: Nadarad.
        """
        self.round_name = round_name
        self.matches = matches

    def play_round(self):
        """Kar-e in bakhsh: Tamam-e bazi-haye marhale ra ejra mikonad.
        Daryafti-ha: Nadarad.
        Natije: Nadarad.
        """
        # Ravesh-e ejra: Har Match tanha yek bar dar in marhale ejra mishavad.
        for match in self.matches:
            match.play()

    def get_winners(self):
        """Kar-e in bakhsh: Barandegan ra be tartib-e bracket pas midahad.
        Daryafti-ha: Nadarad.
        Natije: Tim-haye barande (list).
        """
        winners = []

        # Ravesh-e ejra: Tartib-e list jahat-e sakht-e dor-e badi hefz mishavad.
        for match in self.matches:
            winners.append(match.winner)

        return winners

    def display_results(self):
        """Kar-e in bakhsh: Natayej-e marhale ra chap mikonad.
        Daryafti-ha: Nadarad.
        Natije: Nadarad.
        """
        print('\n===== ' + self.round_name + ' =====')

        # Ravesh-e ejra: Class-e Match matn-e gol, penalty va barande ra amade mikonad.
        for match in self.matches:
            print(match.result_text())
