from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rtbca= Factor("rtbca", ["wdcnuv","weees","tevmvl","loe","csskmf","ibf","tgddbk"])
zxtt= Factor("zxtt", ["wcaqjk","lln","yjdv","zltbig","wlran","kdtqcf","djyl","pub"])
def is_edud_hbbs(rtbca, zxtt):
    return rtbca[-1] == "ibf" and zxtt[0] != "wlran"
def is_edud_slsizl(rtbca, zxtt):
    return rtbca[-1] != "ibf" and zxtt[0] == "wlran"
def is_edud_swgha(rtbca, zxtt):
    return not (is_edud_hbbs(rtbca, zxtt) or is_edud_slsizl(rtbca, zxtt))
edud= Factor("edud", [DerivedLevel("hbbs", Transition(is_edud_hbbs, [rtbca, zxtt])), DerivedLevel("slsizl", Transition(is_edud_slsizl, [rtbca, zxtt])), DerivedLevel("swgha", Transition(is_edud_swgha, [rtbca, zxtt]))])

design=[rtbca,zxtt,edud]
crossing=[edud]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
