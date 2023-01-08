from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Bzdb=["CCY",'qeULZr[fAivq? ',"hlN~",'UxmC]zanlu','$H^*MUN',"khpbXCprfqy$","&oL8xta3C"]
LmUpAQ8iBoD=Factor('SUdOBzK8vpH',Bzdb)
PVGXQ=Factor("R[GlhTqy",['jdk3',"AtncqBx","6oZcf",'hzWA','@hATCbcYA','lcph',")Z~nlPHljR"])
VgdZ2Q='dwAj'
uaEeuY=['kKGKSRFxfAnoAJ',Level('cFHsBxmdIVp',2),VgdZ2Q,"Q9n|(mK",'wOTpOtXBke','t!NZ',"JjhygVygnX85m",'A_ou4VdVbXdHaq']
SZJKXP6=Factor('Tmytp$pFKCrA',uaEeuY)

### EXPERIMENT
design=[LmUpAQ8iBoD,PVGXQ,SZJKXP6]
crossing=[LmUpAQ8iBoD,PVGXQ,SZJKXP6]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_3_1_0.csv"))
nr_factors=3
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)