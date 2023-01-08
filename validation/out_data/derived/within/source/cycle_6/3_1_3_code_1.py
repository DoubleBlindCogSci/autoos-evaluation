from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
flf = Factor("flf", ["mzt","idcvup","ejpvyk","lliic","igbcrl","hwlruj","tbtts","rieymr"])
def lfs(flf):
     return "igbcrl" == flf
def keg(flf):
     return flf == "hwlruj"
def tkv(flf):
     return (not lfs(flf)) and (not keg(flf))
zmaj = DerivedLevel("hne", WithinTrial(lfs, [flf]))
hvoeb = DerivedLevel("naof", WithinTrial(keg, [flf]))
lfxs = DerivedLevel("hanqhq", WithinTrial(tkv, [flf]))
fqm = Factor("cpgwf", [zmaj, hvoeb, lfxs])

### EXPERIMENT
design=[flf,fqm]
crossing=[fqm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END