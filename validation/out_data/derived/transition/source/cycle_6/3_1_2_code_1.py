from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xatn = Factor("xatn", ["zzmnb","zqjdqg","agwq","opkof","lpx","fwxt","rhk"])
def epjo(xatn):
     return "rhk" == xatn[0] and xatn[-1] != "zqjdqg"
def dpmnri(xatn):
     return (not "rhk" != xatn[0]) and  xatn[-1] == "zqjdqg"
def jodp(xatn):
     return (not epjo(xatn)) and (not xatn[-1] == "zqjdqg")
grd = DerivedLevel("ftgjj", Transition(epjo, [xatn]))
xni = DerivedLevel("byul", Transition(dpmnri, [xatn]))
nxljwe = DerivedLevel("wuzutq", Transition(jodp, [xatn]))
wraa = Factor("lpnq", [grd, xni, nxljwe])

### EXPERIMENT
design=[xatn,wraa]
crossing=[wraa]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END