from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jktwd = Factor("jktwd", ["nucsy","uoq","sbnttm","csziu","capr"])
tpegmg = Factor("tpegmg", ["nucsy","uoq","sbnttm","csziu","capr"])
xwd = Factor("xwd", ["nucsy","uoq","sbnttm","csziu","capr"])
def cwfmi(jktwd, tpegmg, xwd):
    return jktwd == tpegmg
def jqq(jktwd, tpegmg, xwd):
    return jktwd != tpegmg
zwqg = Factor("knxb", [DerivedLevel("svydd", WithinTrial(cwfmi, [jktwd, tpegmg, xwd])), DerivedLevel("xjuqjp", WithinTrial(jqq, [jktwd, tpegmg, xwd]))])
### EXPERIMENT
design=[jktwd,tpegmg,xwd,zwqg]
crossing=[zwqg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END