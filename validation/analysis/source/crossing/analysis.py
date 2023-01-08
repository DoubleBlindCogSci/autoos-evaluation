import os
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


def main():
    df_error_c1 = pd.read_csv(abs_path('cycle_1/error.csv'))
    df_error_c2 = pd.read_csv(abs_path('cycle_2/error.csv'))
    df_error_c3 = pd.read_csv(abs_path('cycle_3/error.csv'))
    df_error = pd.concat([df_error_c1, df_error_c2, df_error_c3])
    main_logistic(df_error)
    df_rouge_c1 = pd.read_csv(abs_path('cycle_1/result_rouge.csv'))
    df_rouge_c2 = pd.read_csv(abs_path('cycle_2/result_rouge.csv'))
    df_rouge_c3 = pd.read_csv(abs_path('cycle_3/result_rouge.csv'))
    df_rouge = pd.concat([df_rouge_c1, df_rouge_c2, df_rouge_c3])
    df_error['intercept'] = 1
    main_linear(df_rouge, df_error[['intercept', 'nr_crossing', 'nr_factors']])


def main_logistic(df):
    # x = df[['nr_factors', 'nr_levels','accuracy']]
    #
    # model = smf.mnlogit('accuracy ~ nr_factors + nr_levels' ,x).fit()
    print('accuracy')
    df['intercept'] = 1
    x = df[['intercept', 'nr_crossing', 'nr_factors']]
    y = df['accuracy']
    print(y.describe())
    model = sm.Logit(y, x).fit()
    print(model.summary())


def main_linear(df, x):
    print('rouge')
    df['intercept'] = 1
    y = df['rougeL(fmeasure)']
    print(y.describe())
    model = sm.OLS(y, x).fit()
    print(model.summary())


def make_binary_df(in_path, out_path):
    df = pd.read_csv(abs_path(in_path))
    df['accuracy'] = df['p(code_1)'] == df['p(code_2)']
    df['accuracy'] = df['accuracy'].astype(int)
    df[['nr_crossing', 'nr_factors', 'accuracy']].to_csv(abs_path(out_path))


def add_number_of_lines_error(in_path):
    df = pd.read_csv(abs_path(abs_path(in_path)))
    df['complexity'] = df['nr_factors'] * 3#+ df['nr_crossing']
    df.to_csv(abs_path(in_path), index=False)


def add_number_of_lines_rouge(in_path_rouge, in_path_error):
    df_rouge = pd.read_csv(abs_path(abs_path(in_path_rouge)))
    df_error = pd.read_csv(abs_path(abs_path(in_path_error)))
    df_rouge['nr_factors'] = df_error['nr_factors']
    df_rouge['complexity'] = df_error['nr_factors'] * 3#+ df_error['nr_crossing']
    df_rouge.to_csv(abs_path(in_path_rouge), index=False)


def preprocess():
    for i in range(1, 8):
        add_number_of_lines_error(f'cycle_{i}/error.csv')
        add_number_of_lines_rouge(f'cycle_{i}/result_rouge.csv', f'cycle_{i}/error.csv')
    df_errors = []
    df_rouges = []
    for i in range(1, 8):
        df_errors.append(pd.read_csv(abs_path(f'cycle_{i}/error.csv')))
        df_rouges.append(pd.read_csv(abs_path(f'cycle_{i}/result_rouge.csv')))
    df_error = pd.concat(df_errors)
    df_rouge = pd.concat(df_rouges)
    df_rouge['nr_crossing'] = df_error['nr_crossing']
    # df_error['complexity'] = (df_error['complexity'] - df_error['complexity'].min()) / (
    #            df_error['complexity'].max() - df_error['complexity'].min())
    # df_rouge['complexity'] = (df_rouge['complexity'] - df_rouge['complexity'].min()) / (
    #            df_rouge['complexity'].max() - df_rouge['complexity'].min())
    df_error.to_csv(abs_path('error.csv'), index=False)
    df_rouge.to_csv(abs_path('rouge.csv'), index=False)


def abs_path(rel_path):
    _dir = os.path.dirname(__file__)
    return (os.path.join(_dir, rel_path))


if __name__ == '__main__':
    # make_binary_df('cycle_7/result_sour.csv', 'cycle_7/error.csv')
    # make_binary_df('cycle_4/result_sour.csv', 'cycle_4/error.csv')
    # main()
    preprocess()
    # main_logistic()
    # main_linear()
