from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rztogc = Factor("rztogc", ["kth","xtlb","exoqu","hyb","jngzfo"])
def ifnqr(rztogc):
    return rztogc[0] == "jngzfo" and rztogc[-1] != "xtlb"
def irctur(rztogc):
    return not (rztogc[0] == "jngzfo") or not (rztogc[0] != "xtlb")
pbuzf = DerivedLevel("uaajm", Transition(ifnqr, [rztogc]))
tlbzc = DerivedLevel("jtwlz", Transition(irctur, [rztogc]))
lrxa = Factor("psjx", [pbuzf, tlbzc])

### EXPERIMENT
design=[rztogc,lrxa]
crossing=[lrxa]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END