from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DvscD=['XuHVRnZAkHn','E3M@8Em',Level("sIv",2)]
kwe4JYBw9=Factor('l>HDHBWxR',[Level("Ls(t",3),"sTUiO3eXcy^I","at*(bs9jDinb",DvscD[0],'WTayEPxExi^',Level('Nnrp!n&dQJ',8),"qUwDOPNIMCJ",Level(' XmHk1',9)])
NA_2EBrpDHO='OvVrLC'
uympBb5=[Level("14KKMYqM",8),Level('afw',8),Level("jcQiT",10),"vRe",NA_2EBrpDHO,"Ka Le",'vgwJ','%zQxUl}YWtoB']
FqPNOl=Factor('uBKrQeGEhYKrb',uympBb5)
l2b90wr=Factor('NcIdaI',["TtS9fTWcz>I",'bJbuVL',Level('CxIbZLCmEiy',8),'V uDd^vq',"G_yvV)5",Level('}LI^jmZ:!}s',4),'u&gvyt'])

### EXPERIMENT
design=[kwe4JYBw9,FqPNOl,l2b90wr]
crossing=[kwe4JYBw9,FqPNOl,l2b90wr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/7_3_0"))
### END