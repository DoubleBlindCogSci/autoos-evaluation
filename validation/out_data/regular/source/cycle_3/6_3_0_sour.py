from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tG7ep="mkG"
fLpN=["o&hqnoGLqDytjX","OdH",'VOfxC3Omb%A','jJAN18N',tG7ep,"CwpAf4rQGNA",Level('ZRjSb*9E:n>',7)]
IbcH2=Factor('zmlMNmIsOxRD',fLpN)
QGteir42GsR=Factor('MSpw(dWsfrsZw',["SSaaahFktKaKIS",Level('MDrEK<QAy',4),'zZH','gWGsXcb',"OqxH","db sNZuZI)MwCx"])
r9hIUz8LBR=Factor("3J:b[",['qc^7(t^Ulc',"TPPZfRaEXs4u",Level("~JZESduWvLrpV3",8),"@gU(mw$tim","4ORsMW",Level('oPDRL',4)])

### EXPERIMENT
design=[IbcH2,QGteir42GsR,r9hIUz8LBR]
crossing=[IbcH2,QGteir42GsR,r9hIUz8LBR]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)