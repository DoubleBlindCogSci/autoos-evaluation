from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wsle= Factor("wsle", ["jerlq","dthqsq","hpuvln","sorijz","zwze","nxcmu","amrfiy","oemibc"])
def is_zhyw_zldik(wsle):
    return wsle[0] == "sorijz"
def is_zhyw_oflt(wsle):
    return wsle[0] == "jerlq"
def is_zhyw_ziowfh(wsle):
    return not (is_zhyw_zldik(wsle) or is_zhyw_oflt(wsle))
zhyw= Factor("zhyw", [DerivedLevel("zldik", Transition(is_zhyw_zldik, [wsle])), DerivedLevel("oflt", Transition(is_zhyw_oflt, [wsle])), DerivedLevel("ziowfh", Transition(is_zhyw_ziowfh, [wsle]))])

design=[wsle,zhyw]
crossing=[zhyw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END
