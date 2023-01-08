from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
lnc = Factor("lnc", ["wdzc","grzhyq","cfsi","kxy","wabm","mhh"])
ziyuus = Factor("ziyuus", ["wdzc","grzhyq","cfsi","kxy","wabm","mhh"])
fpj = Factor("fpj", ["wdzc","grzhyq","cfsi","kxy","wabm","mhh"])
def hzrcms(lnc, ziyuus, fpj):
    return lnc[-1] != ziyuus[0]
def jdk(lnc, ziyuus, fpj):
    return lnc[-1] == ziyuus[0]
gubqwb = Factor("dsny", [DerivedLevel("hxibgp", Window(hzrcms, [lnc, ziyuus, fpj],2,1)), DerivedLevel("cbvbbo", Window(jdk, [lnc, ziyuus, fpj],2,1))])
### EXPERIMENT
design=[lnc,ziyuus,fpj,gubqwb]
crossing=[gubqwb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END