from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
xllver = Factor("xllver", ["kdzk", "yea"])
isvnwz = Factor("isvnwz", ["egcg", "vmymn"])
ayptso = Factor("ayptso", ["kdzk", "yea"])
ayupup = Factor("ayupup", ["egcg", "vmymn"])
design=[xllver,isvnwz,ayptso,ayupup]
constraints=[MinimumTrials(60),ExactlyKInARow(4, ayptso)]
crossing=[ayptso,ayupup]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0_2"))
