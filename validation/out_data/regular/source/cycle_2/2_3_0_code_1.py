from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZBdW_si='kRtKnoE7XVWjvL'
js3bK23B=Factor("en gxxvL",[ZBdW_si,'OSPyW{fR',Level("FUWAO",1)])
y7_4Pfp2d=["g*iu",'CSaQw']
Dm6kohXX=Factor("PaGCajYpIEehuq",y7_4Pfp2d)
V353f0TROt=Factor("E[_elRfqN",[Level("U[x?obejL%",8),"yjOmrT"])

### EXPERIMENT
design=[js3bK23B,Dm6kohXX,V353f0TROt]
crossing=[js3bK23B,Dm6kohXX,V353f0TROt]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3_0"))
### END