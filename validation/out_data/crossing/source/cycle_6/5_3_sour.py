from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ymc = Factor("ymc", ["uyj", "ogz"])
utp = Factor("utp", ["ugeam", "btblx"])
tjkftk = Factor("tjkftk", ["xpo", "muf"])
yvy = Factor("yvy", ["xbv", "rcnus"])
knrww = Factor("knrww", ["eli", "eqoj"])
wjlkwe = Factor("wjlkwe", ["vjrjex", "geco"])
fqp = Factor("fqp", ["hbz", "lwu"])
ivlj = Factor("ivlj", ["apceqb", "sej"])
ems = Factor("ems", ["xjoxx", "wiei"])

### EXPERIMENT
design=[ymc,utp,tjkftk,yvy,knrww,wjlkwe,fqp,ivlj,ems]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/5_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/5_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [wjlkwe,fqp]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [yvy,knrww]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ivlj,ems]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [tjkftk]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ymc,utp]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
nr_crossings = 5
nr_factors = 9
df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
