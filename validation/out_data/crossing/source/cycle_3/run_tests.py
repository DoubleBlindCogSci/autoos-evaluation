import os
import pandas as pd
from rouge_score import rouge_scorer

### random code was not compileable (exclude without mention):
EXCLUDES_CODE_1 = []

### NO_COMPILE
NO_COMPILE = [(4,4)]


def run_code_1():
    directory = os.path.join(os.path.dirname(__file__))
    for l in range(5):
        for i in range(1, 5):
            if not (i, l) in EXCLUDES_CODE_1:
                out_f = os.path.join(directory, f'out_code_1/{i}_{l}_0.csv')
                if not os.path.exists(out_f):
                    print(i, l)
                    __import__(f'{i}_{l}_code_1')


def run_code_2():
    directory = os.path.join(os.path.dirname(__file__))
    for l in range(5):
        for i in range(1, 5):
            if not (i, l) in EXCLUDES_CODE_1 + NO_COMPILE:
                out_f = os.path.join(directory, f'out_code_2/{i}_{l}_0.csv')
                if not os.path.exists(out_f):
                    print(i, l)
                    __import__(f'{i}_{l}_code_2')


def run_sour():
    directory = os.path.join(os.path.dirname(__file__))
    for l in range(5):
        for i in range(1, 5):
            if not (i, l) in EXCLUDES_CODE_1 + NO_COMPILE:
                print(i, l)
                f = os.path.join(directory, f'{i}_{l}_sour.py')
                __import__(f'{i}_{l}_sour')

def run_sour_2():
    directory = os.path.join(os.path.dirname(__file__))
    for l in range(5):
        for i in range(1, 5):
            if not (i, l) in EXCLUDES_CODE_1 + NO_COMPILE:
                print(i, l)
                __import__(f'{i}_{l}_sour_2')


def run_rouge():
    directory = os.path.join(os.path.dirname(__file__))
    for l in range(5):
        for i in range(1, 5):
            p_1 = os.path.join(directory, f'{i}_{l}_text_1.txt')
            p_2 = os.path.join(directory, f'{i}_{l}_text_2.txt')
            with open(p_1) as f:
                text_1 = f.read()
            with open(p_2) as f:
                text_2 = f.read()

            scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
            score = scorer.score(text_1, text_2)
            df = pd.read_csv(os.path.join(directory, "result_rouge.csv"))
            s1 = score['rouge1']
            sL = score['rougeL']
            df.loc[len(df.index)] = [s1.precision, s1.recall, s1.fmeasure, sL.precision, sL.recall, sL.fmeasure, i]
            df.to_csv(os.path.join(directory, "result_rouge.csv"), index=False)


run_sour_2()
