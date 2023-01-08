from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wkubq= Factor("wkubq", ["rayt","zjpnms","cfa","msyvl","nbwg","czw"])
def is_wze_miacvj(wkubq):
    return wkubq == "rayt"
def is_wze_xqgv(wkubq):
    return wkubq == "msyvl"
def is_wze_djghro(wkubq):
    return wkubq != "rayt" and wkubq != "msyvl"
wze= Factor("wze", [DerivedLevel("miacvj", WithinTrial(is_wze_miacvj, [wkubq])), DerivedLevel("xqgv", WithinTrial(is_wze_xqgv, [wkubq])), DerivedLevel("djghro", WithinTrial(is_wze_djghro, [wkubq]))])

design=[wkubq, wze]
crossing=[wze]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END
