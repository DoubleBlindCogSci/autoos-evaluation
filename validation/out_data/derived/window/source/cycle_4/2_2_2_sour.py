from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
molokf = Factor("molokf", ["zihb","ffmhv","pyklyv","etbiy","xhrx"])
ooyt = Factor("ooyt", ["hlhdjb","hhd","vaq","rdv","hoin","qte","opv"])
def jtgqu(molokf, ooyt):
    return molokf[-3] == "zihb" and ooyt[-2] != "hoin"
def hzbbg(molokf,ooyt):
    return molokf[-3] != "zihb" or not (ooyt[-2] != "hoin")
pahzol = Factor("mod", [DerivedLevel("lgdc", Window(jtgqu, [molokf, ooyt],4)), DerivedLevel("pmkjr", Window(hzbbg, [molokf, ooyt],4))])
### EXPERIMENT
design=[molokf,ooyt,pahzol]
crossing=[pahzol]
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