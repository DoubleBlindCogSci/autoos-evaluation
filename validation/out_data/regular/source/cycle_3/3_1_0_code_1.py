from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ubnQMb2RRl=Factor('tATmUjPjsp~lA',[Level('WBEFPxwX',10),Level('lJAd',1),'1pivlOsnIUdd6t'])

### EXPERIMENT
design=[ubnQMb2RRl]
crossing=[ubnQMb2RRl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END