from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
FlVLt="ddspwc"
R2MPCXhrD=Factor("KIjvFbXUcopz",['pgsL','ZPGskZAMaesama','YB~)B!cDv>oQ^','{tTJIa;',FlVLt])
m2VBFe4PyR=Factor("SAmFY^1UowhBKP",['vEhWx$',"HIlrlr","JvD","}mO"])
Qlz6='NsRtrg'
hG7jmK34Ic=['ZxUhg3oG;hGs',"VGU[ijSWL)HFjh","SQl8zhw","s_i_RNBG",'r7c$DZFhQ']
LRZnH=Factor("soLnO",[Level("qhCLBSMkJ;Dg5",3),"1RPWRot>c",'CK;1',hG7jmK34Ic[2],Qlz6,'d:Wk3sEb^JZvYS'])
EBFDn=['XPasGLpcNt','PPy',Level('ZNt*hPMwIC',4),'A[~elsmMIkA']
pxOG9caLsu=Factor("@n!jhRxRGt",EBFDn)

### EXPERIMENT
design=[R2MPCXhrD,m2VBFe4PyR,LRZnH,pxOG9caLsu]
crossing=[R2MPCXhrD,m2VBFe4PyR,LRZnH,pxOG9caLsu]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_4_0_0.csv"))
nr_factors=4
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_4_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)