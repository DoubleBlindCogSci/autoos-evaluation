from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ghgsgh = Factor("ghgsgh", ["ygygmn","bhhi","wswgl", "miilqs"])
jzbdqh = Factor("jzbdqh", ["tebltl","owcd", "ctucf"])
ajw = Factor("ajw", ["psmlbt", "ayhrhh"])
gqju = Factor("gqju", ["atn", "xdgug"])
qtjk = Factor("qtjk", ["omyo","kdh","euw", "vhuhb"])

### EXPERIMENT
constraints=[AtLeastKInARow(3,(ghgsgh,"miilqs")),AtMostKInARow(3,(jzbdqh,"ctucf")),ExactlyKInARow(3,(ajw,"ayhrhh"))]
design=[ghgsgh,jzbdqh,ajw,gqju,qtjk]
crossing=[gqju,qtjk]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1"))
### END