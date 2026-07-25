# ================================================
# Daneshjoo: Mohammad Mahdi Rahimi Tabalvandani
# Shomare-ye daneshjooei: [Vared nashode]
# Onvan-e proje: Shabih-saz-e Jam-e Jahani
# Tarikh-e tahvil: 1405/05/01
# ================================================

"""Hamahang-konande-ye dade va tamame-ye marhale-haye jam.

In class file-e CSV, seedbandi, daste-ha, bracket, final va gozaresh-e darsad ra sazmandehi mikonad. Ghesmat-e amari shey-e joda darad."""

import csv
import os
import random

from ClassGroup import Group
from ClassKnockoutStage import KnockoutStage
from ClassMatch import Match
from ClassTeam import Team


class WorldCupSimulator:
    """Kar-e in bakhsh: Dade-ha, ghorekeshi va ejra-ye jam ra hamahang mikonad."""

    def __init__(self):
        """Kar-e in bakhsh: Shabih-saz-e khali amade mikonad.
        Daryafti-ha: Nadarad.
        Natije: Nadarad.
        """
        self.teams = []
        self.groups = []
        self.round_of_16 = self.quarterfinals = None
        self.semifinals = self.final = None
        self.champion = None
        self.group_stage_completed = False

    def _clear_tournament_results(self):
        # Ravesh-e ejra: Marhale-ha va ghahreman-e jam-e pishin khali mishavand.
        self.round_of_16 = self.quarterfinals = None
        self.semifinals = self.final = None
        self.champion = None
        self.group_stage_completed = False

    def _reset_all_stats(self):
        # Ravesh-e ejra: Amar-e tamam-e tim-ha pish az shabih-sazi-e taze sefr mishavad.
        for team in self.teams:
            team.reset_stats()

    def load_teams_from_csv(self, filename):
        """Kar-e in bakhsh: Tim-ha ra az file-e CSV mikhanad va etebarsanji mikonad.
        Daryafti-ha: filename (str), nam ya masir-e file.
        Natije: Movafaghiat-e bargozari (bool).
        """
        # Ravesh-e ejra: Ghabl az open, vojood-e file kontrol mishavad.
        if not os.path.isfile(filename):
            print('Eshkal: File-e entekhabi peyda nashod.')
            return False

        candidate_teams = []
        registered_names = set()
        registered_ranks = set()

        with open(filename, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            needed_columns = ['name', 'attack', 'defense', 'rank']

            # Ravesh-e ejra: File bayad satr-e onvan va har chahar sotoon-e lazem ra dashte bashad.
            if csv_reader.fieldnames is None:
                print('Eshkal: File-e CSV onvan-e sotoon nadarad.')
                return False

            for field_name in needed_columns:
                if field_name not in csv_reader.fieldnames:
                    print(
                        'Eshkal: Sotoon-e ' + field_name
                        + ' dar file vojood nadarad.'
                    )
                    return False

            # Ravesh-e ejra: Har satr pish az sakhte-shodan-e shey-e Team etebarsanji mishavad.
            for team_row in csv_reader:
                if (
                    team_row['name'] is None
                    or team_row['attack'] is None
                    or team_row['defense'] is None
                    or team_row['rank'] is None
                ):
                    print('Eshkal: Yeki az satr-haye file naghes ast.')
                    return False

                name = team_row['name'].strip()
                attack_text = team_row['attack'].strip()
                defense_text = team_row['defense'].strip()
                rank_text = team_row['rank'].strip()

                if name == '':
                    print('Eshkal: Nam-e yek team khali ast.')
                    return False

                if not (
                    attack_text.isdigit()
                    and defense_text.isdigit()
                    and rank_text.isdigit()
                ):
                    print(
                        'Eshkal: Attack, defense va rank '
                        'bayad adad-e sahih bashand.'
                    )
                    return False

                attack = int(attack_text)
                defense = int(defense_text)
                rank = int(rank_text)

                if not (1 <= attack <= 100 and 1 <= defense <= 100):
                    print(
                        'Eshkal: Attack va defense bayad '
                        'bein-e 1 ta 100 bashand.'
                    )
                    return False

                if not 1 <= rank <= 32:
                    print('Eshkal: Rank-e team bayad bein-e 1 ta 32 bashad.')
                    return False

                if name in registered_names or rank in registered_ranks:
                    print('Eshkal: Nam-e team ya rank dar file tekrari ast.')
                    return False

                registered_names.add(name)
                registered_ranks.add(rank)
                candidate_teams.append(Team(name, attack, defense, rank))

        # Ravesh-e ejra: Dade-ye kamtar ya bishtar az 32 team jahat-e in proje motabar nist.
        if len(candidate_teams) != 32:
            print('Eshkal: File bayad daghighan shamel-e 32 team bashad.')
            return False

        # Ravesh-e ejra: Vaziyat-e pishin tanha pas az bargozari-e movafagh jaygozin mishavad.
        self.teams = candidate_teams
        self.groups = []
        self._clear_tournament_results()
        print('32 team ba movafaghiat az file bargozari shodand.')
        return True

    def seed_and_draw_groups(self, display_groups=True):
        """Kar-e in bakhsh: Chahar seed ra dorost mikonad va tim-ha ra ghorekeshi mikonad.
        Daryafti-ha: display_groups (bool), ejaze-ye chap-e daste-ha.
        Natije: Movafaghiat-e ghorekeshi (bool).
        """
        if len(self.teams) != 32:
            print('Aval tim-ha ra bargozari konid.')
            return False

        # Ravesh-e ejra: Tim-ha bar asas rank be chahar pot-e hasht-team-i taghsim mishavand.
        rank_ordered_teams = sorted(self.teams, key=lambda team: team.rank)
        pots = [
            rank_ordered_teams[0:8],
            rank_ordered_teams[8:16],
            rank_ordered_teams[16:24],
            rank_ordered_teams[24:32]
        ]
        mixed_pots = []

        # Ravesh-e ejra: Tartib-e har pot bedoon-e tekrar tasadofi mishavad.
        for pot in pots:
            mixed_pots.append(random.sample(pot, len(pot)))

        group_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.groups = []
        self._clear_tournament_results()

        # Ravesh-e ejra: Har grooh daghighan yek team az har pot migirad.
        for group_number in range(8):
            selected_teams = []
            for pot_number in range(4):
                team = mixed_pots[pot_number][group_number]
                team.group = group_names[group_number]
                selected_teams.append(team)
            self.groups.append(Group(group_names[group_number], selected_teams))

        if display_groups:
            print('\nGhorekeshi-e daste-ha ba movafaghiat ejra shod.')
            for group in self.groups:
                registered_names = []
                for team in group.teams:
                    registered_names.append(team.name)
                print('Daste ' + group.name + ': ' + ', '.join(registered_names))

        return True

    def _play_group_stage(self, display_tables):
        # Ravesh-e ejra: Hame-ye daste-ha bazi mikonand va dar sorat-e niaz chap mishavand.
        for group in self.groups:
            group.play_all_matches()
            if display_tables:
                group.display_table()
        self.group_stage_completed = True

    def run_group_stage(self):
        """Kar-e in bakhsh: Marhale-ye groohi va jadval-e har hasht grooh ra ejra mikonad.
        Daryafti-ha: Nadarad.
        Natije: Movafaghiat-e ejra (bool).
        """
        if len(self.groups) != 8:
            print('Aval ghorekeshi-e daste-ha ra anjam dahid.')
            return False

        # Ravesh-e ejra: Ejra-ye taze nabayad amar ya bracket-e pishin ra negah darad.
        self._reset_all_stats()
        self._clear_tournament_results()
        self._play_group_stage(True)
        return True

    def setup_knockout_bracket(self):
        """Kar-e in bakhsh: Bracket-e sabet-e yek-hashtom nahaei ra dorost mikonad.
        Daryafti-ha: Nadarad.
        Natije: Movafaghiat-e sakht-e bracket (bool).
        """
        if not self.group_stage_completed:
            print('Aval marhale-ye groohi ra ejra konid.')
            return False

        # Ravesh-e ejra: Do tim-e aval-e har grooh be tartib-e A ta H zakhire mishavand.
        qualified_teams = []
        for group in self.groups:
            qualified_teams.append(group.advance_teams())

        # Ravesh-e ejra: Pair-ha daghighan tebghe bracket-e sabet-e file-e proje hastand.
        round_pairs = [
            (qualified_teams[0][0], qualified_teams[1][1]),
            (qualified_teams[2][0], qualified_teams[3][1]),
            (qualified_teams[4][0], qualified_teams[5][1]),
            (qualified_teams[6][0], qualified_teams[7][1]),
            (qualified_teams[1][0], qualified_teams[0][1]),
            (qualified_teams[3][0], qualified_teams[2][1]),
            (qualified_teams[5][0], qualified_teams[4][1]),
            (qualified_teams[7][0], qualified_teams[6][1])
        ]
        matches = []

        for match_pair in round_pairs:
            matches.append(Match(match_pair[0], match_pair[1], True))

        self.round_of_16 = KnockoutStage('Yek-hashtom nahaei', matches)
        return True

    def _build_next_round(self, round_name, winners):
        matches = []

        # Ravesh-e ejra: Har do barande-ye motavali yek bazi-e dor-e badi ra misazand.
        for index in range(0, len(winners), 2):
            matches.append(Match(winners[index], winners[index + 1], True))

        return KnockoutStage(round_name, matches)

    def _play_stage(self, stage, display_results):
        # Ravesh-e ejra: Marhale ejra mishavad va barandegan jahat-e dor-e badi bargasht dade mishavand.
        stage.play_round()
        if display_results:
            stage.display_results()
        return stage.get_winners()

    def run_knockout_stage(self, display_results=True):
        """Kar-e in bakhsh: Tamam-e marhale-haye hazfi ra ta taein-e ghahreman ejra mikonad.
        Daryafti-ha: display_results (bool), ejaze-ye chap-e khorooji-ha.
        Natije: Tim-e ghahreman ya None.
        """
        if self.round_of_16 is None:
            print('Aval bracket-e marhale-ye hazfi ra besazid.')
            return None

        # Ravesh-e ejra: Barandegan-e har marhale pair-haye marhale-ye badi ra misazand.
        winners = self._play_stage(self.round_of_16, display_results)
        self.quarterfinals = self._build_next_round(
            'Yek-chaharom nahaei', winners
        )
        winners = self._play_stage(self.quarterfinals, display_results)
        self.semifinals = self._build_next_round('Nime-nahaei', winners)
        winners = self._play_stage(self.semifinals, display_results)
        self.final = self._build_next_round('Final', winners)
        self.champion = self._play_stage(self.final, display_results)[0]
        return self.champion

    def run_full_simulation(self, display_results=True):
        """Kar-e in bakhsh: Ghorekeshi, marhale-ye groohi va hazfi ra kamel ejra mikonad.
        Daryafti-ha: display_results (bool), ejaze-ye chap-e khorooji-ha.
        Natije: Tim-e ghahreman ya None.
        """
        if len(self.teams) != 32:
            print('Aval tim-ha ra bargozari konid.')
            return None

        # Ravesh-e ejra: Har jam-e kamel az amar-e sefr va ghorekeshi-e taze shoroo mishavad.
        self._reset_all_stats()
        self.seed_and_draw_groups(display_results)
        self._play_group_stage(display_results)
        self.setup_knockout_bracket()
        champion = self.run_knockout_stage(display_results)

        if display_results and champion is not None:
            print('\nGhahreman-e Jam-e Jahani: ' + champion.name)

        return champion

    def most_likely_champion(self, num_simulations=1000):
        """Kar-e in bakhsh: Darsad-e ghahremani ra ba chand ejra mohasebe mikonad.
        Daryafti-ha: num_simulations (int), tedad-e ejra; meghdar-e avalie 1000.
        Natije: Darsad-e ghahremani-e tim-ha (dict) ya None.
        """
        if len(self.teams) != 32:
            print('Aval tim-ha ra bargozari konid.')
            return None

        if num_simulations <= 0:
            print('Eshkal: Tedad-e shabih-sazi bayad bishtar az sefr bashad.')
            return None

        title_counts = {}
        report_simulator = WorldCupSimulator()

        # Ravesh-e ejra: Tim-haye amari joda hastand ta bracket-e jam-e markazi baznevisi nashavad.
        for team in self.teams:
            title_counts[team.name] = 0
            report_simulator.teams.append(
                Team(team.name, team.attack, team.defense, team.rank)
            )

        # Ravesh-e ejra: Har ejra yek jam-e kamel-e makhfi dar shabih-saz-e amari ast.
        for run_number in range(num_simulations):
            champion = report_simulator.run_full_simulation(False)
            title_counts[champion.name] += 1

        chance_percentages = {}
        for team_name in title_counts:
            count = title_counts[team_name]
            chance_percentages[team_name] = count * 100 / num_simulations

        ordered_percentages = sorted(
            chance_percentages.items(), key=lambda item: item[1], reverse=True
        )

        # Ravesh-e ejra: Gozaresh az bishtarin darsad ta kamtarin darsad chap mishavad.
        print('\nShabih-sazi ' + str(num_simulations) + ' bar ejra shod.')
        print('Darsad-e ghahremani-e har team:')
        for result in ordered_percentages:
            print(result[0] + ': ' + format(result[1], '.1f') + '%')

        return chance_percentages

    def display_bracket(self):
        """Kar-e in bakhsh: Bracket-e hazfi-e akharin jam-e kamel ra chap mikonad.
        Daryafti-ha: Nadarad.
        Natije: Vojood-e bracket-e kamel (bool).
        """
        # Ravesh-e ejra: Shabih-sazi-e amari bracket-e in shey ra taghir nemidahad.
        if self.final is None:
            print('Hanooz shabih-sazi-e kameli anjam nashode ast.')
            return False

        print('\n===== Bracket-e Hazfi =====')
        stages = [
            self.round_of_16,
            self.quarterfinals,
            self.semifinals,
            self.final
        ]

        # Ravesh-e ejra: Natayej az yek-hashtom ta final az hafeze chap mishavand.
        for stage in stages:
            stage.display_results()

        print('\nGhahreman: ' + self.champion.name)
        return True
