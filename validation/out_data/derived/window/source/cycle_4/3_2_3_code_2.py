from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rwrsdm = Factor("rwrsdm", ["aces","wra","fmka","yel","asnf","toojjb","tzjfni"])
rxykvf = Factor("rxykvf", ["aces","wra","fmka","yel","asnf","toojjb","tzjfni"])
vmyy = Factor("vmyy", ["aces","wra","fmka","yel","asnf","toojjb","tzjfni"])
def is_dzcim_qsaeu(rwrsdm, rxykvf, vmyy):
    return rxykvf[-3] == rwrsdm[-1] and rwrsdm[-3] != vmyy[-1]
def is_dzcim_ehbbeo(rwrsdm, rxykvf, vmyy):
    return rxykvf[-3] != rwrsdm[-1] and rwrsdm[-3] == vmyy[-1]
def is_dzcim_lec(rwrsdm, rxykvf, vmyy):
    return not (is_dzcim_qsaeu(rwrsdm, rxykvf, vmyy) or is_dzcim_ehbbeo(rwrsdm, rxykvf, vmyy))
dzcim = Factor("dzcim", [DerivedLevel("qsaeu", Window(is_dzcim_qsaeu, [rwrsdm, rxykvf, vmyy], 4, 1)), DerivedLevel("ehbbeo", Window(is_dzcim_ehbbeo, [rwrsdm, rxykvf, vmyy], 4, 1)), DerivedLevel("lec", Window(is_dzcim_lec, [rwrsdm, rxykvf, vmyy], 4, 1))])

design=[rwrsdm,rxykvf,vmyy,dzcim]
crossing=[dzcim]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END