from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
xrmdtq = Factor("xrmdtq", ["qsdwuv", "rtel"])
lejj = Factor("lejj", ["czoo", "dnmdzs"])
hqht = Factor("hqht", ["elxnc", "mxzpkv"])
constraints = []
crossing = [xrmdtq, lejj, hqht]


design=[xrmdtq,lejj,hqht]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/1_4_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/1_4_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [xrmdtq, lejj, hqht]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
