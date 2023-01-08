from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xdmw = Factor("xdmw", ["toqcz","jmo","ozq","fkrzoq","udxdqm","grtdkn"])
jbuwv = Factor("jbuwv", ["pbwyzq","sxkube","idbiq","jepqi","bwchkn","xnxzio","vjw"])
def sjiwk(xdmw, jbuwv):
    return xdmw[0] != "toqcz" or jbuwv[-1] == "vjw"
def lvqv(xdmw,jbuwv):
    return xdmw[0] == "toqcz" and jbuwv[-1] != "vjw"
etvsdv = Factor("zbomms", [DerivedLevel("zyvsm", Window(sjiwk, [xdmw, jbuwv],2,1)), DerivedLevel("yqfyl", Window(lvqv, [xdmw, jbuwv],2,1))])
### EXPERIMENT
design=[xdmw,jbuwv,etvsdv]
crossing=[etvsdv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END