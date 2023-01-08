from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
ftg = Factor("ftg", ["nqxlo", "iqtp"])
cdt = Factor("cdt", ["pcm", "hqiju"])
wgrk = Factor("wgrk", ["nqxlo", "iqtp"])
buvqha = Factor("buvqha", ["pcm", "hqiju"])
def is_gcu_wziqu(cdt, wgrk):
    return cdt == wgrk
def is_gcu_slbd(cdt, wgrk):
    return not is_gcu_wziqu(cdt, wgrk)
gcu = Factor("gcu", [DerivedLevel("wziqu", WithinTrial(is_gcu_wziqu, [cdt, wgrk])), DerivedLevel("slbd", WithinTrial(is_gcu_slbd, [cdt, wgrk]))])
constraints = [MinimumTrials(35), ExactlyK(3, (gcu, "wziqu"))]
crossing = [ftg, gcu]

design=[ftg,cdt,wgrk,buvqha,gcu]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_2"))
