from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xkvzol = Factor("xkvzol", ["bwhmes","hglfvm","vxs","oardm","nxd","rmhnb","kqozyw"])
xeyjrr = Factor("xeyjrr", ["bwhmes","hglfvm","vxs","oardm","nxd","rmhnb","kqozyw"])
fdwq = Factor("fdwq", ["bwhmes","hglfvm","vxs","oardm","nxd","rmhnb","kqozyw"])
def is_rwnqf_cwkz(xkvzol, xeyjrr, fdwq):
    return xkvzol[-2] == xeyjrr[-1] and xkvzol[-1] != fdwq[-2]
def is_rwnqf_uvpjb(xkvzol, xeyjrr, fdwq):
    return xeyjrr[-1] != xkvzol[-2] and xkvzol[-1] == fdwq[-2]
def is_rwnqf_ihyhas(xkvzol, xeyjrr, fdwq):
    return not (is_rwnqf_cwkz(xkvzol, xeyjrr, fdwq) or is_rwnqf_uvpjb(xkvzol, xeyjrr, fdwq))
rwnqf = Factor("rwnqf", [DerivedLevel("cwkz", Window(is_rwnqf_cwkz, [xkvzol, xeyjrr, fdwq], 3, 1)), DerivedLevel("uvpjb", Window(is_rwnqf_uvpjb, [xkvzol, xeyjrr, fdwq], 3, 1)), DerivedLevel("ihyhas", Window(is_rwnqf_ihyhas, [xkvzol, xeyjrr, fdwq], 3, 1))])

design=[xkvzol,xeyjrr,fdwq,rwnqf]
crossing=[rwnqf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END