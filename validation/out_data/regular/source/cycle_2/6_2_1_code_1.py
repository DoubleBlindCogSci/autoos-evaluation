from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
RZRcs5yj=Factor(']kT',['gfno%S!y',"5Ex!Si",Level("SFuS$^dox]O",1),"JNM",'FXgs9U;xQ',"cpxjNiurae_P"])
UKx4A4WzDX=[Level('XDQm',7),'8*b2',"OVk6EQh",'{<T_aIYLJQO',"mSb0",Level("&ftzV",4)]
noyLNW=Factor("t toElWzUOfkCN",UKx4A4WzDX)

### EXPERIMENT
design=[RZRcs5yj,noyLNW]
crossing=[RZRcs5yj,noyLNW]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_1"))
### END