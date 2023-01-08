from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kxma = Factor("kxma", ["nozq", "adiacv"])
uhy = Factor("uhy", ["dafua", "nwvyg"])
gsvtjw = Factor("gsvtjw", ["ifvlbq", "aoyhnl"])
prkinm = Factor("prkinm", ["wvby", "rixgcr"])
rzqvop = Factor("rzqvop", ["ownoyx", "jeammm"])
wfrq = Factor("wfrq", ["qwdiz", "kfsmw"])
htgxg = Factor("htgxg", ["jwiv", "edvpcb"])
ktkj = Factor("ktkj", ["lyc", "afc"])
pmtqn = Factor("pmtqn", ["hkjjoz", "abgrj"])
buriha = Factor("buriha", ["engbyt", "xbhzun"])
rdsfc = Factor("rdsfc", ["dgt", "pof"])

### EXPERIMENT
design=[kxma,uhy,gsvtjw,prkinm,rzqvop,wfrq,htgxg,ktkj,pmtqn,buriha,rdsfc]
crossing=[[kxma,uhy,gsvtjw,prkinm],[rzqvop],[wfrq,htgxg],[ktkj,pmtqn,buriha,rdsfc],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1"))
### END