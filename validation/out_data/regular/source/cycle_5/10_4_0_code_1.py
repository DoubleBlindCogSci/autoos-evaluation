from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
TkiHuKlPG6=Factor(']ulhEIFPmeJSJ',[Level('Dwpo',3),'7n0ydtuaiU_t(',"AFBQ{KYt]fr",Level('kXk|wYLB5u2',2),'WuegvJYYn9qv','iRHYrymSM',"8K1yRQ^RE",'Tsr',"GDe52DggggTKB","reOS]reif"])
KjFx9Lq3l=Factor('VJLkA}',['WGJHzqlek',"|DYDBrO^ffLh","yGe#erym","swix33","Blwe:sUNz^gsrr","vSDdLAZb",Level('FYp{hvfY?qa',4),'jQuH','@IxWFlz>D^jm9T',"gvjD"])
szf2LfsDntB=Factor('ghFYiRoNS',["cMLo2i",'RrrRufq6syg3E',"}YPvGjLBhCC5gB",'VARXTTx','8:V','CrHT|KdTRDL','Ajjj 8Jtl',"xRKUH>UdNjnpV","hlZs","5njxHRsA6k"])
XQFytBayt='y;JA'
fYXymiDb="Bxg"
tvME45cf=[Level("_Uj",3),'gXOxQuK',"JqLBkFqmb1e"]
UiKx4BTmFj=["~bxvduQ|",XQFytBayt,'WjIwj%U',"f@%WtkW","OtjyBLn&SWdC",'ooxmiQdV5A','hyhIBh)rE',Level("UhOzDdN",1),"&G!r[?nTdCbcIt",tvME45cf[2],Level('wdvQPk7i',4),fYXymiDb,'yCV@bfYbI']
X9ido=Factor("[b6XDFe}}:m",UiKx4BTmFj)

### EXPERIMENT
design=[TkiHuKlPG6,KjFx9Lq3l,szf2LfsDntB,X9ido]
crossing=[TkiHuKlPG6,KjFx9Lq3l,szf2LfsDntB,X9ido]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/10_4_0"))
### END