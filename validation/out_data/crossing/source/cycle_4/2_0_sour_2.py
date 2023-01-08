from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
pfqbgl = Factor("pfqbgl", ["jjdrdd", "ihrd"])
zwpkf = Factor("zwpkf", ["wvo", "bput"])
kmidu = Factor("kmidu", ["gdcuv", "cestss"])
constraints = []
crossing = [[pfqbgl, zwpkf], [kmidu]]


design=[pfqbgl,zwpkf,kmidu]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/2_0_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/2_0_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [pfqbgl, zwpkf]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ kmidu]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
