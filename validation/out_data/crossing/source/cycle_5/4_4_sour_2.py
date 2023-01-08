from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
jmiuft = Factor("jmiuft", ["rnc", "dqdrtn"])
svdm = Factor("svdm", ["mbmol", "saesu"])
aksmc = Factor("aksmc", ["qfo", "yifmv"])
pcxmnv = Factor("pcxmnv", ["wmivwu", "higb"])
xka = Factor("xka", ["fkqkzs", "sfhg"])
juio = Factor("juio", ["rrpne", "ozmo"])
qdr = Factor("qdr", ["nat", "yddki"])
qjbhw = Factor("qjbhw", ["afh", "rkdgo"])
constraints = []
crossing = [[jmiuft, svdm], [aksmc, pcxmnv, xka], [juio, qdr, qjbhw]]


design=[jmiuft,svdm,aksmc,pcxmnv,xka,juio,qdr,qjbhw]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_4_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_4_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [jmiuft, svdm]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ aksmc, pcxmnv, xka]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ juio, qdr, qjbhw]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
