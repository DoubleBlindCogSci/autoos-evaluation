from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
R9k3X=Factor("emnMyZcbxQ",["MrtiTMs(aSeyvu","Vg$[ChLt(E ",'jrUWLycz b7W%','oyRv',"jgZAGcLgxblY","MPM",'I5aAsle','x~g:oNl]'])
C_CgHF=Factor('He2~  qjh',['La)SsIQczx','GpaG'," ko","V5are8AHhv",'nWMpcCrXv{K',"qtQUS",'3tsd<',"NQsByAwBdy"])

### EXPERIMENT
design=[R9k3X,C_CgHF]
crossing=[R9k3X,C_CgHF]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_2_1"))
### END