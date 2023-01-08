from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xoapz = Factor("xoapz", ["xzhi", "masc"])
gpsnc = Factor("gpsnc", ["vkva", "jswc"])
enj = Factor("enj", ["jlun", "wybygq"])
lmmq = Factor("lmmq", ["zsaqq", "msgxd"])
mfyos = Factor("mfyos", ["whbsjk", "hgbp"])
pwpk = Factor("pwpk", ["mdr", "qittio"])
qntnmx = Factor("qntnmx", ["ufemf", "vczuu"])
rbg = Factor("rbg", ["jvv", "fegunx"])
iqa = Factor("iqa", ["eccdfq", "umjq"])
ddt = Factor("ddt", ["cdastd", "gco"])
fbaktv = Factor("fbaktv", ["alxa", "szol"])
mtgm = Factor("mtgm", ["uju", "tux"])
fkp = Factor("fkp", ["nnmp", "zed"])
zhgeq = Factor("zhgeq", ["oqwzp", "qiv"])
qbog = Factor("qbog", ["jmwndg", "wzzjc"])
mzor = Factor("mzor", ["mbr", "yha"])
kaikdk = Factor("kaikdk", ["ignd", "txevam"])

### EXPERIMENT
design=[xoapz,gpsnc,enj,lmmq,mfyos,pwpk,qntnmx,rbg,iqa,ddt,fbaktv,mtgm,fkp,zhgeq,qbog,mzor,kaikdk]
crossing=[[xoapz],[gpsnc,enj,lmmq,mfyos],[pwpk,qntnmx,rbg],[iqa,ddt],[fbaktv,mtgm,fkp],[zhgeq,qbog,mzor,kaikdk],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_3"))
### END