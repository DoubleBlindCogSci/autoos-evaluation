from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
snqKMoKbnHg="LfMk7F2"
mDgHC=Factor('aW5XF^Ppl',['CtY',"y2HTrxgQOIGf",snqKMoKbnHg,'D&OxumH>',Level("giokp",5),'lwOE',Level("wp)!M",10)])
ORZfTh=["Gpkk)Z1 c"]
Z4g9CUQo2=["_v0K p6SrNn",ORZfTh[0],"FCw","ImRK",'hklgw',"@fJ",Level('>rEEKoL9{Wd',1)]
l_tbBWNhm=Factor('s;^ttxWvCB',Z4g9CUQo2)

### EXPERIMENT
design=[mDgHC,l_tbBWNhm]
crossing=[mDgHC,l_tbBWNhm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_0"))
### END