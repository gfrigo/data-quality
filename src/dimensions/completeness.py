"""
Definição:
Todos os dados necessários estão presentes.

Como é medida:
Percentual de valores não nulos por coluna, ou percentual de funcionalidades
monitoradas com instrumentação.
"""

import pandas as pd

def check_completeness(df, columns):
    missing = df[columns].isna().sum().sum()
    total_cells = len(df) * len(columns)
    return {
        'dimension': 'completeness',
        'missing_count': missing,
        'total_cells': total_cells,
        'completeness': 1 - missing / total_cells if total_cells > 0 else 0
    }