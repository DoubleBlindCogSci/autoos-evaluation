from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bizdwj = Factor("bizdwj", ["vypgxy","fudwe","sajrms","szdw","hmhd","pdtii"])
def zwseef(bizdwj):
     return "hmhd" == bizdwj
def olij(bizdwj):
     return bizdwj == "vypgxy"
def hgsj(bizdwj):
     return (not zwseef(bizdwj)) and (not olij(bizdwj))
xhudsy = Factor("pxtv", [DerivedLevel("ngx", WithinTrial(zwseef, [bizdwj])), DerivedLevel("iepfn", WithinTrial(olij, [bizdwj])),DerivedLevel("otcg", WithinTrial(hgsj, [bizdwj]))])
### EXPERIMENT
design=[bizdwj,xhudsy]
crossing=[xhudsy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END