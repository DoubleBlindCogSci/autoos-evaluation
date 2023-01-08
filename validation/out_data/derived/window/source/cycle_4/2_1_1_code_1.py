from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ldnw = Factor("ldnw", ["zgdbnp","iziur","rgrmbc","mly","tijokn","kmfir"])
def zhic(ldnw):
    return ldnw[0] == "iziur" or ldnw[-1] == "mly"
def qhgmpl(ldnw):
    return not zhic(ldnw)
lsz = DerivedLevel("qyw", Window(zhic, [ldnw],2,1))
mfoqx = DerivedLevel("esrlc", Window(qhgmpl, [ldnw],2,1))
nerby = Factor("fwcwhx", [lsz, mfoqx])

### EXPERIMENT
design=[ldnw,nerby]
crossing=[nerby]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END