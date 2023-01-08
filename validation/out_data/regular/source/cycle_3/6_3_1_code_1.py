from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vHVze=['<Pf',"FDMiXDRDQ#mwDO",'jcuyb2i?Hu']
pFEp="K@7N_q"
kfffL6f_3=['GDJDoHTiO<',"BmBERcRytWF","TR~OmrjLEscjK",pFEp,vHVze[0],"(TJ$KJ9cCjF",'sGLswZAxy',Level('qlKxBtKj',2)]
z5Od=Factor('e1c',kfffL6f_3)
Zu2rhM=Level("f DVVjHcThY2hs",10)
NetD=[Level("kWqbHkKZ[!F",7),"^xRG",Level("~M5i",7),"Cwa",Zu2rhM,Level("2jatR0pLGxmg",4),"&qp"]
kV91=Factor("DKsJ",NetD)
JbGQ5hBD5Gw=Factor('qKX',[Level("5gO",4),"lSmc",Level('0yf8d',9),'J8W4',Level("rqKuLWd",8),Level("I<!jFcLxZ",6)])

### EXPERIMENT
design=[z5Od,kV91,JbGQ5hBD5Gw]
crossing=[z5Od,kV91,JbGQ5hBD5Gw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_3_1"))
### END