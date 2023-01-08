from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rxh = Factor("rxh", ["yzi", "fqwrs"])
zvocuf = Factor("zvocuf", ["cmhub", "bebv"])
yvhe = Factor("yvhe", ["kjzw", "fijsg"])
wofih = Factor("wofih", ["rpvkm", "mmh"])

### EXPERIMENT
design=[rxh,zvocuf,yvhe,wofih]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_4_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_4_0.csv"))
nr_crossings = 1
nr_factors=4
p_code_1 = 0
p_code_2 = 0
crossing = rxh
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = zvocuf
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = yvhe
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = wofih
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [rxh,zvocuf,yvhe,wofih]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
