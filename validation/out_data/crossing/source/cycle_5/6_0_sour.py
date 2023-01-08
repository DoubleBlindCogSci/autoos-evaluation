from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
elxl = Factor("elxl", ["ctvf", "lea"])
pqwvq = Factor("pqwvq", ["iftn", "hprjq"])
kcl = Factor("kcl", ["qriutk", "pevnwl"])
qdxl = Factor("qdxl", ["dzc", "tyuliq"])
chtr = Factor("chtr", ["bxqg", "juts"])
pqjfxe = Factor("pqjfxe", ["taepv", "luvlh"])
geiwkq = Factor("geiwkq", ["enhya", "admil"])
ixq = Factor("ixq", ["jxj", "yanaax"])
qybwhm = Factor("qybwhm", ["rmxb", "gqf"])
nevkb = Factor("nevkb", ["zccx", "kxl"])
qyv = Factor("qyv", ["cdijcy", "yjbmam"])
cxuy = Factor("cxuy", ["nmwxr", "zkwxqe"])
gnpfhs = Factor("gnpfhs", ["qvmt", "meaqbq"])
mxi = Factor("mxi", ["omu", "nzidy"])
sic = Factor("sic", ["cicax", "reb"])
kxy = Factor("kxy", ["clwiuj", "gke"])

### EXPERIMENT
design=[elxl,pqwvq,kcl,qdxl,chtr,pqjfxe,geiwkq,ixq,qybwhm,nevkb,qyv,cxuy,gnpfhs,mxi,sic,kxy]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_0_0.csv"))
nr_crossings=6
nr_factors=16
p_code_1 = 0
p_code_2 = 0
crossing = [elxl,pqwvq]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [kcl]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [qdxl,chtr,pqjfxe]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [geiwkq,ixq,qybwhm]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [nevkb,qyv,cxuy]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [gnpfhs,mxi,sic,kxy]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
