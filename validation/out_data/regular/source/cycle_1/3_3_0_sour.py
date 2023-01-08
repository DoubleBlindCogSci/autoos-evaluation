from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nvfINal2bE=Factor("IIAvEBEBnZqhA",["yNQKZrsUXCMb4h",'<MS9A',"bu5}iwBG)mu"])
lTwRq8wYj=[Level("HK4LftZdK",1),'@BZZomKQ','CDAjJy|veKYfMF']
cRHB=Factor('dCU%3hdNP>W?#x',lTwRq8wYj)
XZ9VWQnu=Factor("oeAtWT",[Level("ntz",10),Level('Ptbb',8),Level("8Ml",8)])

### EXPERIMENT
design=[nvfINal2bE,cRHB,XZ9VWQnu]
crossing=[nvfINal2bE,cRHB,XZ9VWQnu]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/3_3_0_0.csv"))
nr_factors=3
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/3_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)