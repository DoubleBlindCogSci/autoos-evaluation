from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ktmnf = Factor("ktmnf", ["tie", "zzxf"])
nncpy = Factor("nncpy", ["vdrklk", "enhbkm"])
cgflq = Factor("cgflq", ["cybcua", "xqlfqu"])
coxoc = Factor("coxoc", ["vvq", "oid"])
icpxef = Factor("icpxef", ["evovf", "vlh"])
knlto = Factor("knlto", ["caj", "oxgxq"])
cmsfp = Factor("cmsfp", ["qslgt", "lvj"])

### EXPERIMENT
design=[ktmnf,nncpy,cgflq,coxoc,icpxef,knlto,cmsfp]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_4_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_4_0.csv"))
nr_crossings = 1
nr_factors=7
p_code_1 = 0
p_code_2 = 0
crossing = ktmnf
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = nncpy
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = cgflq
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = coxoc
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = icpxef
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = knlto
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = cmsfp
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ktmnf,nncpy,cgflq,coxoc,icpxef,knlto,cmsfp]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
