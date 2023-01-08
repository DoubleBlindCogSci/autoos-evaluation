from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
lxnxij = Factor("lxnxij", ["lwzqoa","urrq","uaul","sterc","rwtyfh","ajwxk","qfmuoj"])
xhik = Factor("xhik", ["lwzqoa","urrq","uaul","sterc","rwtyfh","ajwxk","qfmuoj"])
llerqc = Factor("llerqc", ["lwzqoa","urrq","uaul","sterc","rwtyfh","ajwxk","qfmuoj"])
def gvjyg(lxnxij, xhik, llerqc):
    return lxnxij[-1] == xhik[-2] and lxnxij[-2] == llerqc[-1]
def dtursk(lxnxij, xhik, llerqc):
    return lxnxij[-1] != xhik[-2] or not (lxnxij[-2] == llerqc[-1])
bxis = Factor("yadag", [DerivedLevel("lbfgh", Window(gvjyg, [lxnxij, xhik, llerqc],3,1)), DerivedLevel("dwtgix", Window(dtursk, [lxnxij, xhik, llerqc],3,1))])
### EXPERIMENT
design=[lxnxij,xhik,llerqc,bxis]
crossing=[bxis]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END