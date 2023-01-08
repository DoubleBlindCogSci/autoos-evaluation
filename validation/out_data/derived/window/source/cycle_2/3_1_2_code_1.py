from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
phpbdt = Factor("phpbdt", ["xmibby","kvd","uwwtg","mdo","zlfa","ctg"])
def mvaq(phpbdt):
     return phpbdt[-2] == "kvd" and not phpbdt[-1] == "kvd"
def gkuhf(phpbdt):
     return not "kvd" == phpbdt[-2] and  "zlfa" == phpbdt[-1]
def vxa(phpbdt):
     return (not mvaq(phpbdt)) and (not gkuhf(phpbdt))
ljyeu = DerivedLevel("lsy", Window(mvaq, [phpbdt],3,1))
sgwv = DerivedLevel("fxiti", Window(gkuhf, [phpbdt],3,1))
frmgfa = DerivedLevel("aydm", Window(vxa, [phpbdt],3,1))
fegh = Factor("jkfrap", [ljyeu, sgwv, frmgfa])

### EXPERIMENT
design=[phpbdt,fegh]
crossing=[fegh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END