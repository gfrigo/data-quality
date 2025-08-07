"""
Definição:
Os dados são entregues ao público certo, no formato certo e no momento certo. 
Garante a proatividade necessária para mudança de condições e tomada de decisões.

Como é medida:
Atende às expectativas dos usuários (ex.: se uma tabela deve ser atualizada até
9h e for, é considerada pontual)
"""

import pandas as pd

def check_timeliness(df, column):
    outdated = df[df[column] > 45]
    return {
        'dimension': 'timeliness',
        'outdated_count': len(outdated),
        'total': len(df),
        'timeliness': 1 - len(outdated) / len(df) if len(df) > 0 else 0
    }