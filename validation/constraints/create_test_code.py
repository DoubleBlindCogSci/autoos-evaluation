import os
import random
import string

from validation.string_constants import *

CONSTRAINTS = ['ExactlyK', 'AtMostKInARow', 'AtLeastKInARow', 'ExactlyKInARow', 'Exclude', 'MinimumTrials']

K_CONSTRAINTS = ['ExactlyK', 'AtMostKInARow', 'AtLeastKInARow', 'ExactlyKInARow']


def main():
    for l in range(5):
        for i in range(1, 4):
            write_code(i, f'{i}_{l}')


def write_code(nr_constraints, filename):
    _dir = os.path.dirname(__file__)
    path_code_1 = os.path.join(_dir, f'test_set/{filename}_code_1.py')
    path_sour = os.path.join(_dir, f'test_set/{filename}_sour.py')
    preamble_code_1 = PREAMBLE_SWEET
    preamble_sour = PREAMBLE_SOUR
    out = '### REGULAR FACTORS\n'
    factors = []
    factors_names = []
    factors_names_2 = []
    constraints = []
    for i in range(1, nr_constraints + 1):
        constraints_r = random.sample(CONSTRAINTS, k=i)
    for c in constraints_r:
        f = _rand_name()
        l = _rand_name()
        factors_names.append(f)
        factors.append(
            f'{f} = Factor("{f}", [{",".join([_rand_name_() for _ in range(random.randint(1, 3))])}, "{l}"])')
        if c in K_CONSTRAINTS:
            constraints.append(f'{c}({random.randint(2, 4)},({f},"{l}"))')
        elif c == 'Exclude':
            constraints.append(f'{c}(({f},"{l}"))')
        elif c == 'MinimumTrials':
            constraints.append(f'{c}({random.randint(10, 50)})')
    for i in range(random.randint(1, 3)):
        f = _rand_name()
        l = _rand_name()
        factors_names_2.append(f)
        factors.append(
            f'{f} = Factor("{f}", [{",".join([_rand_name_() for _ in range(random.randint(1, 3))])}, "{l}"])')
    for f in factors:
        out += f'{f}\n'
    out += '\n### EXPERIMENT\n'
    c_str = '[' + ','.join(constraints) + ']'
    out += f'constraints={c_str}\n'
    f_str = '[' + ','.join(factors_names+factors_names_2) + ']'
    f_str_2 = '[' + ','.join(factors_names_2) + ']'
    out += f'design={f_str}\n'
    out += f'crossing={f_str_2}\n'
    out += '### APPENDIX\n'
    out_code_1 = preamble_code_1 + out + 'block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)\n'
    out_code_1 += 'experiment=synthesize_trials(block,1)\n'
    out_code_1 += f'save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/{filename}"))\n'
    out_code_1 += f'### END'
    out_sour = preamble_sour + out + 'block=Block(design,crossing,constraints)\n'
    out_sour += f'sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/{filename}_0.csv"))\n'
    out_sour += f'nr_constraints={nr_constraints}\n'
    out_sour += 'test_code_1=block.test(sequence_code_1)\n'
    out_sour += 'try:\n'
    out_sour += f'\tsequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/{filename}_0.csv"))\n'
    out_sour += '\ttest_code_2=block.test(sequence_code_2)\n'
    out_sour += 'except:\n'
    out_sour += '\ttest_code_2={"pValue":0}\n'
    out_sour += 'df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))\n'
    out_sour += 'df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]\n'
    out_sour += 'df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)'
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
