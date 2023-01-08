from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nsJXW99ZIla=Factor("RiIw7ZGdxgzqi",['oUIZXF4S',Level("dkpm[",3),'uFvTVnb','tDgoKwQvv','KzozGI7x0#oc!u',Level('YbErnP',2),"R;Dt"])
KDngQH_2ZzN=["&$t2ptrwUaj",'~Nh acC',Level('sFmAipnn',3)]
FzQAV=['VFlRZUFhYdA']
Ln_8ZZRdx9=Factor("Im$~JagACs4$Z",[Level('nDGt%',4),'iBtWtz8F',"HpVeN?QcZdg;RS",Level('XCC',1),"qC]PhLDmg2l",KDngQH_2ZzN[2],'vfg%lVGtz &Taw',FzQAV[0],'Qdu'])
gBz34HC8b=['aP9rYcn',"yCyrhJKVG",Level("pfnl;SC6",3),"nrE^5L{G",'DDvK^']
uEQy7=Factor('8Gl%FcSwL',["IcP","rrs",'ymaaeSXZltSlT',"Guct&f_wiqcYr"," yPkbXMIZh",'IChBrBMr^a',gBz34HC8b[2],Level("DpN&ZQGRp",1)])

### EXPERIMENT
design=[nsJXW99ZIla,Ln_8ZZRdx9,uEQy7]
crossing=[nsJXW99ZIla,Ln_8ZZRdx9,uEQy7]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_3_0"))
### END