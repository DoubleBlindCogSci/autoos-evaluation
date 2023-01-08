from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
wkubq = Factor("wkubq", ["rayt","zjpnms","cfa","msyvl","nbwg","czw"])
def bgd(wkubq):
     return wkubq == "rayt"
def dvge(wkubq):
     return "msyvl" == wkubq
def nvdd(wkubq):
     return (not wkubq == "rayt") and (not wkubq == "msyvl")
bbzcn = Factor("wze", [DerivedLevel("miacvj", WithinTrial(bgd, [wkubq])), DerivedLevel("xqgv", WithinTrial(dvge, [wkubq])),DerivedLevel("djghro", WithinTrial(nvdd, [wkubq]))])
### EXPERIMENT
design=[wkubq,bbzcn]
crossing=[bbzcn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END