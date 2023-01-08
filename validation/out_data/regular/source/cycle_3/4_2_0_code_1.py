from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZYWlSe=[Level("UkGodpK",10),'XTl7;0ojFdtDkC',Level('fTjX',3),"rETujOKaOl"]
cXNJ1j0K=Factor('Houj;bCo$Do',ZYWlSe)
odjYrUj=Factor('CUA2WGwQ',['xJvBbqaal?LMUD',Level('Rrch?sDWbsC',7),'sytZkHy',Level("vAyCMFvWlmc}ef",5)])

### EXPERIMENT
design=[cXNJ1j0K,odjYrUj]
crossing=[cXNJ1j0K,odjYrUj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_0"))
### END