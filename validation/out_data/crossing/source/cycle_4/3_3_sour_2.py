from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
hqprq = Factor("hqprq", ["uiukoq", "mwwmjt"])
nojzr = Factor("nojzr", ["tqjxm", "aktrgm"])
izxwg = Factor("izxwg", ["bxbrh", "ipq"])
tola = Factor("tola", ["drlmk", "pucl"])
xrfvnt = Factor("xrfvnt", ["zto", "bipe"])
xfqckj = Factor("xfqckj", ["ptrv", "wedek"])
doyf = Factor("doyf", ["xolhdn", "wilzr"])
constraints = []
crossing = [[hqprq, nojzr], [izxwg, tola, xrfvnt, xfqckj], [doyf]]


design=[hqprq,nojzr,izxwg,tola,xrfvnt,xfqckj,doyf]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [hqprq, nojzr]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ izxwg, tola, xrfvnt, xfqckj]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ doyf]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
