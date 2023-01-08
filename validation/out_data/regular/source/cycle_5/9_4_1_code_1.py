from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
JAmxrd=Factor('Tj(dqKuDai',["mvVxuGpSSy:vp","J2TqQMdGeghh"," )}F(VaIy"," hn0eWdieS",'xZ1d{','VPWkyEw',"WYXSe?dG","pOPgX9#aGRX_k",'yeXm '])
LNRY7SnZJ1=Factor(')HZFDkQEKcx',['b[SIBy|VQQyjD',"L@DYJX",'HBbX[1xgf',"wiedIudnsBT&Xd","Tov<gm2nQx",":1v","xdsdZgjq0Gsw","DMHM","eTSkZuwq;"])
qpvlJkZMj=Factor('1?W',['{FsKTamx',Level('Hk!FI*fF',3),Level("[sWQAwcVu|ovk",2),'NO)M6','EGxDU@3SVqdzJu',"psBQMfCk","}xpxITnxbft",'HqgyfKXq;v','DWGQocI'])
Z6R3DR=Factor('gYm}dH:(',["eLSs<",')BAnfERE','*_2kFQ','iXa',"YNE]mlvZ",'pLK',Level("e[ibcwsjfzBpj",3),"sfX",'IuIbQm#Spsz{yM'])

### EXPERIMENT
design=[JAmxrd,LNRY7SnZJ1,qpvlJkZMj,Z6R3DR]
crossing=[JAmxrd,LNRY7SnZJ1,qpvlJkZMj,Z6R3DR]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_4_1"))
### END