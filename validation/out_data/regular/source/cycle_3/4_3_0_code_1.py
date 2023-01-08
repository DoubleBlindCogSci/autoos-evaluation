from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
AtdO1GnKzF2=[Level("KcW2ZxggE",4),"QBj;_x",'eUB6*Apaft','}OrlEdVL',"dvAL",Level('r f<DtUg{ZNQ',2),Level('nBfilTtc&$M',6)]
ZXZ_Zbz=Factor("w]wKEQfjtuL",[AtdO1GnKzF2[4],"qU)P","nHGLbkYRAT","iFUGatGZaeVYjl",Level('ejdSnrjVVeqh',8)])
RdD7Gj=Factor("C4krZwd",['Jhlf#sDUj','?hQrS',Level("RuRJCC",6),Level("vuzr",1)])
nnv1Z=Factor('EFRWROtJQG',["LKFVp;8MzDY8F","KPZRhqX",'Kh{fGMvOjo(Rw','bjJNM%rv'])

### EXPERIMENT
design=[ZXZ_Zbz,RdD7Gj,nnv1Z]
crossing=[ZXZ_Zbz,RdD7Gj,nnv1Z]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_3_0"))
### END