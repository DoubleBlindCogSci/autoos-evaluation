from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pkhem = Factor("pkhem", ["xybs","kraak","tyiw","two","qoqbq","kigd","skiq"])
def is_zraiw_baghw(pkhem):
    return pkhem[0] == "skiq" and pkhem[-1] != "kigd"
def is_zraiw_nadv(pkhem):
    return pkhem[0] != "skiq" and pkhem[-1] == "kigd"
def is_zraiw_jonu(pkhem):
    return not (is_zraiw_baghw(pkhem) or is_zraiw_nadv(pkhem))
zraiw= Factor("zraiw", [DerivedLevel("baghw", Transition(is_zraiw_baghw, [pkhem])), DerivedLevel("nadv", Transition(is_zraiw_nadv, [pkhem])), DerivedLevel("jonu", Transition(is_zraiw_jonu, [pkhem]))])

design=[pkhem,zraiw]
crossing=[zraiw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END