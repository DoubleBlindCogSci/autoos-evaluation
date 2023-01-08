### REGULAR FACTORS
hhf = Factor("hhf", ["aumgo", "mav"])
glbouc = Factor("glbouc", ["utchpn", "cenp"])
apb = Factor("apb", ["aumgo", "mav"])
deff = Factor("deff", ["utchpn", "cenp"])
sfg = Factor("sfg", ["cjxkp", "pwwc"])
hpyuyl = Factor("hpyuyl", ["twhkmc", "meeugm"])
### DERIVED FACTORS
##
def nqvjba (apb, deff):
    return apb == deff
def kyz (apb, deff):
    return not nqvjba(apb, deff)
iqne = Factor("iqne", [DerivedLevel("kicuw", WithinTrial(nqvjba, [apb, deff])), DerivedLevel("yhcqux", WithinTrial(kyz, [apb, deff]))])
##
### EXPERIMENT
design=[iqne,hhf,glbouc,apb,deff,sfg,hpyuyl]
constraints=[]
crossing=[iqne,sfg]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
