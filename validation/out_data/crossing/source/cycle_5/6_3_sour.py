from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
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
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_3_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_3_0.csv"))
nr_crossings=6
nr_factors=17
p_code_1 = 0
p_code_2 = 0
crossing = [xoapz]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [gpsnc,enj,lmmq,mfyos]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [pwpk,qntnmx,rbg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [iqa,ddt]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [fbaktv,mtgm,fkp]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [zhgeq,qbog,mzor,kaikdk]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
