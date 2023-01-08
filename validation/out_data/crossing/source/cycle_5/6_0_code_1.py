from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
elxl = Factor("elxl", ["ctvf", "lea"])
pqwvq = Factor("pqwvq", ["iftn", "hprjq"])
kcl = Factor("kcl", ["qriutk", "pevnwl"])
qdxl = Factor("qdxl", ["dzc", "tyuliq"])
chtr = Factor("chtr", ["bxqg", "juts"])
pqjfxe = Factor("pqjfxe", ["taepv", "luvlh"])
geiwkq = Factor("geiwkq", ["enhya", "admil"])
ixq = Factor("ixq", ["jxj", "yanaax"])
qybwhm = Factor("qybwhm", ["rmxb", "gqf"])
nevkb = Factor("nevkb", ["zccx", "kxl"])
qyv = Factor("qyv", ["cdijcy", "yjbmam"])
cxuy = Factor("cxuy", ["nmwxr", "zkwxqe"])
gnpfhs = Factor("gnpfhs", ["qvmt", "meaqbq"])
mxi = Factor("mxi", ["omu", "nzidy"])
sic = Factor("sic", ["cicax", "reb"])
kxy = Factor("kxy", ["clwiuj", "gke"])

### EXPERIMENT
design=[elxl,pqwvq,kcl,qdxl,chtr,pqjfxe,geiwkq,ixq,qybwhm,nevkb,qyv,cxuy,gnpfhs,mxi,sic,kxy]
crossing=[[elxl,pqwvq],[kcl],[qdxl,chtr,pqjfxe],[geiwkq,ixq,qybwhm],[nevkb,qyv,cxuy],[gnpfhs,mxi,sic,kxy],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_0"))
### END