from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_4_0"))
### END