from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zpik = Factor("zpik", ["fmpi","ynxy","xbo","cugq","wkksi"])
hzeny = Factor("hzeny", ["fmpi","ynxy","xbo","cugq","wkksi"])
hajvj = Factor("hajvj", ["fmpi","ynxy","xbo","cugq","wkksi"])
def is_eihb_txc(zpik, hzeny, hajvj):
    return zpik[-1] == hajvj[0]
def is_eihb_zkbc(zpik, hzeny, hajvj):
    return not is_eihb_txc(zpik, hzeny, hajvj)
eihb = Factor("eihb", [DerivedLevel("txc", Window(is_eihb_txc, [zpik, hzeny, hajvj], 2, 1)), DerivedLevel("zkbc", Window(is_eihb_zkbc, [zpik, hzeny, hajvj], 2, 1))])

design=[zpik,hzeny,hajvj,eihb]
crossing=[eihb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END