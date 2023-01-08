from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
letkr = Factor("letkr", ["zil","ukuxyy","xkmrbl","idyql","izyc"])
fsre = Factor("fsre", ["rlsi","baqb","argp","gkfi","vscoiz"])
def grmrkm(letkr, fsre):
    return letkr[0] != "xkmrbl" or fsre[-1] != "argp"
def iixgm(letkr,fsre):
    return not grmrkm(letkr, fsre)
jkqxs = DerivedLevel("zrdges", Window(grmrkm, [letkr, fsre],2))
gyjna = DerivedLevel("tnibr", Window(iixgm, [letkr, fsre],2))
zzrje = Factor("wzau", [jkqxs, gyjna])

### EXPERIMENT
design=[letkr,fsre,zzrje]
crossing=[zzrje]
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