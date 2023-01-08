from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vkq = Factor("vkq", ["fyiqva", "fyhezn"])
drg = Factor("drg", ["fdb", "ehn"])
fqjdvj = Factor("fqjdvj", ["sqcmmj", "lno"])
uej = Factor("uej", ["iks", "skb"])
lhbo = Factor("lhbo", ["oeqbie", "kabzup"])
tryat = Factor("tryat", ["zvlu", "wgs"])
dwqc = Factor("dwqc", ["gskzu", "traua"])
yxl = Factor("yxl", ["irk", "gzm"])

### EXPERIMENT
design=[vkq,drg,fqjdvj,uej,lhbo,tryat,dwqc,yxl]
crossing=[[vkq,drg],[fqjdvj,uej,lhbo],[tryat,dwqc],[yxl],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2"))
### END