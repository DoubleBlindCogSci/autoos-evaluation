import os
from rouge_score import rouge_scorer
import pandas as pd

###
EXCLUDES = [(7,3,0),(8,3,0),(9,3,0),(6,3,1),(7,3,1),(8,3,1),(9,3,1),(9,2,1)]
NO_COMPILE = [(9,3,1),(5,3,0)]


def run_code_1():
    directory = os.path.join(os.path.dirname(__file__))
    for l in range(2):
        for i in range(2, 10):
            for j in range(1, 4):
                if not (i, j, l) in EXCLUDES:
                    out_f = os.path.join(directory, f'out_code_1/{i}_{j}_{l}_0.csv')
                    if not os.path.exists(out_f):
                        print(i, j, l)
                        f = os.path.join(directory, f'{i}_{j}_{l}_code_1.py')
                        exec(open(f).read())


def run_code_2():
    directory = os.path.join(os.path.dirname(__file__))
    for l in range(2):
        for i in range(2, 10):
            for j in range(1, 4):
                if not (i, j, l) in EXCLUDES + NO_COMPILE:
                    out_f = os.path.join(directory, f'out_code_2/{i}_{j}_{l}_0.csv')
                    if not os.path.exists(out_f):
                        print(i, j, l)
                        f = os.path.join(directory, f'{i}_{j}_{l}_code_2.py')
                        exec(open(f).read())


def run_sour():
    directory = os.path.join(os.path.dirname(__file__))
    for l in range(2):
        for i in range(2, 10):
            for j in range(1, 4):
                if not (i, j, l) in EXCLUDES + NO_COMPILE:
                    f = os.path.join(directory, f'{i}_{j}_{l}_sour.py')
                    exec(open(f).read())


def run_rouge():
    directory = os.path.join(os.path.dirname(__file__))
    for l in range(2):
        for i in range(2, 10):
            for j in range(1, 4):
                p_1 = os.path.join(directory, f'{i}_{j}_{l}_text_1.txt')
                p_2 = os.path.join(directory, f'{i}_{j}_{l}_text_2.txt')
                with open(p_1) as f:
                    text_1 = f.read()
                with open(p_2) as f:
                    text_2 = f.read()

                scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
                score = scorer.score(text_1, text_2)
                df = pd.read_csv(os.path.join(directory, "result_rouge.csv"))
                s1 = score['rouge1']
                sL = score['rougeL']
                df.loc[len(df.index)] = [s1.precision, s1.recall, s1.fmeasure, sL.precision, sL.recall, sL.fmeasure, j,
                                         i]
                df.to_csv(os.path.join(directory, "result_rouge.csv"), index=False)


run_rouge()
