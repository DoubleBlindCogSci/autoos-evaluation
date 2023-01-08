from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hcwy = Factor("hcwy", ["rts","furb","mutfqd","zqowsh","ytm","ivhzdn","hvqke","stoh"])
mhcn = Factor("mhcn", ["rts","furb","mutfqd","zqowsh","ytm","ivhzdn","hvqke","stoh"])
wnsekp = Factor("wnsekp", ["rts","furb","mutfqd","zqowsh","ytm","ivhzdn","hvqke","stoh"])
def qazj(hcwy, mhcn, wnsekp):
     return mhcn[-1] == hcwy[0] and hcwy[-1] != wnsekp[0]
def tdzlj(hcwy, mhcn, wnsekp):
     return mhcn[-1] != hcwy[0] and hcwy[-1] == wnsekp[0]
def ucwav(hcwy, mhcn, wnsekp):
     return (hcwy[0] != mhcn[-1]) and (hcwy[-1] != wnsekp[0])
qkzfmn = Factor("tqfiyn", [DerivedLevel("poqmg", Transition(qazj, [hcwy, mhcn, wnsekp])), DerivedLevel("vgrgin", Transition(tdzlj, [hcwy, mhcn, wnsekp])),DerivedLevel("wxp", Transition(ucwav, [hcwy, mhcn, wnsekp]))])
### EXPERIMENT
design=[hcwy,mhcn,wnsekp,qkzfmn]
crossing=[qkzfmn]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)