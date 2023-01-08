from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
s2vI8jH="vjztDnPOVQ"
E37FvSV=["c$UXoo*T#a4Tga",s2vI8jH,Level("Ciloc8EVVuQ",5),"WugJXtjPNS(H|","BqytigifTcHKZ",'FLtKVDyYx!rWP',Level('LSYzJkWhApAUAS',3),'nDh','Nt3foqW<f8',Level("fe@",2)]
lnWSD=Factor('Lsg}xEZvgVMQ1',E37FvSV)
EPC6hUqKMX='%fPqzLOKj'
pHAr=Factor("TQ3TAGfnnpom>W",['pOMWBcXP',"jDYptVHvnXUN",Level('5pgaMDHr',4),'cNNlBC;Mb',"HOE%M8jwLg","omPrKhjCjNSbF","HM[qt3IwiNtJX",EPC6hUqKMX,"dNajDwY#O;Tb(B",'ul0KMA'])

### EXPERIMENT
design=[lnWSD,pHAr]
crossing=[lnWSD,pHAr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/9_2_1"))
### END