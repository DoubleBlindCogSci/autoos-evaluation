from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sdqvrg = Factor("sdqvrg", ["zzgq", "aacmjn"])
fslc = Factor("fslc", ["nlxb", "flf"])
tsgtb = Factor("tsgtb", ["ntylcv", "nhewl"])
esqvyn = Factor("esqvyn", ["bgle", "lstm"])
ymyvec = Factor("ymyvec", ["uoqaig", "yyzmz"])
dlzxx = Factor("dlzxx", ["aebclx", "lgwhqs"])
kxb = Factor("kxb", ["mbd", "pwa"])
lzqnv = Factor("lzqnv", ["xgmgbq", "zcigso"])

### EXPERIMENT
design=[sdqvrg,fslc,tsgtb,esqvyn,ymyvec,dlzxx,kxb,lzqnv]
crossing=[[sdqvrg,fslc],[tsgtb,esqvyn],[ymyvec,dlzxx,kxb,lzqnv],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_4"))
### END