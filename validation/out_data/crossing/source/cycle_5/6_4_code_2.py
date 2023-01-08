from sweetpea import *
import os
_dir=os.path.dirname(__file__)
sltrm = Factor("sltrm", ["mhsus", "jzhbu"])
gxvyt = Factor("gxvyt", ["jcuyrv", "aof"])
lrh = Factor("lrh", ["xtd", "xlb"])
kysk = Factor("kysk", ["fkkujk", "zlkc"])
juxz = Factor("juxz", ["izv", "fah"])
fck = Factor("fck", ["ytvv", "wzh"])
tbobi = Factor("tbobi", ["hif", "gny"])
gjod = Factor("gjod", ["opb", "vqfr"])
wlfiko = Factor("wlfiko", ["tbg", "ssumnb"])
jdas = Factor("jdas", ["edrl", "jay"])
gghrp = Factor("gghrp", ["zrxc", "pfeqt"])
emq = Factor("emq", ["fervwz", "cun"])
ugo = Factor("ugo", ["llq", "mbb"])
gxaro = Factor("gxaro", ["hieop", "knh"])
constraints = []
crossing = [[sltrm, gxvyt, lrh], [kysk, juxz, fck, tbobi], [gjod, wlfiko, jdas, gghrp, emq, ugo, gxaro]]


design=[sltrm,gxvyt,lrh,kysk,juxz,fck,tbobi,gjod,wlfiko,jdas,gghrp,emq,ugo,gxaro]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_4"))

### END