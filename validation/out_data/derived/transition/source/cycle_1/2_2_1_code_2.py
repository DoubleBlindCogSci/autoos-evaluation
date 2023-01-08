from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ufgywf= Factor("ufgywf", ["xmtfpe","ehji","ayiczf","izdsqj","snhh","cxpgi","hyshb"])
rudnb= Factor("rudnb", ["xmtfpe","ehji","ayiczf","izdsqj","snhh","cxpgi","hyshb"])
inb= Factor("inb", ["xmtfpe","ehji","ayiczf","izdsqj","snhh","cxpgi","hyshb"])
def is_jxoudi_epi(ufgywf, rudnb):
    return ufgywf[0] == rudnb[-1]
def is_jxoudi_oeefb(ufgywf, rudnb):
    return not is_jxoudi_epi(ufgywf, rudnb)
jxoudi= Factor("jxoudi", [DerivedLevel("epi", Transition(is_jxoudi_epi, [ufgywf, rudnb])), DerivedLevel("oeefb", Transition(is_jxoudi_oeefb, [ufgywf, rudnb]))])

design=[ufgywf,rudnb,inb,jxoudi]
crossing=[jxoudi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
