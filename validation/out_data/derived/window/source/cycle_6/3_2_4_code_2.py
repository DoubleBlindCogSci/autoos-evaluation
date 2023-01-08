from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ffw = Factor("ffw", ["zjewp","mfde","tsg","vjqa","yrskd","omo","xfkz"])
qce = Factor("qce", ["zjewp","mfde","tsg","vjqa","yrskd","omo","xfkz"])
atrss = Factor("atrss", ["zjewp","mfde","tsg","vjqa","yrskd","omo","xfkz"])
def is_sscn_yrewqx(ffw, qce, atrss):
    return ffw[0] == qce[-2] and ffw[-2] != atrss[0]
def is_sscn_qsx(ffw, qce, atrss):
    return qce[-2] != ffw[0] and ffw[-2] == atrss[0]
def is_sscn_uoskx(ffw, qce, atrss):
    return not (is_sscn_yrewqx(ffw, qce, atrss) or is_sscn_qsx(ffw, qce, atrss))
sscn = Factor("sscn", [DerivedLevel("yrewqx", Window(is_sscn_yrewqx, [ffw, qce, atrss], 3, 1)), DerivedLevel("qsx", Window(is_sscn_qsx, [ffw, qce, atrss], 3, 1)), DerivedLevel("uoskx", Window(is_sscn_uoskx, [ffw, qce, atrss], 3, 1))])

design=[ffw,qce,atrss,sscn]
crossing=[sscn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END