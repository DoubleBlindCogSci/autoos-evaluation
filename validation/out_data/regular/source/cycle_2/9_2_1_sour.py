from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
TN_uzMuxLbZ=Factor('EURYH68',['SxYEA',"rGtQrRKtSF","pHEp)RWpyZ",Level('sMSo2F;!',8),'nx6GulJ','c{Oeo<QF','bON','vEMO {FwTRQH',"71s"])
uOFNi2=Level("0mjNr",5)
FzGJwhJqr=Factor('wX#^laii',[uOFNi2,"fPET",Level("Hb)",9),'yuJOaLEA',"o]jJ9g%MLYfZC",Level('TPNi2trc}hy',6),"lRsU6vwOQJa4","p6b$hq[A","*Lf|!Ft~zG3QF","hiEuuxnMoB7I"])

### EXPERIMENT
design=[TN_uzMuxLbZ,FzGJwhJqr]
crossing=[TN_uzMuxLbZ,FzGJwhJqr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_2_1_0.csv"))
nr_factors=2
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)