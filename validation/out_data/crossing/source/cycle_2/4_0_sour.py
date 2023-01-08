from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pjw = Factor("pjw", ["yfn", "ecwpfd"])
bovuke = Factor("bovuke", ["ryoi", "ydr"])
qylqc = Factor("qylqc", ["duag", "zvutv"])
nhlg = Factor("nhlg", ["ywg", "kktt"])
ynyb = Factor("ynyb", ["jbs", "xbe"])
vhnsj = Factor("vhnsj", ["avphmd", "kkjx"])
zrsapb = Factor("zrsapb", ["nbybed", "gvd"])
hukp = Factor("hukp", ["igg", "jvufve"])
acns = Factor("acns", ["grnqpx", "tfvsf"])
qnzux = Factor("qnzux", ["lmzyfv", "mdn"])
tldpnx = Factor("tldpnx", ["oqeizn", "qznl"])
wchxn = Factor("wchxn", ["udcy", "bedt"])
brrsj = Factor("brrsj", ["dbz", "hcyucc"])

### EXPERIMENT
design=[pjw,bovuke,qylqc,nhlg,ynyb,vhnsj,zrsapb,hukp,acns,qnzux,tldpnx,wchxn,brrsj]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_0_0.csv"))
nr_crossings=4
nr_factors=13
p_code_1 = 0
p_code_2 = 0
crossing = [pjw,bovuke,qylqc,nhlg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ynyb,vhnsj,zrsapb]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [hukp,acns]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [qnzux,tldpnx,wchxn,brrsj]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
