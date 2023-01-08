from sweetpea import *
import os
_dir=os.path.dirname(__file__)
axpru = Factor("axpru", ["hytm", "qaqhoc"])
heunm = Factor("heunm", ["pvhedb", "yfwoj"])
rvgyt = Factor("rvgyt", ["jjgzie", "drt"])
ojm = Factor("ojm", ["dvn", "uvwkmq"])
izo = Factor("izo", ["tkvhau", "qdmijn"])
bygfzv = Factor("bygfzv", ["ayw", "ldee"])
qbh = Factor("qbh", ["bsz", "rprng"])
vdwawv = Factor("vdwawv", ["fqpnf", "ghnb"])
constraints = []
crossing = [[ qbh, vdwawv],[ izo, bygfzv],[ rvgyt],[ heunm],[axpru],[ ojm],]


design=[axpru,heunm,rvgyt,ojm,izo,bygfzv,qbh,vdwawv]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1"))

### END
