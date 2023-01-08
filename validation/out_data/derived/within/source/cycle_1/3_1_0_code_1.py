from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
swz = Factor("swz", ["ucnqkl","gxliu","wsxdz","gtlksr","bii","xdtrys"])
def vjxfqd(swz):
     return swz == "gxliu"
def jisyxl(swz):
     return "bii" == swz
def uhmbng(swz):
     return (swz != "gxliu") and (swz != "bii")
riu = Factor("sxq", [DerivedLevel("zlxf", WithinTrial(vjxfqd, [swz])), DerivedLevel("bjfgc", WithinTrial(jisyxl, [swz])),DerivedLevel("cuouqr", WithinTrial(uhmbng, [swz]))])
### EXPERIMENT
design=[swz,riu]
crossing=[riu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END