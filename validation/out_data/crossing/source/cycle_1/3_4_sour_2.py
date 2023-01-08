from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
cuifi = Factor("cuifi", ["xmyzsu", "nlhh"])
miyu = Factor("miyu", ["zshea", "wdht"])
alkgs = Factor("alkgs", ["uia", "ndxara"])
ucn = Factor("ucn", ["vweh", "wuutz"])
ped = Factor("ped", ["ycsmkq", "uoqst"])
fxkg = Factor("fxkg", ["nunbpb", "nyvhp"])
sray = Factor("sray", ["vgvvo", "uuux"])
almiim = Factor("almiim", ["ybcgog", "quj"])
constraints = []
crossing = [[cuifi, miyu, alkgs], [ucn, ped, fxkg], [sray, almiim]]


design=[cuifi,miyu,alkgs,ucn,ped,fxkg,sray,almiim]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_4_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_4_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [cuifi, miyu, alkgs]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ ucn, ped, fxkg]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ sray, almiim]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
