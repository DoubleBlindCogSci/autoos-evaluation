from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
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
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_2_0_0.csv"))
nr_factors=2
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)