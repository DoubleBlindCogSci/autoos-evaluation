from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rwrsdm = Factor("rwrsdm", ["aces","wra","fmka","yel","asnf","toojjb","tzjfni"])
rxykvf = Factor("rxykvf", ["aces","wra","fmka","yel","asnf","toojjb","tzjfni"])
vmyy = Factor("vmyy", ["aces","wra","fmka","yel","asnf","toojjb","tzjfni"])
def ykfx(rwrsdm, rxykvf, vmyy):
     return rxykvf[-3] == rwrsdm[-1] and rwrsdm[-3] != vmyy[-1]
def zjd(rwrsdm, rxykvf, vmyy):
     return rxykvf[-3] != rwrsdm[-1] and vmyy[-1] == rwrsdm[-3]
def psoh(rwrsdm, rxykvf, vmyy):
     return (not ykfx(rwrsdm, rxykvf, vmyy)) and (not rwrsdm[-3] == vmyy[-1])
ukbc = Factor("dzcim", [DerivedLevel("qsaeu", Window(ykfx, [rwrsdm, rxykvf, vmyy],4,1)), DerivedLevel("ehbbeo", Window(zjd, [rwrsdm, rxykvf, vmyy],4,1)),DerivedLevel("lec", Window(psoh, [rwrsdm, rxykvf, vmyy],4,1))])
### EXPERIMENT
design=[rwrsdm,rxykvf,vmyy,ukbc]
crossing=[ukbc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END