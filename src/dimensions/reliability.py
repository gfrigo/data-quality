"""
Definição:
Os dados são confiáveis e credíveis.

Como é medida:
Percentual de tempo em que os dados não atendem às expectativas de qualidade
(ex.: imprecisos, inconsistentes, etc.)
"""

import pandas as pd

def check_reliability(df, column):
    unreliable = df[~df[column].astype(str).str.startswith("http")]
    return {
        'dimension': 'reliability',
        'unreliable_count': len(unreliable),
        'total': len(df),
        'reliability': 1 - len(unreliable) / len(df) if len(df) > 0 else 0
    }