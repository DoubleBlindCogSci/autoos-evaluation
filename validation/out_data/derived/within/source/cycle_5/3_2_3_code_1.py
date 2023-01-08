from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qnydp = Factor("qnydp", ["nervs","yui","exbykd","ofjg","pnkdfj","kpip","gmy","jsno"])
wayn = Factor("wayn", ["ljxc","hdyo","engxux","atdyxi","dtuvgm","zjhnyn","tvb","rinri"])
def gguc(qnydp, wayn):
     return qnydp == "ofjg"
def tljbaz(qnydp, wayn):
     return "ofjg" != qnydp and  wayn == "tvb"
def pssejb(qnydp, wayn):
     return (qnydp != "ofjg") and (not wayn == "tvb")
phvxez = Factor("ltd", [DerivedLevel("xqosw", WithinTrial(gguc, [qnydp, wayn])), DerivedLevel("eortzq", WithinTrial(tljbaz, [qnydp, wayn])),DerivedLevel("czvpgj", WithinTrial(pssejb, [qnydp, wayn]))])
### EXPERIMENT
design=[qnydp,wayn,phvxez]
crossing=[phvxez]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END