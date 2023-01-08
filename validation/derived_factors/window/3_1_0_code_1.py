from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
eogjc = Factor("eogjc", ["jgzfq","sbohcz","uzjcr","bytwvi","tflo","ttrmbh","dizicq"])
def objcth(eogjc):
     return "tflo" == eogjc[0] and not eogjc[-1] == "tflo"
def tlnda(eogjc):
     return not "tflo" == eogjc[0] and  "dizicq" == eogjc[-1]
def erqt(eogjc):
     return (eogjc[0] != "tflo") and (not tlnda(eogjc))
pweof = DerivedLevel("jcndf", Window(objcth, [eogjc],2,1))
tyx = DerivedLevel("chjln", Window(tlnda, [eogjc],2,1))
eln = DerivedLevel("the", Window(erqt, [eogjc],2,1))
dnhoe = Factor("qyyis", [pweof, tyx, eln])

### EXPERIMENT
design=[eogjc,dnhoe]
crossing=[dnhoe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END