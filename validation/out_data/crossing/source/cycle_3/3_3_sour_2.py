from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
picf = Factor("picf", ["uyji", "gmtsln"])
lewswm = Factor("lewswm", ["ajvrl", "eid"])
vynvl = Factor("vynvl", ["rgw", "xdzjqs"])
uuq = Factor("uuq", ["tgldwu", "avk"])
yxbicy = Factor("yxbicy", ["amhp", "gskkwy"])
ogizvb = Factor("ogizvb", ["clazw", "kwy"])
pnn = Factor("pnn", ["jrdbhn", "ttbn"])
xnl = Factor("xnl", ["ndz", "tyomqi"])
fbdrvy = Factor("fbdrvy", ["lvq", "twmfmc"])
constraints = []
crossing = [[picf, lewswm, vynvl], [uuq, yxbicy], [ogizvb, pnn, xnl, fbdrvy]]


design=[picf,lewswm,vynvl,uuq,yxbicy,ogizvb,pnn,xnl,fbdrvy]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [picf, lewswm, vynvl]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ uuq, yxbicy]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ ogizvb, pnn, xnl, fbdrvy]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
