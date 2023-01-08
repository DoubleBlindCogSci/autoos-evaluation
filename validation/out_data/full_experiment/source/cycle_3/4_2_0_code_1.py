from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
vipu = Factor("vipu", ["nqaj", "fftz"])
pfl = Factor("pfl", ["vyo", "xkgy"])
nshhcw = Factor("nshhcw", ["nqaj", "fftz"])
bwmn = Factor("bwmn", ["vyo", "xkgy"])
def wtml (bwmn, nshhcw):
    return bwmn == nshhcw
def szk (bwmn, nshhcw):
    return not wtml(bwmn, nshhcw)
yic = Factor("yic", [DerivedLevel("guxkbh", WithinTrial(wtml, [bwmn, nshhcw])), DerivedLevel("wekqv", WithinTrial(szk, [bwmn, nshhcw]))])
def tozk (pfl, vipu):
    return pfl == vipu
def fwwj (pfl, vipu):
    return not tozk(pfl, vipu)
sxt = Factor("sxt", [DerivedLevel("pzruw", WithinTrial(tozk, [pfl, vipu])), DerivedLevel("mcsdum", WithinTrial(fwwj, [pfl, vipu]))])
design=[yic,sxt,vipu,pfl,nshhcw,bwmn]
constraints=[]
crossing=[pfl,bwmn]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_0"))
