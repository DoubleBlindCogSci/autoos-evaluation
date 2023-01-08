from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ehx = Factor("ehx", ["pvzdw","qdmyk","twks","gch","uee","wcmw"])
def is_hyjga_baxa(ehx):
    return ehx[-1] != "qdmyk" or ehx[0] == "uee"
def is_hyjga_ebsnz(ehx):
    return not is_hyjga_baxa(ehx)
hyjga = Factor("hyjga", [DerivedLevel("baxa", Window(is_hyjga_baxa, [ehx], 2, 1)), DerivedLevel("ebsnz", Window(is_hyjga_ebsnz, [ehx], 2, 1))])

design=[ehx,hyjga]
crossing=[hyjga]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END