import string
import random
import os


def main():
    for l in range(2):
        for i in range(2, 11):
            for j in range(1, 5):
                write_code_regular(i, j, f'{i}_{j}_{l}')



def write_code_regular(n_levels, n_factors, filename):
    _dir = os.path.dirname(__file__)
    path_code_1 = os.path.join(_dir, f'test_set/{filename}_code_1.py')
    path_sour = os.path.join(_dir, f'test_set/{filename}_sour.py')
    factors = []
    preamble_code_1 = 'from sweetpea import *\nimport os\n_dir=os.path.dirname(__file__)\n'
    preamble_sour = 'from sourpea.primitives import *\n'
    preamble_sour += 'from sourpea.util import *\n'
    preamble_sour += 'import pandas as pd\nimport os\n_dir=os.path.dirname(__file__)\n'
    out = '### REGULAR FACTORS\n'
    for _ in range(n_factors):
        code, _, _, f = get_factor(n_levels)
        factors.append(f)
        out += code
        out += '\n'
    out += '\n### EXPERIMENT\n'
    f_str = '[' + ','.join(factors) + ']'
    out += f'design={f_str}\n'
    out += f'crossing={f_str}\n'
    out += '### APPENDIX\n'
    out_code_1 = preamble_code_1 + out + 'block=CrossBlock(design,crossing,[])\n'
    out_code_1 += 'experiment=synthesize_trials(block,1)\n'
    out_code_1 += f'save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/{filename}"))\n'
    out_code_1 += f'### END'
    out_sour = preamble_sour + out + 'block=Block(design,crossing,[])\n'
    out_sour += f'sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/{filename}_0.csv"))\n'
    out_sour += f'nr_factors={n_factors}\n'
    out_sour += f'nr_levels={n_levels}\n'
    out_sour += 'test_code_1=block.test(sequence_code_1)\n'
    out_sour += 'try:\n'
    out_sour += f'\tsequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/{filename}_0.csv"))\n'
    out_sour += '\ttest_code_2=block.test(sequence_code_2)\n'
    out_sour += 'except:\n'
    out_sour += '\ttest_code_2={"pValue":0}\n'
    out_sour += 'df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))\n'
    out_sour += 'df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]\n'
    out_sour += 'df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)'
    with open(path_code_1, 'w') as f:
        f.write(out_code_1)
    with open(path_sour, 'w') as f:
        f.write(out_sour)


def get_factor(n):
    outside_declaration_chance = .3
    outside_levels = []
    o = 0
    s = ''
    levels = []
    for i in range(n):
        if random.random() < outside_declaration_chance * .2:
            if random.random() < .7:
                l_n = _get_random_python_name()
                l = _get_level()
                levels.append((l[1], l[2]))
                s += f'{l_n}={l[0]}\n'
                outside_levels.append(l_n)
            else:
                l_n = _get_random_python_name()
                l = _get_level()
                index = random.randint(0, 4)
                tail = random.randint(0, 4)
                lst = '['+','.join([_get_level()[0] for _ in range(index)] + [l[0]] + [_get_level()[0] for _ in range(tail)]) + ']'
                levels.append((l[1], l[2]))
                outside_levels.append(f'{l_n}[{index}]')
                s += f'{l_n}={lst}\n'

    _lst = [_get_level() for _ in range(n - o)]
    levels.append([(l[1], l[2]) for l in _lst])
    lst = [l[0] for l in _lst] + outside_levels
    random.shuffle(lst)
    _levels = ','.join(lst)
    factor_name = _get_factor_name()
    if random.random() < outside_declaration_chance:
        list_name = _get_random_python_name()
        factor_py_name = _get_random_python_name()
        return s + f'{list_name}=[{_levels}]\n{factor_py_name}=Factor({factor_name},{list_name})', factor_name, levels, factor_py_name
    factor_py_name = _get_random_python_name()
    return s + f'{factor_py_name}=Factor({factor_name},[{_levels}])', factor_name, levels, factor_py_name


def _get_factor_name():
    single_quotation_change = .5
    quotation = '"'
    if random.random() < single_quotation_change:
        quotation = "'"
    return f'{quotation}{_get_random_name()}{quotation}'


def _get_level():
    weight_chance = .1
    single_quotation_change = .5
    quotation = '"'
    level_name = _get_random_name()
    if random.random() < single_quotation_change:
        quotation = "'"
    if random.random() < weight_chance:
        weight = 1 #random.randint(1, 4)
        return f'Level({quotation}{level_name}{quotation},{weight})', level_name, weight
    else:
        return f'{quotation}{level_name}{quotation}', level_name, 1


def _get_random_whitespace():
    whitespace_chance = .3
    start = ''
    while random.randint() < whitespace_chance:
        start += ' '
    return start


def _get_random_name():
    length = random.randint(3, 14)
    choose_string = 4 * string.ascii_letters + string.digits + '~!@#$%^&*()_{}:[];<>?|' + 2 * ' '
    choose_string = choose_string.replace("'", "")
    choose_string = choose_string.replace('"', "")
    return ''.join(random.choices(choose_string, k=length))


def _get_random_python_name():
    length = random.randint(3, 10)
    start = random.choice(string.ascii_letters + '_')
    tail = random.choices(string.ascii_letters + string.digits + '_', k=length)
    return start + ''.join(tail)


if __name__ == '__main__':
    main()
