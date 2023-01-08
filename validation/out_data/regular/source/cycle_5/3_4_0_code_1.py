from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_4_0"))
### END