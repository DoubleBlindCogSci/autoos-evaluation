from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uaijwz= Factor("uaijwz", ["ekn","fzqg","szbai","pfoq","glg"])
def is_lnauvj_oueuq(uaijwz):
    return uaijwz[0] == "glg" or uaijwz[-1] == "pfoq"
def is_lnauvj_mriz(uaijwz):
    return not is_lnauvj_oueuq(uaijwz)
lnauvj= Factor("lnauvj", [DerivedLevel("oueuq", Transition(is_lnauvj_oueuq, [uaijwz])), DerivedLevel("mriz", Transition(is_lnauvj_mriz, [uaijwz]))])

design=[uaijwz,lnauvj]
crossing=[lnauvj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END
