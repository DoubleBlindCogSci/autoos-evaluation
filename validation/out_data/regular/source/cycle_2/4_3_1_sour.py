from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DLVLG7iZI0=Factor('UVq[fEbnWkk',[Level('KiLzF',5),'tiYQydlil>',"I13",Level('QMoi@D',7)])
Apuf=Factor("P3WfL]UX>iOyf",["DpD*VprHYcl","#Si!7ZG","dagYxP","AmTaWIpRQ"])
cRnfgItBL=Factor('cuuvWqk (x)RA',["ZTaZOVVLK",Level("IZ8",2),Level('3bB%KC3xHUf',3),'WSG;T>D5af{D4B'])

### EXPERIMENT
design=[DLVLG7iZI0,Apuf,cRnfgItBL]
crossing=[DLVLG7iZI0,Apuf,cRnfgItBL]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_3_1_0.csv"))
nr_factors=3
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)