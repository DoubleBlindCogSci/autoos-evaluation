from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fum= Factor("fum", ["vrgjb","kzdb","otqv","lqyhz","bvfjr","nfueqd"])
def is_sfk_gthv(fum):
    return fum[0] == "nfueqd" and fum[-1] != "otqv"
def is_sfk_lyd(fum):
    return fum[0] != "nfueqd" and fum[-1] == "otqv"
def is_sfk_ctzx(fum):
    return not (is_sfk_gthv(fum) or is_sfk_lyd(fum))
sfk= Factor("sfk", [DerivedLevel("gthv", Transition(is_sfk_gthv, [fum])), DerivedLevel("lyd", Transition(is_sfk_lyd, [fum])), DerivedLevel("ctzx", Transition(is_sfk_ctzx, [fum]))])

design=[fum,sfk]
crossing=[sfk]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END
