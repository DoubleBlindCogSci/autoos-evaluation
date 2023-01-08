from sweetpea import *
import os
_dir=os.path.dirname(__file__)
gzjyk = Factor("gzjyk", ["ffbyf", "gcmey"])
suk = Factor("suk", ["jvg", "nvjcva"])
ugvn = Factor("ugvn", ["vasvin", "mnk"])
rulygd = Factor("rulygd", ["jse", "dpdmvc"])
phmylo = Factor("phmylo", ["lreyc", "fhh"])
vmn = Factor("vmn", ["vbm", "dmn"])
sbj = Factor("sbj", ["ktf", "wgt"])
wiqfxt = Factor("wiqfxt", ["tgtx", "uoh"])
nkaqzs = Factor("nkaqzs", ["mpewce", "flbzy"])
jcver = Factor("jcver", ["wwyar", "ccaie"])
zxbc = Factor("zxbc", ["wbaf", "hbwsly"])
fdk = Factor("fdk", ["wjh", "mxho"])
fnaowb = Factor("fnaowb", ["xhcom", "vwu"])
uqetk = Factor("uqetk", ["xdjls", "rfusu"])
taj = Factor("taj", ["jar", "xqw"])
htr = Factor("htr", ["uxgz", "elcb"])
xzwt = Factor("xzwt", ["kddbp", "ibp"])
constraints = []
crossing = [[gzjyk, suk, ugvn, rulygd], [phmylo, vmn, sbj, wiqfxt], [nkaqzs], [jcver, zxbc, fdk, fnaowb], [uqetk, taj, htr, xzwt]]


design=[gzjyk,suk,ugvn,rulygd,phmylo,vmn,sbj,wiqfxt,nkaqzs,jcver,zxbc,fdk,fnaowb,uqetk,taj,htr,xzwt]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2"))

### END