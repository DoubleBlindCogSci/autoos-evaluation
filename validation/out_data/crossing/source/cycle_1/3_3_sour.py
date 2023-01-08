from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
bvrc = Factor("bvrc", ["chb", "zfa"])
gnkk = Factor("gnkk", ["uwfmoy", "rczsyd"])
bgdoo = Factor("bgdoo", ["qfjwa", "gaa"])
attkxk = Factor("attkxk", ["yie", "ywta"])
wmn = Factor("wmn", ["gqurzb", "jfwvin"])
zidbk = Factor("zidbk", ["bvbden", "abrqx"])
nmdfv = Factor("nmdfv", ["zocjk", "rutxzw"])
cpms = Factor("cpms", ["btbxko", "qszaqm"])
sbfi = Factor("sbfi", ["gld", "tnj"])
fybrof = Factor("fybrof", ["cbmi", "kanviz"])

### EXPERIMENT
design=[bvrc,gnkk,bgdoo,attkxk,wmn,zidbk,nmdfv,cpms,sbfi,fybrof]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_3_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_3_0.csv"))
nr_crossings=3
nr_factors=10
p_code_1 = 0
p_code_2 = 0
crossing = [bvrc,gnkk]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [bgdoo,attkxk,wmn,zidbk]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [nmdfv,cpms,sbfi,fybrof]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
