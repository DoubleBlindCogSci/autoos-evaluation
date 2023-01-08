from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rtll = Factor("rtll", ["weogwb","nflf","zsakwu","hcnt","feyutr","jmepj"])
def thamu(rtll):
    return rtll != "nflf" or rtll == "weogwb"
def rbtfe(rtll):
    return not thamu(rtll)
nejlc = Factor("xwvuae", [DerivedLevel("feozq", WithinTrial(thamu, [rtll])), DerivedLevel("ybvc", WithinTrial(rbtfe, [rtll]))])
### EXPERIMENT
design=[rtll,nejlc]
crossing=[nejlc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END