from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
xmm = Factor("xmm", ["czc", "indw"])
cjry = Factor("cjry", ["vyc", "ysdm"])
eymoy = Factor("eymoy", ["djt", "vzndld"])
jkjp = Factor("jkjp", ["zbidzn", "terh"])
yjs = Factor("yjs", ["acnmty", "veoqvv"])
constraints = []
crossing = [[xmm, cjry, eymoy, jkjp], [yjs]]


design=[xmm,cjry,eymoy,jkjp,yjs]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/2_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/2_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [xmm, cjry, eymoy, jkjp]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ yjs]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
