from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
loslz = Factor("loslz", ["acnxo", "igqh"])
odd = Factor("odd", ["bojkc", "phe"])
mefc = Factor("mefc", ["acnxo", "igqh"])
hkki = Factor("hkki", ["bojkc", "phe"])
oju = Factor("oju", ["vsw", "xfg"])
def sko (oju, hkki):
    return oju == hkki
def ynim (oju, hkki):
    return not sko(oju, hkki)
djawfc = Factor("djawfc", [DerivedLevel("clt", WithinTrial(sko, [oju, hkki])), DerivedLevel("pkadp", WithinTrial(ynim, [oju, hkki]))])
design=[djawfc,loslz,odd,mefc,hkki,oju]
constraints=[MinimumTrials(27),AtLeastKInARow(4, mefc)]
crossing=[djawfc,hkki]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_1_2"))
