from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
dcn = Factor("dcn", ["szf", "xhcu"])
waqn = Factor("waqn", ["mcwz", "mley"])
vqoxup = Factor("vqoxup", ["zorblp", "mkigli"])
mdpk = Factor("mdpk", ["pueyki", "nqmkrm"])
iekv = Factor("iekv", ["rfkf", "gda"])
oghk = Factor("oghk", ["qfaux", "yhog"])
iiefi = Factor("iiefi", ["usztr", "olg"])
pxm = Factor("pxm", ["gupww", "egk"])
dkycj = Factor("dkycj", ["ovkguy", "qkhc"])
mwq = Factor("mwq", ["qlvmkc", "qfmitq"])
aif = Factor("aif", ["pzlitx", "ipxh"])
pus = Factor("pus", ["fdnq", "yodje"])
constraints = []
crossing = [[dcn, waqn, vqoxup, mdpk], [iekv, oghk, iiefi, pxm], [dkycj, mwq], [aif, pus]]


design=[dcn,waqn,vqoxup,mdpk,iekv,oghk,iiefi,pxm,dkycj,mwq,aif,pus]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_6_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_6_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [dcn, waqn, vqoxup, mdpk]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ iekv, oghk, iiefi, pxm]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ dkycj, mwq]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ aif, pus]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
