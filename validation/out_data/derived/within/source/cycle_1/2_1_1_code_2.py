from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zlduos= Factor("zlduos", ["yvf","odgih","etkhti","wfkk","pyxs"])

def is_bgbyst_biedl(zlduos):
    return zlduos != "wfkk"
def is_bgbyst_lrionk(zlduos):
    return not is_bgbyst_biedl(zlduos)
bgbyst= Factor("bgbyst", [DerivedLevel("biedl", WithinTrial(is_bgbyst_biedl, [zlduos])), DerivedLevel("lrionk", WithinTrial(is_bgbyst_lrionk, [zlduos]))])


design=[zlduos,bgbyst]
crossing=[bgbyst]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
