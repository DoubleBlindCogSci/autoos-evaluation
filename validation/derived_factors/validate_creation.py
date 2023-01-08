from autoos.translate import translate
from autoos.extract import extract
from autoos.text_processing_sweet_pea import get_factors_from_code_as_list, get_factors_from_code_as_list_of_lines
from autoos.post_processing import correct_variable_declarations
import os
import time

_dir = os.path.dirname(__file__)

with open(os.path.join(_dir, '../prompts/derived_code.txt')) as f:
    train_prompt_derived_text = f.read()
with open(os.path.join(_dir, '../prompts/derived_text.txt')) as f:
    train_prompt_derived_code = f.read()


def main():
    for l in range(5):
        for i in range(2, 4):
            for j in range(1, 3):
                create_text1_code2_text2_regular(f'transition/{i}_{j}_{l}_code_1.py')
                create_text1_code2_text2_regular(f'within/{i}_{j}_{l}_code_1.py')
                create_text1_code2_text2_regular(f'window/{i}_{j}_{l}_code_1.py')


def create_text1_code2_text2_regular(path):
    with open(path) as file:
        full_text = file.read()
    to_translate = extract(full_text, '### DERIVED FACTORS', '###')
    appendix = extract(full_text, '### APPENDIX', '###')
    print('Translating code_1 to text_1')
    if not os.path.exists(f'{path[:-9]}text_1.txt'):
        text_1 = translate(to_translate, train_prompt_derived_text, response_length=500)
        with open(f'{path[:-9]}text_1.txt', 'w') as file:
            file.write(text_1)
        time.sleep(20)
    else:
        with open(f'{path[:-9]}text_1.txt') as file:
            text_1 = file.read()
    print('Translating text_1 to code_2')
    if not os.path.exists(f'{path[:-9]}code_2.py'):
        factor_lines = get_factors_from_code_as_list_of_lines(to_translate)
        code_2 = ''
        for l in factor_lines[:-1]:
            code_2 += l + '\n'
        code_2 += translate(text_1, train_prompt_derived_code, response_length=500)
        factors = get_factors_from_code_as_list(code_2)
        factors = [f[0] for f in factors]
        f_str = '[' + ','.join(factors) + ']'
        t_design = f'design={f_str}\n'
        t_crossing = f'crossing=[{factors[-1]}]\n'
        with open(f'{path[:-9]}code_2.py', 'w') as file:
            appendix = appendix.replace('out_code_1/', 'out_code_2/')
            code_2_full = f'from sweetpea import *\nimport os\n_dir=os.path.dirname(__file__)\n### REGULAR FACTORS\n{code_2}\n{t_design + t_crossing}\n### APPENDIX\n{appendix}\n### END'
            file.write(code_2_full)
        time.sleep(20)
    else:
        with open(f'{path[:-9]}code_2.py') as file:
            code_2 = file.read()
    print('Translating code_2 to text_2')
    if not os.path.exists(f'{path[:-9]}text_2.txt'):
        text_2 = translate(code_2, train_prompt_derived_text, response_length=500)
        time.sleep(20)
        with open(f'{path[:-9]}text_2.txt', 'w') as file:
            file.write(text_2)


if __name__ == '__main__':
    main()
