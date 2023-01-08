from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
xllver = Factor("xllver", ["kdzk", "yea"])
isvnwz = Factor("isvnwz", ["egcg", "vmymn"])
ayptso = Factor("ayptso", ["kdzk", "yea"])
ayupup = Factor("ayupup", ["egcg", "vmymn"])
constraints = [AtLeastKInARow(4, ayptso), MinimumTrials(60)]
crossing = [ayptso, ayupup]

design=[xllver,isvnwz,ayptso,ayupup]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_0_2"))
