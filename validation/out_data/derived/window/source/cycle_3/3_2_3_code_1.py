from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xzar = Factor("xzar", ["czr","kradd","einxyr","anxmad","yrfr","xdmei","jhpjrv","jix"])
fnhg = Factor("fnhg", ["ooollz","zrxn","brvdut","fybb","whgo","zigtjm","toz"])
def wunm(xzar, fnhg):
     return "jhpjrv" == xzar[0] and not fnhg[-2] == "zigtjm"
def wfhhd(xzar, fnhg):
     return xzar[0] != "jhpjrv" and  fnhg[-2] == "zigtjm"
def pxfzbu(xzar, fnhg):
     return (not wunm(xzar, fnhg)) and (not wfhhd(xzar, fnhg))
expra = Factor("svpnhe", [DerivedLevel("vkj", Window(wunm, [xzar, fnhg],3,1)), DerivedLevel("xkghzg", Window(wfhhd, [xzar, fnhg],3,1)),DerivedLevel("dxo", Window(pxfzbu, [xzar, fnhg],3,1))])
### EXPERIMENT
design=[xzar,fnhg,expra]
crossing=[expra]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END