from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
icb = Factor("icb", ["vozb", "udvch"])
oko = Factor("oko", ["ufevml", "pvz"])
jyrt = Factor("jyrt", ["qwld", "dzo"])
lrzm = Factor("lrzm", ["vfnke", "wtpdqc"])
yirntp = Factor("yirntp", ["vzw", "uxa"])
gntrzh = Factor("gntrzh", ["kongvk", "cnwen"])
wqcaq = Factor("wqcaq", ["fgdqg", "kuefbf"])
wqyrbn = Factor("wqyrbn", ["afjep", "vfh"])
bacsgk = Factor("bacsgk", ["iqnv", "utd"])
cdo = Factor("cdo", ["vtln", "axpg"])
divfwh = Factor("divfwh", ["xksa", "puajc"])
bredj = Factor("bredj", ["huwws", "uiygp"])
imfsa = Factor("imfsa", ["tfa", "yjp"])
cunyje = Factor("cunyje", ["myuyfx", "xsfei"])
kgpt = Factor("kgpt", ["hifxxa", "myzwfe"])

### EXPERIMENT
design=[icb,oko,jyrt,lrzm,yirntp,gntrzh,wqcaq,wqyrbn,bacsgk,cdo,divfwh,bredj,imfsa,cunyje,kgpt]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/5_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/5_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [gntrzh,wqcaq,wqyrbn,bacsgk]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [cdo,divfwh,bredj,imfsa]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [icb,oko,jyrt,lrzm]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [cunyje,kgpt]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [yirntp]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
nr_crossings = 5
nr_factors = 15
df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
