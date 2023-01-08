from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
wsle = Factor("wsle", ["jerlq","dthqsq","hpuvln","sorijz","zwze","nxcmu","amrfiy","oemibc"])
def aly(wsle):
     return "sorijz" == wsle[0]
def iaun(wsle):
     return wsle[-1] == "jerlq"
def xxtxnd(wsle):
     return (not wsle[0] == "sorijz") and (not iaun(wsle))
owbhqo = Factor("zhyw", [DerivedLevel("zldik", Transition(aly, [wsle])), DerivedLevel("oflt", Transition(iaun, [wsle])),DerivedLevel("ziowfh", Transition(xxtxnd, [wsle]))])
### EXPERIMENT
design=[wsle,owbhqo]
crossing=[owbhqo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END