from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wnt4p="fTGxLOrXBBhg"
zq_E='Tg}J#Tu'
RVG66926=["ThvR >Zq*moZI"," bsoVKrY?vCP",'pTTS_Cm!|fF',Level("X[fYi5Y",4),'bLQNt','jZCE|M',"lhKZ2"]
pTNrGeQ=Factor('vlaGqWn9o',["QExdHPz",'PxuyEyg',RVG66926[2],zq_E,wnt4p,'AJGXdOyf@ZT','gjQsiXe}npsSB',":kwFkKaYA#^j",Level("]mSaanhOy?GJg",3)])
O6up8C="2QD}PUXxzDy)"
B9W6NPnuQ=["9KwN(~[a T~mM",O6up8C,'AR?UqJjF$A1mT8','2qG(I',"zcyOnK","Gczy","LfhTXQrFnc"]
hJR4xY=Factor("XnN}xX|NLRvh",B9W6NPnuQ)

### EXPERIMENT
design=[pTNrGeQ,hJR4xY]
crossing=[pTNrGeQ,hJR4xY]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_1"))
### END