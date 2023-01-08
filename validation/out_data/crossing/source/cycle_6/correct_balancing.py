import os
import pandas as pd
from rouge_score import rouge_scorer

### random code was not compileable (exclude without mention):
EXCLUDES_CODE_1 = []

### NO_COMPILE
NO_COMPILE = []

preamble = ["from sourpea.primitives import *", "from sourpea.util import *", "import pandas as pd", "import os", "_dir=os.path.dirname(__file__)"]


def create_corrected():
    directory = os.path.join(os.path.dirname(__file__))
    for file in os.listdir(directory):
        if file.endswith('code_2.py') or file.endswith('code_1.py'):
            out = ''
            with open(file, 'r') as f:
                lines = f.read().splitlines()
                for line in lines:
                    crossing_list_txt = []
                    formatted_list = []
                    if line.startswith('crossing = '):
                        crossing_list_txt = line[11:].split('],')
                    if line.startswith('crossing='):
                        crossing_list_txt = line[9:].split(']')
                    if line.startswith('crossing = ') or line.startswith('crossing='):
                        for c in crossing_list_txt:
                            formatted = c.replace('[', '').replace(']', '')
                            formatted_list.append(formatted)
                        formatted_list_sorted = list(sorted(formatted_list, key=len))
                        formatted_list_sorted.reverse()
                        new_line = 'crossing = ['
                        for f in formatted_list_sorted:
                            if f and f != ',':
                                if f[0] == ',':
                                    f = f[1:]
                                new_line += f'[{f}],'
                        out += f'{new_line}]\n'
                    else:
                        out += f'{line}\n'
            out = out.replace(' CrossBlock', ' MultiCrossBlock')
            out = out.replace('=CrossBlock', '=MultiCrossBlock')
            out = out.replace("experiment=synthesize_trials(block,1)","experiment=synthesize_trials(block,1,IterateGen)")
            with open(f'{file[:-3]}_corrected.py', 'w') as f:
                f.write(out)

def correct_sour():
    directory = os.path.join(os.path.dirname(__file__))
    for file in os.listdir(directory):
        if file.endswith('sour.py') or file.endswith('sour_2.py'):
            out = ''
            with open(file, 'w+') as f:
                out = f.read()
                out = out.replace('uncorrected/', '')
                f.write(out)


def check_balancing():
    directory = os.path.join(os.path.dirname(__file__))
    for l in range(4):
        for i in range(1, 7):
            p_1 = os.path.join(directory, f'{i}_{l}_code_1_corrected.py')
            p_2 = os.path.join(directory, f'{i}_{l}_code_2_corrected.py')
            code_1 = []
            code_1_c_text = ''
            code_2 = []
            code_2_c_text = ''
            nr_crossings = 0
            with open(p_1) as f:
                code_1 = f.read().splitlines()
            with open(p_2) as f:
                code_2 = f.read().splitlines()
            for c_1 in code_1:
                if c_1.startswith('crossing = '):
                    code_1_c_text = c_1[11:]
                    code_1_c_text = code_1_c_text.replace(' ','')
                    nr_crossings = len([i for i in code_1_c_text if i == '[']) - 1
                    nr_factors = len([i for i in code_1_c_text if i == ','])
            for c_2 in code_2:
                if c_2.startswith('crossing = '):
                    code_2_c_text = c_2[11:]
                    code_2_c_text = code_2_c_text.replace(' ', '')
            with open('result_sour.csv', 'a') as f:
                f.write(f'\n{code_1_c_text},{code_2_c_text},{code_1_c_text == code_2_c_text},{nr_crossings},{nr_factors}')





create_corrected()
check_balancing()

