from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
axm = Factor("axm", ["couero", "yfyrkr"])
frzyz = Factor("frzyz", ["sbgfa", "xyssqj"])
wmmsy = Factor("wmmsy", ["hrcoly", "fwv"])
mcdtsd = Factor("mcdtsd", ["riexm", "ytuwcr"])
prfwwr = Factor("prfwwr", ["zkw", "bfi"])
mlnqg = Factor("mlnqg", ["gtv", "neslzn"])
ejgvc = Factor("ejgvc", ["wkxi", "fbihqw"])
ouefco = Factor("ouefco", ["limde", "caim"])
vhcey = Factor("vhcey", ["spwoe", "xjnw"])

### EXPERIMENT
design=[axm,frzyz,wmmsy,mcdtsd,prfwwr,mlnqg,ejgvc,ouefco,vhcey]
crossing=[[axm],[frzyz],[wmmsy,mcdtsd,prfwwr,mlnqg],[ejgvc,ouefco,vhcey],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0"))
### END