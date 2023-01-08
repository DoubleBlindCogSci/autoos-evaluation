from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
pskm = Factor("pskm", ["qyfi", "lbgpxh"])
gvrb = Factor("gvrb", ["fgga", "mzyjc"])
layijh = Factor("layijh", ["qqag", "jpcc"])
txyx = Factor("txyx", ["dkz", "aqwho"])
cmroqn = Factor("cmroqn", ["vazbo", "jjv"])
hqebl = Factor("hqebl", ["hgmkpq", "lrqd"])
shpzn = Factor("shpzn", ["xxjjwh", "klfswg"])
gew = Factor("gew", ["wrlow", "mlawg"])
jznr = Factor("jznr", ["sdc", "sboxd"])
yulqsk = Factor("yulqsk", ["tstpr", "qovok"])
dtpt = Factor("dtpt", ["bbva", "fpw"])
syp = Factor("syp", ["fvd", "vznm"])
yeykw = Factor("yeykw", ["jlvmd", "njtm"])
mckky = Factor("mckky", ["ftsvmu", "yjv"])
constraints = []
crossing = [[ layijh, txyx, cmroqn, hqebl],[ syp, yeykw, mckky],[ yulqsk, dtpt],[ shpzn, gew],[pskm, gvrb],[ jznr],]


design=[pskm,gvrb,layijh,txyx,cmroqn,hqebl,shpzn,gew,jznr,yulqsk,dtpt,syp,yeykw,mckky]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/6_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/6_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [ layijh, txyx, cmroqn, hqebl]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ syp, yeykw, mckky]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ yulqsk, dtpt]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ shpzn, gew]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [pskm, gvrb]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ jznr]
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
