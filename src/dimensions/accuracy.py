"""
Definição:
O quão bem os dados representam a realidade.

Como é medida:
Percentual de correção necessária em relação aos dados reais válidos.
"""

import pandas as pd

def check_accuracy(df, column, valid_values):
    invalid = df[~df[column].isin(valid_values)]
    return {
        'dimension': 'accuracy',
        'invalid_count': len(invalid),
        'total': len(df),
        'accuracy': 1 - len(invalid) / len(df) if len(df) > 0 else 0
    }