from sweetpea import *
import os
_dir=os.path.dirname(__file__)
cqtrgj = Factor("cqtrgj", ["geno", "aioxn"])
vwd = Factor("vwd", ["potv", "cmshe"])
vzlh = Factor("vzlh", ["nbgvdl", "xqoza"])
jkyxw = Factor("jkyxw", ["deyngt", "qyk"])
isq = Factor("isq", ["ewu", "pjlyt"])
ffroz = Factor("ffroz", ["zppp", "pfi"])
sgm = Factor("sgm", ["tboo", "zpi"])
rosl = Factor("rosl", ["dgqoia", "oms"])
constraints = []
crossing = [[cqtrgj, vwd, vzlh, jkyxw], [isq, ffroz, sgm], [rosl]]


design=[cqtrgj,vwd,vzlh,jkyxw,isq,ffroz,sgm,rosl]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1"))

### END