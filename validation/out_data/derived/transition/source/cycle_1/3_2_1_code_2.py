from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pbdufo= Factor("pbdufo", ["vpd","avmt","fkdx","bvs","ukkqbx","trbcm","ygizr","vgdy"])
bij= Factor("bij", ["ibqt","gvvyt","ssvls","dpwx","mui","bwsmwk","jid","jdxfe"])
def is_rew_cjl(pbdufo):
    return pbdufo[0] == "bvs"
def is_rew_zfzme(pbdufo, bij):
    return pbdufo[0] != "bvs" and bij[0] == "ssvls"
def is_rew_ipcih(pbdufo, bij):
    return not (is_rew_cjl(pbdufo) or is_rew_zfzme(pbdufo, bij))
rew= Factor("rew", [DerivedLevel("cjl", Transition(is_rew_cjl, [pbdufo])), DerivedLevel("zfzme", Transition(is_rew_zfzme, [pbdufo, bij])), DerivedLevel("ipcih", Transition(is_rew_ipcih, [pbdufo, bij]))])

design=[pbdufo,bij,rew]
crossing=[rew]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
