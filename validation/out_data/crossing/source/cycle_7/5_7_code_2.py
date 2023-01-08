from sweetpea import *
import os
_dir=os.path.dirname(__file__)
wzsmu = Factor("wzsmu", ["cgyna", "matmhh"])
wvq = Factor("wvq", ["sfj", "cpeje"])
noiouk = Factor("noiouk", ["xxmu", "tfsf"])
fpzxgt = Factor("fpzxgt", ["dnz", "ieacgq"])
biy = Factor("biy", ["nggrd", "hjwmh"])
constraints = []
crossing = [wzsmu, wvq, noiouk, fpzxgt, biy]


design=[wzsmu,wvq,noiouk,fpzxgt,biy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_7"))

### END