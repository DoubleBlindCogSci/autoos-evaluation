from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
hhf = Factor("hhf", ["aumgo", "mav"])
glbouc = Factor("glbouc", ["utchpn", "cenp"])
apb = Factor("apb", ["aumgo", "mav"])
deff = Factor("deff", ["utchpn", "cenp"])
sfg = Factor("sfg", ["cjxkp", "pwwc"])
hpyuyl = Factor("hpyuyl", ["twhkmc", "meeugm"])
def is_iqne_kicuw(apb, deff):
    return apb == deff
def is_iqne_yhcqux(apb, deff):
    return not is_iqne_kicuw(apb, deff)
iqne = Factor("iqne", [DerivedLevel("kicuw", WithinTrial(is_iqne_kicuw, [apb, deff])), DerivedLevel("yhcqux", WithinTrial(is_iqne_yhcqux, [apb, deff]))])
constraints = []
crossing = [iqne, sfg]

design=[hhf,glbouc,apb,deff,sfg,hpyuyl,iqne]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_1_0"))
