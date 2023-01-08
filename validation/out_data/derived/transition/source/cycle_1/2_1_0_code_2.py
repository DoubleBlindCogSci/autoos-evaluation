from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ogsg= Factor("ogsg", ["emad","otnwpd","fdntx","surzu","uvjxds"])
def is_qcq_yhhwqh(ogsg):
    return ogsg[0] == "uvjxds" and ogsg[-1] != "surzu"
def is_qcq_war(ogsg):
    return not is_qcq_yhhwqh(ogsg)
qcq= Factor("qcq", [DerivedLevel("yhhwqh", Transition(is_qcq_yhhwqh, [ogsg])), DerivedLevel("war", Transition(is_qcq_war, [ogsg]))])

design=[ogsg,qcq]
crossing=[qcq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
