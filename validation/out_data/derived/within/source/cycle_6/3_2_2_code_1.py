from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
khg = Factor("khg", ["das","nef","nzdsi","mlbqzo","qlnb","quq"])
jcs = Factor("jcs", ["kojxp","nnj","kbf","hrrluj","uftz","kwakqp","dbo"])
def jnzxb(khg, jcs):
     return "mlbqzo" == khg
def vspr(khg, jcs):
     return khg != "mlbqzo" and  jcs == "hrrluj"
def gqagd(khg, jcs):
     return (not khg == "mlbqzo") and (jcs != "hrrluj")
pooq = DerivedLevel("qwzph", WithinTrial(jnzxb, [khg, jcs]))
tju = DerivedLevel("adqp", WithinTrial(vspr, [khg, jcs]))
hkbv = DerivedLevel("xxmgu", WithinTrial(gqagd, [khg, jcs]))
oxdgdz = Factor("ojj", [pooq, tju, hkbv])

### EXPERIMENT
design=[khg,jcs,oxdgdz]
crossing=[oxdgdz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END