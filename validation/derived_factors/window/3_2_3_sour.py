from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ooox = Factor("ooox", ["yzcvnr","cfyizy","hes","qnez","sliev","bosm","rkx"])
plmzac = Factor("plmzac", ["yzcvnr","cfyizy","hes","qnez","sliev","bosm","rkx"])
xwlxbv = Factor("xwlxbv", ["yzcvnr","cfyizy","hes","qnez","sliev","bosm","rkx"])
def dooc(ooox, xwlxbv, plmzac):
     return ooox[-1] == xwlxbv[-2] and ooox[-2] != plmzac[-1]
def pma(ooox, xwlxbv, plmzac):
     return xwlxbv[-2] != ooox[-1] and plmzac[-1] == ooox[-2]
def bqo(ooox, xwlxbv, plmzac):
     return (ooox[-1] != xwlxbv[-2]) and (not pma(ooox, xwlxbv, plmzac))
ilgksd = DerivedLevel("aldchc", Window(dooc, [ooox, plmzac, xwlxbv],3,1))
whbkkh = DerivedLevel("xlzynf", Window(pma, [ooox, plmzac, xwlxbv],3,1))
ren = DerivedLevel("omb", Window(bqo, [ooox, plmzac, xwlxbv],3,1))
nhuo = Factor("seqkw", [ilgksd, whbkkh, ren])

### EXPERIMENT
design=[ooox,plmzac,xwlxbv,nhuo]
crossing=[nhuo]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)