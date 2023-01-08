from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yxskru = Factor("yxskru", ["dlljcl","vrfb","wuhu","wuo","zhwffj","cyv","eougmo"])
xwdi = Factor("xwdi", ["dlljcl","vrfb","wuhu","wuo","zhwffj","cyv","eougmo"])
ybzis = Factor("ybzis", ["dlljcl","vrfb","wuhu","wuo","zhwffj","cyv","eougmo"])
def rish(yxskru, ybzis, xwdi):
     return yxskru[0] == ybzis[-1] and yxskru[-1] != xwdi[0]
def xyep(yxskru, ybzis, xwdi):
     return ybzis[-1] != yxskru[0] and yxskru[-1] == xwdi[0]
def crf(yxskru, ybzis, xwdi):
     return (not rish(yxskru, ybzis, xwdi)) and (not yxskru[-1] == xwdi[0])
wdduca = DerivedLevel("jtwgjn", Transition(rish, [yxskru, xwdi, ybzis]))
thayor = DerivedLevel("hjzs", Transition(xyep, [yxskru, xwdi, ybzis]))
mmvgjj = DerivedLevel("gnrwj", Transition(crf, [yxskru, xwdi, ybzis]))
uooi = Factor("keh", [wdduca, thayor, mmvgjj])

### EXPERIMENT
design=[yxskru,xwdi,ybzis,uooi]
crossing=[uooi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END