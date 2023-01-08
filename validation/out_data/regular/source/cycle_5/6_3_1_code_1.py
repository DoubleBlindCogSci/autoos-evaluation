from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
f4Zws6JrXJ=["<LNtSV",'%ZHAtUoQD',"PrH",'te9nWzStC',"t!m{YqJd","zkWIHDEMn"]
HFb4KO2XOq=Factor(' KRGb]oxJ S%E',f4Zws6JrXJ)
bnGov5Z=['j#n#t',"QjgG_zuF",'vX[OaFdCWV','VEBlp','CSaQe#6CYihBGy']
JRwwyE4uKxz=[bnGov5Z[3],"Or5F1pdvJaT|Sk",'QtUWmc$Np|',"?U6MT","N)rIBZqwjGQ",'SiwZSDH(',"aah3EeA"]
sn0iAJH_2=Factor("Ncvzjt~zwtl",JRwwyE4uKxz)
QGS1=['eSfvQg',Level(" N} bG8IiO",2),Level("9n>",3),"2Y1JFWinNt5","SJjHwS$",'YKhkxIXGNeuzYM']
dLp5J6Bu3M=Factor('%OCBIdJXiSXz',QGS1)

### EXPERIMENT
design=[HFb4KO2XOq,sn0iAJH_2,dLp5J6Bu3M]
crossing=[HFb4KO2XOq,sn0iAJH_2,dLp5J6Bu3M]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_3_1"))
### END