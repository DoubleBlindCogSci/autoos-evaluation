from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ghljns= Factor("ghljns", ["dgbxuu","wxfjh","tgxq","fqttg","bcgva","kwxwwg","sassnr","fpa"])
def is_youocf_ery(ghljns):
    return ghljns[0] == "sassnr"
def is_youocf_ltxz(ghljns):
    return ghljns[0] == "tgxq"
def is_youocf_kybpzi(ghljns):
    return not (is_youocf_ery(ghljns) or is_youocf_ltxz(ghljns))
youocf= Factor("youocf", [DerivedLevel("ery", Transition(is_youocf_ery, [ghljns])), DerivedLevel("ltxz", Transition(is_youocf_ltxz, [ghljns])), DerivedLevel("kybpzi", Transition(is_youocf_kybpzi, [ghljns]))])

design=[ghljns,youocf]
crossing=[youocf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END
