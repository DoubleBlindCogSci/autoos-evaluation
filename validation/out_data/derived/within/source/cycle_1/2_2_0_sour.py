from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
vhuevy = Factor("vhuevy", ["nlnmo","hgjot","axst","cgaogw","fhit","fhay","bxph"])
ddn = Factor("ddn", ["nlnmo","hgjot","axst","cgaogw","fhit","fhay","bxph"])
cfsfa = Factor("cfsfa", ["nlnmo","hgjot","axst","cgaogw","fhit","fhay","bxph"])
def eeetnn(vhuevy, cfsfa, ddn):
    return vhuevy != cfsfa
def cyy(vhuevy, cfsfa, ddn):
    return vhuevy == cfsfa
his = DerivedLevel("ilpaj", WithinTrial(eeetnn, [vhuevy, ddn, cfsfa]))
nyl = DerivedLevel("jnoqn", WithinTrial(cyy, [vhuevy, ddn, cfsfa]))
jawdy = Factor("zkkck", [his, nyl])

### EXPERIMENT
design=[vhuevy,ddn,cfsfa,jawdy]
crossing=[jawdy]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)