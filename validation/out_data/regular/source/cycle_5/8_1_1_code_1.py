from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_RzJE=["qxS","F}Fv","QnmTo",'WAB 2;ZVH)f','NF?WtqD']
RCOXr=Factor("jGhkG",[' GyKQz6AtL','kHE^tK#PsSu','b6Cxtj{','dWZRHs SNQy5qt',"eMYNaS 9",':UhRc','yEhe]FrBMMhjn~',_RzJE[4],'I*LN '])

### EXPERIMENT
design=[RCOXr]
crossing=[RCOXr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_1_1"))
### END