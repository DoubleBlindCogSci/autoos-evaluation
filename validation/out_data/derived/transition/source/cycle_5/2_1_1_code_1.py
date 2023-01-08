from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dikfjs = Factor("dikfjs", ["nyx","bma","petkz","gyap","fgw"])
def vnc(dikfjs):
    return dikfjs[0] == "nyx" or dikfjs[-1] != "petkz"
def ubezwx(dikfjs):
    return dikfjs[0] != "nyx" and not (dikfjs[-1] != "petkz")
pgdskw = DerivedLevel("bgkms", Transition(vnc, [dikfjs]))
ctlx = DerivedLevel("dzzqz", Transition(ubezwx, [dikfjs]))
kfik = Factor("ygkt", [pgdskw, ctlx])

### EXPERIMENT
design=[dikfjs,kfik]
crossing=[kfik]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END