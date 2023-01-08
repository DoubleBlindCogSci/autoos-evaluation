from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ephyg = Factor("ephyg", ["klxa","chgc","vcnwcv","ofycwv","zctxz","xvikon","fsp"])
def is_ulhgwg_pxky(ephyg):
    return ephyg[0] == "ofycwv" and ephyg[-1] != "ofycwv"
def is_ulhgwg_bcsghi(ephyg):
    return ephyg[0] != "ofycwv" and ephyg[-1] == "vcnwcv"
def is_ulhgwg_gmpmeb(ephyg):
    return not (is_ulhgwg_pxky(ephyg) or is_ulhgwg_bcsghi(ephyg))
ulhgwg = Factor("ulhgwg", [DerivedLevel("pxky", Window(is_ulhgwg_pxky, [ephyg], 2, 1)), DerivedLevel("bcsghi", Window(is_ulhgwg_bcsghi, [ephyg], 2, 1)), DerivedLevel("gmpmeb", Window(is_ulhgwg_gmpmeb, [ephyg], 2, 1))])

design=[ephyg,ulhgwg]
crossing=[ulhgwg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END