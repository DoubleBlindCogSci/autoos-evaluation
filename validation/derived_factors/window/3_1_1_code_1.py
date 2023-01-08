from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
psxzzw = Factor("psxzzw", ["spa","iigdr","dhsxwz","urwb","sfr","hqigv","noe"])
def hhrnkb(psxzzw):
     return "spa" == psxzzw[-2] and not psxzzw[0] == "spa"
def kyo(psxzzw):
     return psxzzw[-2] != "spa" and  psxzzw[0] == "iigdr"
def rqxl(psxzzw):
     return (psxzzw[-2] != "spa") and (psxzzw[0] != "iigdr")
ngvb = DerivedLevel("sxxi", Window(hhrnkb, [psxzzw],3,1))
ywqddf = DerivedLevel("hsrtsa", Window(kyo, [psxzzw],3,1))
rknz = DerivedLevel("ile", Window(rqxl, [psxzzw],3,1))
eok = Factor("yknaja", [ngvb, ywqddf, rknz])

### EXPERIMENT
design=[psxzzw,eok]
crossing=[eok]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END