from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
esi= Factor("esi", ["pnoy","hfmto","izzlv","usgm","trrvms","onuueg","gofjiv"])

def is_eefept_bqgjor(esi):
    return esi != "gofjiv" and esi == "trrvms"
def is_eefept_myep(esi):
    return not is_eefept_bqgjor(esi)
eefept= Factor("eefept", [DerivedLevel("bqgjor", WithinTrial(is_eefept_bqgjor, [esi])), DerivedLevel("myep", WithinTrial(is_eefept_myep, [esi]))])


design=[esi,eefept]
crossing=[eefept]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
