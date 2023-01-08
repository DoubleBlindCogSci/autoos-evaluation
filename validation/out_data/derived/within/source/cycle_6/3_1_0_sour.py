from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ppf = Factor("ppf", ["sqyxw","qzpevj","hmsmwv","rdxy","rjzf","ijlar"])
def zpfigl(ppf):
     return "hmsmwv" == ppf
def zykzsi(ppf):
     return ppf == "qzpevj"
def fsmsp(ppf):
     return (not zpfigl(ppf)) and (ppf != "qzpevj")
adit = Factor("jqgpn", [DerivedLevel("ljo", WithinTrial(zpfigl, [ppf])), DerivedLevel("lxz", WithinTrial(zykzsi, [ppf])),DerivedLevel("ibye", WithinTrial(fsmsp, [ppf]))])
### EXPERIMENT
design=[ppf,adit]
crossing=[adit]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)