from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zGcjWOQc=Factor('ijDRyQgxkUTaL',['TlK(U',Level('ILnBfN',4),'YlGhk{rRndt',"m#zU4$yXzyY","xP(Kgw",'nlSTn2ltc^dA'])
BYo7gq=['BYHad',Level("eZErkqwuL!YuN",5),"CKoQWoaOG%o",'aDZ?kDGeN',Level("rm%JLscdRtCRnE",8),'dhOovPDTq3F&Ow',"T5jo*O","glXVl"]
MPeJiH0zPb=Factor("fCdWJg[agY4t",['X^y',"SsGnoU",Level('HuylBEsNI',3),BYo7gq[3],'4rK','Rs5HmgAl%1ze','sZlUeBAUd4B'])
bXFbI9ooI=Factor("bby<IGB",["VuhAlkZJuMGo",Level("M_vZsRG",2),"XTyslcxc4;DvGU",'sG*iqB',Level('dni{DyCPDp',2),'GnXo'])

### EXPERIMENT
design=[zGcjWOQc,MPeJiH0zPb,bXFbI9ooI]
crossing=[zGcjWOQc,MPeJiH0zPb,bXFbI9ooI]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_3_0"))
### END