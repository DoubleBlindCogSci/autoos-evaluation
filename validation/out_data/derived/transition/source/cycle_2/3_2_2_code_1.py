from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zfr = Factor("zfr", ["hefubi","ykc","lexmh","hqijd","zicb","fwrian"])
whs = Factor("whs", ["hefubi","ykc","lexmh","hqijd","zicb","fwrian"])
amxjcp = Factor("amxjcp", ["hefubi","ykc","lexmh","hqijd","zicb","fwrian"])
def dhaeta(zfr, whs, amxjcp):
     return zfr[0] == whs[-1] and zfr[-1] != amxjcp[0]
def uqngx(zfr, whs, amxjcp):
     return whs[-1] != zfr[0] and amxjcp[0] == zfr[-1]
def qoyvvj(zfr, whs, amxjcp):
     return (not zfr[0] == whs[-1]) and (zfr[-1] != amxjcp[0])
edmv = Factor("srpb", [DerivedLevel("ahjve", Transition(dhaeta, [zfr, whs, amxjcp])), DerivedLevel("wtj", Transition(uqngx, [zfr, whs, amxjcp])),DerivedLevel("oasw", Transition(qoyvvj, [zfr, whs, amxjcp]))])
### EXPERIMENT
design=[zfr,whs,amxjcp,edmv]
crossing=[edmv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END