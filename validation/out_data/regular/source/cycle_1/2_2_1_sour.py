from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Jbz6lL=Factor('NvWsk&S6Q',['fGWygGC1','z9bO'])
Uvy9KTRw1JW=Factor("usoTdsJdQX",[Level("^iAkR",1),')O8T'])

### EXPERIMENT
design=[Jbz6lL,Uvy9KTRw1JW]
crossing=[Jbz6lL,Uvy9KTRw1JW]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/2_2_1_0.csv"))
nr_factors=2
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/2_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)