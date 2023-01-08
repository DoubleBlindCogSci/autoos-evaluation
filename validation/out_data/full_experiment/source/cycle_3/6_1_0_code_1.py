from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
hhf = Factor("hhf", ["aumgo", "mav"])
glbouc = Factor("glbouc", ["utchpn", "cenp"])
apb = Factor("apb", ["aumgo", "mav"])
deff = Factor("deff", ["utchpn", "cenp"])
sfg = Factor("sfg", ["cjxkp", "pwwc"])
hpyuyl = Factor("hpyuyl", ["twhkmc", "meeugm"])
def nqvjba (apb, deff):
    return apb == deff
def kyz (apb, deff):
    return not nqvjba(apb, deff)
iqne = Factor("iqne", [DerivedLevel("kicuw", WithinTrial(nqvjba, [apb, deff])), DerivedLevel("yhcqux", WithinTrial(kyz, [apb, deff]))])
design=[iqne,hhf,glbouc,apb,deff,sfg,hpyuyl]
constraints=[]
crossing=[iqne,sfg]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_0"))
