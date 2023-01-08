from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ihlv= Factor("ihlv", ["dfuu","aramdr","yadl","vekpr","vvhj"])
ngheks= Factor("ngheks", ["sctvll","qjpsrm","anz","zsmnya","ifcx","xbcj","ganxoa"])
def is_yxyzr_psyro(ihlv, ngheks):
    return ihlv == "yadl" and ngheks == "ganxoa"
def is_yxyzr_igmf(ihlv, ngheks):
    return not is_yxyzr_psyro(ihlv, ngheks)
yxyzr= Factor("yxyzr", [DerivedLevel("psyro", WithinTrial(is_yxyzr_psyro, [ihlv, ngheks])), DerivedLevel("igmf", WithinTrial(is_yxyzr_igmf, [ihlv, ngheks]))])

design=[ihlv,ngheks, yxyzr]
crossing=[yxyzr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END
