from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
lrlvkb = Factor("lrlvkb", ["xdm", "omt"])
bcuuqr = Factor("bcuuqr", ["ghui", "daqwq"])
etqenb = Factor("etqenb", ["fcajbk", "prbzrx"])
oyir = Factor("oyir", ["hkj", "zulbj"])
constraints = []
crossing = [[lrlvkb, bcuuqr, etqenb], [bcuuqr, etqenb], [oyir]]


design=[lrlvkb,bcuuqr,etqenb,oyir]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [lrlvkb, bcuuqr, etqenb]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ bcuuqr, etqenb]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ oyir]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
