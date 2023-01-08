from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zwin = Factor("zwin", ["gylpcf","zdd","tid","lipuj","aajchu","flbwb","bixk","asxya"])
tqxev = Factor("tqxev", ["hnabb","nenp","blvuz","tkvk","rdjog","yub"])
def is_nwm_fbnbrn(zwin, tqxev):
    return zwin[-1] == "tid" and tqxev[0] != "yub"
def is_nwm_gex(zwin, tqxev):
    return zwin[-1] != "tid" and tqxev[0] == "yub"
def is_nwm_gliqlb(zwin, tqxev):
    return not (is_nwm_fbnbrn(zwin, tqxev) or is_nwm_gex(zwin, tqxev))
nwm = Factor("nwm", [DerivedLevel("fbnbrn", Window(is_nwm_fbnbrn, [zwin, tqxev], 2, 1)), DerivedLevel("gex", Window(is_nwm_gex, [zwin, tqxev], 2, 1)), DerivedLevel("gliqlb", Window(is_nwm_gliqlb, [zwin, tqxev], 2, 1))])

design=[zwin,tqxev,nwm]
crossing=[nwm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END