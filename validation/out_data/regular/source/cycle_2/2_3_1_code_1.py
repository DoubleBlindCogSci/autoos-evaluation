from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xmPXCagiE=Factor("kPX",["RIXHSCRm]&w9",'BAv@xW'])
AvV0v1G_x=Factor("Sg_",["zA7UZgVJKR","wrMNGFRkex"])
jBZuftztcvq=Factor('Wd68D',['AxgIH','aiFdCWzYlwNNK'])

### EXPERIMENT
design=[xmPXCagiE,AvV0v1G_x,jBZuftztcvq]
crossing=[xmPXCagiE,AvV0v1G_x,jBZuftztcvq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3_1"))
### END