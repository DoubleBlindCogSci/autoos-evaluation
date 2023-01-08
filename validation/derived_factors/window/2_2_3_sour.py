from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yhwoc = Factor("yhwoc", ["bjnqig","rwmp","ivv","drq","fnftsx"])
qkf = Factor("qkf", ["bjnqig","rwmp","ivv","drq","fnftsx"])
gbhqo = Factor("gbhqo", ["bjnqig","rwmp","ivv","drq","fnftsx"])
def tmlazi(yhwoc, gbhqo, qkf):
    return yhwoc[-2] != gbhqo[-1]
def nfrdqo(yhwoc, gbhqo, qkf):
    return not tmlazi(yhwoc, gbhqo, qkf)
pql = DerivedLevel("jcqift", Window(tmlazi, [yhwoc, qkf, gbhqo],3,1))
syfviz = DerivedLevel("keko", Window(nfrdqo, [yhwoc, qkf, gbhqo],3,1))
jpes = Factor("hmig", [pql, syfviz])

### EXPERIMENT
design=[yhwoc,qkf,gbhqo,jpes]
crossing=[jpes]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)