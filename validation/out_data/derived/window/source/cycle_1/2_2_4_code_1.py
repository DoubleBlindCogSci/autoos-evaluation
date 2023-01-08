from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bxuppq = Factor("bxuppq", ["aeztdd","dfmej","qghegk","frl","xbd"])
ckg = Factor("ckg", ["eedo","hchmj","wgjcl","rjmyxh","ykcly"])
def vtlhke(bxuppq, ckg):
    return bxuppq[0] == "frl" and ckg[-3] == "eedo"
def ewcw(bxuppq,ckg):
    return bxuppq[0] != "frl" or not (ckg[-3] == "eedo")
fozwx = DerivedLevel("amfn", Window(vtlhke, [bxuppq, ckg],4,1))
dlebs = DerivedLevel("jyet", Window(ewcw, [bxuppq, ckg],4,1))
djkz = Factor("cal", [fozwx, dlebs])

### EXPERIMENT
design=[bxuppq,ckg,djkz]
crossing=[djkz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END