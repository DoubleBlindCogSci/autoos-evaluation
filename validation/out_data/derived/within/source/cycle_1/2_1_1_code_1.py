from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zlduos = Factor("zlduos", ["yvf","odgih","etkhti","wfkk","pyxs"])
def aslvik(zlduos):
    return zlduos != "wfkk"
def xdwnz(zlduos):
    return not (zlduos != "wfkk")
yygr = DerivedLevel("biedl", WithinTrial(aslvik, [zlduos]))
yheuah = DerivedLevel("lrionk", WithinTrial(xdwnz, [zlduos]))
vwwhma = Factor("bgbyst", [yygr, yheuah])

### EXPERIMENT
design=[zlduos,vwwhma]
crossing=[vwwhma]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END