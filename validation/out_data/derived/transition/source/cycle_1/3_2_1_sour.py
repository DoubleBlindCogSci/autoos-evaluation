from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
pbdufo = Factor("pbdufo", ["vpd","avmt","fkdx","bvs","ukkqbx","trbcm","ygizr","vgdy"])
bij = Factor("bij", ["ibqt","gvvyt","ssvls","dpwx","mui","bwsmwk","jid","jdxfe"])
def soc(pbdufo, bij):
     return "bvs" == pbdufo[-1]
def mzfxbp(pbdufo, bij):
     return "bvs" != pbdufo[-1] and  bij[0] == "ssvls"
def mme(pbdufo, bij):
     return (pbdufo[-1] != "bvs") and (not bij[0] == "ssvls")
tdrvi = Factor("rew", [DerivedLevel("cjl", Transition(soc, [pbdufo, bij])), DerivedLevel("zfzme", Transition(mzfxbp, [pbdufo, bij])),DerivedLevel("ipcih", Transition(mme, [pbdufo, bij]))])
### EXPERIMENT
design=[pbdufo,bij,tdrvi]
crossing=[tdrvi]
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