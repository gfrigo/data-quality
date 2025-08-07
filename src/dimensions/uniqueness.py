"""
Definição:
Não há duplicação de dados.

Como é medida:
Percentual de colunas, linhas e conjuntos de dados que apresentam informações
duplicadas.
"""

import pandas as pd

def check_uniqueness(df, column):
    duplicates = df[column].duplicated().sum()
    return {
        'dimension': 'uniqueness',
        'duplicate_count': duplicates,
        'total': len(df),
        'uniqueness': 1 - duplicates / len(df) if len(df) > 0 else 0
    }