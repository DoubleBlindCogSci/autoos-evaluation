from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HEvoy7hdj=['zIM',"DY5","msr"]
RloV=Factor('pyOE~N7yFBpB',[Level('IDtdzk(QdMaMl',1),"wrbmtjn#CxL",'Q2Y','H&bDpC',':VAJHl${Lso','XmEcAJgQYMNJf',HEvoy7hdj[1]])

### EXPERIMENT
design=[RloV]
crossing=[RloV]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_0"))
### END