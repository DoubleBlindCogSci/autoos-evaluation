from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nhsc = Factor("nhsc", ["hbvvrp", "ioeya"])
hfxlmo = Factor("hfxlmo", ["wmgn", "poq"])
mwp = Factor("mwp", ["yziwti", "rns"])
tch = Factor("tch", ["whev", "fnfqa"])
zqb = Factor("zqb", ["arwngo", "lif"])
xtk = Factor("xtk", ["gyf", "cooh"])
pyvkfe = Factor("pyvkfe", ["upuuq", "osle"])
kfks = Factor("kfks", ["dnfel", "zslzc"])

### EXPERIMENT
design=[nhsc,hfxlmo,mwp,tch,zqb,xtk,pyvkfe,kfks]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0.csv"))
nr_crossings=3
nr_factors=8
p_code_1 = 0
p_code_2 = 0
crossing = [nhsc,hfxlmo,mwp]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [tch,zqb,xtk]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [pyvkfe,kfks]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
