from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
viNOzS=Factor('jyMJFmejL^$riP',[Level('dJI%LKQM2b',8),"6nNM9JzBH",'4lvw9vkCXAd','b5v#{rQmbVl',Level("dnVGG$jGosiw",4),"CsLiKY","X3]Xg%Ybv(SS","sJEXiFaDEPF2tI",Level("uinKOa?R4NQ^p;",5)])
N7prew=["vaoA",Level("aZ!YBxSO",5),'{AVQE','LBYK_mIvsATdRY',"kDlxS_}VgRTK"]
b7YHa6W=Level("cmSrfDovTtUU",10)
AAKNpTg=Factor('b;xatqivt',['pC4]5quBFbYx#',"rRgLFs_b","Y&IqDNTxiZ",Level('ENeYshy',1),"CDwDwCV","FJ{H8",Level("MYmNwuFq",3),N7prew[3],b7YHa6W,'d:UQ','ghbnXlPeFaKhGL'])

### EXPERIMENT
design=[viNOzS,AAKNpTg]
crossing=[viNOzS,AAKNpTg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_2_0"))
### END