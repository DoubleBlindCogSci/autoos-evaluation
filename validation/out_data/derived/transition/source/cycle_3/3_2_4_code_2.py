from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yxskru = Factor("yxskru", ["dlljcl","vrfb","wuhu","wuo","zhwffj","cyv","eougmo"])
xwdi = Factor("xwdi", ["dlljcl","vrfb","wuhu","wuo","zhwffj","cyv","eougmo"])
ybzis = Factor("ybzis", ["dlljcl","vrfb","wuhu","wuo","zhwffj","cyv","eougmo"])
def is_keh_jtwgjn(yxskru, xwdi, ybzis):
    return yxskru[0] == ybzis[-1] and yxskru[-1] != xwdi[0]
def is_keh_hjzs(yxskru, xwdi, ybzis):
    return ybzis[-1] != yxskru[0] and yxskru[-1] == xwdi[0]
def is_keh_gnrwj(yxskru, xwdi, ybzis):
    return not (is_keh_jtwgjn(yxskru, xwdi, ybzis) or is_keh_hjzs(yxskru, xwdi, ybzis))
keh= Factor("keh", [DerivedLevel("jtwgjn", Transition(is_keh_jtwgjn, [yxskru, xwdi, ybzis])), DerivedLevel("hjzs", Transition(is_keh_hjzs, [yxskru, xwdi, ybzis])), DerivedLevel("gnrwj", Transition(is_keh_gnrwj, [yxskru, xwdi, ybzis]))])

design=[yxskru,xwdi,ybzis,keh]
crossing=[keh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END
