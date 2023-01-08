from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mqt = Factor("mqt", ["gmbm","jezzl","dcea","tibpp","kwnm","vfd"])
def qjaax(mqt):
    return mqt[0] != "vfd" or mqt[-2] == "gmbm"
def nvbar(mqt):
    return not qjaax(mqt)
phwiz = Factor("lwd", [DerivedLevel("uvkig", Window(qjaax, [mqt],3,1)), DerivedLevel("hxxhr", Window(nvbar, [mqt],3,1))])
### EXPERIMENT
design=[mqt,phwiz]
crossing=[phwiz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END