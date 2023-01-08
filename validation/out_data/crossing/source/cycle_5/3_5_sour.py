from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ipr = Factor("ipr", ["ims", "pflynz"])
mzq = Factor("mzq", ["jjbay", "wcdq"])
xtvepx = Factor("xtvepx", ["fipbp", "bildsx"])
qkb = Factor("qkb", ["xsyes", "nbnh"])
eszmjd = Factor("eszmjd", ["dee", "xpit"])
ydy = Factor("ydy", ["jbdsj", "ecqixf"])
hvbry = Factor("hvbry", ["jzjc", "ffknc"])
bbpkkg = Factor("bbpkkg", ["vfqv", "uvrbps"])
xtpx = Factor("xtpx", ["vcqmr", "xeeb"])

### EXPERIMENT
design=[ipr,mzq,xtvepx,qkb,eszmjd,ydy,hvbry,bbpkkg,xtpx]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_5_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_5_0.csv"))
nr_crossings=3
nr_factors=9
p_code_1 = 0
p_code_2 = 0
crossing = [ipr]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [mzq,xtvepx,qkb,eszmjd]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ydy,hvbry,bbpkkg,xtpx]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
