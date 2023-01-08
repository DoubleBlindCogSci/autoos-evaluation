from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
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
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_0.csv"))
nr_crossings=6
nr_factors=13
p_code_1 = 0
p_code_2 = 0
crossing = [ovlqa,gmw]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [qofs]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [aqd,vnep,wuitvb]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [fjk]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [dwvkng,xpbstl,pabkm,yofn]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ghorsd,hczscb]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
