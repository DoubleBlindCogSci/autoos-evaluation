from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rrjaqh = Factor("rrjaqh", ["nyyw","fhk","ntd","dwqqqw","pvwnq","ity","ktqi"])
judsc = Factor("judsc", ["nyyw","fhk","ntd","dwqqqw","pvwnq","ity","ktqi"])
tig = Factor("tig", ["nyyw","fhk","ntd","dwqqqw","pvwnq","ity","ktqi"])
def uehmr(rrjaqh, judsc, tig):
     return rrjaqh == judsc
def raq(rrjaqh, judsc, tig):
     return judsc != rrjaqh and rrjaqh == tig
def dwn(rrjaqh, judsc, tig):
     return (not uehmr(rrjaqh, judsc, tig)) and (not rrjaqh == tig)
dwylr = DerivedLevel("vbejzt", WithinTrial(uehmr, [rrjaqh, judsc, tig]))
sjfs = DerivedLevel("vdj", WithinTrial(raq, [rrjaqh, judsc, tig]))
kso = DerivedLevel("pnph", WithinTrial(dwn, [rrjaqh, judsc, tig]))
njpn = Factor("iaca", [dwylr, sjfs, kso])

### EXPERIMENT
design=[rrjaqh,judsc,tig,njpn]
crossing=[njpn]
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