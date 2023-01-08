from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
kfn = Factor("kfn", ["yxl", "bcomrr"])
fxnb = Factor("fxnb", ["jyqgj", "vcj"])
nfneo = Factor("nfneo", ["wrk", "mes"])
yeorq = Factor("yeorq", ["gdrghk", "zddjuj"])
alfwgo = Factor("alfwgo", ["zeb", "wqiwq"])
constraints = []
crossing = [[kfn], [fxnb, nfneo, yeorq, alfwgo]]


design=[kfn,fxnb,nfneo,yeorq,alfwgo]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [kfn]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ fxnb, nfneo, yeorq, alfwgo]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
