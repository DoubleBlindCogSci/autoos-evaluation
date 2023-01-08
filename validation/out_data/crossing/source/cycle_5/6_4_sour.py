from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sltrm = Factor("sltrm", ["mhsus", "jzhbu"])
gxvyt = Factor("gxvyt", ["jcuyrv", "aof"])
lrh = Factor("lrh", ["xtd", "xlb"])
kysk = Factor("kysk", ["fkkujk", "zlkc"])
juxz = Factor("juxz", ["izv", "fah"])
fck = Factor("fck", ["ytvv", "wzh"])
tbobi = Factor("tbobi", ["hif", "gny"])
gjod = Factor("gjod", ["opb", "vqfr"])
wlfiko = Factor("wlfiko", ["tbg", "ssumnb"])
jdas = Factor("jdas", ["edrl", "jay"])
gghrp = Factor("gghrp", ["zrxc", "pfeqt"])
emq = Factor("emq", ["fervwz", "cun"])
ugo = Factor("ugo", ["llq", "mbb"])
gxaro = Factor("gxaro", ["hieop", "knh"])

### EXPERIMENT
design=[sltrm,gxvyt,lrh,kysk,juxz,fck,tbobi,gjod,wlfiko,jdas,gghrp,emq,ugo,gxaro]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_4_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_4_0.csv"))
nr_crossings=6
nr_factors=14
p_code_1 = 0
p_code_2 = 0
crossing = [sltrm,gxvyt,lrh]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [kysk]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [juxz,fck,tbobi]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [gjod]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [wlfiko,jdas,gghrp,emq]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ugo,gxaro]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
