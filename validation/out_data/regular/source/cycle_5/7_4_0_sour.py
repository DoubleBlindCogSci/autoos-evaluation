from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
E_IwQuWF=Factor('iZOtp',['yYfWqaYvkZegd',"zzTbk",Level("6EBviLCcpDG",3),"SldRo PXU","WiwkykvcfEyD",'T*s9(D',"Pc<sDukSLP"])
I_NmnhIUqM=['IDfaKMD'," [x ^HBB","Gu:",Level("cAJn",1),")L#8ATLFlJR","CzUJWssX",'kk<kwOWnImQEQ']
Td1HCu=Factor("UB9",I_NmnhIUqM)
fQ3mu='}B}5FVBXJpcY'
ATorhYwAns=Factor('GSqpO~C1gi7',['wBCCEQ7sinDW',"lyss",'gt@YCh','#euKvDlGsAk',"SkK0WEnW!TTP","KIuwXw]B",fQ3mu,"~nnvN"])
dVK1PcVJ4="tO:GLRD"
TxyxypZPkEd=Factor("IigMbEZE0B",['Am(gmCwehx^l','WX5Uj7qXpr',"VXRGDU",'Vu!ErD_Tc','e6sBpLbxlWwt ',dVK1PcVJ4,'NW{RWkaO*[','wfuQ?ydYw%ZkMN'])

### EXPERIMENT
design=[E_IwQuWF,Td1HCu,ATorhYwAns,TxyxypZPkEd]
crossing=[E_IwQuWF,Td1HCu,ATorhYwAns,TxyxypZPkEd]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_4_0_0.csv"))
nr_factors=4
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_4_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)