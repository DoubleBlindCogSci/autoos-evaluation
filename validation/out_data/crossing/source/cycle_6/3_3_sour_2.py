from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
xyhn = Factor("xyhn", ["icwff", "nnf"])
rvrao = Factor("rvrao", ["rajkbb", "xzc"])
axio = Factor("axio", ["pwdgf", "wvt"])
yfbaat = Factor("yfbaat", ["ikexn", "bnevbc"])
mrgl = Factor("mrgl", ["xzqi", "loqbrj"])
qdg = Factor("qdg", ["isr", "exdeo"])
jiodvp = Factor("jiodvp", ["dlll", "fgg"])
constraints = []
crossing = [[ mrgl, qdg, jiodvp],[ axio, yfbaat],[xyhn, rvrao],]


design=[xyhn,rvrao,axio,yfbaat,mrgl,qdg,jiodvp]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [ mrgl, qdg, jiodvp]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ axio, yfbaat]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [xyhn, rvrao]
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
