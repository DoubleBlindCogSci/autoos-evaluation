from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
fchlax = Factor("fchlax", ["rrxgg", "vej"])
tyk = Factor("tyk", ["zulume", "fqhh"])
sdtf = Factor("sdtf", ["uej", "mmhiio"])
ues = Factor("ues", ["uols", "tiy"])
mgw = Factor("mgw", ["ubr", "dta"])
pbbno = Factor("pbbno", ["qdiqdy", "jsm"])
ruwiv = Factor("ruwiv", ["cxrs", "icb"])
khq = Factor("khq", ["uce", "wwi"])
unx = Factor("unx", ["rajj", "rvmuo"])
lkcp = Factor("lkcp", ["ptdk", "dnttu"])
zylbl = Factor("zylbl", ["tkpms", "xllmgx"])
hehd = Factor("hehd", ["kml", "ysefia"])
jrqn = Factor("jrqn", ["zjxlt", "bule"])
constraints = []
crossing = [[fchlax, tyk, sdtf, ues, mgw], [pbbno, ruwiv], [khq, unx, lkcp], [zylbl, hehd, jrqn]]


design=[fchlax,tyk,sdtf,ues,mgw,pbbno,ruwiv,khq,unx,lkcp,zylbl,hehd,jrqn]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/5_5_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/5_5_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [fchlax, tyk, sdtf, ues, mgw]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ pbbno, ruwiv]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ khq, unx, lkcp]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ zylbl, hehd, jrqn]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
