from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jqnhlp = Factor("jqnhlp", ["hyl","qugw","mwgk","ojnya","kpg","zul","mjsx"])
def tkzr(jqnhlp):
     return jqnhlp[0] == "ojnya"
def xbrdbz(jqnhlp):
     return "mjsx" == jqnhlp[-1]
def fqfno(jqnhlp):
     return (not jqnhlp[0] == "ojnya") and (not jqnhlp[-1] == "mjsx")
owuhjx = Factor("ylw", [DerivedLevel("vszfo", Transition(tkzr, [jqnhlp])), DerivedLevel("bqhaz", Transition(xbrdbz, [jqnhlp])),DerivedLevel("ugwna", Transition(fqfno, [jqnhlp]))])
### EXPERIMENT
design=[jqnhlp,owuhjx]
crossing=[owuhjx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END