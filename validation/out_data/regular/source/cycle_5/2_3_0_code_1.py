from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Ejnzat=Factor("OMBWTW3$VTOT ",["g0sUmwgnfwr",'(eJ'])
VHTW84ESb=Factor("rUVsgeRdoGm",["$DBdp","BUc|c5bTF"])
_ob8X=Factor("fF_",['XoWq>jmLWIW',"Ke*fjQc&OdxAD_"])

### EXPERIMENT
design=[Ejnzat,VHTW84ESb,_ob8X]
crossing=[Ejnzat,VHTW84ESb,_ob8X]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3_0"))
### END