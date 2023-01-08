from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rtll = Factor("rtll", ["weogwb","nflf","zsakwu","hcnt","feyutr","jmepj"])
def is_xwvuae_feozq(rtll):
    return rtll != "nflf" or rtll == "weogwb"
def is_xwvuae_ybvc(rtll):
    return not is_xwvuae_feozq(rtll)
xwvuae= Factor("xwvuae", [DerivedLevel("feozq", WithinTrial(is_xwvuae_feozq, [rtll])), DerivedLevel("ybvc", WithinTrial(is_xwvuae_ybvc, [rtll]))])

design=[rtll,xwvuae]
crossing=[xwvuae]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END