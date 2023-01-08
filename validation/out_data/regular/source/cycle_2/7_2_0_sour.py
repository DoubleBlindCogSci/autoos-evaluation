from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Jtr6olMcw='vJYW'
eK21M6Kr=Factor('ZTTKcHt<I',[Level("OS|yv{[UpvDa",9),"UMWKNHvJdD","LzSMH","0fo",'$JU]GUA',Jtr6olMcw,"CsdovqHpChLd","gSgOSIT"])
VvQM54mWA3=[Level("tNfwIuKYoqvIFJ",9),'RtrQVwWj(pUY[',Level("aHoK7P",8)]
kw9HWt=['JYtSUk',Level("thgDE]Jp",9),'Mcd xm3e}B',Level('MrrRen$acYzgHf',7),"CuELFAwb",'Adi%G0VIDSaDy',VvQM54mWA3[0],Level('h}CZD',8)]
EMmB=Factor("bC@X",kw9HWt)

### EXPERIMENT
design=[eK21M6Kr,EMmB]
crossing=[eK21M6Kr,EMmB]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_2_0_0.csv"))
nr_factors=2
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)