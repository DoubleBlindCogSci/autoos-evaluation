from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cfs = Factor("cfs", ["unbwah","hidt","muml","opnyde","jrt","wqptl","xtj","iwmwm"])
ytg = Factor("ytg", ["unbwah","hidt","muml","opnyde","jrt","wqptl","xtj","iwmwm"])
gjruka = Factor("gjruka", ["unbwah","hidt","muml","opnyde","jrt","wqptl","xtj","iwmwm"])
def khyzg(cfs, gjruka, ytg):
     return cfs == gjruka
def jfnhpi(cfs, gjruka, ytg):
     return gjruka != cfs and ytg == cfs
def njxe(cfs, gjruka, ytg):
     return (cfs != gjruka) and (not jfnhpi(cfs, gjruka, ytg))
mozr = DerivedLevel("gntah", WithinTrial(khyzg, [cfs, ytg, gjruka]))
lcex = DerivedLevel("wbey", WithinTrial(jfnhpi, [cfs, ytg, gjruka]))
vvkpsu = DerivedLevel("wtug", WithinTrial(njxe, [cfs, ytg, gjruka]))
aca = Factor("agrgs", [mozr, lcex, vvkpsu])

### EXPERIMENT
design=[cfs,ytg,gjruka,aca]
crossing=[aca]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END