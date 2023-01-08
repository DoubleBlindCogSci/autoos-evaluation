from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ntn = Factor("ntn", ["pzf", "brjg"])
avbl = Factor("avbl", ["kgxjut", "ptlzjd"])
czjb = Factor("czjb", ["nztwlf", "equjjz"])
rbrro = Factor("rbrro", ["kcgv", "eqx"])
teosi = Factor("teosi", ["hafgvn", "mend"])
jlp = Factor("jlp", ["kjshow", "vfzvdy"])
qglvta = Factor("qglvta", ["qhopii", "zfnsvy"])
ixq = Factor("ixq", ["grv", "vzd"])
wij = Factor("wij", ["lvptf", "gqrr"])
purl = Factor("purl", ["riavs", "pfao"])
baih = Factor("baih", ["yvz", "ymd"])
fhvv = Factor("fhvv", ["nutx", "xpv"])
vdc = Factor("vdc", ["ojvxll", "hafzm"])
hyeq = Factor("hyeq", ["bxtcrc", "nemz"])

### EXPERIMENT
design=[ntn,avbl,czjb,rbrro,teosi,jlp,qglvta,ixq,wij,purl,baih,fhvv,vdc,hyeq]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/6_0_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/6_0_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [avbl,czjb,rbrro,teosi]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [baih,fhvv,vdc,hyeq]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [qglvta,ixq,wij]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [purl]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [jlp]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ntn]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
nr_crossings = 6
nr_factors = 14
df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
