from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
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
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/6_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/6_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [quhsl,tspj,dwtliw,kipdl]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [nqa,hpsau,vtpq,bxwiuo]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [rzocy,kzy,qyxq,lzgci]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [rzna,koabuf,qlxmc]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ystfh,zoso]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [zmitzu]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
nr_crossings = 6
nr_factors = 18
df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
