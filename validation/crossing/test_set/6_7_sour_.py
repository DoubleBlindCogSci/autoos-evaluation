from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wmfo = Factor("wmfo", ["pdloah", "kgpj"])
rqhpgd = Factor("rqhpgd", ["tzflh", "mqlae"])
jobz = Factor("jobz", ["qeweeh", "uxvd"])
ygd = Factor("ygd", ["vll", "yhhwqb"])
tbfb = Factor("tbfb", ["jgjwtk", "rnmpmf"])
aik = Factor("aik", ["sbzmfr", "pqpwy"])

### EXPERIMENT
design=[wmfo,rqhpgd,jobz,ygd,tbfb,aik]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_7_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_7_0.csv"))
nr_crossings = 1
nr_factors=6
p_code_1 = 0
p_code_2 = 0
crossing = [wmfo,rqhpgd,jobz,ygd,tbfb,aik]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
