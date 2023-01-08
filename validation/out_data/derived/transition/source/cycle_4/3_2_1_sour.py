from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cllom = Factor("cllom", ["iguxfw","wlovos","auc","luy","rje","qwukso"])
dqbabm = Factor("dqbabm", ["iguxfw","wlovos","auc","luy","rje","qwukso"])
hvd = Factor("hvd", ["iguxfw","wlovos","auc","luy","rje","qwukso"])
def tar(cllom, dqbabm, hvd):
     return dqbabm[-1] == cllom[0] and cllom[-1] != hvd[0]
def ngmexx(cllom, dqbabm, hvd):
     return dqbabm[-1] != cllom[0] and cllom[-1] == hvd[0]
def qke(cllom, dqbabm, hvd):
     return (cllom[0] != dqbabm[-1]) and (cllom[-1] != hvd[0])
yreign = DerivedLevel("vcllmd", Transition(tar, [cllom, dqbabm, hvd]))
gtbv = DerivedLevel("kvhw", Transition(ngmexx, [cllom, dqbabm, hvd]))
irnehw = DerivedLevel("zkoh", Transition(qke, [cllom, dqbabm, hvd]))
mecohz = Factor("ucdmr", [yreign, gtbv, irnehw])

### EXPERIMENT
design=[cllom,dqbabm,hvd,mecohz]
crossing=[mecohz]
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