from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Mxdqx_9Ws=Level("osUdJB&Edxl",4)
Z1MUEw0Cisl=Factor("eIRV%I",[Mxdqx_9Ws,"hAimCiOE","XbB^LaV","pRW3HNV4FkK","lo@vVSx","!bPl:LIiQzwukG",'#DzQ3'])
VJblWGDK=Factor('Fxz$Uob?boxm1b',["&uypFVf",'IfOKO|',"~6ZvX*Hl|VI7NJ","vdQPuaKTdc","vMshw[HSHoJJhZ","pqFGMs<"])
KkK1SyE4R='XTb1X~ZLlgEe'
goOyC7c5Om=Factor("EwaZ&gw;b4",[Level('oRyp',4),'WQknLrt','zwlTSd',"nD en:WCYHa6d",'~wdw',Level('|CUWyxo',1),KkK1SyE4R])

### EXPERIMENT
design=[Z1MUEw0Cisl,VJblWGDK,goOyC7c5Om]
crossing=[Z1MUEw0Cisl,VJblWGDK,goOyC7c5Om]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_3_0_0.csv"))
nr_factors=3
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)