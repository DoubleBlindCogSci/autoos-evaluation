from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
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
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_0_0.csv"))
nr_crossings=4
nr_factors=15
p_code_1 = 0
p_code_2 = 0
crossing = [monf,ijsoxa,rlfo,gcal]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [pcl,hutnjw,qdedt,tvnr]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ayjsai,epdgkr,xdk,agh]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [zpfwx,qhokp,hvi]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
