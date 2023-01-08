from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ogsg = Factor("ogsg", ["emad","otnwpd","fdntx","surzu","uvjxds"])
def hrw(ogsg):
    return ogsg[0] == "uvjxds" and ogsg[-1] != "surzu"
def sqc(ogsg):
    return not hrw(ogsg)
ipvgty = Factor("qcq", [DerivedLevel("yhhwqh", Transition(hrw, [ogsg])), DerivedLevel("war", Transition(sqc, [ogsg]))])
### EXPERIMENT
design=[ogsg,ipvgty]
crossing=[ipvgty]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END