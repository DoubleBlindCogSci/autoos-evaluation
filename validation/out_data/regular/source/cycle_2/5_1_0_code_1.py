from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
C9vdKnAkLY=[Level("VzUCehpBnaP",3),Level('uDBGgsjDf2Q',1),Level("vTxdbNj",9),"ua9E} f",Level("1tGp2tK",5)]
Z7oaO=Factor("JarEPo",C9vdKnAkLY)

### EXPERIMENT
design=[Z7oaO]
crossing=[Z7oaO]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_0"))
### END