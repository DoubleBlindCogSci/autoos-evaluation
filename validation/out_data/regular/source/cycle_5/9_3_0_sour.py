from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_RRQZQD=['#XJypJwAp)dqZ2',"pxfy^LcNmTxKE",Level('s|QiEfF#i',1),'H)DaSf','cdZJZp|7n','@L;VwcSW']
ko_7LMx=Factor("!qDN3",[Level("Q6LqyfUp",4),'XuFE','QFwd:Z',Level('SngMlW',3),Level('4gdOh',2),'VMJiMBbJIAJG','gHZt(KrcldOm ','Gd[H)cXWZV',_RRQZQD[3],'UM_jFL'])
tWWLLpgt5=Factor('FL0p',['aJAa:mCAghLnBK',Level("Jgfo;KxshSxI",2),Level("TY?L",1),Level('AlKm>BrgqA',2),'dvioV#QkuM','ej)OFcG',">:9","n2p!tFmY","AUMdbMtmV"])
s8L0Yr=Factor('EhRYA!$iR',["{?$rH6SD5T",'q81aEhA','manacASWYHb','lNMWaaiKUtZOf','xNT|W&W',"MZlyiN","QLrZP",Level("nwYY}VI",1),'CwSopuVm;yn}O'])

### EXPERIMENT
design=[ko_7LMx,tWWLLpgt5,s8L0Yr]
crossing=[ko_7LMx,tWWLLpgt5,s8L0Yr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_3_0_0.csv"))
nr_factors=3
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)