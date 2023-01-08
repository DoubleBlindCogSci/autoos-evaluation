from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dctt = Factor("dctt", ["bguc","fojt","lte","oiq","ivyk","aezr"])
zftfq = Factor("zftfq", ["tkrv","rktx","kpf","ssf","wllw","vohs"])
def uqhxhw(dctt, zftfq):
    return dctt[-2] != "oiq" or zftfq[0] == "tkrv"
def fnt(dctt,zftfq):
    return not (dctt[-2] != "oiq") and not (zftfq[0] == "tkrv")
mlq = DerivedLevel("uuov", Window(uqhxhw, [dctt, zftfq],3,1))
zgfi = DerivedLevel("npy", Window(fnt, [dctt, zftfq],3,1))
ypl = Factor("ibcdmx", [mlq, zgfi])

### EXPERIMENT
design=[dctt,zftfq,ypl]
crossing=[ypl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END