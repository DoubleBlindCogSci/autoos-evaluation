from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uano = Factor("uano", ["hspapo","hlyj","swp","motz","okbuz","scxcn"])
def qei(uano):
     return uano[0] == "hspapo" and uano[-1] != "okbuz"
def tvozp(uano):
     return (not "hspapo" != uano[0]) and  uano[-1] == "okbuz"
def msqg(uano):
     return (uano[0] != "hspapo") and (not uano[-1] == "okbuz")
lem = DerivedLevel("szyjh", Transition(qei, [uano]))
ydozt = DerivedLevel("xogpak", Transition(tvozp, [uano]))
ruinsa = DerivedLevel("fkkgx", Transition(msqg, [uano]))
hmz = Factor("zzbnv", [lem, ydozt, ruinsa])

### EXPERIMENT
design=[uano,hmz]
crossing=[hmz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END