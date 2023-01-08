from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
orv = Factor("orv", ["ecf","ctx","ydzol","fry","tmjvn"])
umaucr = Factor("umaucr", ["ecf","ctx","ydzol","fry","tmjvn"])
fdcldf = Factor("fdcldf", ["ecf","ctx","ydzol","fry","tmjvn"])
def is_nlgc_ayso(orv, umaucr, fdcldf):
    return orv[-1] == umaucr[0] and orv[0] == fdcldf[-1]
def is_nlgc_asl(orv, umaucr, fdcldf):
    return not is_nlgc_ayso(orv, umaucr, fdcldf)
nlgc = Factor("nlgc", [DerivedLevel("ayso", Window(is_nlgc_ayso, [orv, umaucr, fdcldf], 2, 1)), DerivedLevel("asl", Window(is_nlgc_asl, [orv, umaucr, fdcldf], 2, 1))])

design=[orv,umaucr,fdcldf,nlgc]
crossing=[nlgc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END