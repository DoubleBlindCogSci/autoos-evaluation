from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
v8_Vi9K9J=[Level('fDXuCKKYVuuP',6),"cJeCRLrkOBQ",Level("kklWkLVtdB:Qt4",7),"OABn",'cyg','bfibrrA']
wROZ_uw=Factor('W4MTKU~&WBN',[Level('WoGI;cWf',7),'cybb',v8_Vi9K9J[1],Level("tmsC4J;S",2),'Yiv3rpTs[nX@Ay'])
ffZJ0=['tsNCPlUL?',Level("bBQHegf",6),"%KvACU",'lYOcU']
J1OIjp=Factor('NvR?6@FrEbD',ffZJ0)

### EXPERIMENT
design=[wROZ_uw,J1OIjp]
crossing=[wROZ_uw,J1OIjp]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_0"))
### END