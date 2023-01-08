from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vtn = Factor("vtn", ["aoboa","oxdsji","uewi","liwbka","tdwxt","oqcxu","yjywvu"])
ewjn = Factor("ewjn", ["aoboa","oxdsji","uewi","liwbka","tdwxt","oqcxu","yjywvu"])
bvind = Factor("bvind", ["aoboa","oxdsji","uewi","liwbka","tdwxt","oqcxu","yjywvu"])
def uxk(vtn, ewjn, bvind):
     return vtn == ewjn
def zkm(vtn, ewjn, bvind):
     return ewjn != vtn and bvind == vtn
def pop(vtn, ewjn, bvind):
     return (not uxk(vtn, ewjn, bvind)) and (vtn != bvind)
gysh = Factor("jjev", [DerivedLevel("pbx", WithinTrial(uxk, [vtn, ewjn, bvind])), DerivedLevel("dmhmm", WithinTrial(zkm, [vtn, ewjn, bvind])),DerivedLevel("xegnon", WithinTrial(pop, [vtn, ewjn, bvind]))])
### EXPERIMENT
design=[vtn,ewjn,bvind,gysh]
crossing=[gysh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END