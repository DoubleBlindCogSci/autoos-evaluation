from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fmxd = Factor("fmxd", ["vhlg","maa","hcosa","unh","wqsak","ioxf"])
def tja(fmxd):
     return "hcosa" == fmxd[-1] and not fmxd[0] == "hcosa"
def aixubj(fmxd):
     return not "hcosa" == fmxd[-1] and  fmxd[0] == "maa"
def asx(fmxd):
     return (fmxd[-1] != "hcosa") and (not aixubj(fmxd))
vtdco = Factor("knikh", [DerivedLevel("wnlbw", Window(tja, [fmxd],2,1)), DerivedLevel("hsdr", Window(aixubj, [fmxd],2,1)),DerivedLevel("nykz", Window(asx, [fmxd],2,1))])
### EXPERIMENT
design=[fmxd,vtdco]
crossing=[vtdco]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END