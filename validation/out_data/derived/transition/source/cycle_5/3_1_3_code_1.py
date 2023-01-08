from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tglvmx = Factor("tglvmx", ["tkon","nzbpe","eyjenc","fkjtmj","pulu","uls","hkfa"])
def eszjnf(tglvmx):
     return "pulu" == tglvmx[0] and not tglvmx[-1] == "tkon"
def ejrf(tglvmx):
     return (not "pulu" != tglvmx[0]) and  "tkon" == tglvmx[-1]
def cter(tglvmx):
     return (not eszjnf(tglvmx)) and (not ejrf(tglvmx))
evjw = Factor("brbmt", [DerivedLevel("prtnf", Transition(eszjnf, [tglvmx])), DerivedLevel("racrn", Transition(ejrf, [tglvmx])),DerivedLevel("olao", Transition(cter, [tglvmx]))])
### EXPERIMENT
design=[tglvmx,evjw]
crossing=[evjw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END