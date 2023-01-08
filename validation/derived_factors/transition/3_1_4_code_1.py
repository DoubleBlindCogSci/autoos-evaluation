from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
keckox = Factor("keckox", ["ianb","prvy","pwbtw","neujiq","miby","unxcn","opll","mlgvng"])
def zoyn(keckox):
     return "opll" == keckox[0] and keckox[-1] != "mlgvng"
def skhts(keckox):
     return (keckox[0] != "opll") and  "mlgvng" == keckox[-1]
def znihu(keckox):
     return (not zoyn(keckox)) and (not keckox[-1] == "mlgvng")
crazd = Factor("avn", [DerivedLevel("wcgjk", Transition(zoyn, [keckox])), DerivedLevel("tbyd", Transition(skhts, [keckox])),DerivedLevel("wrcikv", Transition(znihu, [keckox]))])
### EXPERIMENT
design=[keckox,crazd]
crossing=[crazd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END