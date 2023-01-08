from sweetpea import *
import os
_dir=os.path.dirname(__file__)
iwr = Factor("iwr", ["sswxtv", "jkuber"])
tpwu = Factor("tpwu", ["lfhpt", "yyvsxh"])
rxng = Factor("rxng", ["mfa", "pcpeov"])
xzm = Factor("xzm", ["hzjf", "dypphl"])
dkzxv = Factor("dkzxv", ["hci", "jjwp"])
rhjn = Factor("rhjn", ["klyu", "vzdql"])
gsy = Factor("gsy", ["odt", "lgnoh"])
sqzd = Factor("sqzd", ["tnb", "qmkjbq"])
nhagce = Factor("nhagce", ["jszi", "ywl"])
rkawni = Factor("rkawni", ["tmnohm", "bgemlq"])
xilc = Factor("xilc", ["nnifgz", "lhq"])
ixcig = Factor("ixcig", ["nip", "cgxdw"])
vfn = Factor("vfn", ["yrxq", "rpkn"])
zbzahn = Factor("zbzahn", ["brcgu", "ofpi"])
constraints = []
crossing = [[iwr, tpwu, rxng, xzm], [dkzxv, rhjn, gsy, sqzd], [nhagce, rkawni], [xilc, ixcig, vfn, zbzahn]]


design=[iwr,tpwu,rxng,xzm,dkzxv,rhjn,gsy,sqzd,nhagce,rkawni,xilc,ixcig,vfn,zbzahn]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_3"))

### END