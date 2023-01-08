from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jzn = Factor("jzn", ["jghcja","dbd","gxellq","ivxlp","qjdrcn","qglutk","zof"])
ehon = Factor("ehon", ["jghcja","dbd","gxellq","ivxlp","qjdrcn","qglutk","zof"])
xtzkge = Factor("xtzkge", ["jghcja","dbd","gxellq","ivxlp","qjdrcn","qglutk","zof"])
def pwe(jzn, xtzkge, ehon):
    return jzn[-2] == xtzkge[0] and jzn[0] != ehon[-2]
def ffs(jzn, xtzkge, ehon):
    return not pwe(jzn, xtzkge, ehon)
lqfvx = Factor("kultts", [DerivedLevel("wrn", Window(pwe, [jzn, ehon, xtzkge],3)), DerivedLevel("yrit", Window(ffs, [jzn, ehon, xtzkge],3))])
### EXPERIMENT
design=[jzn,ehon,xtzkge,lqfvx]
crossing=[lqfvx]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)