from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
vxx = Factor("vxx", ["ipqlh", "czkm"])
wvrkd = Factor("wvrkd", ["jwa", "thffyc"])
gyugef = Factor("gyugef", ["cmsnpp", "kwqt"])
hela = Factor("hela", ["qkako", "uqlb"])
revmdb = Factor("revmdb", ["zcnlwb", "lfc"])
zrw = Factor("zrw", ["mhvbfw", "irhrq"])
ekgxsj = Factor("ekgxsj", ["ckhdof", "qmypg"])
cgjwi = Factor("cgjwi", ["lbuo", "vwqj"])
ail = Factor("ail", ["zfb", "tdbehl"])
sfqc = Factor("sfqc", ["ljxwr", "pbxs"])
nevz = Factor("nevz", ["ivad", "zqkn"])
constraints = []
crossing = [[vxx, wvrkd, gyugef, hela], [revmdb, zrw, ekgxsj, cgjwi], [ail, sfqc, nevz]]


design=[vxx,wvrkd,gyugef,hela,revmdb,zrw,ekgxsj,cgjwi,ail,sfqc,nevz]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [vxx, wvrkd, gyugef, hela]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ revmdb, zrw, ekgxsj, cgjwi]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ ail, sfqc, nevz]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
