from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HfE5TQG=['eUXQY~UfK|hbdd',"vlaptPlbBJs6"," hk0?xV",'ymMw2JDzWDpRQm',"JqvgY}yQ1aF",'oxnvLAIdAey',Level("tLGjZGyva",2),"tfhpM{TBq"]
IHMB=['9O_rvODulBv3If',"IHVDXja","ZWZpJyrFha9O","@YwzMm5d"]
tIfy2ZKd9D1=Factor("xeT8sUVeZ",['x0jozyEr',"N ?x[i AC","C}eWW%UuhVy",HfE5TQG[4],Level("eHV",2),'J~odOQmitm','dzIh]EyV:ls1nI','H0CpB',IHMB[1],"oAt[QoOzW xm",'BJKUev4xH'])
aFtTJhbEl87=Factor("hF]y:l",["QzWHb<dLIKacrh",'woC%sL','kQQDyLn{o','s>2',"UK1q?",'cqZ8L}SZVT_O','eN51vNrQQ','zGT<yFyyNZ','AypcOqde'])

### EXPERIMENT
design=[tIfy2ZKd9D1,aFtTJhbEl87]
crossing=[tIfy2ZKd9D1,aFtTJhbEl87]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_2_0"))
### END