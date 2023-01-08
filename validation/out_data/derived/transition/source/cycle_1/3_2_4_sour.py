from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
kekvlw = Factor("kekvlw", ["znvr","gdmc","hkozq","rxu","bzrshc","eksbhu"])
fpcf = Factor("fpcf", ["znvr","gdmc","hkozq","rxu","bzrshc","eksbhu"])
cbbiqs = Factor("cbbiqs", ["znvr","gdmc","hkozq","rxu","bzrshc","eksbhu"])
def bzlngb(kekvlw, cbbiqs, fpcf):
     return cbbiqs[-1] == kekvlw[0]
def hrh(kekvlw, cbbiqs, fpcf):
     return cbbiqs[-1] != kekvlw[0] and fpcf[0] == kekvlw[-1]
def chofh(kekvlw, cbbiqs, fpcf):
     return (not kekvlw[0] == cbbiqs[-1]) and (not kekvlw[-1] == fpcf[0])
ozflzc = DerivedLevel("iwbpyw", Transition(bzlngb, [kekvlw, fpcf, cbbiqs]))
lmbz = DerivedLevel("drcljo", Transition(hrh, [kekvlw, fpcf, cbbiqs]))
xjeuuy = DerivedLevel("jxgp", Transition(chofh, [kekvlw, fpcf, cbbiqs]))
gzqze = Factor("fjl", [ozflzc, lmbz, xjeuuy])

### EXPERIMENT
design=[kekvlw,fpcf,cbbiqs,gzqze]
crossing=[gzqze]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)