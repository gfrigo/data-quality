"""
Definição:
Alinhamento dos dados com o contexto específico de negócio garantindo dados
servem a proposta pretendida e prevê insights úteis.

Como é medida:
Quantas decisões importantes foram tomadas com os dados? Quantos usuários ou
sistemas utilizam esses dados?
"""

import pandas as pd

def check_usefulness(df, required_columns):
    useful = 0
    for col in required_columns:
        if col in df.columns and df[col].notna().sum() > 0:
            useful += 1
    return {
        'dimension': 'usefulness',
        'useful_columns': useful,
        'required_columns': len(required_columns),
        'usefulness': useful / len(required_columns) if required_columns else 0
    }