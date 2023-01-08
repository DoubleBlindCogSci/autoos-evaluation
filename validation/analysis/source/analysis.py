import os
import pandas as pd
import statsmodels.formula.api as smf


def main():
    types = ['regular', 'derived', 'crossing', 'constraints', 'full_experiment']
    error = []
    rouge = []

    for t in types:
        path_in_error = f'{t}/error.csv'
        path_in_rouge = f'{t}/rouge.csv'
        _error = pd.read_csv(path_in_error)
        if t == 'full_experiment':
            t = 'segmenting'
        _error['translation'] = t
        error.append(_error)
        _rouge = pd.read_csv(path_in_rouge)
        _rouge['translation'] = t
        rouge.append(_rouge)
    df_error = pd.concat(error)
    df_rouge = pd.concat(rouge)

    df_rouge.to_csv('rouge_all.csv')
    df_error.to_csv('error_all.csv')

    # accuracy
    # main_logistic(df_error)
    # main_linear(df_rouge)


def main_logistic(df):
    x = df[['accuracy', 'nr_lines', 'translation']]
    print(df['accuracy'].describe())
    # model = Lmer("accuracy  ~ nr_lines  + (1|translation)", data=x, family='binomial').fit()
    # print(model)


def main_linear(df):
    x = df[['rougeL(fmeasure)', 'nr_lines', 'translation']]
    print(df['rougeL(fmeasure)'].describe())
    model = smf.mixedlm('rougeL(fmeasure) ~ nr_lines', x, groups=x['translation'])
    print(model.summary())


def abs_path(rel_path):
    _dir = os.path.dirname(__file__)
    return (os.path.join(_dir, rel_path))


if __name__ == '__main__':
    main()
    # make_binary_all()
    # t_test_improvement()
    # main()
    # main_logistic()
    # main_linear()
