from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vksj = Factor("vksj", ["zmzan","cfohyl","vafjcn","lojc","quu","rfqmb","qydd"])
def jzzon(vksj):
     return vksj[0] == "cfohyl"
def iga(vksj):
     return vksj[-1] == "quu"
def hlir(vksj):
     return (not jzzon(vksj)) and (not iga(vksj))
ixzfh = Factor("etwf", [DerivedLevel("pkxzmq", Transition(jzzon, [vksj])), DerivedLevel("aman", Transition(iga, [vksj])),DerivedLevel("zuttft", Transition(hlir, [vksj]))])
### EXPERIMENT
design=[vksj,ixzfh]
crossing=[ixzfh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END