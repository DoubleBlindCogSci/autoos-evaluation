from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
A7QDPGygnJz=Factor('HtCPuxXG',[Level('mUWJ[VHkU',1),'pDaTAkwbK['])
fgwj05dIyzg=Factor("x&}VYLN",["INxF(e5pv","lNzHD"])
cATUTyRV8R=Factor('gHs',["BkFi3BXfDs6dZ","HVdvc&>;<iZ*"])

### EXPERIMENT
design=[A7QDPGygnJz,fgwj05dIyzg,cATUTyRV8R]
crossing=[A7QDPGygnJz,fgwj05dIyzg,cATUTyRV8R]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/2_3_0_0.csv"))
nr_factors=3
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/2_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)