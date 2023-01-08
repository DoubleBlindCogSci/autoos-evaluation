from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ikgamn = Factor("ikgamn", ["ucsa","inj","udhmv","gaebof","npc","vhu","loyim"])
def wswdbp(ikgamn):
     return ikgamn == "udhmv"
def ntpfhj(ikgamn):
     return ikgamn == "gaebof"
def krabcl(ikgamn):
     return (ikgamn != "udhmv") and (ikgamn != "gaebof")
zqa = DerivedLevel("frpat", WithinTrial(wswdbp, [ikgamn]))
rsuo = DerivedLevel("otrfsn", WithinTrial(ntpfhj, [ikgamn]))
ymjl = DerivedLevel("pwai", WithinTrial(krabcl, [ikgamn]))
pwrfho = Factor("xvidu", [zqa, rsuo, ymjl])

### EXPERIMENT
design=[ikgamn,pwrfho]
crossing=[pwrfho]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_2_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)