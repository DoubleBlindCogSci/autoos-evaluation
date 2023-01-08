from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
eov = Factor("eov", ["fivo","ryik","urca","ghfive","lfyir","hbzi","xvedsc","hetd"])
jryyb = Factor("jryyb", ["fivo","ryik","urca","ghfive","lfyir","hbzi","xvedsc","hetd"])
fnan = Factor("fnan", ["fivo","ryik","urca","ghfive","lfyir","hbzi","xvedsc","hetd"])
def avqosx(eov, jryyb, fnan):
     return eov[-1] == jryyb[0] and eov[0] != fnan[-1]
def ugqol(eov, jryyb, fnan):
     return jryyb[0] != eov[-1] and fnan[-1] == eov[0]
def gfva(eov, jryyb, fnan):
     return (not eov[-1] == jryyb[0]) and (not ugqol(eov, jryyb, fnan))
emfamx = DerivedLevel("qfcwn", Window(avqosx, [eov, jryyb, fnan],2))
epmsqc = DerivedLevel("tvzgy", Window(ugqol, [eov, jryyb, fnan],2))
tswodf = DerivedLevel("pgdgge", Window(gfva, [eov, jryyb, fnan],2))
nudlrq = Factor("owcv", [emfamx, epmsqc, tswodf])

### EXPERIMENT
design=[eov,jryyb,fnan,nudlrq]
crossing=[nudlrq]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)