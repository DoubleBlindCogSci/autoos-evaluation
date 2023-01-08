from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bvy= Factor("bvy", ["enk","ajwz","mrus","fshjjo","zqhidt"])
def is_ixjekz_xxnqkg(bvy):
    return bvy == "mrus" and bvy != "enk"
def is_ixjekz_hwity(bvy):
    return not is_ixjekz_xxnqkg(bvy)
ixjekz= Factor("ixjekz", [DerivedLevel("xxnqkg", WithinTrial(is_ixjekz_xxnqkg, [bvy])), DerivedLevel("hwity", WithinTrial(is_ixjekz_hwity, [bvy]))])

design=[bvy,ixjekz]
crossing=[ixjekz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END
