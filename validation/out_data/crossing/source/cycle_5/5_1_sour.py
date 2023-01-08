from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wee = Factor("wee", ["zjoqhd", "krk"])
dgz = Factor("dgz", ["wxbpos", "lcne"])
ouvm = Factor("ouvm", ["buliuk", "gsli"])
deh = Factor("deh", ["sfg", "ldnpt"])
neqfot = Factor("neqfot", ["hnppn", "dfgbv"])
aog = Factor("aog", ["cshz", "yovat"])
qfmfp = Factor("qfmfp", ["msqhgh", "ymgtp"])
klty = Factor("klty", ["yglpr", "ncamk"])
keuta = Factor("keuta", ["fxgp", "skmu"])
bejhda = Factor("bejhda", ["hhqy", "nzxijm"])
whd = Factor("whd", ["tertin", "hjt"])
jchi = Factor("jchi", ["zxqfuw", "flxay"])
wvuhk = Factor("wvuhk", ["dtsl", "zqn"])

### EXPERIMENT
design=[wee,dgz,ouvm,deh,neqfot,aog,qfmfp,klty,keuta,bejhda,whd,jchi,wvuhk]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_1_0.csv"))
nr_crossings=5
nr_factors=13
p_code_1 = 0
p_code_2 = 0
crossing = [wee,dgz,ouvm,deh]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [neqfot,aog,qfmfp,klty]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [keuta]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [bejhda]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [whd,jchi,wvuhk]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
