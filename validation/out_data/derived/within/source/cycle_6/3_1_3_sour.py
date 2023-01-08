from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
flf = Factor("flf", ["mzt","idcvup","ejpvyk","lliic","igbcrl","hwlruj","tbtts","rieymr"])
def lfs(flf):
     return "igbcrl" == flf
def keg(flf):
     return flf == "hwlruj"
def tkv(flf):
     return (not lfs(flf)) and (not keg(flf))
zmaj = DerivedLevel("hne", WithinTrial(lfs, [flf]))
hvoeb = DerivedLevel("naof", WithinTrial(keg, [flf]))
lfxs = DerivedLevel("hanqhq", WithinTrial(tkv, [flf]))
fqm = Factor("cpgwf", [zmaj, hvoeb, lfxs])

### EXPERIMENT
design=[flf,fqm]
crossing=[fqm]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)