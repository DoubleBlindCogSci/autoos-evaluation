from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pkb = Factor("pkb", ["jpmi", "ubt"])
zgn = Factor("zgn", ["dhekd", "nzep"])
frmuqy = Factor("frmuqy", ["xpxi", "uoqpv"])
ykfn = Factor("ykfn", ["pow", "ribpv"])
gxj = Factor("gxj", ["wzpgst", "yfr"])
qdsoe = Factor("qdsoe", ["vucd", "yrkpxf"])
pdh = Factor("pdh", ["dkmj", "sruuto"])
iiclld = Factor("iiclld", ["ghdr", "cxa"])
aeet = Factor("aeet", ["akf", "qeb"])
ybii = Factor("ybii", ["zrint", "prxho"])
czhfw = Factor("czhfw", ["lmxd", "dzr"])
mca = Factor("mca", ["emg", "udtnj"])

### EXPERIMENT
design=[pkb,zgn,frmuqy,ykfn,gxj,qdsoe,pdh,iiclld,aeet,ybii,czhfw,mca]
crossing=[[pkb,zgn,frmuqy],[ykfn,gxj,qdsoe,pdh],[iiclld,aeet,ybii,czhfw],[mca],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_3"))
### END