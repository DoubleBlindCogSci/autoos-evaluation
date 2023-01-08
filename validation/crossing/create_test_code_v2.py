import os
import random
import string

from validation.string_constants import *


def main():
    for l in range(8):
        for i in range(1,8):
            write_code(i, f'{i}_{l}')


def write_code(nr_factors, filename):
    _dir = os.path.dirname(__file__)
    path_code_1 = os.path.join(_dir, f'test_set/{filename}_code_1.py')
    path_sour = os.path.join(_dir, f'test_set/{filename}_sour.py')
    preamble_code_1 = PREAMBLE_SWEET
    preamble_sour = PREAMBLE_SOUR
    out = '### REGULAR FACTORS\n'
    crossings = []
    factor_names = []
    for i in range(0, nr_factors):
        f_name = _rand_name()
        factor_names.append(f_name)
        out += f'{f_name} = Factor("{f_name}", ["{_rand_name()}", "{_rand_name()}"])\n'
        crossings.append(f_name)
    crossing_str = '[' + ','.join(crossings) + ']'
    crossings.append(crossing_str)
    out += '\n### EXPERIMENT\n'
    f_str = ','.join(factor_names)
    out += f'design=[{f_str}]\n'
    out_1 = f'crossing=[{crossing_str}]\n'
    out_1 += '### APPENDIX\n'
    out_code_1 = preamble_code_1 + out + out_1 + 'block=MultiCrossBlock(design,crossing,[])\n'
    out_code_1 += 'experiment=synthesize_trials(block,1)\n'
    out_code_1 += f'save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/{filename}"))\n'
    out_code_1 += f'### END'
    out_sour = preamble_sour + out
    out_sour += f'sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/{filename}_0.csv"))\n'
    out_sour += f'sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/{filename}_0.csv"))\n'
    out_sour += f'nr_crossings = 1\n'
    out_sour += f'nr_factors={nr_factors}\n'
    out_sour += f'p_code_1 = 0\n'
    out_sour += f'p_code_2 = 0\n'
    for i in range(len(crossings)):
        out_sour += f'crossing = {crossings[i]}\n'
        out_sour += f'block = Block(design,crossing,[])\n'
        out_sour += 'p_code_1 += block.test(sequence_code_1)["pValue"] >= 1\n'
        out_sour += 'p_code_2 += block.test(sequence_code_2)["pValue"] >= 1\n'
    out_sour += 'df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))\n'
    out_sour += 'df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]\n'
    out_sour += 'df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)\n'
    with open(path_code_1, 'w') as f:
        f.write(out_code_1)
    with open(path_sour, 'w') as f:
        f.write(out_sour)


def _rand_name():
    return ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))


def _rand_name_():
    return '"' + ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 6))) + '"'


if __name__ == "__main__":
    main()
