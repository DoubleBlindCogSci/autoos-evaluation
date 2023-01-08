from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
esi = Factor("esi", ["pnoy","hfmto","izzlv","usgm","trrvms","onuueg","gofjiv"])
def qwq(esi):
    return esi != "gofjiv" and esi == "trrvms"
def loop(esi):
    return not qwq(esi)
gletk = DerivedLevel("bqgjor", WithinTrial(qwq, [esi]))
jxagbq = DerivedLevel("myep", WithinTrial(loop, [esi]))
xpaki = Factor("eefept", [gletk, jxagbq])

### EXPERIMENT
design=[esi,xpaki]
crossing=[xpaki]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END