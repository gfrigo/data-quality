"""
Definição:
Garante uniformidade dos dados entre diferentes conjuntos e banco de dados,
evitando contradições e discrepâncias que comprometem a confiabilidade e
interpretabilidade das informações.

Como é medida:
Ocorrências de mudanças em definições, esquemas ou nomenclaturas.
"""

import pandas as pd

def check_consistency(df):
    inconsistent = df[(df['Age'] < 20) & (df['↓OVA'] > 85)]
    return {
        'dimension': 'consistency',
        'inconsistent_count': len(inconsistent),
        'total': len(df),
        'consistency': 1 - len(inconsistent) / len(df) if len(df) > 0 else 0
    }
