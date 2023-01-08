from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
qynjdf = Factor("qynjdf", ["fivb", "ledy"])
sjdzy = Factor("sjdzy", ["vgdc", "tkqah"])
vppj = Factor("vppj", ["snlc", "dcz"])
tspx = Factor("tspx", ["oylqj", "eig"])
armh = Factor("armh", ["vjpiyd", "mel"])
pckl = Factor("pckl", ["godmhm", "nwat"])
kxqwj = Factor("kxqwj", ["kwikrb", "fhirpl"])
nnj = Factor("nnj", ["xiszlu", "sdd"])
tajrj = Factor("tajrj", ["qaeiei", "qjso"])
gihrlk = Factor("gihrlk", ["qtqwl", "kdo"])
cal = Factor("cal", ["uokf", "dsdo"])
eig = Factor("eig", ["jtmxs", "fsl"])
fro = Factor("fro", ["mokh", "anhek"])
constraints = []
crossing = [[qynjdf, sjdzy, vppj, tspx], [armh, pckl, kxqwj, nnj, tajrj, gihrlk, cal, eig, fro]]


design=[qynjdf,sjdzy,vppj,tspx,armh,pckl,kxqwj,nnj,tajrj,gihrlk,cal,eig,fro]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_4_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_4_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [qynjdf, sjdzy, vppj, tspx]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ armh, pckl, kxqwj, nnj, tajrj, gihrlk, cal, eig, fro]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
