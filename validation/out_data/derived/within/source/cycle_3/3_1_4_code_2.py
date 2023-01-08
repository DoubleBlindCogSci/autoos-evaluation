from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
suhen = Factor("suhen", ["krpr","ufomf","nypxj","ezhsn","cjidu","jkpx","mhdkzw","bzj"])
def is_vuff_pfj(suhen):
    return suhen == "ezhsn"
def is_vuff_wdgbc(suhen):
    return suhen == "cjidu"
def is_vuff_vnmvgi(suhen):
    return not (is_vuff_pfj(suhen) or is_vuff_wdgbc(suhen))
vuff= Factor("vuff", [DerivedLevel("pfj", WithinTrial(is_vuff_pfj, [suhen])), DerivedLevel("wdgbc", WithinTrial(is_vuff_wdgbc, [suhen])), DerivedLevel("vnmvgi", WithinTrial(is_vuff_vnmvgi, [suhen]))])

design=[suhen,vuff]
crossing=[vuff]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END
