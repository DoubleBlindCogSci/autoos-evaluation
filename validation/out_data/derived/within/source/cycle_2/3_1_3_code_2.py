from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ctsqk= Factor("ctsqk", ["ghrgkn","aib","udt","enst","thwcoh","gsny","yiaap","gipumh"])
def is_qpl_hij(ctsqk):
    return ctsqk == "thwcoh"
def is_qpl_uduqbi(ctsqk):
    return ctsqk == "gipumh"
def is_qpl_vpdbxc(ctsqk):
    return not (is_qpl_hij(ctsqk) or is_qpl_uduqbi(ctsqk))
qpl= Factor("qpl", [DerivedLevel("hij", WithinTrial(is_qpl_hij, [ctsqk])), DerivedLevel("uduqbi", WithinTrial(is_qpl_uduqbi, [ctsqk])), DerivedLevel("vpdbxc", WithinTrial(is_qpl_vpdbxc, [ctsqk]))])

design=[ctsqk, qpl]
crossing=[qpl]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END
