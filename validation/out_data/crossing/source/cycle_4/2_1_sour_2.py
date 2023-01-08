from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
dmkl = Factor("dmkl", ["vho", "zkj"])
ansje = Factor("ansje", ["bogw", "vcub"])
zffjgs = Factor("zffjgs", ["yckc", "ayr"])
ashmc = Factor("ashmc", ["wfdi", "pmvu"])
hiw = Factor("hiw", ["fspw", "aop"])
constraints = []
crossing = [[dmkl], [ansje, zffjgs, ashmc, hiw]]


design=[dmkl,ansje,zffjgs,ashmc,hiw]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/2_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/2_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [dmkl]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ ansje, zffjgs, ashmc, hiw]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
