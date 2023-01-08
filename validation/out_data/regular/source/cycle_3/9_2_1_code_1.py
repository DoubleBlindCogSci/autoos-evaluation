from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bJvPc=Level('DBv6tnuw',10)
Wglr=Factor('Ncp',['u%whc','NAhQ2 &waGA','puZz4teJMKJ',"vmlShuSG_h","juX3RSd8qJ",Level('wIY4vATHmeHn',10),Level('~i)HFQmcpRH',5),"lg%9szyeLPs",Level('I3cUKG',6),bJvPc])
CiHCx0YwN=Factor('gD!MZ[US',['QRvUD*fo','b&gSEeGoXmkW',"bmqI~wVl{GDGra","KNo D8",Level("gI2YFl]syX",3),'LtAgghskcb&',Level('yGK',7),"OFkXIpQ>",Level("CiGQ^LCZiZGsUt",4)])

### EXPERIMENT
design=[Wglr,CiHCx0YwN]
crossing=[Wglr,CiHCx0YwN]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_2_1"))
### END