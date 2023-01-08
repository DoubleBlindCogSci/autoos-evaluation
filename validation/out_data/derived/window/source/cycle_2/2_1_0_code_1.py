from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jux = Factor("jux", ["jvpa","oxp","vgfogi","swxoq","xwmy","rceiym","szd"])
def nbz(jux):
    return jux[-3] != "oxp" or jux[-1] != "jvpa"
def sng(jux):
    return not nbz(jux)
fde = DerivedLevel("nct", Window(nbz, [jux],4,1))
hizs = DerivedLevel("xfgem", Window(sng, [jux],4,1))
cyh = Factor("koux", [fde, hizs])

### EXPERIMENT
design=[jux,cyh]
crossing=[cyh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END