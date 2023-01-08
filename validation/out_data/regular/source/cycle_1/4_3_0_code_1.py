from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
JfmA=Factor('DGMf',['KFBYQRG$t(8Rt',':evlU^Da0n','fkMsUUrrVwnq','EYtgegWyFLEZC'])
dOD2=Factor('$BqTAtQZR',[Level("deuc_<b",3),"Qnm[)WPhY","CPvx",";Eskx"])
rMVGG=Factor("RJdhjTrR)",['vAONvJuQMfDD','KX%LpLfwX','tL10fRF|iM',"@Ey"])

### EXPERIMENT
design=[JfmA,dOD2,rMVGG]
crossing=[JfmA,dOD2,rMVGG]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_3_0"))
### END