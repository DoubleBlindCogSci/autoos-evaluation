from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
siPi=Factor('Clt[CF',["l22dmT|iW[Wa",'IcuLjigs?8',Level('rh;nbLysFxfYop',3),Level('aWL',6)])
aSb3xlnA0=Factor("P|J%L^y",[Level(";oKZhQWhvC",1),'rqF^P;v0I',Level('#iMgXnO:',6),Level('PVWYarfX',3)])

### EXPERIMENT
design=[siPi,aSb3xlnA0]
crossing=[siPi,aSb3xlnA0]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_1"))
### END