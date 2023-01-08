from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EXBCuSOt6Po=["!kNySyZU","rkZJb#}TZ)I",'nLI*YFg',"VABI",'IbD']
CJQ0X=Factor('ATt',['hON',"gSvq_",'ijm}CjTDpBompc',EXBCuSOt6Po[2],'ZkQHyJN(j~ ','$ZzoKDfJOb|','dcfxkQnOR6r','NwPbastQN',"eI setsNY","FesW]S",'IyxCxQQHV'])
OR37=Factor('W7AzyZw~?MSK',['lseRor!cqHCa','T}fikaFghFlNYz',"pk<b LuZ^oGY","bLs","rrnjycxVCiROM","ktBGy$","hGVKFWCd0F","wSou_ejp",'2wQ','#rithj(Zxe'])

### EXPERIMENT
design=[CJQ0X,OR37]
crossing=[CJQ0X,OR37]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/10_2_0"))
### END