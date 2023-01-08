from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
oyjjvq = Factor("oyjjvq", ["izk","dok","kcnrhz","erpusv","lftdl","pal","ukmnw"])
pci = Factor("pci", ["bjs","nnwbkt","cvrzdw","pld","agium","mnb","kgyfy"])
def levalc(oyjjvq, pci):
    return oyjjvq[0] != "lftdl" or pci[-1] != "kgyfy"
def hvvz(oyjjvq,pci):
    return not levalc(oyjjvq, pci)
ysit = DerivedLevel("dovw", Transition(levalc, [oyjjvq, pci]))
wqywqx = DerivedLevel("gga", Transition(hvvz, [oyjjvq, pci]))
caqd = Factor("bib", [ysit, wqywqx])

### EXPERIMENT
design=[oyjjvq,pci,caqd]
crossing=[caqd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END