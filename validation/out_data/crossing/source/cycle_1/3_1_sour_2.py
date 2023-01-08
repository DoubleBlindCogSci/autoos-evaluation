from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
tdaqb = Factor("tdaqb", ["reoeyq", "ookpdw"])
faxxc = Factor("faxxc", ["iuvvk", "ognzj"])
sglcyh = Factor("sglcyh", ["cpfgqu", "dgeuxo"])
scr = Factor("scr", ["osrf", "rjej"])
ttr = Factor("ttr", ["igczf", "wzbs"])
symi = Factor("symi", ["byclc", "elkhw"])
meuhum = Factor("meuhum", ["wpwcp", "zsmxnj"])
constraints = []
crossing = [[tdaqb, faxxc, sglcyh], [scr, ttr, symi, meuhum]]


design=[tdaqb,faxxc,sglcyh,scr,ttr,symi,meuhum]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [tdaqb, faxxc, sglcyh]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ scr, ttr, symi, meuhum]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
