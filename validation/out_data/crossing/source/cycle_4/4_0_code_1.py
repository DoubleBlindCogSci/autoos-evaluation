from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
monf = Factor("monf", ["pqunn", "lzp"])
ijsoxa = Factor("ijsoxa", ["xpmtxu", "qjdvy"])
rlfo = Factor("rlfo", ["ifxu", "thz"])
gcal = Factor("gcal", ["fdrug", "jjv"])
pcl = Factor("pcl", ["kmkt", "vjra"])
hutnjw = Factor("hutnjw", ["qsat", "xipb"])
qdedt = Factor("qdedt", ["jwfn", "pftxf"])
tvnr = Factor("tvnr", ["cpreo", "wmt"])
ayjsai = Factor("ayjsai", ["argqn", "zrm"])
epdgkr = Factor("epdgkr", ["uufdh", "xfbdn"])
xdk = Factor("xdk", ["poptjz", "odexc"])
agh = Factor("agh", ["jtvw", "qwykkw"])
zpfwx = Factor("zpfwx", ["nkofj", "mjmor"])
qhokp = Factor("qhokp", ["udqzt", "xqlqm"])
hvi = Factor("hvi", ["cxbip", "rcpflu"])

### EXPERIMENT
design=[monf,ijsoxa,rlfo,gcal,pcl,hutnjw,qdedt,tvnr,ayjsai,epdgkr,xdk,agh,zpfwx,qhokp,hvi]
crossing=[[monf,ijsoxa,rlfo,gcal],[pcl,hutnjw,qdedt,tvnr],[ayjsai,epdgkr,xdk,agh],[zpfwx,qhokp,hvi],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0"))
### END