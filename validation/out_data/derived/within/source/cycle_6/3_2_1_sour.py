from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
clbqjx = Factor("clbqjx", ["ypb","bqttzr","rwf","hezs","yzx","koedqy"])
axqomn = Factor("axqomn", ["ypb","bqttzr","rwf","hezs","yzx","koedqy"])
ggxdbw = Factor("ggxdbw", ["ypb","bqttzr","rwf","hezs","yzx","koedqy"])
def yztmtc(clbqjx, axqomn, ggxdbw):
     return axqomn == clbqjx
def jylgrl(clbqjx, axqomn, ggxdbw):
     return axqomn != clbqjx and ggxdbw == clbqjx
def xiry(clbqjx, axqomn, ggxdbw):
     return (not clbqjx == axqomn) and (not jylgrl(clbqjx, axqomn, ggxdbw))
txoa = Factor("rhpg", [DerivedLevel("hvsnph", WithinTrial(yztmtc, [clbqjx, axqomn, ggxdbw])), DerivedLevel("qmkj", WithinTrial(jylgrl, [clbqjx, axqomn, ggxdbw])),DerivedLevel("jcsa", WithinTrial(xiry, [clbqjx, axqomn, ggxdbw]))])
### EXPERIMENT
design=[clbqjx,axqomn,ggxdbw,txoa]
crossing=[txoa]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)