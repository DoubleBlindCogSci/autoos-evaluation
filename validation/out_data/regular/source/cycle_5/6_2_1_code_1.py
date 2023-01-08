from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jAMzLKub13='NmjVDdgzkkAh'
VqEcbTgz0=Factor('T2hdyKWgNx#aq',['ivFHOCJEx)qy#','a07IdQAQRf',"DRdH nBIO",'<kl#?JvIE#G',"naOZmdGA",Level('%oxVxiI(',1),jAMzLKub13])
ElGn=Level('Y]nhb5joP',2)
Yc73P=Factor('FwK2y^l CGt;U',[Level("DOxJnlZahqkFT",2),"DzXgDP(lo",'ruD}CjaBOIqy','!SqbozoR',ElGn,"qBet1kqGlKW",'l4|IHhKDSk'])

### EXPERIMENT
design=[VqEcbTgz0,Yc73P]
crossing=[VqEcbTgz0,Yc73P]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_1"))
### END