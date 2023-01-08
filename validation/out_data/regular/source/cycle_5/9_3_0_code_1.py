from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_3_0"))
### END