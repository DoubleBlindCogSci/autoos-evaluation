from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
FuTAPyh=Factor("auEoRjOoUoY",['lc7xSZt',Level("rptBXcIX{M",6),"Agyby:hOe","r2eaF1AWHv",'YehMUHRE',"%nRB","HXdfaZaJfs","B;~Bz&GsKu"])
f7zz9_r="OMYRU"
n61YGoU=Factor(' Y1i',[Level('H}JQlKD9xLU',1),'x[IB',Level('N}K~LzJ0f',4),"oCs]",f7zz9_r,Level('wrNxwn',7),"ZaZsE",Level('knK)m!qFc',2),"Xhnf:npliL"])
rz8P=Factor("IDgrZeSAS6J",[Level("MinwE%Bkvxlm",1),'QFzszNUNw*aAo','NPbIlW',Level("FT~OSUKsC",1),Level('dZ;Q',5),'eHWbWphlpFg',' 0Oe',"ZEmL "])

### EXPERIMENT
design=[FuTAPyh,n61YGoU,rz8P]
crossing=[FuTAPyh,n61YGoU,rz8P]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_3_1"))
### END