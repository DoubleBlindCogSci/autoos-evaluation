import os
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


def main():
    df_error_c1 = pd.read_csv(abs_path('cycle_1/error.csv'))
    df_error_c2 = pd.read_csv(abs_path('cycle_2/error.csv'))
    df_error_c3 = pd.read_csv(abs_path('cycle_3/error.csv'))
    df_error = pd.concat([df_error_c1, df_error_c2,df_error_c3])
    #main_logistic(df_error)
    df_rouge_c1 = pd.read_csv(abs_path('cycle_1/result_rouge.csv'))
    df_rouge_c2 = pd.read_csv(abs_path('cycle_2/result_rouge.csv'))
    df_rouge_c3 = pd.read_csv(abs_path('cycle_3/result_rouge.csv'))
    df_rouge = pd.concat([df_rouge_c1, df_rouge_c2, df_rouge_c3])
    #main_logistic(df_error)
    main_linear(df_rouge)


def main_logistic(df):
    # x = df[['nr_factors', 'nr_levels','accuracy']]
    #
    # model = smf.mnlogit('accuracy ~ nr_factors + nr_levels' ,x).fit()
    print('accuracy')
    df['intercept'] = 1
    x = df[['intercept', 'nr_constraints']]
    y = df['accuracy']
    print(y.describe())
    model = sm.Logit(y, x).fit()
    print(model.summary())


def main_linear(df):
    print('rouge')
    df['intercept'] = 1
    x = df[['intercept', 'nr_constraints']]
    y = df['rougeL(fmeasure)']
    print(y.describe())
    model = sm.OLS(y, x).fit()
    print(model.summary())


def make_binary_df(in_path, out_path):
    df = pd.read_csv(abs_path(in_path))
    df['accuracy'] = (df['p(code_1)'] == df['p(code_2)']) & (df['constraints(code_1)'] == df['constraints(code_2)'])
    df['accuracy'] = df['accuracy'].astype(int)
    df[['nr_constraints', 'accuracy']].to_csv(abs_path(out_path))

def add_number_of_lines(in_path):
    df = pd.read_csv(abs_path(abs_path(in_path)))
    df['complexity'] = df['nr_constraints'] * 6 # for each constraint one factor
    df.to_csv(abs_path(in_path), index=False)

def preprocess():
    for i in range(1, 4):
        add_number_of_lines(f'cycle_{i}/error.csv')
        add_number_of_lines(f'cycle_{i}/result_rouge.csv')
    df_errors = []
    df_rouges = []
    for i in range(1,4):
        df_errors.append(pd.read_csv(abs_path(f'cycle_{i}/error.csv')))
        df_rouges.append(pd.read_csv(abs_path(f'cycle_{i}/result_rouge.csv')))
    df_error = pd.concat(df_errors)
    df_rouge = pd.concat(df_rouges)
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
    # make_binary_df('cycle_1/result_sour.csv', 'cycle_1/error.csv')
    # make_binary_df('cycle_3/result_sour.csv', 'cycle_3/error.csv')
    # main()
    preprocess()
    # main_logistic()
    # main_linear()
