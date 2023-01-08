from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DGEJ2HR4H=Factor("aCxZeoeIL3juMW",["AxszFnNWuiI",'eweZMTbkNOD^',Level("u?v_KojSN|WPkS",4),Level('v)StcoGOF',3),"dFcgB","gHPSg",Level('Lq?FQcPOtb0nWj',4),'QWNm','gqeq'])
nxKHGQ1aeq=Factor('Yvxqae',['NkTvHpRSBqz',Level(":@C tggT>F0)NH",7),"Btt7",Level("NLsPUZqahHqnL",1),Level("vZom[QL",2),Level("ZMyqTbglCTDi0",2),"tkT$FZJ",'JLX)','Bdm'])
AskoRG="IfWH!xcHsJK"
TUfDA8n=Factor('mEpmn;lMKd?',[Level("TxWoCsPHzHTAV",3),'b6lkWxOWN',Level('RYY!oBjzT[qy',5),'|ZPSx1L',"0jeea","9ZiOey7","q WNxi:F[BY","L6qqLLzMeAuz","SoZ",AskoRG])

### EXPERIMENT
design=[DGEJ2HR4H,nxKHGQ1aeq,TUfDA8n]
crossing=[DGEJ2HR4H,nxKHGQ1aeq,TUfDA8n]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/9_3_1_0.csv"))
nr_factors=3
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/9_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)