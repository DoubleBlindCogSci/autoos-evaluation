from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
vbuipz = Factor("vbuipz", ["wkzx", "iuoqy"])
ilcgi = Factor("ilcgi", ["vkdwcr", "klerfi"])
ggw = Factor("ggw", ["wkzx", "iuoqy"])
dolfc = Factor("dolfc", ["vkdwcr", "klerfi"])
constraints = [AtMostKInARow(2, ggw), MinimumTrials(46)]
crossing = [ggw, vbuipz]

design=[vbuipz,ilcgi,ggw,dolfc]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_0_2"))
