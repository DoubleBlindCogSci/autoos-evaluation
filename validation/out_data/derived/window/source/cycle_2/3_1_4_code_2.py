from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sdlbze= Factor("sdlbze", ["gar","ydyws","ronryb","kowlow","aduc","yhyj","yepupr","fgzxj"])
def is_cfa_nrzh(sdlbze):
    return sdlbze[-3] == "gar" and sdlbze[-1] != "gar"
def is_cfa_hyzlfw(sdlbze):
    return sdlbze[-3] != "gar" and sdlbze[-1] == "aduc"
def is_cfa_osuagf(sdlbze):
    return not (is_cfa_nrzh(sdlbze) or is_cfa_hyzlfw(sdlbze))
cfa= Factor("cfa", [DerivedLevel("nrzh", Window(is_cfa_nrzh, [sdlbze], 4, 1)), DerivedLevel("hyzlfw", Window(is_cfa_hyzlfw, [sdlbze], 4, 1)), DerivedLevel("osuagf", Window(is_cfa_osuagf, [sdlbze], 4, 1))])

design=[sdlbze,cfa]
crossing=[cfa]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END
