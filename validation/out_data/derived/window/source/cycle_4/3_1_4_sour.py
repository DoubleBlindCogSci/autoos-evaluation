from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
miyzdq = Factor("miyzdq", ["klaaay","qyw","vmzbe","jzywnf","kklavl","aalk","zyek","dtpi"])
def kcmci(miyzdq):
     return miyzdq[-2] == "klaaay" and not miyzdq[0] == "klaaay"
def senihx(miyzdq):
     return not "klaaay" == miyzdq[-2] and  miyzdq[0] == "aalk"
def poxpf(miyzdq):
     return (not miyzdq[-2] == "klaaay") and (not miyzdq[0] == "aalk")
vqvtj = Factor("brsv", [DerivedLevel("animf", Window(kcmci, [miyzdq],3)), DerivedLevel("dpmihp", Window(senihx, [miyzdq],3)),DerivedLevel("ypsd", Window(poxpf, [miyzdq],3))])
### EXPERIMENT
design=[miyzdq,vqvtj]
crossing=[vqvtj]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)