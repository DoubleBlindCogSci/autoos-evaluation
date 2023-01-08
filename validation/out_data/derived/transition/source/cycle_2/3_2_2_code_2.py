from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zfr= Factor("zfr", ["hefubi","ykc","lexmh","hqijd","zicb","fwrian"])
whs= Factor("whs", ["hefubi","ykc","lexmh","hqijd","zicb","fwrian"])
amxjcp= Factor("amxjcp", ["hefubi","ykc","lexmh","hqijd","zicb","fwrian"])
def is_srpb_ahjve(zfr, whs, amxjcp):
    return zfr[0] == whs[-1] and zfr[-1] != amxjcp[0]
def is_srpb_wtj(zfr, whs, amxjcp):
    return whs[-1] != zfr[0] and amxjcp[0] == zfr[-1]
def is_srpb_oasw(zfr, whs, amxjcp):
    return not (is_srpb_ahjve(zfr, whs, amxjcp) or is_srpb_wtj(zfr, whs, amxjcp))
srpb= Factor("srpb", [DerivedLevel("ahjve", Transition(is_srpb_ahjve, [zfr, whs, amxjcp])), DerivedLevel("wtj", Transition(is_srpb_wtj, [zfr, whs, amxjcp])), DerivedLevel("oasw", Transition(is_srpb_oasw, [zfr, whs, amxjcp]))])

design=[zfr,whs,amxjcp,srpb]
crossing=[srpb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END
