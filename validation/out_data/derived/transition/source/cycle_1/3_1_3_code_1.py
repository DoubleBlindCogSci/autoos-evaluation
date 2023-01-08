from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ghljns = Factor("ghljns", ["dgbxuu","wxfjh","tgxq","fqttg","bcgva","kwxwwg","sassnr","fpa"])
def pmm(ghljns):
     return "sassnr" == ghljns[0]
def bzwtlz(ghljns):
     return "tgxq" == ghljns[-1]
def qisax(ghljns):
     return (ghljns[0] != "sassnr") and (not ghljns[-1] == "tgxq")
jlwva = DerivedLevel("ery", Transition(pmm, [ghljns]))
oiji = DerivedLevel("ltxz", Transition(bzwtlz, [ghljns]))
uav = DerivedLevel("kybpzi", Transition(qisax, [ghljns]))
gva = Factor("youocf", [jlwva, oiji, uav])

### EXPERIMENT
design=[ghljns,gva]
crossing=[gva]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END