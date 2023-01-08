from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
vbuipz = Factor("vbuipz", ["wkzx", "iuoqy"])
ilcgi = Factor("ilcgi", ["vkdwcr", "klerfi"])
ggw = Factor("ggw", ["wkzx", "iuoqy"])
dolfc = Factor("dolfc", ["vkdwcr", "klerfi"])
design=[vbuipz,ilcgi,ggw,dolfc]
constraints=[AtMostKInARow(2, ggw),MinimumTrials(46)]
crossing=[ggw,vbuipz]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0_2"))
