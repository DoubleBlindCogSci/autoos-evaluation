from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Snvb=Factor("cmEc[JU2p",["c9QZvI^rfrKM",'VroUQ(Ys',"Bt0Z","nEQVMmO",Level('YNvvFVv',2),'U(CegASjt&',Level("KMgp$",1),"iAKYajm uRQ%X",Level('|BrrihbKua~',3)])

### EXPERIMENT
design=[Snvb]
crossing=[Snvb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_1_1"))
### END