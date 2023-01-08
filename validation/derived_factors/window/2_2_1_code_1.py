from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zpik = Factor("zpik", ["fmpi","ynxy","xbo","cugq","wkksi"])
hzeny = Factor("hzeny", ["fmpi","ynxy","xbo","cugq","wkksi"])
hajvj = Factor("hajvj", ["fmpi","ynxy","xbo","cugq","wkksi"])
def ppjyq(zpik, hajvj, hzeny):
    return zpik[-1] == hajvj[0]
def tffw(zpik, hajvj, hzeny):
    return not (zpik[-1] == hajvj[0])
plvzj = Factor("eihb", [DerivedLevel("txc", Window(ppjyq, [zpik, hzeny, hajvj],2,1)), DerivedLevel("zkbc", Window(tffw, [zpik, hzeny, hajvj],2,1))])
### EXPERIMENT
design=[zpik,hzeny,hajvj,plvzj]
crossing=[plvzj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END