from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nit = Factor("nit", ["kxzzp","ypycp","laywua","sdotn","kvin","bfkgv"])
zaqgel = Factor("zaqgel", ["zuvwb","ebsp","xsw","fhkoez","tug","ltnvdy","toytrl"])
def efpic(nit, zaqgel):
    return nit == "ypycp" or zaqgel == "zuvwb"
def caygx(nit,zaqgel):
    return not efpic(nit, zaqgel)
fimvht = Factor("niy", [DerivedLevel("tybllc", WithinTrial(efpic, [nit, zaqgel])), DerivedLevel("asjj", WithinTrial(caygx, [nit, zaqgel]))])
### EXPERIMENT
design=[nit,zaqgel,fimvht]
crossing=[fimvht]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)