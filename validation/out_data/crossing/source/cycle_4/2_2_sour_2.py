from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
hqvr = Factor("hqvr", ["tzen", "coy"])
ujagxt = Factor("ujagxt", ["cgog", "ufzdj"])
mbg = Factor("mbg", ["dbgrs", "hadedm"])
gokba = Factor("gokba", ["ehywrw", "beod"])
hre = Factor("hre", ["ewm", "buahn"])
ecwe = Factor("ecwe", ["opgm", "cti"])
constraints = []
crossing = [[hqvr, ujagxt], [mbg, gokba, hre, ecwe]]


design=[hqvr,ujagxt,mbg,gokba,hre,ecwe]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/2_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/2_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [hqvr, ujagxt]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ mbg, gokba, hre, ecwe]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
