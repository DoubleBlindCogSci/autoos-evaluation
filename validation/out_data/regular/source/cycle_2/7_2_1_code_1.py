from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tNkWN=[Level("{vrGALh#w",7),Level("O8RV)rv{Vh",6),"AT[w",'!lIwNNNzZhXSE',"byA^d<jnV",'4NMpPWsLpj','ap~)y7bFUm!)']
siyFfY=Factor("MP7FzIHmqdW",tNkWN)
k_lfXnaFQu='TlZM'
YJ8p=Level("Z4QEwqb",8)
exdU=Factor('RBx',[YJ8p,'Q)HnCEu5I',"d3nmjAaP",Level('XPtVlLK2gKCrj',10),"5S*MThl og>jN","fREIS5qcowiSjA","YbWiXA","Ko>0W",k_lfXnaFQu])

### EXPERIMENT
design=[siyFfY,exdU]
crossing=[siyFfY,exdU]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_2_1"))
### END