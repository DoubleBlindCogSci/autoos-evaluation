from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
avahh = Factor("avahh", ["yax","rxkwhl","hhuxrh","ikxtd","uxzog","rwemy","enfch"])
gzc = Factor("gzc", ["yax","rxkwhl","hhuxrh","ikxtd","uxzog","rwemy","enfch"])
wzfxxn = Factor("wzfxxn", ["yax","rxkwhl","hhuxrh","ikxtd","uxzog","rwemy","enfch"])
def ddyxvs(avahh, gzc, wzfxxn):
    return avahh[-2] == gzc[0] or avahh[0] != wzfxxn[-2]
def zwuig(avahh, gzc, wzfxxn):
    return not ddyxvs(avahh, gzc, wzfxxn)
pwqdl = DerivedLevel("ddgmep", Window(ddyxvs, [avahh, gzc, wzfxxn],3))
kpdrzq = DerivedLevel("usy", Window(zwuig, [avahh, gzc, wzfxxn],3))
hrm = Factor("eanb", [pwqdl, kpdrzq])

### EXPERIMENT
design=[avahh,gzc,wzfxxn,hrm]
crossing=[hrm]
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
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)