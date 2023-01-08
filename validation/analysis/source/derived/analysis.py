import os
import pandas as pd
import statsmodels.api as sm
import pingouin as pg



def main():
    types = ['within', 'window', 'transition']
    error_after = []
    rouge_after = []
    for t in types:
        for i in range(2, 6):
            path_in_error = f'{t}/cycle_{i}/error.csv'
            path_rouge = f'{t}/cycle_{i}/result_rouge.csv'
            error_after.append(pd.read_csv(path_in_error))
            rouge_after.append(pd.read_csv(path_rouge))
    df_error = pd.concat(error_after)
    df_rouge = pd.concat(rouge_after)


    # accuracy
    main_logistic(df_error)
    main_linear(df_rouge)


def main_logistic(df):
    df['intercept'] = 1
    x = df[['intercept', 'nr_input_factors', 'nr_output_levels']]
    y = df['accuracy']
    print(y.describe())
    model = sm.Logit(y, x).fit()
    print(model.summary())


def main_linear(df):
    df['intercept'] = 1
    x = df[['intercept', 'nr_factors', 'nr_levels']]
    y = df['rougeL(fmeasure)']
    print(y.describe())
    model = sm.OLS(y, x).fit()
    print(model.summary())


def make_binary_df(in_path, out_path):
    df = pd.read_csv(abs_path(in_path))
    df['accuracy'] = (df['p(code_1)'] == df['p(code_2)']) & (df['levels(code_1)'] == df['levels(code_2)'])
    df['accuracy'] = df['accuracy'].astype(int)
    df[['nr_input_factors', 'nr_output_levels', 'accuracy']].to_csv(abs_path(out_path))

def make_binary_all():
    types = ['within', 'window', 'transition']
    for t in types:
        for i in range(6, 7):
            path_in = f'{t}/cycle_{i}/result_sour.csv'
            path_out = f'{t}/cycle_{i}/error.csv'
            make_binary_df(path_in, path_out)



def t_test_improvement():
    types = ['within', 'window', 'transition']
    errors_before = []
    rouge_before = []
    error_after = []
    rouge_after = []
    for t in types:
        path_in_error = f'{t}/cycle_1/error.csv'
        path_rouge = f'{t}/cycle_1/result_rouge.csv'
        errors_before.append(pd.read_csv(path_in_error))
        rouge_before.append(pd.read_csv(path_rouge))
        for i in range(2, 7):
            path_in_error = f'{t}/cycle_{i}/error.csv'
            path_rouge = f'{t}/cycle_{i}/result_rouge.csv'
            error_after.append(pd.read_csv(path_in_error))
            rouge_after.append(pd.read_csv(path_rouge))
    df_error_before = pd.concat(errors_before)
    df_rouge_before = pd.concat(rouge_before)
    df_error_after = pd.concat(error_after)
    df_rouge_after = pd.concat(rouge_after)

    # accuracy
    x_error_before = df_error_before['accuracy']
    print('accuracy\n', x_error_before.describe())
    x_error_after = df_error_after['accuracy']
    print('accuracy\n', x_error_after.describe())
    res = pg.ttest(x_error_before, x_error_after, correction=False)
    print(res.T)

    x_rougeL_before = df_rouge_before['rougeL(fmeasure)']
    print('rougeL\n', x_rougeL_before.describe())
    x_rougeL_after = df_rouge_after['rougeL(fmeasure)']
    print('rougeL\n', x_rougeL_after.describe())
    res = pg.ttest(x_rougeL_before, x_rougeL_after, correction=False)
    print(res.T)


def add_number_of_lines_error(in_path, t):
    df = pd.read_csv(abs_path(abs_path(in_path)))
    df['complexity'] = df['nr_input_factors'] + df['nr_output_levels']
    df['derived_type'] = t
    df.to_csv(abs_path(in_path), index=False)

def add_number_of_lines_rouge(in_path, t):
    df = pd.read_csv(abs_path(abs_path(in_path)))
    df['complexity'] = df['nr_factors'] + df['nr_levels']
    df['derived_type'] = t
    df.to_csv(abs_path(in_path), index=False)

def preprocess():
    types = ['within', 'window', 'transition']
    for t in types:
        for i in range(1, 7):
            add_number_of_lines_error(f'{t}/cycle_{i}/error.csv', t)
            add_number_of_lines_rouge(f'{t}/cycle_{i}/result_rouge.csv', t)


    df_errors = []
    df_rouges = []
    for t in types:
        for i in range(2,7):
            df_errors.append(pd.read_csv(abs_path(f'{t}/cycle_{i}/error.csv')))
            df_rouges.append(pd.read_csv(abs_path(f'{t}/cycle_{i}/result_rouge.csv')))
    df_error = pd.concat(df_errors)
    df_rouge = pd.concat(df_rouges)
    # df_error['complexity'] = (df_error['complexity'] - df_error['complexity'].min()) / (
    #             df_error['complexity'].max() - df_error['complexity'].min())
    # df_rouge['complexity'] = (df_rouge['complexity'] - df_rouge['complexity'].min()) / (
    #             df_rouge['complexity'].max() - df_rouge['complexity'].min())
    df_error.to_csv(abs_path('error.csv'), index=False)
    df_rouge.to_csv(abs_path('rouge.csv'), index=False)


def abs_path(rel_path):
    _dir = os.path.dirname(__file__)
    return (os.path.join(_dir, rel_path))


if __name__ == '__main__':
    preprocess()
    # make_binary_all()
    #t_test_improvement()
    # main()
    # main_logistic()
    # main_linear()
