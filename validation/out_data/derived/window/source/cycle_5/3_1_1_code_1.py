from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ephyg = Factor("ephyg", ["klxa","chgc","vcnwcv","ofycwv","zctxz","xvikon","fsp"])
def khluue(ephyg):
     return "ofycwv" == ephyg[0] and not ephyg[-1] == "ofycwv"
def fmlw(ephyg):
     return not "ofycwv" == ephyg[0] and  "vcnwcv" == ephyg[-1]
def cmshgu(ephyg):
     return (not khluue(ephyg)) and (not ephyg[-1] == "vcnwcv")
wwpsay = DerivedLevel("pxky", Window(khluue, [ephyg],2,1))
vsiv = DerivedLevel("bcsghi", Window(fmlw, [ephyg],2,1))
ujz = DerivedLevel("gmpmeb", Window(cmshgu, [ephyg],2,1))
zwphls = Factor("ulhgwg", [wwpsay, vsiv, ujz])

### EXPERIMENT
design=[ephyg,zwphls]
crossing=[zwphls]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END