from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ehx = Factor("ehx", ["pvzdw","qdmyk","twks","gch","uee","wcmw"])
def ando(ehx):
    return ehx[0] != "qdmyk" or ehx[-1] == "uee"
def mpjdj(ehx):
    return not (ehx[0] != "qdmyk") and ehx[-1] != "uee"
zekaq = Factor("hyjga", [DerivedLevel("baxa", Window(ando, [ehx],2,1)), DerivedLevel("ebsnz", Window(mpjdj, [ehx],2,1))])
### EXPERIMENT
design=[ehx,zekaq]
crossing=[zekaq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END