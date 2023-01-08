from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hxtk = Factor("hxtk", ["rnl","umdg","xoc","bdfo","jood","iqjrov"])
def rlcndh(hxtk):
     return "iqjrov" == hxtk[0] and not hxtk[-1] == "jood"
def qldv(hxtk):
     return (not "iqjrov" != hxtk[0]) and  hxtk[-1] == "jood"
def zrnep(hxtk):
     return (not rlcndh(hxtk)) and (hxtk[-1] != "jood")
mgfvbg = DerivedLevel("xzyabw", Transition(rlcndh, [hxtk]))
zih = DerivedLevel("fqpfw", Transition(qldv, [hxtk]))
bimdrp = DerivedLevel("cacgyf", Transition(zrnep, [hxtk]))
ntpar = Factor("jofvzx", [mgfvbg, zih, bimdrp])

### EXPERIMENT
design=[hxtk,ntpar]
crossing=[ntpar]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END