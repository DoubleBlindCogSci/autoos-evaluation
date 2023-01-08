from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vgbnj = Factor("vgbnj", ["mgvnrk","wjeuh","okv","vlm","xerqu","rzmec","lkbnr","jmqwwf"])
def jprt(vgbnj):
     return "xerqu" == vgbnj[0] and vgbnj[-1] != "okv"
def ioek(vgbnj):
     return (vgbnj[0] != "xerqu") and  "okv" == vgbnj[-1]
def ewpbf(vgbnj):
     return (not jprt(vgbnj)) and (vgbnj[-1] != "okv")
qkk = Factor("jgigg", [DerivedLevel("ocpjh", Transition(jprt, [vgbnj])), DerivedLevel("lzq", Transition(ioek, [vgbnj])),DerivedLevel("vzyhs", Transition(ewpbf, [vgbnj]))])
### EXPERIMENT
design=[vgbnj,qkk]
crossing=[qkk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END