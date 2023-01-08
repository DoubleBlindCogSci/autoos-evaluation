from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
r1cT3mPbw=Factor("TpSyH",["qvv","~uZzSl",Level('~UX>Akw NFk',7),Level('ZXObQhL',4),"PXCmymqM<",Level('UpGGxXu% ',10),'pDBXfz','VyYSVwPgFac x_'])
_TBsM46xr=Level('cJnhg@jVoPlAO9',9)
fQAPXL8wRZ=['GuRaQE','iByNS',"5Wrmnt"]
Be07=["Sv?Q",Level("Y0lQ j#aT",4),Level('z^jVnIZC6k',7),"1i[c3IC",_TBsM46xr,"6eyaLcBL:vy@d|",'Hzd@WSISDdt2x',"@wjzxGHMxkh5",fQAPXL8wRZ[1],'NjQ)']
aRQrvO2UB=Factor("hoVgtgpKmVWe",Be07)
_FC1=[Level('Rsxk',3),Level("cdaQVimM",7),Level("GvMk",9),';sF0',"gvTmz_C0ByQAK","Zi;2rF@R",'g]nkKj','o;rGrZT8d']
zoEXXn=Factor('t$hSsEQ]nDHGxg',_FC1)

### EXPERIMENT
design=[r1cT3mPbw,aRQrvO2UB,zoEXXn]
crossing=[r1cT3mPbw,aRQrvO2UB,zoEXXn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_3_0"))
### END