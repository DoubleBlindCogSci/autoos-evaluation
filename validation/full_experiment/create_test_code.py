import os
import random
import string

from validation.string_constants import *

CONSTRAINTS = ['AtMostKInARow', 'AtLeastKInARow', 'ExactlyKInARow', 'MinimumTrials']


def main():
    for i in range(4, 7):
        for j in range(3):
            for k in range(3):
                write_code(i, j, k, f'{i}_{j}_{k}')


def write_code(nr_regular, nr_derived, nr_constraints, filename):
    _dir = os.path.dirname(__file__)
    path_code_1 = os.path.join(_dir, f'test_set/{filename}_code_1.py')
    path_sour = os.path.join(_dir, f'test_set/{filename}_sour.py')
    preamble_code_1 = PREAMBLE_SWEET
    preamble_sour = PREAMBLE_SOUR
    factor_names_r = []
    factor_names_d = []
    out = '### START\n'
    level_i_1 = [_rand_name(), _rand_name()]
    level_i_2 = [_rand_name(), _rand_name()]
    for i in range(nr_regular):
        f_name = _rand_name()
        factor_names_r.append(f_name)
        if i < 4 and i % 2:
            out += f'{f_name} = Factor("{f_name}", ["{level_i_1[0]}", "{level_i_1[1]}"])\n'
        elif i < 4 and not i % 2:
            out += f'{f_name} = Factor("{f_name}", ["{level_i_2[0]}", "{level_i_2[1]}"])\n'
        else:
            out += f'{f_name} = Factor("{f_name}", ["{_rand_name()}", "{_rand_name()}"])\n'
    factor_for_derived = random.sample(factor_names_r, 4)
    for i in range(nr_derived):
        fct_name = _rand_name()
        fct_name_2 = _rand_name()
        out += f'def {fct_name} ({factor_for_derived[i]}, {factor_for_derived[i + 2]}):\n'
        out += f'    return {factor_for_derived[i]} == {factor_for_derived[i + 2]}\n'
        out += f'def {fct_name_2} ({factor_for_derived[i]}, {factor_for_derived[i + 2]}):\n'
        out += f'    return not {fct_name}({factor_for_derived[i]}, {factor_for_derived[i + 2]})\n'
        f_name = _rand_name()
        factor_names_d.append(f_name)
        out += f'{f_name} = Factor("{f_name}", [' \
               f'DerivedLevel("{_rand_name()}", WithinTrial({fct_name}, [{factor_for_derived[i]}, {factor_for_derived[i + 2]}])), ' \
               f'DerivedLevel("{_rand_name()}", WithinTrial({fct_name_2}, [{factor_for_derived[i]}, {factor_for_derived[i + 2]}]))])\n'
    constraints_sample = random.sample(CONSTRAINTS, 2)
    constraints = []
    for c in constraints_sample:
        if c != 'MinimumTrials':
            constraints.append(f'{c}({random.randint(2, 4)}, {random.choice(factor_names_r + factor_names_d)})')
        else:
            constraints.append(f'{c}({random.randint(10, 60)})')
    f_str = ','.join(factor_names_d + factor_names_r)
    c_str = ','.join(constraints[:nr_constraints])
    out += f'design=[{f_str}]\n'
    out += f'constraints=[{c_str}]\n'
    c_names = random.sample(factor_names_r + factor_names_d, 2)
    out_1 = f'crossing=[{",".join(c_names)}]\n'


    out_code_1 = preamble_code_1 + out + out_1 + 'block=CrossBlock(design,crossing,constraints)\n### END\n'
    out_code_1 += 'experiment=synthesize_trials(block,1)\n'
    out_code_1 += f'save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/{filename}"))\n'
    out_sour = preamble_sour + out + out_1
    out_sour += f'sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/{filename}_0.csv"))\n'
    out_sour += f'sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/{filename}_0.csv"))\n'
    out_sour += f'nr_regular={nr_regular}\n'
    out_sour += f'nr_derived={nr_derived}\n'
    out_sour += f'nr_constraints={nr_constraints}\n'
    out_sour += f'block = Block(design,crossing,constraints)\n'
    out_sour += f'test_1 = block.test(sequence_code_1)\n'
    out_sour += f'test_2 = block.test(sequence_code_2)\n'
    out_sour += 'df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))\n'
    out_sour += 'df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], ' \
                'test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],' \
                'nr_regular, nr_derived, nr_constraints]\n'
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
