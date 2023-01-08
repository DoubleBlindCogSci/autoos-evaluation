from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
rwkz = Factor("rwkz", ["vtddew", "rha"])
dhuwc = Factor("dhuwc", ["mklqzk", "zyquia"])
moadg = Factor("moadg", ["lpr", "cawkn"])
otjxz = Factor("otjxz", ["vlifgg", "lxpn"])
hqvz = Factor("hqvz", ["vlm", "lqjayy"])
zmrh = Factor("zmrh", ["zgd", "bppzyn"])
lwxlx = Factor("lwxlx", ["efkalb", "xjrbbf"])
cumsze = Factor("cumsze", ["emcjm", "jwyyg"])
pgsh = Factor("pgsh", ["wakkb", "bnl"])
yfmdz = Factor("yfmdz", ["rtm", "iophnl"])
azcv = Factor("azcv", ["iqnhr", "mlenr"])
sonr = Factor("sonr", ["axek", "gvhme"])
swg = Factor("swg", ["kxhb", "xoxaiz"])
constraints = []
crossing = [[rwkz, dhuwc, moadg], [otjxz, hqvz, zmrh, lwxlx], [cumsze, pgsh, yfmdz], [azcv, sonr, swg]]


design=[rwkz,dhuwc,moadg,otjxz,hqvz,zmrh,lwxlx,cumsze,pgsh,yfmdz,azcv,sonr,swg]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/5_0_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/5_0_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [rwkz, dhuwc, moadg]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ otjxz, hqvz, zmrh, lwxlx]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ cumsze, pgsh, yfmdz]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ azcv, sonr, swg]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
