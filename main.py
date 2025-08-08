import pandas as pd
from src.dimensions.accuracy import check_accuracy
from src.dimensions.completeness import check_completeness
from src.dimensions.consistency import check_consistency
from src.dimensions.reliability import check_reliability
from src.dimensions.timeliness import check_timeliness
from src.dimensions.uniqueness import check_uniqueness
from src.dimensions.usefulness import check_usefulness

def run_data_quality_checks(df):
    countries = ['Argentina', 'Brazil', 'Portugal', 'Belgium', 'Slovenia', 'France', 'Germany', 'Spain', 'England']
    results = []
    results.append(check_accuracy(df, 'Nationality', countries))
    results.append(check_completeness(df, ['Club', 'Age', 'Name']))
    results.append(check_consistency(df))
    results.append(check_reliability(df, 'photoUrl'))
    results.append(check_timeliness(df, 'Age'))
    results.append(check_uniqueness(df, 'ID'))
    results.append(check_usefulness(df, ['Name', 'Nationality', 'Age']))
    return results

if __name__ == '__main__':
    df = pd.read_csv('./src/data/fifa21.csv')
    results = run_data_quality_checks(df)
    for r in results:
        print(r)