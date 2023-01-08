from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xdmw = Factor("xdmw", ["toqcz","jmo","ozq","fkrzoq","udxdqm","grtdkn"])
jbuwv = Factor("jbuwv", ["pbwyzq","sxkube","idbiq","jepqi","bwchkn","xnxzio","vjw"])
def is_zbomms_zyvsm(xdmw, jbuwv):
    return xdmw[0] != "toqcz" or jbuwv[-1] == "vjw"
def is_zbomms_yqfyl(xdmw, jbuwv):
    return not is_zbomms_zyvsm(xdmw, jbuwv)
zbomms= Factor("zbomms", [DerivedLevel("zyvsm", Window(is_zbomms_zyvsm, [xdmw, jbuwv], 2, 1)), DerivedLevel("yqfyl", Window(is_zbomms_yqfyl, [xdmw, jbuwv], 2, 1))])

design=[xdmw,jbuwv,zbomms]
crossing=[zbomms]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END