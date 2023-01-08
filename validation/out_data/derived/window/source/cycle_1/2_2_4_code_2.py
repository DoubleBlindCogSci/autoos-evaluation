from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bxuppq= Factor("bxuppq", ["aeztdd","dfmej","qghegk","frl","xbd"])
ckg= Factor("ckg", ["eedo","hchmj","wgjcl","rjmyxh","ykcly"])
def is_cal_amfn(bxuppq, ckg):
    return bxuppq[0] == "frl" and ckg[0] == "eedo"
def is_cal_jyet(bxuppq, ckg):
    return not is_cal_amfn(bxuppq, ckg)
cal= Factor("cal", [DerivedLevel("amfn", Window(is_cal_amfn, [bxuppq, ckg], 4, 1)), DerivedLevel("jyet", Window(is_cal_jyet, [bxuppq, ckg], 4, 1))])

design=[bxuppq,ckg,cal]
crossing=[cal]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END
