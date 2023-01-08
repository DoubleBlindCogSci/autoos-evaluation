from sweetpea import *
import os
_dir=os.path.dirname(__file__)
hrr = Factor("hrr", ["swlws", "gbsh"])
xpjcm = Factor("xpjcm", ["hlmsbm", "nswin"])
jjrgha = Factor("jjrgha", ["uvmpfw", "tpbqd"])
wrigoa = Factor("wrigoa", ["cxauz", "kbhyq"])
nsoq = Factor("nsoq", ["buro", "oqt"])
jzclv = Factor("jzclv", ["laesay", "dfayf"])
yvygqo = Factor("yvygqo", ["vnyq", "jhg"])
kysqr = Factor("kysqr", ["qtrg", "urib"])
fzvds = Factor("fzvds", ["mph", "vie"])
ioyues = Factor("ioyues", ["ydnac", "yud"])
eldf = Factor("eldf", ["qwey", "fkuoqp"])
apq = Factor("apq", ["xfz", "tuxr"])
kun = Factor("kun", ["hktj", "czd"])
qbhn = Factor("qbhn", ["ncnagk", "gvwgmt"])
constraints = []
crossing = [[hrr, xpjcm, jjrgha, wrigoa, nsoq], [jzclv, yvygqo, kysqr, fzvds], [ioyues, eldf], [apq, kun], [qbhn]]


design=[hrr,xpjcm,jjrgha,wrigoa,nsoq,jzclv,yvygqo,kysqr,fzvds,ioyues,eldf,apq,kun,qbhn]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_6"))

### END