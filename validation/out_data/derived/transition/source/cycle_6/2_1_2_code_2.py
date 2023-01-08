from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vamcd = Factor("vamcd", ["vrqqx","rfmjl","azx","vlcx","szoehc","lnfm"])
def is_facr_qrcgfn(vamcd):
    return vamcd[0] == "azx" and vamcd[-1] == "vlcx"
def is_facr_swse(vamcd):
    return not is_facr_qrcgfn(vamcd)
facr = Factor("facr", [DerivedLevel("qrcgfn", Transition(is_facr_qrcgfn, [vamcd])), DerivedLevel("swse", Transition(is_facr_swse, [vamcd]))])

design=[vamcd,facr]
crossing=[facr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END