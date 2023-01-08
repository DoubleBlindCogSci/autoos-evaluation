from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
V0qQ4jSsZy="HZ0"
VR9ni4T4=Factor("U0CWjYXT~xv",["t$N@UYjUe!","ISEvByPGf",Level('lepI?EB[$AvTc',4),"EEcurcEwyyAIAO","isCI",'{kFp4ZKurdWJ',Level('^c5~xvuCTJYu',7),V0qQ4jSsZy,"MpAWIbWNMMnV"])

### EXPERIMENT
design=[VR9ni4T4]
crossing=[VR9ni4T4]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_1_0"))
### END