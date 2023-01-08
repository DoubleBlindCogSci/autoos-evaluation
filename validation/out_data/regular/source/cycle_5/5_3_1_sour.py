from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
UA9tJ='@UfGUQ#oOE'
C37H1Z6hH4=Factor('qZiA&rdFb!',[Level('dhZz',1),"W]HTNkuTPPauH_",'dRSUOQN',"H?2cPcLFghVTlv",'O%aCsphHO',UA9tJ])
gb57VRKKaDM="jd7mGapM"
UPi_nZl03=Factor('BYbmeW]JhESi',['Izhtx',gb57VRKKaDM,"0HVETiRa","AZCw8vbYXO",' fdafalQj','FLoZQfQEDLnC'])
MH7XCjFO=Factor('F GXAnimmff',['[VE',Level("d:CFFaGGBtd",3),"UeKS","lOs>ojr%eMbJ","1X1CnPsI>I1eeg"])

### EXPERIMENT
design=[C37H1Z6hH4,UPi_nZl03,MH7XCjFO]
crossing=[C37H1Z6hH4,UPi_nZl03,MH7XCjFO]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_3_1_0.csv"))
nr_factors=3
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)