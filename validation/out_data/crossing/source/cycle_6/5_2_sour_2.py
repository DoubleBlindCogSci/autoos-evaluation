from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
pjmy = Factor("pjmy", ["xvrb", "tjmz"])
lusfem = Factor("lusfem", ["oxvc", "omcx"])
zsta = Factor("zsta", ["lbnkco", "rpk"])
vae = Factor("vae", ["xkpucs", "vxrft"])
dpx = Factor("dpx", ["aina", "izvh"])
rwf = Factor("rwf", ["ktjd", "zhfxox"])
eyik = Factor("eyik", ["lutgng", "oguc"])
tqkcmk = Factor("tqkcmk", ["diwa", "fhnprz"])
uog = Factor("uog", ["ipssyq", "ayzcg"])
deayhu = Factor("deayhu", ["lyrfma", "iagvfk"])
zpa = Factor("zpa", ["qgxok", "dlkmzh"])
ame = Factor("ame", ["flhz", "snx"])
jrbu = Factor("jrbu", ["mkecrz", "tpqsvu"])
dzwu = Factor("dzwu", ["txb", "vsm"])
ymwjh = Factor("ymwjh", ["fubc", "xqljtv"])
constraints = []
crossing = [[ jrbu, dzwu, ymwjh],[ eyik, tqkcmk, uog],[pjmy, lusfem, zsta],[ deayhu, zpa, ame],[ vae, dpx, rwf],]


design=[pjmy,lusfem,zsta,vae,dpx,rwf,eyik,tqkcmk,uog,deayhu,zpa,ame,jrbu,dzwu,ymwjh]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/5_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/5_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [ jrbu, dzwu, ymwjh]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ eyik, tqkcmk, uog]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [pjmy, lusfem, zsta]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ deayhu, zpa, ame]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ vae, dpx, rwf]
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
