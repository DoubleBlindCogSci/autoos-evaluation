from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uxyjnj= Factor("uxyjnj", ["mzu","ygl","nhyooa","ngolyh","twszfx","sjw"])
scdrdp= Factor("scdrdp", ["inryki","dvjwud","lfta","yjalb","yhxucp"])
def is_bxaau_vjgv(uxyjnj, scdrdp):
    return uxyjnj[0] == "mzu" or scdrdp[-3] != "dvjwud"
def is_bxaau_csj(uxyjnj, scdrdp):
    return not is_bxaau_vjgv(uxyjnj, scdrdp)
bxaau= Factor("bxaau", [DerivedLevel("vjgv", Window(is_bxaau_vjgv, [uxyjnj, scdrdp], 4, 1)), DerivedLevel("csj", Window(is_bxaau_csj, [uxyjnj, scdrdp], 4, 1))])

design=[uxyjnj,scdrdp,bxaau]
crossing=[bxaau]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END
