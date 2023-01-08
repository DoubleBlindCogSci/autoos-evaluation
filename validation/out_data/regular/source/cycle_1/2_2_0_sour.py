from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
VlTtXKL4g=Factor('XhhZiGB',[Level('hPGl uOtisLND',6),'syCRDMI'])
D_haHS4wf=Factor("uXUzDyTLRmY",["&WZJORykj__bx<",'yvbPMPvTBO'])

### EXPERIMENT
design=[VlTtXKL4g,D_haHS4wf]
crossing=[VlTtXKL4g,D_haHS4wf]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/2_2_0_0.csv"))
nr_factors=2
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)