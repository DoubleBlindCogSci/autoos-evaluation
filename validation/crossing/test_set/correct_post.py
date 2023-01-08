import os
import pandas as pd
from rouge_score import rouge_scorer


def correct_multi_block():
    directory = os.path.join(os.path.dirname(__file__))
    for file in os.listdir(directory):
        if file.endswith('code_2.py'):
            with open(file, 'r') as f:
                out = f.read()
                out = out.replace('MultiCrossBlock', 'CrossBlock')
                with open(file, 'w') as fi:
                    fi.write(out)

def correct_sour():
    directory = os.path.join(os.path.dirname(__file__))
    for file in os.listdir(directory):
        if file.endswith('sour.py'):
            out = []
            with open(file, 'r') as f:
                i = 0
                lines = f.read().splitlines()
                while i < len(lines):
                    if lines[i].startswith('crossing') and '[' not in lines[i]:
                        i += 4
                    else:
                        out.append(lines[i])
                        i += 1
            with open(f'{file[:-3]}_.py', 'w') as f:
                for o in out:
                    f.write(f'{o}\n')


correct_sour()
