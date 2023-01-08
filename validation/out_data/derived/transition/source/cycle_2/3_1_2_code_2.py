from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mes= Factor("mes", ["vvmbzw","hbj","uhi","cuetl","cvk","fgar","hilp"])
def is_hrsqjf_hvrwc(mes):
    return mes[-1] == "hbj" and mes[0] != "fgar"
def is_hrsqjf_fhi(mes):
    return mes[-1] == "hbj" and mes[0] == "fgar"
def is_hrsqjf_oxtbkp(mes):
    return not (is_hrsqjf_hvrwc(mes) or is_hrsqjf_fhi(mes))
hrsqjf= Factor("hrsqjf", [DerivedLevel("hvrwc", Transition(is_hrsqjf_hvrwc, [mes])), DerivedLevel("fhi", Transition(is_hrsqjf_fhi, [mes])), DerivedLevel("oxtbkp", Transition(is_hrsqjf_oxtbkp, [mes]))])

design=[mes,hrsqjf]
crossing=[hrsqjf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END
