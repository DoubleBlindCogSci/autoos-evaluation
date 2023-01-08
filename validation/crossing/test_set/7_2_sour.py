from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xtf = Factor("xtf", ["cbi", "xsk"])
vcblky = Factor("vcblky", ["skpvas", "ihho"])
blv = Factor("blv", ["ypksjf", "ilui"])
fnhazr = Factor("fnhazr", ["qnv", "bdhyn"])
isjn = Factor("isjn", ["gqsdeg", "idk"])
lyls = Factor("lyls", ["veq", "hvdnc"])
idw = Factor("idw", ["frbr", "lapno"])

### EXPERIMENT
design=[xtf,vcblky,blv,fnhazr,isjn,lyls,idw]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_2_0.csv"))
nr_crossings = 1
nr_factors=7
p_code_1 = 0
p_code_2 = 0
crossing = xtf
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = vcblky
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = blv
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = fnhazr
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = isjn
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = lyls
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = idw
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [xtf,vcblky,blv,fnhazr,isjn,lyls,idw]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
