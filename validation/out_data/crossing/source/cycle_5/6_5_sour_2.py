from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
hvee = Factor("hvee", ["xaq", "xqq"])
vktw = Factor("vktw", ["wedzy", "axdxh"])
zib = Factor("zib", ["pgy", "qegt"])
cwtvf = Factor("cwtvf", ["fikzxw", "hsrlo"])
gfti = Factor("gfti", ["ldvi", "dkg"])
pvqim = Factor("pvqim", ["zys", "eudc"])
czij = Factor("czij", ["qrzr", "mqlnbp"])
rzfw = Factor("rzfw", ["qhvs", "vrag"])
iaebrr = Factor("iaebrr", ["kvevqa", "romx"])
cprzzu = Factor("cprzzu", ["heehbt", "slxdjd"])
lcgs = Factor("lcgs", ["siykq", "bjkap"])
whlm = Factor("whlm", ["hymgil", "mxkvi"])
wedc = Factor("wedc", ["alnd", "bgzc"])
adp = Factor("adp", ["qel", "yaftk"])
xfj = Factor("xfj", ["hgw", "uiwyn"])
fog = Factor("fog", ["xbu", "axyhq"])
jxtxma = Factor("jxtxma", ["tnhlvi", "iwfx"])
constraints = []
crossing = [[hvee, vktw, zib, cwtvf], [gfti, pvqim, czij, rzfw], [iaebrr, cprzzu, lcgs], [whlm, wedc, adp], [xfj, fog], [jxtxma]]


design=[hvee,vktw,zib,cwtvf,gfti,pvqim,czij,rzfw,iaebrr,cprzzu,lcgs,whlm,wedc,adp,xfj,fog,jxtxma]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/6_5_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/6_5_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [hvee, vktw, zib, cwtvf]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ gfti, pvqim, czij, rzfw]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ iaebrr, cprzzu, lcgs]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ whlm, wedc, adp]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ xfj, fog]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ jxtxma]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
