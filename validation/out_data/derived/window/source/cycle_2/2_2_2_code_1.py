from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uxyjnj = Factor("uxyjnj", ["mzu","ygl","nhyooa","ngolyh","twszfx","sjw"])
scdrdp = Factor("scdrdp", ["inryki","dvjwud","lfta","yjalb","yhxucp"])
def zbojsr(uxyjnj, scdrdp):
    return uxyjnj[0] == "mzu" or scdrdp[-3] != "dvjwud"
def xbhn(uxyjnj,scdrdp):
    return not (uxyjnj[0] == "mzu") and not (scdrdp[-3] != "dvjwud")
acvqk = DerivedLevel("vjgv", Window(zbojsr, [uxyjnj, scdrdp],4,1))
vdnga = DerivedLevel("csj", Window(xbhn, [uxyjnj, scdrdp],4,1))
kni = Factor("bxaau", [acvqk, vdnga])

### EXPERIMENT
design=[uxyjnj,scdrdp,kni]
crossing=[kni]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END