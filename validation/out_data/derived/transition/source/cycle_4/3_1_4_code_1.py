from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jvsf = Factor("jvsf", ["kivh","kqagto","zqksk","xae","twyc","epq","rtxaw"])
def set(jvsf):
     return "xae" == jvsf[0] and jvsf[-1] != "rtxaw"
def hpgt(jvsf):
     return (jvsf[0] != "xae") and  jvsf[-1] == "rtxaw"
def qai(jvsf):
     return (not jvsf[0] == "xae") and (not jvsf[-1] == "rtxaw")
jguq = DerivedLevel("tngyia", Transition(set, [jvsf]))
gweb = DerivedLevel("gemffy", Transition(hpgt, [jvsf]))
cbqulv = DerivedLevel("sspc", Transition(qai, [jvsf]))
wvqnfc = Factor("nfx", [jguq, gweb, cbqulv])

### EXPERIMENT
design=[jvsf,wvqnfc]
crossing=[wvqnfc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END