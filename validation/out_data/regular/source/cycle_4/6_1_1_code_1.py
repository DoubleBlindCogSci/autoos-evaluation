from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
SORPMN1z2=[Level('fhi1',3),'BY&sLXcP',Level("fbcBJenTtBWNQD",2),'eOQNP^Ko',"nWmBG","zyVolwh"]
aoXeFLgg=Factor('udetjD',SORPMN1z2)

### EXPERIMENT
design=[aoXeFLgg]
crossing=[aoXeFLgg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_1"))
### END