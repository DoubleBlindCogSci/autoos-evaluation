from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jtwv = Factor("jtwv", ["ghrnec", "mzfr"])
zsxy = Factor("zsxy", ["saxr", "yig"])
sjkzq = Factor("sjkzq", ["cvubz", "ygwe"])
tzx = Factor("tzx", ["etqke", "kfns"])
taict = Factor("taict", ["gcwcs", "ziks"])
zcbq = Factor("zcbq", ["ckmkd", "kjvm"])
ahdmub = Factor("ahdmub", ["jtenks", "pxgvv"])

### EXPERIMENT
design=[jtwv,zsxy,sjkzq,tzx,taict,zcbq,ahdmub]
crossing=[[jtwv,zsxy],[sjkzq],[tzx,taict,zcbq],[ahdmub],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_4"))
### END