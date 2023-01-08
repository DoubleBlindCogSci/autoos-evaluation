from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tfyKlPXVXP = Factor("tfyKlPXVXP", ["vYSOFJOhS:f", "AiglQzZ", "isRtlBsBseu"])
HAkIkDJZuKD_B = Factor("HAkIkDJZuKD8B", [Level("ClgR", 1), Level("GfboYLKKEdQHUj", 1), Level("J:s", 3)])
Tm_ = Factor("Tm}", ["hrG", "kAWWLIQc", "ZtyhQrMJDJ5"])

design=[tfyKlPXVXP,HAkIkDJZuKD_B,Tm_]
crossing=[tfyKlPXVXP,HAkIkDJZuKD_B,Tm_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3_1"))

### END
