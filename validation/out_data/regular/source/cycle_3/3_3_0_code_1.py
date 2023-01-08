from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
E6fSw=Factor("m&PHyvQ",[Level('i#D)yTu3P',5),Level('lvIY:P?MB',6),Level('DZsh',1)])
e5xtj=['PFYD5','FtU<PsDEEGvBN<',Level("*RO6qw$lFxs",4)]
XUBHar4zpyg=Factor('vVp b',e5xtj)
Di1NB=Factor("pzr[XuysBLwLxh",[Level('VxaIv:XbDfJ',1),'sAfRl',Level('#8zqe',10)])

### EXPERIMENT
design=[E6fSw,XUBHar4zpyg,Di1NB]
crossing=[E6fSw,XUBHar4zpyg,Di1NB]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3_0"))
### END