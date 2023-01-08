from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
U8ZQKvU6=['xuqvUI!QNWD','A1 apR:KOeUU',"BqBe;Uhi0%EyX","pKeu*C(Hrn","IG%qtiaBZ",'fBA}urKu',';chV']
NY3QxDQ_=Factor(":MJoBcljx",U8ZQKvU6)
Xt6Zi=["Wgqi4{kIhJV1)",'bTDHI',Level('rcSbkSrtNbBB',1),'oirf6Q']
dPSL0X=['uECHZECESk','TCQg','Z%Lb#6BOZbiQU',"%CWqrBAS*Uhu",Xt6Zi[1],'$lYKR','vwiNX',"uknjk"]
DdyM4=Factor("WTwbv",dPSL0X)
Km7tKgzr=Factor('fj%}(&xg',['AFgnPVcxla>w','h6JuFbxP<R','qwMx','Kr)XjtrZQhsF>P',"v%!So2AT F",'BEk ro',Level('^X81XESyrf:bf',4)])

### EXPERIMENT
design=[NY3QxDQ_,DdyM4,Km7tKgzr]
crossing=[NY3QxDQ_,DdyM4,Km7tKgzr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_3_0_0.csv"))
nr_factors=3
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)