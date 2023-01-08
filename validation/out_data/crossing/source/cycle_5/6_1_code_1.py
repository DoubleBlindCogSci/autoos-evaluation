from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ovlqa = Factor("ovlqa", ["xvv", "zfec"])
gmw = Factor("gmw", ["jwk", "loh"])
qofs = Factor("qofs", ["wluel", "fvux"])
aqd = Factor("aqd", ["koxhpg", "oebb"])
vnep = Factor("vnep", ["oppxtt", "svc"])
wuitvb = Factor("wuitvb", ["wqxab", "cunto"])
fjk = Factor("fjk", ["ejzvzj", "olo"])
dwvkng = Factor("dwvkng", ["oghxlr", "agq"])
xpbstl = Factor("xpbstl", ["gir", "uwsdf"])
pabkm = Factor("pabkm", ["alezzi", "sjmzuf"])
yofn = Factor("yofn", ["qclyyp", "ywk"])
ghorsd = Factor("ghorsd", ["gdj", "uwcjnf"])
hczscb = Factor("hczscb", ["xko", "gcv"])

### EXPERIMENT
design=[ovlqa,gmw,qofs,aqd,vnep,wuitvb,fjk,dwvkng,xpbstl,pabkm,yofn,ghorsd,hczscb]
crossing=[[ovlqa,gmw],[qofs],[aqd,vnep,wuitvb],[fjk],[dwvkng,xpbstl,pabkm,yofn],[ghorsd,hczscb],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1"))
### END