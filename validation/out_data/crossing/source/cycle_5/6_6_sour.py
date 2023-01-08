from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
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

### EXPERIMENT
design=[hrr,xpjcm,jjrgha,wrigoa,nsoq,jzclv,yvygqo,kysqr,fzvds,ioyues,eldf,apq,kun,qbhn]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_6_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_6_0.csv"))
nr_crossings=6
nr_factors=14
p_code_1 = 0
p_code_2 = 0
crossing = [hrr]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [xpjcm,jjrgha,wrigoa,nsoq]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [jzclv,yvygqo,kysqr,fzvds]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ioyues,eldf]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [apq,kun]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [qbhn]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
