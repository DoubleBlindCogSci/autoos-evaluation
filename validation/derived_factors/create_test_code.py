from generate_functions import generate_code_within, generate_code_transition, generate_code_window
from autoos.text_processing_sweet_pea import get_factors_from_code_as_list
import os
from validation.string_constants import *

def main():
    for l in range(5):
        for i in range(2, 4):
            for j in range(1, 3):
                write_code(generate_code_within, i, j, 'within', f'{i}_{j}_{l}')
                write_code(generate_code_transition, i, j, 'transition', f'{i}_{j}_{l}')
                write_code(generate_code_window, i, j , 'window', f'{i}_{j}_{l}')

def write_code(generator_function, output_level_count, input_factor_count, dir, filename):
    _dir = os.path.dirname(__file__)
    path_code_1 = os.path.join(_dir, f'{dir}/{filename}_code_1.py')
    path_sour = os.path.join(_dir, f'{dir}/{filename}_sour.py')
    preamble_code_1 = PREAMBLE_SWEET
    preamble_sour = PREAMBLE_SOUR
    out = '### DERIVED FACTORS\n'
    out += generator_function(output_level_count, input_factor_count)
    out += '\n### EXPERIMENT\n'
    factors = get_factors_from_code_as_list(out)
    factors = [f[0] for f in factors]
    f_str = '[' + ','.join(factors) + ']'
    out += f'design={f_str}\n'
    out += f'crossing=[{factors[-1]}]\n'
    out += '### APPENDIX\n'
    out_code_1 = preamble_code_1 + out + 'block=CrossBlock(design,crossing,[])\n'
    out_code_1 += 'experiment=synthesize_trials(block,1)\n'
    out_code_1 += f'save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/{filename}"))\n'
    out_code_1 += f'### END'
    out_sour = preamble_sour + out + 'block=Block(design,crossing,[])\n'
    out_sour += f'sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/{filename}_0.csv"))\n'
    out_sour += f'nr_input_factors={input_factor_count}\n'
    out_sour += f'nr_output_levels={output_level_count}\n'
    out_sour += 'test_code_1=block.test(sequence_code_1)\n'
    out_sour += 'try:\n'
    out_sour += f'\tsequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/{filename}_0.csv"))\n'
    out_sour += '\ttest_code_2=block.test(sequence_code_2)\n'
    out_sour += 'except:\n'
    out_sour += '\ttest_code_2={"pValue":0}\n'
    out_sour += 'df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))\n'
    out_sour += 'df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]\n'
    out_sour += 'df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)'
    with open(path_code_1, 'w') as f:
        f.write(out_code_1)
    with open(path_sour, 'w') as f:
        f.write(out_sour)

if __name__ == "__main__":
    main()
