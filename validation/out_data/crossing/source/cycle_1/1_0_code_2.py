from sweetpea import *
import os
_dir=os.path.dirname(__file__)
uwvqtu = Factor("uwvqtu", ["mmchlu", "qcdtnd"])
uazsjy = Factor("uazsjy", ["xtkp", "xthps"])
luk = Factor("luk", ["mugj", "wpw"])
buo = Factor("buo", ["rdrjy", "dyh"])
constraints = []
crossing = [uwvqtu, uazsjy, luk, buo]


design=[uwvqtu,uazsjy,luk,buo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_0"))

### END