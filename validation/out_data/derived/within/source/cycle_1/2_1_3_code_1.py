from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bvy = Factor("bvy", ["enk","ajwz","mrus","fshjjo","zqhidt"])
def rig(bvy):
    return bvy == "mrus" and bvy != "enk"
def dje(bvy):
    return not (bvy == "mrus") or not (bvy != "enk")
uhchux = Factor("ixjekz", [DerivedLevel("xxnqkg", WithinTrial(rig, [bvy])), DerivedLevel("hwity", WithinTrial(dje, [bvy]))])
### EXPERIMENT
design=[bvy,uhchux]
crossing=[uhchux]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END