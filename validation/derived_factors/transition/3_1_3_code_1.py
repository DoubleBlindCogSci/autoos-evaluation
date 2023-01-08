from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
iovk = Factor("iovk", ["myck","tok","jrlroa","rzjp","wbans","dvtuyz","kbikwr"])
def gmtnpb(iovk):
     return iovk[0] == "wbans" and not iovk[-1] == "kbikwr"
def hfvbz(iovk):
     return (iovk[0] != "wbans") and  "kbikwr" == iovk[-1]
def wjgwva(iovk):
     return (not iovk[0] == "wbans") and (not hfvbz(iovk))
aknpis = DerivedLevel("gza", Transition(gmtnpb, [iovk]))
rizi = DerivedLevel("hll", Transition(hfvbz, [iovk]))
dgk = DerivedLevel("ffmnii", Transition(wjgwva, [iovk]))
vfzxe = Factor("gli", [aknpis, rizi, dgk])

### EXPERIMENT
design=[iovk,vfzxe]
crossing=[vfzxe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END