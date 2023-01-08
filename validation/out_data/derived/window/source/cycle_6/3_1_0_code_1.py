from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ensgf = Factor("ensgf", ["uhk","vjri","vln","zrw","mbemo","rmnz"])
def ekiei(ensgf):
     return "vln" == ensgf[-2] and not ensgf[-1] == "vln"
def dwscw(ensgf):
     return not "vln" == ensgf[-2] and  ensgf[-1] == "mbemo"
def znrk(ensgf):
     return (not ensgf[-2] == "vln") and (not dwscw(ensgf))
hdsl = DerivedLevel("gynbxm", Window(ekiei, [ensgf],3,1))
rkrvcz = DerivedLevel("bknfk", Window(dwscw, [ensgf],3,1))
pkyus = DerivedLevel("nqatc", Window(znrk, [ensgf],3,1))
xdf = Factor("qwkebc", [hdsl, rkrvcz, pkyus])

### EXPERIMENT
design=[ensgf,xdf]
crossing=[xdf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END