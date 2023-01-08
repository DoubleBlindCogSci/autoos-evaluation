from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xkvzol = Factor("xkvzol", ["bwhmes","hglfvm","vxs","oardm","nxd","rmhnb","kqozyw"])
xeyjrr = Factor("xeyjrr", ["bwhmes","hglfvm","vxs","oardm","nxd","rmhnb","kqozyw"])
fdwq = Factor("fdwq", ["bwhmes","hglfvm","vxs","oardm","nxd","rmhnb","kqozyw"])
def ljwnh(xkvzol, xeyjrr, fdwq):
     return xkvzol[-2] == xeyjrr[-1] and xkvzol[-1] != fdwq[-2]
def qeyvjo(xkvzol, xeyjrr, fdwq):
     return xeyjrr[-1] != xkvzol[-2] and xkvzol[-1] == fdwq[-2]
def dmvw(xkvzol, xeyjrr, fdwq):
     return (not xkvzol[-2] == xeyjrr[-1]) and (not qeyvjo(xkvzol, xeyjrr, fdwq))
bzndc = Factor("rwnqf", [DerivedLevel("cwkz", Window(ljwnh, [xkvzol, xeyjrr, fdwq],3,1)), DerivedLevel("uvpjb", Window(qeyvjo, [xkvzol, xeyjrr, fdwq],3,1)),DerivedLevel("ihyhas", Window(dmvw, [xkvzol, xeyjrr, fdwq],3,1))])
### EXPERIMENT
design=[xkvzol,xeyjrr,fdwq,bzndc]
crossing=[bzndc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END