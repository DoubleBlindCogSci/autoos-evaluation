from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tqsng = Factor("tqsng", ["bhda", "akda"])
mkh = Factor("mkh", ["takc", "gutyuz"])
fieq = Factor("fieq", ["blelt", "cbb"])
fljmr = Factor("fljmr", ["bvwupc", "iwlcuk"])
ktpjut = Factor("ktpjut", ["shteo", "dsgk"])

### EXPERIMENT
design=[tqsng,mkh,fieq,fljmr,ktpjut]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_4_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_4_0.csv"))
nr_crossings = 1
nr_factors=5
p_code_1 = 0
p_code_2 = 0
crossing = tqsng
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = mkh
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = fieq
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = fljmr
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = ktpjut
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [tqsng,mkh,fieq,fljmr,ktpjut]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
