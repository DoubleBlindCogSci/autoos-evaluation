from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
heWP8tNP=["vYSOFJOhS:f","AiglQzZ","isRtlBsBseu"]
ADlox=Factor('tfyKlPXVXP',heWP8tNP)
bzd151vvC0=Factor("HAkIkDJZuKD8B",["ClgR",'GfboYLKKEdQHUj',Level("J:s",3)])
J_LsxU=['hrG',"kAWWLIQc","ZtyhQrMJDJ5"]
E6ORdZx=Factor("Tm}",J_LsxU)

### EXPERIMENT
design=[ADlox,bzd151vvC0,E6ORdZx]
crossing=[ADlox,bzd151vvC0,E6ORdZx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3_1"))
### END