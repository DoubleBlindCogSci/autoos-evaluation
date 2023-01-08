from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uaijwz = Factor("uaijwz", ["ekn","fzqg","szbai","pfoq","glg"])
def szlq(uaijwz):
    return uaijwz[0] == "glg" or uaijwz[-1] == "pfoq"
def vjk(uaijwz):
    return uaijwz[0] != "glg" and uaijwz[-1] != "pfoq"
iragz = DerivedLevel("oueuq", Transition(szlq, [uaijwz]))
gki = DerivedLevel("mriz", Transition(vjk, [uaijwz]))
aku = Factor("lnauvj", [iragz, gki])

### EXPERIMENT
design=[uaijwz,aku]
crossing=[aku]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END