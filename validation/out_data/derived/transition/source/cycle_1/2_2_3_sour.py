from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
cfgp = Factor("cfgp", ["zhb","auqymj","yadxcf","foatf","zmuqt","zaydr"])
zotx = Factor("zotx", ["fvqksd","qokmyw","mvhnjp","spmw","ldmd","gndf","gob"])
def hsuzp(cfgp, zotx):
    return cfgp[0] != "yadxcf" and zotx[-1] != "ldmd"
def qzs(cfgp,zotx):
    return cfgp[0] == "yadxcf" or not (zotx[-1] != "ldmd")
ajvm = DerivedLevel("uhrgs", Transition(hsuzp, [cfgp, zotx]))
cei = DerivedLevel("vrqyuv", Transition(qzs, [cfgp, zotx]))
sje = Factor("oum", [ajvm, cei])

### EXPERIMENT
design=[cfgp,zotx,sje]
crossing=[sje]
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