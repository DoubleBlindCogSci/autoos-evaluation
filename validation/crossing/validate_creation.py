from autoos.translate import translate
from autoos.extract import extract
from autoos.text_processing_sweet_pea import get_factors_from_code_as_list, get_factors_from_code_as_list_of_lines
import os
import time

_dir = os.path.dirname(__file__)

with open(os.path.join(_dir, '../prompts/design_code.txt')) as f:
    train_prompt_text = f.read()
with open(os.path.join(_dir, '../prompts/design_text.txt')) as f:
    train_prompt_code = f.read()


def main():
    for l in range(8):
        for i in range(1, 8):
            create_text1_code2_text2(f'test_set/{i}_{l}_code_1.py')


def create_text1_code2_text2(path):
    with open(path) as file:
        full_text = file.read()
    regular = extract(full_text, '### REGULAR FACTORS', '###')
    crossing = extract(full_text, '### EXPERIMENT', '###')
    appendix = extract(full_text, '### APPENDIX', '###')
    to_translate = regular + crossing + 'block=MultiCrossBlock(design, crossing, [])'
    print('Translating code_1 to text_1')
    if not os.path.exists(f'{path[:-9]}text_1.txt'):
        text_1 = translate(to_translate, train_prompt_text, response_length=300)
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
        for l in factor_lines:
            code_2 += l + '\n'
        code_2 += translate(text_1, train_prompt_code, response_length=500)
        code_2 += '\n'
        with open(f'{path[:-9]}code_2.py', 'w') as file:
            appendix = appendix.replace('out_code_1/', 'out_code_2/')
            factors = get_factors_from_code_as_list(code_2)
            variable_list_factors = ','.join([fac[0] for fac in factors])
            f_design = f'design=[{variable_list_factors}]'
            code_2_full = f'from sweetpea import *\nimport os\n_dir=os.path.dirname(__file__)\n{code_2}\n{f_design}\n### APPENDIX\n{appendix}\n### END'
            file.write(code_2_full)
        time.sleep(20)
    else:
        with open(f'{path[:-9]}code_2.py') as file:
            code_2 = file.read()
    print('Translating code_2 to text_2')
    if not os.path.exists(f'{path[:-9]}text_2.txt'):
        text_2 = translate(code_2, train_prompt_text, response_length=300)
        time.sleep(20)
        with open(f'{path[:-9]}text_2.txt', 'w') as file:
            file.write(text_2)


if __name__ == '__main__':
    main()
