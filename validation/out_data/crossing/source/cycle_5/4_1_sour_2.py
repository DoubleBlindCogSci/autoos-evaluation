from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
xoy = Factor("xoy", ["pxh", "yyoerd"])
enxal = Factor("enxal", ["fooego", "nvkk"])
lcxe = Factor("lcxe", ["ymxua", "ttx"])
klsb = Factor("klsb", ["lbjxpl", "futrp"])
fllfip = Factor("fllfip", ["vsl", "eqf"])
axig = Factor("axig", ["dpn", "qqaf"])
brzoqj = Factor("brzoqj", ["asdbj", "nqz"])
constraints = []
crossing = [[xoy, enxal, lcxe, klsb], [axig, brzoqj]]


design=[xoy,enxal,lcxe,klsb,fllfip,axig,brzoqj]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [xoy, enxal, lcxe, klsb]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ axig, brzoqj]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
