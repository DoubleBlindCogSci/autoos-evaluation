from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qvno = Factor("qvno", ["jgmlk","lmd","wmi","pnlq","lhwdzz"])
yqskm = Factor("yqskm", ["jgmlk","lmd","wmi","pnlq","lhwdzz"])
hrl = Factor("hrl", ["jgmlk","lmd","wmi","pnlq","lhwdzz"])
def jwy(qvno, hrl, yqskm):
    return qvno != hrl
def uqyi(qvno, hrl, yqskm):
    return qvno == hrl
zic = Factor("rcq", [DerivedLevel("tclmcm", WithinTrial(jwy, [qvno, yqskm, hrl])), DerivedLevel("pihm", WithinTrial(uqyi, [qvno, yqskm, hrl]))])
### EXPERIMENT
design=[qvno,yqskm,hrl,zic]
crossing=[zic]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)