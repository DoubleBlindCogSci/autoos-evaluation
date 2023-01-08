from autoos.translate import translate
from autoos.extract import extract, extract_all
from autoos.text_processing_sweet_pea import get_factors_from_code_as_list, get_factors_from_code_as_list_of_lines
import os
import time

_dir = os.path.dirname(__file__)

with open(os.path.join(_dir, '../prompts/format_code.txt')) as f:
    prompt_format_code = f.read()
with open(os.path.join(_dir, '../prompts/format_text.txt')) as f:
    prompt_format_text = f.read()

with open(os.path.join(_dir, '../prompts/regular_code.txt')) as f:
    prompt_regular_text = f.read()
with open(os.path.join(_dir, '../prompts/regular_text.txt')) as f:
    prompt_regular_code = f.read()

with open(os.path.join(_dir, '../prompts/derived_code.txt')) as f:
    prompt_derived_text = f.read()
with open(os.path.join(_dir, '../prompts/derived_text.txt')) as f:
    prompt_derived_code = f.read()

with open(os.path.join(_dir, '../prompts/design_code.txt')) as f:
    prompt_design_text = f.read()
with open(os.path.join(_dir, '../prompts/design_text.txt')) as f:
    prompt_design_code = f.read()


def main():
    for i in range(4, 7):
        for j in range(3):
            for k in range(3):
                create_text1_code2_text2(f'test_set/{i}_{j}_{k}_code_1.py', i, j, k)


def create_text1_code2_text2(path, i, j, k):
    # CODE_1 TO TEXT_1

    with open(path) as file:
        full_text = file.read()
    to_translate = extract(full_text, '### START', '###')
    factor_lines = get_factors_from_code_as_list_of_lines(to_translate)
    preamble_factors = ''.join(factor_lines)

    print(f'To text 1: {path}')
    # Formatting
    print('Formatting code 1')
    if not os.path.exists(f'{path[:-9]}code_1_formatted.py'):
        code_1_formatted = translate(to_translate, prompt_format_code)
        with open(f'{path[:-9]}code_1_formatted.py', 'w') as file:
            file.write(code_1_formatted)
        time.sleep(20)
    else:
        with open(f'{path[:-9]}code_1_formatted.py') as file:
            code_1_formatted = file.read()

    # Regular factors
    print('Translating regular factors...')
    if not os.path.exists(f'{path[:-9]}text_1.txt'):
        section_regular_factors = extract(code_1_formatted, '### REGULAR FACTORS', '###')
        if section_regular_factors:
            text_1 = translate(section_regular_factors, prompt_regular_text)
        time.sleep(20)

    # Derived factors
    print('Translating derived factors...')
    if not os.path.exists(f'{path[:-9]}text_1.txt'):
        section_derived_factors = extract(code_1_formatted, '### DERIVED FACTORS', '###')
        if section_derived_factors:
            section_list = extract_all(section_derived_factors, '##')
            for s in section_list:
                print('Translating factor...')
                _tmp = preamble_factors + '\n' + s
                text_1 += translate(_tmp, prompt_derived_text, response_length=500)
                time.sleep(20)

    # Counterbalancing
    print('Translating counterbalancing...')
    if not os.path.exists(f'{path[:-9]}text_1.txt'):
        section_counterbalancing = extract(code_1_formatted, '### EXPERIMENT', '###')
        if section_counterbalancing:
            _tmp = preamble_factors + '\n' + section_counterbalancing
            text_1 += translate(_tmp, prompt_design_text, response_length=800)
            time.sleep(20)

    if not os.path.exists(f'{path[:-9]}text_1.txt'):
        with open(f'{path[:-9]}text_1.txt', 'w') as file:
            file.write(text_1)
    else:
        with open(f'{path[:-9]}text_1.txt') as file:
            text_1 = file.read()

    # TEXT_1 TO CODE_2

    print(f'To code 2: {path}')

    # Formatting
    print('Formatting text 1')
    if not os.path.exists(f'{path[:-9]}text_1_formatted.txt'):
        text_1_formatted = translate(text_1, prompt_format_text, response_length=1000)
        with open(f'{path[:-9]}text_1_formatted.txt', 'w') as file:
            file.write(text_1_formatted)
        time.sleep(20)
    else:
        with open(f'{path[:-9]}text_1_formatted.txt') as file:
            text_1_formatted = file.read()

    # Regular factors
    print('Translating regular factors...')
    if not os.path.exists(f'{path[:-9]}code_2.py'):
        section_regular_factors = extract(text_1_formatted, '### REGULAR FACTORS', '###')
        if section_regular_factors:
            code_2 = translate(section_regular_factors, prompt_regular_code)
        time.sleep(20)

    # Derived factors
    print('Translating derived factors...')
    if not os.path.exists(f'{path[:-9]}code_2.py'):
        section_derived_factors = extract(text_1_formatted, '### DERIVED FACTORS', '###')
        if section_derived_factors:
            section_list = extract_all(section_derived_factors, '##')
            for s in section_list:
                code_2 += translate(s, prompt_derived_code, response_length=500)
                time.sleep(20)

    # Counterbalancing
    print('Translating counterbalancing...')
    if not os.path.exists(f'{path[:-9]}code_2.py'):
        section_counterbalancing = extract(text_1_formatted, '### EXPERIMENT', '###')
        if section_counterbalancing:
            _tmp = preamble_factors + '\n' + section_counterbalancing
            code_2 += translate(_tmp, prompt_design_code, response_length=800)
            factors = get_factors_from_code_as_list(code_2)
            variable_list_factors = ','.join([fac[0] for fac in factors])
            code_2 += f'\ndesign=[{variable_list_factors}]'
            time.sleep(20)

    preamble_code_2 = 'from sweetpea import *\nimport os\n_dir = os.path.dirname(__file__)\n### START\n'
    appendix_code_2 = f'\nblock=CrossBlock(design,crossing,constraints)\n### END\n' \
                      f'experiment=synthesize_trials(block,1)\n' \
                      f'save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/{i}_{j}_{k}"))\n'



    if not os.path.exists(f'{path[:-9]}code_2.py'):
        code_2 = f'{preamble_code_2}{code_2}{appendix_code_2}'
        with open(f'{path[:-9]}code_2.py', 'w') as file:
            file.write(code_2)
    else:
        with open(f'{path[:-9]}code_2.py') as file:
            code_2 = file.read()

    # CODE 2 TO TEXT 2


    to_translate = extract(code_2, '### START', '###')
    factor_lines = get_factors_from_code_as_list_of_lines(to_translate)
    preamble_factors = ''.join(factor_lines)

    print(f'To text 2: {path}')
    # Formatting
    print('Formatting code 2')
    if not os.path.exists(f'{path[:-9]}code_2_formatted.py'):
        code_2_formatted = translate(to_translate, prompt_format_code)
        with open(f'{path[:-9]}code_2_formatted.py', 'w') as file:
            file.write(code_2_formatted)
        time.sleep(20)
    else:
        with open(f'{path[:-9]}code_2_formatted.py') as file:
            code_2_formatted = file.read()

    # Regular factors
    print('Translating regular factors...')
    if not os.path.exists(f'{path[:-9]}text_2.txt'):
        section_regular_factors = extract(code_2_formatted, '### REGULAR FACTORS', '###')
        if section_regular_factors:
            text_2 = translate(to_translate, prompt_regular_text)
        time.sleep(20)

    # Derived factors
    print('Translating derived factors...')
    if not os.path.exists(f'{path[:-9]}text_2.txt'):
        section_derived_factors = extract(code_2_formatted, '### DERIVED FACTORS', '###')
        if section_derived_factors:
            section_list = extract_all(section_derived_factors, '##')
            for s in section_list:
                print('Translating factor...')
                _tmp = preamble_factors + '\n' + s
                text_2 += translate(_tmp, prompt_derived_text, response_length=500)
                time.sleep(20)

    # Counterbalancing
    print('Translating counterbalancing...')
    if not os.path.exists(f'{path[:-9]}text_2.txt'):
        section_counterbalancing = extract(code_2_formatted, '### EXPERIMENT', '###')
        if section_counterbalancing:
            _tmp = preamble_factors + '\n' + section_counterbalancing
            text_2 += translate(_tmp, prompt_design_text, response_length=800)
            time.sleep(20)

    if not os.path.exists(f'{path[:-9]}text_2.txt'):
        with open(f'{path[:-9]}text_2.txt', 'w') as file:
            file.write(text_2)


if __name__ == '__main__':
    main()
