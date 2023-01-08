from autoos.translate import translate
from autoos.extract import extract
from autoos.text_processing_sweet_pea import get_factors_from_code_as_list
from autoos.post_processing import correct_variable_declarations
import os
import time

_dir = os.path.dirname(__file__)

with open(os.path.join(_dir, '../prompts/regular_code.txt')) as f:
    train_prompt_regular_text = f.read()
with open(os.path.join(_dir, '../prompts/regular_text.txt')) as f:
    train_prompt_regular_code = f.read()


def main():
    for l in range(2):
        for i in range(2, 11):
            for j in range(1, 5):
                create_text1_code2_text2_regular(f'test_set/{i}_{j}_{l}_code_1.py')


def create_text1_code2_text2_regular(path):
    with open(path) as file:
        full_text = file.read()
    to_translate = extract(full_text, '### REGULAR FACTORS', '###')
    appendix = extract(full_text, '### APPENDIX', '###')
    print('Translating code_1 to text_1')
    if not os.path.exists(f'{path[:-9]}text_1.txt'):
        text_1 = translate(to_translate, train_prompt_regular_text)
        with open(f'{path[:-9]}text_1.txt', 'w') as file:
            file.write(text_1)
        time.sleep(20)
    else:
        with open(f'{path[:-9]}text_1.txt') as file:
            text_1 = file.read()
    print('Translating text_1 to code_2')
    if not os.path.exists(f'{path[:-9]}code_2.py'):
        code_2 = translate(text_1, train_prompt_regular_code)
        factors = get_factors_from_code_as_list(code_2)
        variable_list_factors = ','.join([fac[0] for fac in factors])
        t_design = f'design=[{variable_list_factors}]\n'
        t_crossing = f'crossing=[{variable_list_factors}]\n'
        with open(f'{path[:-9]}code_2.py', 'w') as file:
            appendix = appendix.replace('out_code_1/', 'out_code_2/')
            code_2_full = f'from sweetpea import *\nimport os\n_dir=os.path.dirname(__file__)\n### REGULAR FACTORS\n{code_2}\n{t_design + t_crossing}\n### APPENDIX\n{appendix}\n### END'
            code_2_full = correct_variable_declarations(code_2_full)
            file.write(code_2_full)
        time.sleep(20)
    else:
        with open(f'{path[:-9]}code_2.py') as file:
            code_2 = file.read()
    print('Translating code_2 to text_2')
    if not os.path.exists(f'{path[:-9]}text_2.txt'):
        text_2 = translate(code_2, train_prompt_regular_text)
        time.sleep(20)
        with open(f'{path[:-9]}text_2.txt', 'w') as file:
            file.write(text_2)


if __name__ == '__main__':
    main()
