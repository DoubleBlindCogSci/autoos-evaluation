from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oZiPQN = Factor("oZiPQN", [Level("{cWC#}YpFdigjr", 1), Level("StQzaAEqlYBcG", 1), Level("mdIl!w VJKs", 10), Level("ieUXsItNK^hDW", 1), Level("_YY@y v7l$o&a;", 7), Level("0VXhtnFpwwJfY<", 1)])
HDj = Factor("HDj", [Level("x*C@ICLFE", 5), Level("ckcq", 1), Level("Evukv(T)Sa7tqf", 1), Level("(rUjEknVcvxXJ", 1), Level("0wKKm", 1)])
Pt nDbEd7{D = Factor("Pt nDbEd7{D", [Level("^qmIavOLgtr", 1), Level("SuE", 1), Level("QIixsggv", 1), Level("4b8_", 2), Level("x;}r&yN<", 1)])

design=[oZiPQN,HDj]
crossing=[oZiPQN,HDj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_3_0"))

### END
