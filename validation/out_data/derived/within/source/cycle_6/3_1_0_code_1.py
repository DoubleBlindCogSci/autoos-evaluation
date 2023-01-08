from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ppf = Factor("ppf", ["sqyxw","qzpevj","hmsmwv","rdxy","rjzf","ijlar"])
def zpfigl(ppf):
     return "hmsmwv" == ppf
def zykzsi(ppf):
     return ppf == "qzpevj"
def fsmsp(ppf):
     return (not zpfigl(ppf)) and (ppf != "qzpevj")
adit = Factor("jqgpn", [DerivedLevel("ljo", WithinTrial(zpfigl, [ppf])), DerivedLevel("lxz", WithinTrial(zykzsi, [ppf])),DerivedLevel("ibye", WithinTrial(fsmsp, [ppf]))])
### EXPERIMENT
design=[ppf,adit]
crossing=[adit]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END