from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qgpi = Factor("qgpi", ["xgstwk","wknoj","jgcumv","ujvch","fkw"])
def hormnr(qgpi):
    return qgpi[0] != "jgcumv" or qgpi[-2] == "wknoj"
def qpwtx(qgpi):
    return not (qgpi[0] != "jgcumv") and qgpi[-2] != "wknoj"
cpfxyo = Factor("enos", [DerivedLevel("sdrcc", Window(hormnr, [qgpi],3,1)), DerivedLevel("osk", Window(qpwtx, [qgpi],3,1))])
### EXPERIMENT
design=[qgpi,cpfxyo]
crossing=[cpfxyo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END