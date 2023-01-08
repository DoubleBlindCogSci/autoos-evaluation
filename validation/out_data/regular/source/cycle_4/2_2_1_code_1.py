from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
QWjMq0Y=['eBdb',"xo&"]
olAjzZ=Factor('HKaVPV',QWjMq0Y)
SrmrNNRCu=Factor('bkCi_P',['q&wIDJIGEb',Level("fTIAKbvgDKKRN|",3)])

### EXPERIMENT
design=[olAjzZ,SrmrNNRCu]
crossing=[olAjzZ,SrmrNNRCu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END