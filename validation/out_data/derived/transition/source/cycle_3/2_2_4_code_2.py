from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wvbcpr = Factor("wvbcpr", ["tvu","sibqd","zngsmx","vyhnva","cuye"])
gojw = Factor("gojw", ["eye","bpk","imevr","xcdji","boz","rjceq","huhrj"])
def is_xpvgza_feeiiy(wvbcpr, gojw):
    return wvbcpr[0] == "cuye" or gojw[-1] != "eye"
def is_xpvgza_oudod(wvbcpr, gojw):
    return not is_xpvgza_feeiiy(wvbcpr, gojw)
xpvgza= Factor("xpvgza", [DerivedLevel("feeiiy", Transition(is_xpvgza_feeiiy, [wvbcpr, gojw])), DerivedLevel("oudod", Transition(is_xpvgza_oudod, [wvbcpr, gojw]))])

design=[wvbcpr,gojw,xpvgza]
crossing=[xpvgza]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END
