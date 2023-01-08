from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
BHeGJD3d08p='rLCR5h~NLcTLUu'
bsF20Us9hrS=[BHeGJD3d08p,'AFt','CWMql3]HUMVKrN',Level('ljt',2),'piqS#NWhxj',Level("g>BRsRvs",3),"9fusx2lFe GKOL","xQp",Level('hm9fxe(ofqgV',3),"91EmrhgBpu"]
wmV0eRlle=Factor('eIRa<mp<xhDb',bsF20Us9hrS)

### EXPERIMENT
design=[wmV0eRlle]
crossing=[wmV0eRlle]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_1_0_0.csv"))
nr_factors=1
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)