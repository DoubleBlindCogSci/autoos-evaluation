import os
import pandas as pd
from rouge_score import rouge_scorer

### random code was not compileable (exclude without mention):
EXCLUDES_CODE_1 = []

### NO_COMPILE
NO_COMPILE = []

preamble = ["from sourpea.primitives import *", "from sourpea.util import *", "import pandas as pd", "import os", "_dir=os.path.dirname(__file__)"]


def create_sour_2():
    directory = os.path.join(os.path.dirname(__file__))
    for file in os.listdir(directory):
        nr = file[:3]
        appendix = [f"sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/{nr}_0.csv'))",
                    f"sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/{nr}_0.csv'))",
                    "p_code_1 = 0", "p_code_2 = 0"]
        if file.endswith('code_2_corrected.py'):

            with open(file, 'r') as f:
                lines = f.read().splitlines()
                for line in lines:
                    if line.startswith('crossing = '):
                        crossing_list_txt = line[11:].split('],')
                        for c in crossing_list_txt:
                            formatted = c.replace('[', '').replace(']', '')
                            appendix.append(f"crossing = [{formatted}]")
                            appendix.append("block = Block(design, crossing, [])")
                            appendix.append('p_code_1 += block.test(sequence_code_1)["pValue"] >= 1')
                            appendix.append('p_code_2 += block.test(sequence_code_2)["pValue"] >= 1')
            appendix.append('df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))')
            appendix.append('df.loc[len(df.index)] = [p_code_1, p_code_2]')
            appendix.append('df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)')
            text_lines = preamble + lines[2:-6] + appendix
            text = ''
            for l in text_lines:
                text += l + '\n'
            with open(f'{file[:3]}_sour_2.py', 'w') as f_2:
                f_2.write(text)


def create_sour():
    directory = os.path.join(os.path.dirname(__file__))
    for file in os.listdir(directory):
        nr = file[:3]
        appendix = [f"sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/{nr}_0.csv'))",
                    f"sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/{nr}_0.csv'))",
                    "p_code_1 = 0", "p_code_2 = 0"]
        if file.endswith('code_1_corrected.py'):
            with open(file, 'r') as f:
                lines = f.read().splitlines()
                nr_factors = 0
                nr_crossings = 0
                for line in lines:
                    if line.startswith('crossing = '):
                        crossing_list_txt = line[11:].split('],')
                        for c in crossing_list_txt:
                            formatted = c.replace('[', '').replace(']', '')
                            if formatted:
                                nr_crossings += 1
                                nr_factors += len(formatted.split(','))
                                appendix.append(f"crossing = [{formatted}]")
                                appendix.append("block = Block(design, crossing, [])")
                                appendix.append('p_code_1 += block.test(sequence_code_1)["pValue"] >= 1')
                                appendix.append('p_code_2 += block.test(sequence_code_2)["pValue"] >= 1')
            appendix.append(f'nr_crossings = {nr_crossings}')
            appendix.append(f'nr_factors = {nr_factors}')
            appendix.append('df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))')
            appendix.append('df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]')
            appendix.append('df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)')
            text_lines = preamble + lines[2:-6] + appendix
            text = ''
            for l in text_lines:
                text += l + '\n'
            with open(f'{file[:3]}_sour.py', 'w') as f_2:
                f_2.write(text)



create_sour_2()
create_sour()

