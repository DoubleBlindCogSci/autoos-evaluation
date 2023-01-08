from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
ftg = Factor("ftg", ["nqxlo", "iqtp"])
cdt = Factor("cdt", ["pcm", "hqiju"])
wgrk = Factor("wgrk", ["nqxlo", "iqtp"])
buvqha = Factor("buvqha", ["pcm", "hqiju"])
def nfrrw (cdt, wgrk):
    return cdt == wgrk
def jvymc (cdt, wgrk):
    return not nfrrw(cdt, wgrk)
gcu = Factor("gcu", [DerivedLevel("wziqu", WithinTrial(nfrrw, [cdt, wgrk])), DerivedLevel("slbd", WithinTrial(jvymc, [cdt, wgrk]))])
design=[gcu,ftg,cdt,wgrk,buvqha]
constraints=[MinimumTrials(35),ExactlyKInARow(3, gcu)]
crossing=[ftg,gcu]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_2"))
