from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vrh= Factor("vrh", ["omipuk","isgp","ycd","vynlqp","lmylt"])
def is_xtq_jhzoqx(vrh):
    return vrh[0] == "omipuk" and vrh[-3] == "isgp"
def is_xtq_lhbwh(vrh):
    return not is_xtq_jhzoqx(vrh)
xtq= Factor("xtq", [DerivedLevel("jhzoqx", Window(is_xtq_jhzoqx, [vrh], 4, 1)), DerivedLevel("lhbwh", Window(is_xtq_lhbwh, [vrh], 4, 1))])

design=[vrh,xtq]
crossing=[xtq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
