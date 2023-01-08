from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
osey= Factor("osey", ["gdikt","kwfvqa","qhrj","nyvv","ciolxg"])
ndkbz= Factor("ndkbz", ["gdikt","kwfvqa","qhrj","nyvv","ciolxg"])
dwwn= Factor("dwwn", ["gdikt","kwfvqa","qhrj","nyvv","ciolxg"])
def is_pktwz_gubi(osey, ndkbz, dwwn):
    return osey[0] != ndkbz[-1]
def is_pktwz_cdps(osey, ndkbz, dwwn):
    return not is_pktwz_gubi(osey, ndkbz, dwwn)
pktwz= Factor("pktwz", [DerivedLevel("gubi", Transition(is_pktwz_gubi, [osey, ndkbz, dwwn])), DerivedLevel("cdps", Transition(is_pktwz_cdps, [osey, ndkbz, dwwn]))])

design=[osey,ndkbz,dwwn,pktwz]
crossing=[pktwz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
