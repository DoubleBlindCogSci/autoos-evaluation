from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bsNGvyMr169=Factor("ELv",["HNLF",Level("chZk0hKWLDK",3)])
p9yUm3qi=Factor("Cg}|LDfzS3[M?",[Level('mlNItWvVzGZtfR',4),'vJj(;v'])
TEYRKKtHZ="jdq"
qkFOjXE=[TEYRKKtHZ,'bqbaUVrN]rM',"IyGgMQV{"]
yj_773ki=Factor('Y{ZN{rwKgeZkW',qkFOjXE)

### EXPERIMENT
design=[bsNGvyMr169,p9yUm3qi,yj_773ki]
crossing=[bsNGvyMr169,p9yUm3qi,yj_773ki]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3_0"))
### END