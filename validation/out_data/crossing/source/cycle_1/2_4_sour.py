from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
cvkizt = Factor("cvkizt", ["iyqtzz", "hikyaj"])
urm = Factor("urm", ["txrldj", "utm"])
stxg = Factor("stxg", ["rve", "mgz"])
wihk = Factor("wihk", ["vuxf", "rhm"])
rlxyvh = Factor("rlxyvh", ["wwpsc", "tszd"])
kpezd = Factor("kpezd", ["klyk", "bqc"])
knb = Factor("knb", ["opm", "lynvhh"])

### EXPERIMENT
design=[cvkizt,urm,stxg,wihk,rlxyvh,kpezd,knb]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_4_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_4_0.csv"))
nr_crossings=2
nr_factors=7
p_code_1 = 0
p_code_2 = 0
crossing = [cvkizt,urm,stxg]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [wihk,rlxyvh,kpezd,knb]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
