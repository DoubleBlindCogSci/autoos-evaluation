from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
ovlqa = Factor("ovlqa", ["xvv", "zfec"])
gmw = Factor("gmw", ["jwk", "loh"])
qofs = Factor("qofs", ["wluel", "fvux"])
aqd = Factor("aqd", ["koxhpg", "oebb"])
vnep = Factor("vnep", ["oppxtt", "svc"])
wuitvb = Factor("wuitvb", ["wqxab", "cunto"])
fjk = Factor("fjk", ["ejzvzj", "olo"])
dwvkng = Factor("dwvkng", ["oghxlr", "agq"])
xpbstl = Factor("xpbstl", ["gir", "uwsdf"])
pabkm = Factor("pabkm", ["alezzi", "sjmzuf"])
yofn = Factor("yofn", ["qclyyp", "ywk"])
ghorsd = Factor("ghorsd", ["gdj", "uwcjnf"])
hczscb = Factor("hczscb", ["xko", "gcv"])
constraints = []
crossing = [[ovlqa, gmw], [qofs, aqd, vnep, wuitvb, fjk, dwvkng, xpbstl, pabkm, yofn, ghorsd, hczscb]]


design=[ovlqa,gmw,qofs,aqd,vnep,wuitvb,fjk,dwvkng,xpbstl,pabkm,yofn,ghorsd,hczscb]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/6_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/6_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [ovlqa, gmw]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ qofs, aqd, vnep, wuitvb, fjk, dwvkng, xpbstl, pabkm, yofn, ghorsd, hczscb]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
