from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
guh = Factor("guh", ["icgxd","rio","nfnij","spbm","jtmifq","bzfnd"])
def wcazr(guh):
     return "rio" == guh
def uwix(guh):
     return "nfnij" == guh
def ppkhmi(guh):
     return (not wcazr(guh)) and (not guh == "nfnij")
cqv = DerivedLevel("rdl", WithinTrial(wcazr, [guh]))
bybm = DerivedLevel("grs", WithinTrial(uwix, [guh]))
tfopm = DerivedLevel("vujbce", WithinTrial(ppkhmi, [guh]))
pptqih = Factor("jobcfs", [cqv, bybm, tfopm])

### EXPERIMENT
design=[guh,pptqih]
crossing=[pptqih]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)