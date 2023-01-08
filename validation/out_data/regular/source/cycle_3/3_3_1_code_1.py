from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
C2CKDccyw="SoWBiQ&YTqQzcT"
KeXgoi1=[C2CKDccyw,Level("sfQt",7),"y6^Cq_",'EPLv:JMYYMK']
ySyqMZkV=Factor(">rY@eZI}Oc)",KeXgoi1)
xkZFH5W='mEWV^bB}WiGkl'
Jeo4=['fp{G',xkZFH5W,"1jI9QflgLp","PYtvC_ZbJlo"]
agDBde2=Factor('M3UTjqP0VUHvE',Jeo4)
pA2Rh=["eClU}ThYb","LpYI~oVWxscLTg","YlYn zR{gfVehn"]
N_nOYproc=Factor("dtD^MQkuKXy",pA2Rh)

### EXPERIMENT
design=[ySyqMZkV,agDBde2,N_nOYproc]
crossing=[ySyqMZkV,agDBde2,N_nOYproc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3_1"))
### END