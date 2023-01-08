from sweetpea import *
import os
_dir=os.path.dirname(__file__)
ymc = Factor("ymc", ["uyj", "ogz"])
utp = Factor("utp", ["ugeam", "btblx"])
tjkftk = Factor("tjkftk", ["xpo", "muf"])
yvy = Factor("yvy", ["xbv", "rcnus"])
knrww = Factor("knrww", ["eli", "eqoj"])
wjlkwe = Factor("wjlkwe", ["vjrjex", "geco"])
fqp = Factor("fqp", ["hbz", "lwu"])
ivlj = Factor("ivlj", ["apceqb", "sej"])
ems = Factor("ems", ["xjoxx", "wiei"])
constraints = []
crossing = [[ymc, utp], [tjkftk], [yvy, knrww], [wjlkwe, fqp], [ivlj, ems]]


design=[ymc,utp,tjkftk,yvy,knrww,wjlkwe,fqp,ivlj,ems]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_3"))

### END