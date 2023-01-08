from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
loslz = Factor("loslz", ["acnxo", "igqh"])
odd = Factor("odd", ["bojkc", "phe"])
mefc = Factor("mefc", ["acnxo", "igqh"])
hkki = Factor("hkki", ["bojkc", "phe"])
oju = Factor("oju", ["vsw", "xfg"])
def is_djawfc_clt(oju, hkki):
    return oju == hkki
def is_djawfc_pkadp(oju, hkki):
    return not is_djawfc_clt(oju, hkki)
djawfc = Factor("djawfc", [DerivedLevel("clt", WithinTrial(is_djawfc_clt, [oju, hkki])), DerivedLevel("pkadp", WithinTrial(is_djawfc_pkadp, [oju, hkki]))])
constraints = [AtLeastKInARow(4, mefc), MinimumTrials(27)]
crossing = [djawfc, hkki]

design=[loslz,odd,mefc,hkki,oju,djawfc]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/5_1_2"))
