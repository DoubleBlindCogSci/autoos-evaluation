from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lxnxij = Factor("lxnxij", ["lwzqoa","urrq","uaul","sterc","rwtyfh","ajwxk","qfmuoj"])
xhik = Factor("xhik", ["lwzqoa","urrq","uaul","sterc","rwtyfh","ajwxk","qfmuoj"])
llerqc = Factor("llerqc", ["lwzqoa","urrq","uaul","sterc","rwtyfh","ajwxk","qfmuoj"])
def is_yadag_lbfgh(lxnxij, xhik, llerqc):
    return lxnxij[-1] == xhik[-2] and lxnxij[-2] == llerqc[-1]
def is_yadag_dwtgix(lxnxij, xhik, llerqc):
    return not is_yadag_lbfgh(lxnxij, xhik, llerqc)
yadag = Factor("yadag", [DerivedLevel("lbfgh", Window(is_yadag_lbfgh, [lxnxij, xhik, llerqc], 3, 1)), DerivedLevel("dwtgix", Window(is_yadag_dwtgix, [lxnxij, xhik, llerqc], 3, 1))])

design=[lxnxij,xhik,llerqc,yadag]
crossing=[yadag]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END