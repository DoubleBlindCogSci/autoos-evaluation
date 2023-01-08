from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dw1oyxKvJO=['N<ZXJenQog5tU','JTjIEeCPzihX','dZoO$8Z]uxw[eF',"Ia5kE8BG","q7xqINi",Level('Q5UpubySot4',4),Level('AuBb',2)]
CkHutR=[Level("kTgCBo",3),dw1oyxKvJO[2],"utXNld?AdXwG","kg4JqTq%Yt",'PjfbyGLBPRltWg']
rGK8=Factor("xvY",CkHutR)
kP0ksR9P1G=Factor("IVH",["fG^swtQYm","mgUjZ?",';gJBl:P',Level("UWneV",2)])
sx0Dn=Factor('bC3DNg',[Level("lpPrq",1),"BYDwlOTzPr","]czuP",'z4wIcQE'])
nqJXyEXI=Factor('UKGjSSoVt',["Buzg",'aj^p:e','cZFN','jCG;fMVo'])

### EXPERIMENT
design=[rGK8,kP0ksR9P1G,sx0Dn,nqJXyEXI]
crossing=[rGK8,kP0ksR9P1G,sx0Dn,nqJXyEXI]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_4_1"))
### END