import os
import pandas as pd
from rouge_score import rouge_scorer

### random code was not compileable (exclude without mention):
EXCLUDES_CODE_1 = []

### NO_COMPILE
NO_COMPILE = []

### NO_SCORE (couldn't get sequence for 1 and 2)
NO_SCORE = [(4,0,2),(4,1,0),(4,1,2),(4,2,2),(5,1,1),(5,1,2),(5,2,1),(5,2,2),(6,1,0),(6,1,2),(6,2,2)]

### ERROR IN CODE_2
ERROR_2 = []

def run_code_1():
    directory = os.path.join(os.path.dirname(__file__))
    for i in range(4, 7):
        for j in range(3):
            for k in range(3):
                if not (i, j, k) in EXCLUDES_CODE_1:
                    out_f = os.path.join(directory, f'out_code_1/{i}_{j}_{k}.csv')
                    if not os.path.exists(out_f):
                        print(i, j, k)
                        __import__(f'{i}_{j}_{k}_code_1')


def run_code_2():
    directory = os.path.join(os.path.dirname(__file__))
    for i in range(4, 7):
        for j in range(3):
            for k in range(3):
                if not (i, j, k) in EXCLUDES_CODE_1:
                    out_f = os.path.join(directory, f'out_code_2/{i}_{j}_{k}0.csv')
                    if not os.path.exists(out_f):
                        print(i, j, k)
                        __import__(f'{i}_{j}_{k}_code_2')


def run_sour():
    for i in range(4, 7):
        for j in range(3):
            for k in range(3):
                if not (i, j, k) in EXCLUDES_CODE_1 + NO_COMPILE +NO_SCORE + ERROR_2:
                    print(i, j, k)
                    __import__(f'{i}_{j}_{k}_sour')


def run_rouge():
    directory = os.path.join(os.path.dirname(__file__))
    for i in range(4, 7):
        for j in range(3):
            for k in range(3):
                if not (i, j, k) in EXCLUDES_CODE_1 + NO_COMPILE + ERROR_2:
                    p_1 = os.path.join(directory, f'{i}_{j}_{k}_text_1.txt')
                    p_2 = os.path.join(directory, f'{i}_{j}_{k}_text_2.txt')
                    with open(p_1) as f:
                        text_1 = f.read()
                    with open(p_2) as f:
                        text_2 = f.read()

                    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
                    score = scorer.score(text_1, text_2)
                    df = pd.read_csv(os.path.join(directory, "result_rouge.csv"))
                    s1 = score['rouge1']
                    sL = score['rougeL']
                    df.loc[len(df.index)] = [s1.precision, s1.recall, s1.fmeasure, sL.precision, sL.recall, sL.fmeasure, i,j,k]
                    df.to_csv(os.path.join(directory, "result_rouge.csv"), index=False)


run_rouge()
