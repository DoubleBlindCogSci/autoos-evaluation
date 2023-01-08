from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
VYs0a=["tDgc9xpc","rvzmS[Jv|Vy","PGknaVxdd8[5Uh"]
Gsx9ieNYIB=Factor(';rtrQ>iw>u',VYs0a)
M4FXKVxuR=Factor("GCUYG&hEUH YrG",['GQfW]zaOBZxt<',"%Czk5AB",'x6dYnGqey'])
iOdYWc27Wfn=[">lBtL]RileJQ",Level("TtfTZdjXV",4),"JhdVsilJY6z_>{"]
chkuljb=Factor('cgWmLYt',iOdYWc27Wfn)
eFwuB7X6N1=["8VWxl",Level(' qXSKod',4),'QsQ>tkyjkOWvz','rXwy<>@']
_BzrFG=Factor('7EaNu<ZUnHvsm',["GJxFuqBNHktMYr",'JK^D)wKGMvm%bV',eFwuB7X6N1[0],"TqwZp"])

### EXPERIMENT
design=[Gsx9ieNYIB,M4FXKVxuR,chkuljb,_BzrFG]
crossing=[Gsx9ieNYIB,M4FXKVxuR,chkuljb,_BzrFG]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_4_0_0.csv"))
nr_factors=4
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_4_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)