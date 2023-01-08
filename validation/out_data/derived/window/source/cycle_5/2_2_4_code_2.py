from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dctt = Factor("dctt", ["bguc","fojt","lte","oiq","ivyk","aezr"])
zftfq = Factor("zftfq", ["tkrv","rktx","kpf","ssf","wllw","vohs"])
def is_ibcdmx_uuov(dctt, zftfq):
    return dctt[-2] != "oiq" or zftfq[0] == "tkrv"
def is_ibcdmx_npy(dctt, zftfq):
    return not is_ibcdmx_uuov(dctt, zftfq)
ibcdmx = Factor("ibcdmx", [DerivedLevel("uuov", Window(is_ibcdmx_uuov, [dctt, zftfq], 3, 1)), DerivedLevel("npy", Window(is_ibcdmx_npy, [dctt, zftfq], 3, 1))])

design=[dctt,zftfq,ibcdmx]
crossing=[ibcdmx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END