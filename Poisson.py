# ================================================
# Daneshjoo: Mohammad Mahdi Rahimi Tabalvandani
# Shomare-ye daneshjooei: [Vared nashode]
# Onvan-e proje: Shabih-saz-e Jam-e Jahani
# Tarikh-e tahvil: 1405/05/01
# ================================================

"""Tolid-e tedad-e gol ba vazn-haye sade-ye lambda.

In file tabe-i dar ekhtiar-e ClassTeam migozarad ke bedoon-e ketabkhane-ye birouni, tedad-e gol ra az rooye bazehaye ehtemal entekhab mikonad."""

import random


def poisson_simple(lam):
    """Kar-e in bakhsh: Tedad-e gol ra ba taghrib-e dasti-e Poisson tolid mikonad.
    Daryafti-ha: lam (float), miangin-e mored-e entezar-e gol.
    Natije: Tedad-e gol-e tasadofi va na-manfi (int).
    """
    # Ravesh-e ejra: Bar asas bazeye lambda, list-e ehtemal-haye monaseb entekhab mishavad.
    if lam <= 0.5:
        probabilities = [0.6, 0.3, 0.1, 0.0, 0.0]
    elif lam <= 1.0:
        probabilities = [0.37, 0.37, 0.18, 0.06, 0.02]
    elif lam <= 1.5:
        probabilities = [0.22, 0.33, 0.25, 0.12, 0.05, 0.02, 0.01]
    elif lam <= 2.0:
        probabilities = [0.14, 0.27, 0.27, 0.18, 0.09, 0.04, 0.01]
    else:
        probabilities = [0.08, 0.18, 0.27, 0.22, 0.14, 0.07, 0.03, 0.01]

    # Ravesh-e ejra: Index-e entekhab-shode haman tedad-e gol-e shabih-sazi-shode ast.
    return random.choices(range(len(probabilities)), weights=probabilities)[0]
