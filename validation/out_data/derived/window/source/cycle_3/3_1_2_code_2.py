from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
roi = Factor("roi", ["bgydaq","lgvbd","oyrlk","fdzye","pbyu","sdnyy","tcgzw","yvilsd"])
def is_gfws_unzl(roi):
    return roi[0] == "fdzye" and roi[-3] != "fdzye"
def is_gfws_wugp(roi):
    return roi[0] != "fdzye" and roi[-3] == "lgvbd"
def is_gfws_quuxfe(roi):
    return not (is_gfws_unzl(roi) or is_gfws_wugp(roi))
gfws= Factor("gfws", [DerivedLevel("unzl", Window(is_gfws_unzl, [roi], 4, 1)), DerivedLevel("wugp", Window(is_gfws_wugp, [roi], 4, 1)), DerivedLevel("quuxfe", Window(is_gfws_quuxfe, [roi], 4, 1))])

design=[roi,gfws]
crossing=[gfws]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END
