from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
r7kRtNe=Factor("kwUCG",[Level("i;bnjNey",6),'oyPYkKej',Level('fMJP%>kIB: W',6),Level('Xvt%QY[bbU',1),'ApHCipr',"i@GILK",Level("BTo",10)])

### EXPERIMENT
design=[r7kRtNe]
crossing=[r7kRtNe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_1_0"))
### END