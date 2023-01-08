from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dyvxp = Factor("dyvxp", ["lori","cmqw","xrrl","npa","mae"])
akpu = Factor("akpu", ["eced","nvksz","lyct","mamgi","sednn"])
def hbb(dyvxp, akpu):
    return dyvxp != "xrrl" or akpu != "mamgi"
def tglx(dyvxp,akpu):
    return not (dyvxp != "xrrl") and akpu == "mamgi"
wlu = Factor("ekia", [DerivedLevel("qotj", WithinTrial(hbb, [dyvxp, akpu])), DerivedLevel("iacg", WithinTrial(tglx, [dyvxp, akpu]))])
### EXPERIMENT
design=[dyvxp,akpu,wlu]
crossing=[wlu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END