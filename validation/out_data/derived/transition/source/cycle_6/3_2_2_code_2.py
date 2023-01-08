from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vyl = Factor("vyl", ["nfji","ewcnwl","zhrtv","gevbzq","mutl","omuphx"])
lytpda = Factor("lytpda", ["hmeuy","uqjxcp","bgh","kiwcz","rzqhjz","ewmcgk","hxdqz","ygzcc"])
def is_jljwku_zigcr(vyl, lytpda):
    return vyl[-1] == "omuphx" and lytpda[0] != "uqjxcp"
def is_jljwku_ltkzxi(vyl, lytpda):
    return vyl[-1] != "omuphx" and lytpda[0] == "uqjxcp"
def is_jljwku_xinlkr(vyl, lytpda):
    return not (is_jljwku_zigcr(vyl, lytpda) or is_jljwku_ltkzxi(vyl, lytpda))
jljwku = Factor("jljwku", [DerivedLevel("zigcr", Transition(is_jljwku_zigcr, [vyl, lytpda])), DerivedLevel("ltkzxi", Transition(is_jljwku_ltkzxi, [vyl, lytpda])), DerivedLevel("xinlkr", Transition(is_jljwku_xinlkr, [vyl, lytpda]))])

design=[vyl,lytpda,jljwku]
crossing=[jljwku]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END