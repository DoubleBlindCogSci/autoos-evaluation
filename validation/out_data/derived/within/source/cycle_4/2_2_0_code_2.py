from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jktwd = Factor("jktwd", ["nucsy","uoq","sbnttm","csziu","capr"])
tpegmg = Factor("tpegmg", ["nucsy","uoq","sbnttm","csziu","capr"])
xwd = Factor("xwd", ["nucsy","uoq","sbnttm","csziu","capr"])
def is_knxb_svydd(jktwd, tpegmg, xwd):
    return jktwd == tpegmg
def is_knxb_xjuqjp(jktwd, tpegmg, xwd):
    return not is_knxb_svydd(jktwd, tpegmg, xwd)
knxb= Factor("knxb", [DerivedLevel("svydd", WithinTrial(is_knxb_svydd, [jktwd, tpegmg, xwd])), DerivedLevel("xjuqjp", WithinTrial(is_knxb_xjuqjp, [jktwd, tpegmg, xwd]))])

design=[jktwd,tpegmg,xwd,knxb]
crossing=[knxb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END