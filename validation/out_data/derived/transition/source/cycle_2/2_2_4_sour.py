from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ldg = Factor("ldg", ["lpt","gmev","iwrb","rrh","dreekw"])
kjsz = Factor("kjsz", ["lpt","gmev","iwrb","rrh","dreekw"])
anepf = Factor("anepf", ["lpt","gmev","iwrb","rrh","dreekw"])
def dkzi(ldg, anepf, kjsz):
    return ldg[0] != anepf[-1] and ldg[-1] == kjsz[0]
def epachq(ldg, anepf, kjsz):
    return ldg[0] == anepf[-1] or ldg[-1] != kjsz[0]
zbyru = DerivedLevel("qzcn", Transition(dkzi, [ldg, kjsz, anepf]))
jyxav = DerivedLevel("bboag", Transition(epachq, [ldg, kjsz, anepf]))
vjs = Factor("ofltsk", [zbyru, jyxav])

### EXPERIMENT
design=[ldg,kjsz,anepf,vjs]
crossing=[vjs]
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