from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Lsg_xEZvgVMQ_= Factor("Lsg}xEZvgVMQ1", [Level("c$UXoo*T#a4Tga", 1), Level("vjztDnPOVQ", 1), Level("Ciloc8EVVuQ", 5), Level("WugJXtjPNS(H|", 1), Level("BqytigifTcHKZ", 1), Level("FLtKVDyYx!rWP", 1), Level("LSYzJkWhApAUAS", 3), Level("nDh", 1), Level("Nt3foqW<f8", 1), Level("fe@", 2)])
TQ_TAGfnnpom_W= Factor("TQ3TAGfnnpom>W", [Level("pOMWBcXP", 1), Level("jDYptVHvnXUN", 1), Level("5pgaMDHr", 4), Level("cNNlBC;Mb", 1), Level("HOE%M8jwLg", 1), Level("omPrKhjCjNSbF", 1), Level("HM[qt3IwiNtJX", 1), Level("%fPqzLOKj", 1), Level("dNajDwY#O;Tb(B", 1), Level("ul0KMA", 1)])

design=[Lsg_xEZvgVMQ_,TQ_TAGfnnpom_W]
crossing=[Lsg_xEZvgVMQ_,TQ_TAGfnnpom_W]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/9_2_1"))

### END
