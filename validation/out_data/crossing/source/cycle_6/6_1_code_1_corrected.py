from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ystfh = Factor("ystfh", ["cmxahs", "osgxac"])
zoso = Factor("zoso", ["btjkh", "zvgl"])
rzna = Factor("rzna", ["ejp", "idvvpp"])
koabuf = Factor("koabuf", ["gvynn", "yyukej"])
qlxmc = Factor("qlxmc", ["apbttu", "tch"])
quhsl = Factor("quhsl", ["lcscjf", "gwmcki"])
tspj = Factor("tspj", ["smu", "qgjc"])
dwtliw = Factor("dwtliw", ["qkilca", "sfdrwx"])
kipdl = Factor("kipdl", ["lld", "hlkfh"])
nqa = Factor("nqa", ["hyp", "idjo"])
hpsau = Factor("hpsau", ["var", "grdj"])
vtpq = Factor("vtpq", ["tpmuq", "dmu"])
bxwiuo = Factor("bxwiuo", ["sync", "uud"])
rzocy = Factor("rzocy", ["tqy", "ygrfp"])
kzy = Factor("kzy", ["uwfo", "all"])
qyxq = Factor("qyxq", ["qug", "hgmduj"])
lzgci = Factor("lzgci", ["ryccj", "tunv"])
zmitzu = Factor("zmitzu", ["htt", "xjdij"])

### EXPERIMENT
design=[ystfh,zoso,rzna,koabuf,qlxmc,quhsl,tspj,dwtliw,kipdl,nqa,hpsau,vtpq,bxwiuo,rzocy,kzy,qyxq,lzgci,zmitzu]
crossing = [[quhsl,tspj,dwtliw,kipdl],[nqa,hpsau,vtpq,bxwiuo],[rzocy,kzy,qyxq,lzgci],[rzna,koabuf,qlxmc],[ystfh,zoso],[zmitzu],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1"))
### END
