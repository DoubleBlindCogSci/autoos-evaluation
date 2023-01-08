from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
gux = Factor("gux", ["mqb","bimndj","gwta","mgd","fttjig","fwe","hhn","juqlf"])
def qlces(gux):
     return gux[0] == "fwe" and gux[-1] != "gwta"
def qkyq(gux):
     return (gux[0] != "fwe") and  gux[-1] == "gwta"
def fktf(gux):
     return (not gux[0] == "fwe") and (not qkyq(gux))
jetni = Factor("uakm", [DerivedLevel("prbuti", Transition(qlces, [gux])), DerivedLevel("gstiro", Transition(qkyq, [gux])),DerivedLevel("wjb", Transition(fktf, [gux]))])
### EXPERIMENT
design=[gux,jetni]
crossing=[jetni]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END