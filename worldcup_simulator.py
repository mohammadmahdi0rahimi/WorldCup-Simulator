# ================================================
# Daneshjoo: Mohammad Mahdi Rahimi Tabalvandani
# Shomare-ye daneshjooei: [Vared nashode]
# Onvan-e proje: Shabih-saz-e Jam-e Jahani
# Tarikh-e tahvil: 1405/05/01
# ================================================

"""Noghte-ye shoroo va menu-ye noskhe-ye khat-e farman.

In file voroodi-e karbar ra migirad, etebar-e gozine-ha ra kontrol mikonad va dastoor-e monaseb ra rooye WorldCupSimulator ejra mikonad."""

from ClassWorldCupSimulator import WorldCupSimulator


def display_menu():
    """Kar-e in bakhsh: Gozine-haye menu-ye markazi ra chap mikonad.
    Daryafti-ha: Nadarad.
    Natije: Nadarad.
    """
    print('\n===== Shabih-saz-e Jam-e Jahani =====')
    print('1) Bargozari-e tim-ha az file-e CSV')
    print('2) Anjam-e ghorekeshi-e daste-ha')
    print('3) Ejra-ye marhale-ye groohi va chap-e jadval-ha')
    print('4) Ejra-ye kamel-e jam va chap-e ghahreman')
    print('5) Shabih-sazi-e chandbare va gozaresh-e darsad-e ghahremani')
    print('6) Chap-e bracket-e hazfi-e akharin jam-e kamel')
    print('7) Khorooj')


def main():
    """Kar-e in bakhsh: Menu va voroodi-haye karbar ra sazmandehi mikonad.
    Daryafti-ha: Nadarad.
    Natije: Nadarad.
    """
    # Ravesh-e ejra: Yek shey-e markazi dar tamame-ye ejra-ye menu estefade mishavad.
    simulator = WorldCupSimulator()

    while True:
        display_menu()
        choice = input('Gozine-ye entekhabi ra vared konid: ').strip()

        if choice == '1':
            filename = input(
                'Nam-e file ra vared konid '
                '(Meghdar-e avalie: worldcup_2026_teams.csv): '
            ).strip()
            if filename == '':
                filename = 'worldcup_2026_teams.csv'
            simulator.load_teams_from_csv(filename)

        # Ravesh-e ejra: Gozine-haye 2 ta 6 bedoon-e team ejra nemishavand.
        elif choice in ['2', '3', '4', '5', '6'] and len(
            simulator.teams
        ) == 0:
            print('Aval tim-ha ra bargozari konid.')
        elif choice == '2':
            simulator.seed_and_draw_groups()
        elif choice == '3':
            simulator.run_group_stage()
        elif choice == '4':
            simulator.run_full_simulation()
        elif choice == '5':
            number_text = input(
                'Tedad-e shabih-sazi ra vared konid (Meghdar-e avalie: 1000): '
            ).strip()

            # Ravesh-e ejra: Voroodi-e khali meghdar-e avalie-e 1000 ra faal mikonad.
            if number_text == '':
                simulator.most_likely_champion(1000)
            elif number_text.isdigit() and int(number_text) > 0:
                simulator.most_likely_champion(int(number_text))
            else:
                print(
                    'Eshkal: Tedad-e shabih-sazi bayad '
                    'adad-e sahih-e mosbat bashad.'
                )
        elif choice == '6':
            simulator.display_bracket()
        elif choice == '7':
            print('Barname payan yaft.')
            break
        else:
            print('Gozine namotabar ast; yeki az adad-e 1 ta 7 ra vared konid.')


# Ravesh-e ejra: Menu tanha zamani ejra mishavad ke in file mostaghim baz shode bashad.
if __name__ == '__main__':
    main()
