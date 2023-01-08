from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xus = Factor("xus", ["jidj", "wiqy"])
aqxogw = Factor("aqxogw", ["culmql", "vncenr"])
gfauq = Factor("gfauq", ["ygxxx", "zacq"])
jok = Factor("jok", ["priu", "yukw"])
wgfvtm = Factor("wgfvtm", ["umjh", "wieqwy"])
pvzvld = Factor("pvzvld", ["jjsvw", "isl"])

### EXPERIMENT
design=[xus,aqxogw,gfauq,jok,wgfvtm,pvzvld]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0.csv"))
nr_crossings=3
nr_factors=6
p_code_1 = 0
p_code_2 = 0
crossing = [xus,aqxogw,gfauq]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [jok,wgfvtm]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [pvzvld]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
