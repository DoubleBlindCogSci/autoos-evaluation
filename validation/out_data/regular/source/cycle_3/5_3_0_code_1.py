from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oJo_y='StQzaAEqlYBcG'
RAUVKGo9RrX=['{cWC#}YpFdigjr',oJo_y,Level('mdIl!w VJKs',10),"ieUXsItNK^hDW",Level('_YY@y v7l$o&a;',7),"0VXhtnFpwwJfY<"]
jbcGrzS=Factor('oZiPQN',RAUVKGo9RrX)
ZWH1dA=Factor('HDj',[Level("x*C@ICLFE",5),"ckcq","Evukv(T)Sa7tqf",'(rUjEknVcvxXJ','0wKKm'])
B3xvbynqAhr=Factor("Pt nDbEd7{D",["^qmIavOLgtr","SuE","QIixsggv",Level('4b8_',2),"x;}r&yN<"])

### EXPERIMENT
design=[jbcGrzS,ZWH1dA,B3xvbynqAhr]
crossing=[jbcGrzS,ZWH1dA,B3xvbynqAhr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_3_0"))
### END