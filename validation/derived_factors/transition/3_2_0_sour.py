from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
etw = Factor("etw", ["havms","sslbut","ogslo","tpi","kcu","bdxbbr","bwj"])
qkmfhd = Factor("qkmfhd", ["havms","sslbut","ogslo","tpi","kcu","bdxbbr","bwj"])
qcftj = Factor("qcftj", ["havms","sslbut","ogslo","tpi","kcu","bdxbbr","bwj"])
def tmb(etw, qcftj, qkmfhd):
     return qcftj[-1] == etw[0] and etw[-1] != qkmfhd[0]
def jge(etw, qcftj, qkmfhd):
     return qcftj[-1] != etw[0] and qkmfhd[0] == etw[-1]
def ljm(etw, qcftj, qkmfhd):
     return (not tmb(etw, qcftj, qkmfhd)) and (not jge(etw, qcftj, qkmfhd))
ggfx = Factor("uaioe", [DerivedLevel("pozw", Transition(tmb, [etw, qkmfhd, qcftj])), DerivedLevel("wsm", Transition(jge, [etw, qkmfhd, qcftj])),DerivedLevel("azb", Transition(ljm, [etw, qkmfhd, qcftj]))])
### EXPERIMENT
design=[etw,qkmfhd,qcftj,ggfx]
crossing=[ggfx]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)