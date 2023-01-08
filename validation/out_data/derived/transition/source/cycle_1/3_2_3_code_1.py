from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dwrpg = Factor("dwrpg", ["kjdt","syccui","nuzuca","jbwexv","fayn","vut"])
ossys = Factor("ossys", ["jvvyw","xru","juns","bct","slm","gunfs","rijlq","mykt"])
def sifpqk(dwrpg, ossys):
     return "kjdt" == dwrpg[-1]
def jjuqdb(dwrpg, ossys):
     return dwrpg[-1] != "kjdt" and  ossys[0] == "juns"
def fhqe(dwrpg, ossys):
     return (not sifpqk(dwrpg, ossys)) and (not ossys[0] == "juns")
ojhtof = DerivedLevel("zphjm", Transition(sifpqk, [dwrpg, ossys]))
gxl = DerivedLevel("cgtyi", Transition(jjuqdb, [dwrpg, ossys]))
fdg = DerivedLevel("ugeqmm", Transition(fhqe, [dwrpg, ossys]))
hldz = Factor("itia", [ojhtof, gxl, fdg])

### EXPERIMENT
design=[dwrpg,ossys,hldz]
crossing=[hldz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END