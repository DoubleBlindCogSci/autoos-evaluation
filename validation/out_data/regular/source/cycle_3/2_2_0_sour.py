from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
op60qWf8jV2=Factor('OpS',[">2tXWexZ",'dSH|hlFVObONk'])
gxCx3uOcCWr=Factor('e0WxsEDEWgDMz',[Level('wgFdahXpLHV',10),Level("q;dRnYDA",10)])

### EXPERIMENT
design=[op60qWf8jV2,gxCx3uOcCWr]
crossing=[op60qWf8jV2,gxCx3uOcCWr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_factors=2
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)