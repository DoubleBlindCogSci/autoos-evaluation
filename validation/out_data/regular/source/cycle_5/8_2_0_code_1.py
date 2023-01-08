from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
XEcyUp1Rce=['xcjB_uAj0B7x','AbfFYgTAHzYx',Level("udE",1)]
EkQjwzF=['H*mLpzyUtgdRg',XEcyUp1Rce[1],Level('owL',1),"qQ5PYgrQB31","I$Y",'U3p','FJL@wgMrZtT',Level('rm*xPzaYj',2),"lPsN3JsjvALM"]
U2EYjLFj4=Factor("rZggspQ",EkQjwzF)
S1tHeLpiak="HJp2YwhpYk"
oYawM=Factor('jxDBGippuVYiyj',["ikeJYM?mMyl3D",Level('YUK5MWm;OR9Ek',1),"#:AGjVHGKf","EBfb",S1tHeLpiak,"rFp",'HHp43#AiTfv!',"eVBD3Q%6cjs",'Jauc~dJGndi'])

### EXPERIMENT
design=[U2EYjLFj4,oYawM]
crossing=[U2EYjLFj4,oYawM]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_2_0"))
### END