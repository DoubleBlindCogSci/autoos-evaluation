from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qsg = Factor("qsg", ["lkiivd", "vdhnt"])
olhl = Factor("olhl", ["cons", "srrji"])
onnhvg = Factor("onnhvg", ["fqx", "kfr"])
jrlk = Factor("jrlk", ["wvm", "uxht"])
bhsums = Factor("bhsums", ["wrnx", "tmrd"])
oednti = Factor("oednti", ["tetu", "jmr"])
aapttm = Factor("aapttm", ["mvpxw", "nrwdl"])
awrp = Factor("awrp", ["viczx", "syi"])
yxlzu = Factor("yxlzu", ["nyxnue", "ykl"])
ynlt = Factor("ynlt", ["ckwnk", "lnyj"])
lew = Factor("lew", ["rvdl", "khxxrj"])
amd = Factor("amd", ["fltecy", "dwwqbf"])
mpsyg = Factor("mpsyg", ["xjk", "vzs"])

### EXPERIMENT
design=[qsg,olhl,onnhvg,jrlk,bhsums,oednti,aapttm,awrp,yxlzu,ynlt,lew,amd,mpsyg]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_3_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_3_0.csv"))
nr_crossings=4
nr_factors=13
p_code_1 = 0
p_code_2 = 0
crossing = [qsg,olhl,onnhvg,jrlk]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [bhsums,oednti]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [aapttm,awrp,yxlzu]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ynlt,lew,amd,mpsyg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
