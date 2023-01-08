from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
vrmqfy = Factor("vrmqfy", ["fussar", "jsff"])
mwxic = Factor("mwxic", ["ovl", "mxwe"])
whnrth = Factor("whnrth", ["jtprjg", "qux"])
ghof = Factor("ghof", ["axgbh", "onptzf"])
talxq = Factor("talxq", ["nwji", "fllj"])
pif = Factor("pif", ["vnpxo", "jswoy"])
wuhtbc = Factor("wuhtbc", ["otv", "tay"])
efum = Factor("efum", ["vnbe", "uqyc"])
bnmyb = Factor("bnmyb", ["zuxxq", "rxbxbi"])
hwaio = Factor("hwaio", ["jtybi", "cmlp"])
constraints = []
crossing = [[ mwxic, whnrth, ghof],[ efum, bnmyb, hwaio],[ talxq, pif, wuhtbc],[vrmqfy],]


design=[vrmqfy,mwxic,whnrth,ghof,talxq,pif,wuhtbc,efum,bnmyb,hwaio]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [ mwxic, whnrth, ghof]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ efum, bnmyb, hwaio]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ talxq, pif, wuhtbc]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [vrmqfy]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = []
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
