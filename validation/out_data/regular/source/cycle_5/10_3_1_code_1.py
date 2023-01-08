from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
XHpFT0A2MT=['HuoDoP','xycJC5prIolyM',Level('DgaOIZ#IBbQg',3),"DAZuX",'eNI','JvGsraTvrPVEa7']
d_PQ_lpk7wn=["QrTKMJ",XHpFT0A2MT[4],"7]GrzT",'OWSXCwiRxMpvK',"UHc",'HsOSlX',"vM^w#uO]Z",'gXP','FrvfyWS','sD^QgJpQXYSIVO','F*^zIIoP*']
HDRp7jrSvt=Factor("zfe_zhLScy",d_PQ_lpk7wn)
Ewm_Ankv="d2NMsnbFW:CPE"
eY2g=["UKxVXAAf[}f",'gfzf',"}XA",'OCnK)Xb','cXf2LrxWIx#L:4','IEi&AlOC*GC','2cK0xXT',Ewm_Ankv,"oqceZM{kA",Level('Q3NhDI8]k',2),"XUmQ"]
Yr8e=Factor('Ub{Ej',eY2g)
OJPIPAu=['%ahUE$kel',"f*f",'q(exG','Wdiut~b]nOAa',"IgF*h4Qu","4lSP_gqklv~j","u$Kkvue9",Level("gDyIGFpolz",4),'$T!SYP',"ejnWq?"]
SArOsIpJ=Factor('Yi[[hWsP',OJPIPAu)

### EXPERIMENT
design=[HDRp7jrSvt,Yr8e,SArOsIpJ]
crossing=[HDRp7jrSvt,Yr8e,SArOsIpJ]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/10_3_1"))
### END