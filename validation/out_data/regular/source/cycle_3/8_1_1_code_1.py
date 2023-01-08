from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rXpDgnDTX88=Factor("_eEupC2Jwie",[Level('PcVtxJnQCXGZnq',10),'S?mAlmsWc',Level('KKVbMI9x5',9),"N^LhliXCbH?lT",'kXOOQcLN$lEf','My}akkTrp',Level('U]CBm',4),'DTMyiaIZ'])

### EXPERIMENT
design=[rXpDgnDTX88]
crossing=[rXpDgnDTX88]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_1_1"))
### END