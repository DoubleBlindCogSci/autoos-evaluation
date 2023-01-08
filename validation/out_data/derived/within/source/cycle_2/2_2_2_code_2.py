from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dyvxp= Factor("dyvxp", ["lori","cmqw","xrrl","npa","mae"])
akpu= Factor("akpu", ["eced","nvksz","lyct","mamgi","sednn"])
def is_ekia_qotj(dyvxp, akpu):
    return dyvxp != "xrrl" or akpu != "mamgi"
def is_ekia_iacg(dyvxp, akpu):
    return dyvxp == "xrrl" and akpu == "mamgi"
ekia= Factor("ekia", [DerivedLevel("qotj", WithinTrial(is_ekia_qotj, [dyvxp, akpu])), DerivedLevel("iacg", WithinTrial(is_ekia_iacg, [dyvxp, akpu]))])

design=[dyvxp,akpu, ekia]
crossing=[ekia]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END
