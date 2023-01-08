from sweetpea import *
import os
_dir=os.path.dirname(__file__)
jtwv = Factor("jtwv", ["ghrnec", "mzfr"])
zsxy = Factor("zsxy", ["saxr", "yig"])
sjkzq = Factor("sjkzq", ["cvubz", "ygwe"])
tzx = Factor("tzx", ["etqke", "kfns"])
taict = Factor("taict", ["gcwcs", "ziks"])
zcbq = Factor("zcbq", ["ckmkd", "kjvm"])
ahdmub = Factor("ahdmub", ["jtenks", "pxgvv"])
constraints = []
crossing = [[jtwv, zsxy], [sjkzq, tzx, taict, zcbq], [ahdmub, tzx, taict, zcbq, sjkzq]]


design=[jtwv,zsxy,sjkzq,tzx,taict,zcbq,ahdmub]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_4"))

### END