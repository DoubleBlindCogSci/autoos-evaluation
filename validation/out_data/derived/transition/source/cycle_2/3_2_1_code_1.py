from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rtbca = Factor("rtbca", ["wdcnuv","weees","tevmvl","loe","csskmf","ibf","tgddbk"])
zxtt = Factor("zxtt", ["wcaqjk","lln","yjdv","zltbig","wlran","kdtqcf","djyl","pub"])
def hkc(rtbca, zxtt):
     return "ibf" == rtbca[-1] and zxtt[0] != "wlran"
def eobbr(rtbca, zxtt):
     return "ibf" != rtbca[-1] and zxtt[0] == "wlran"
def zacjqf(rtbca, zxtt):
     return (not rtbca[-1] == "ibf") and (not eobbr(rtbca, zxtt))
bxhxol = DerivedLevel("hbbs", Transition(hkc, [rtbca, zxtt]))
ehngjl = DerivedLevel("slsizl", Transition(eobbr, [rtbca, zxtt]))
zio = DerivedLevel("swgha", Transition(zacjqf, [rtbca, zxtt]))
cyh = Factor("edud", [bxhxol, ehngjl, zio])

### EXPERIMENT
design=[rtbca,zxtt,cyh]
crossing=[cyh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END