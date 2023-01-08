from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ldnw = Factor("ldnw", ["zgdbnp","iziur","rgrmbc","mly","tijokn","kmfir"])
def is_fwcwhx_qyw(ldnw):
    return ldnw[0] == "iziur" or ldnw[-1] == "mly"
def is_fwcwhx_esrlc(ldnw):
    return not is_fwcwhx_qyw(ldnw)
fwcwhx= Factor("fwcwhx", [DerivedLevel("qyw", Window(is_fwcwhx_qyw, [ldnw], 2, 1)), DerivedLevel("esrlc", Window(is_fwcwhx_esrlc, [ldnw], 2, 1))])

design=[ldnw,fwcwhx]
crossing=[fwcwhx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END