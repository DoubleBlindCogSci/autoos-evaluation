from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bolifi = Factor("bolifi", ["sugkl","zvzumm","udoj","gtd","iixax","tdstz","ndl"])
def is_jmerhw_gtlcen(bolifi):
    return bolifi == "tdstz"
def is_jmerhw_ximt(bolifi):
    return bolifi == "ndl"
def is_jmerhw_acwjo(bolifi):
    return not (is_jmerhw_gtlcen(bolifi) or is_jmerhw_ximt(bolifi))
jmerhw = Factor("jmerhw", [DerivedLevel("gtlcen", WithinTrial(is_jmerhw_gtlcen, [bolifi])), DerivedLevel("ximt", WithinTrial(is_jmerhw_ximt, [bolifi])), DerivedLevel("acwjo", WithinTrial(is_jmerhw_acwjo, [bolifi]))])

design=[bolifi,jmerhw]
crossing=[jmerhw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END