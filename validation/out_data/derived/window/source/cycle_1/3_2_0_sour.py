from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
kpzzs = Factor("kpzzs", ["trnsf","euqvm","eopzt","hruj","aoi","tsrpg","nysyn","yezi"])
yfbw = Factor("yfbw", ["trnsf","euqvm","eopzt","hruj","aoi","tsrpg","nysyn","yezi"])
pelwq = Factor("pelwq", ["trnsf","euqvm","eopzt","hruj","aoi","tsrpg","nysyn","yezi"])
def cootr(kpzzs, yfbw, pelwq):
     return yfbw[-1] == kpzzs[-3]
def okrank(kpzzs, yfbw, pelwq):
     return yfbw[-1] != kpzzs[-3] and pelwq[-3] == kpzzs[-1]
def tius(kpzzs, yfbw, pelwq):
     return (kpzzs[-3] != yfbw[-1]) and (kpzzs[-1] != pelwq[-3])
kfytpp = DerivedLevel("rlntfd", Window(cootr, [kpzzs, yfbw, pelwq],4))
cnftpf = DerivedLevel("ipwd", Window(okrank, [kpzzs, yfbw, pelwq],4))
qroo = DerivedLevel("crte", Window(tius, [kpzzs, yfbw, pelwq],4))
xkry = Factor("yzrhbj", [kfytpp, cnftpf, qroo])

### EXPERIMENT
design=[kpzzs,yfbw,pelwq,xkry]
crossing=[xkry]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)