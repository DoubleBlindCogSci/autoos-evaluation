from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
srym = Factor("srym", ["lhdm", "iavkmi"])
qjvf = Factor("qjvf", ["nerlf", "toyjbk"])
qbbty = Factor("qbbty", ["bfkw", "wpodjm"])
dnjsfg = Factor("dnjsfg", ["ssyqhd", "prue"])
oyrqzq = Factor("oyrqzq", ["fvzixl", "piwnd"])
wjnwkf = Factor("wjnwkf", ["tccsjk", "rintt"])
gdrvz = Factor("gdrvz", ["fovkuy", "xyexzp"])
wndi = Factor("wndi", ["thujwp", "bgyy"])
omcui = Factor("omcui", ["hsey", "qywyk"])
yxhi = Factor("yxhi", ["ubjjc", "phbd"])
wnfy = Factor("wnfy", ["nadtv", "mkpzpn"])
constraints = []
crossing = [[ qbbty, dnjsfg, oyrqzq],[ wjnwkf, gdrvz],[ wndi, omcui],[srym, qjvf],[ wnfy],[ yxhi],]


design=[srym,qjvf,qbbty,dnjsfg,oyrqzq,wjnwkf,gdrvz,wndi,omcui,yxhi,wnfy]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/6_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/6_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [ qbbty, dnjsfg, oyrqzq]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ wjnwkf, gdrvz]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ wndi, omcui]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [srym, qjvf]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ wnfy]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ yxhi]
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
