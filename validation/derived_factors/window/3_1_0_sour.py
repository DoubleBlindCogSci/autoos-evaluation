from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
eogjc = Factor("eogjc", ["jgzfq","sbohcz","uzjcr","bytwvi","tflo","ttrmbh","dizicq"])
def objcth(eogjc):
     return "tflo" == eogjc[0] and not eogjc[-1] == "tflo"
def tlnda(eogjc):
     return not "tflo" == eogjc[0] and  "dizicq" == eogjc[-1]
def erqt(eogjc):
     return (eogjc[0] != "tflo") and (not tlnda(eogjc))
pweof = DerivedLevel("jcndf", Window(objcth, [eogjc],2,1))
tyx = DerivedLevel("chjln", Window(tlnda, [eogjc],2,1))
eln = DerivedLevel("the", Window(erqt, [eogjc],2,1))
dnhoe = Factor("qyyis", [pweof, tyx, eln])

### EXPERIMENT
design=[eogjc,dnhoe]
crossing=[dnhoe]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)