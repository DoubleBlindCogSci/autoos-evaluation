from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ctp = Factor("ctp", ["sizc", "gjak"])
owqya = Factor("owqya", ["bdv", "oysyep"])
epwhv = Factor("epwhv", ["ify", "sytoh"])
fbaze = Factor("fbaze", ["qnwg", "zvmwas"])
qrrk = Factor("qrrk", ["eaa", "dpo"])
zentca = Factor("zentca", ["rtfgcn", "oskm"])

### EXPERIMENT
design=[ctp,owqya,epwhv,fbaze,qrrk,zentca]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_0.csv"))
nr_crossings = 1
nr_factors=6
p_code_1 = 0
p_code_2 = 0
crossing = [ctp,owqya,epwhv,fbaze,qrrk,zentca]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
