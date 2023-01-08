from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pkhem = Factor("pkhem", ["xybs","kraak","tyiw","two","qoqbq","kigd","skiq"])
def lnztfd(pkhem):
     return "skiq" == pkhem[0] and pkhem[-1] != "kigd"
def wccetw(pkhem):
     return (pkhem[0] != "skiq") and  pkhem[-1] == "kigd"
def nsbehj(pkhem):
     return (pkhem[0] != "skiq") and (pkhem[-1] != "kigd")
azya = Factor("zraiw", [DerivedLevel("baghw", Transition(lnztfd, [pkhem])), DerivedLevel("nadv", Transition(wccetw, [pkhem])),DerivedLevel("jonu", Transition(nsbehj, [pkhem]))])
### EXPERIMENT
design=[pkhem,azya]
crossing=[azya]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END