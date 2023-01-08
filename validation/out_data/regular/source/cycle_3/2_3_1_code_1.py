from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
YJJ7RTs=Factor('EZJJ(VpVz7wUQ',['yJYk3K','MKjjJD3r'])
SxDK=['{NrQk)Sy',Level("#EZV",10)]
oJMM8yfh=Factor('PZ}n1',SxDK)
nJdlJyOBm2=Factor('jmhDcwuB|Xs',["Y eGKV*W",'KwO>F'])

### EXPERIMENT
design=[YJJ7RTs,oJMM8yfh,nJdlJyOBm2]
crossing=[YJJ7RTs,oJMM8yfh,nJdlJyOBm2]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3_1"))
### END