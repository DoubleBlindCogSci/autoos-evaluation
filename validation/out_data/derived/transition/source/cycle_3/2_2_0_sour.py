from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cnpp = Factor("cnpp", ["kvmnqd","wxxfb","qwtsob","pxolf","wyv","cccj","ktjyt"])
zhunlp = Factor("zhunlp", ["kvmnqd","wxxfb","qwtsob","pxolf","wyv","cccj","ktjyt"])
susug = Factor("susug", ["kvmnqd","wxxfb","qwtsob","pxolf","wyv","cccj","ktjyt"])
def zkckv(cnpp, susug, zhunlp):
    return cnpp[0] != susug[-1]
def ggx(cnpp, susug, zhunlp):
    return cnpp[0] == susug[-1]
wkff = Factor("bfrrks", [DerivedLevel("jtqqhx", Transition(zkckv, [cnpp, zhunlp, susug])), DerivedLevel("muozv", Transition(ggx, [cnpp, zhunlp, susug]))])
### EXPERIMENT
design=[cnpp,zhunlp,susug,wkff]
crossing=[wkff]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)