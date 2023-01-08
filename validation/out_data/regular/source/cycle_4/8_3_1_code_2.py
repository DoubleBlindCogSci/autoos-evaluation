from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ina_z = Factor("ina!z", ["MgiwJtHl16WH y", "CtN", "ZVX5ijZl", "Ck]}Lx%", "JqBc", "MwUVB_KmleA", "YWLYkELPQ", "UDTBv", "ljfsd", "PY6onUGzvvwa1"])
VNq_bN = Factor("VNq6bN", ["oVz(n2K", "XtqayL", "wVenwPv7X", "zsckkezrOxyZ", "E}X4nI", "nnHxEuVTcFyBJ", "K#wBYpO[", ">OEUYMCauvi"])
LqJaK = Factor("LqJaK", ["$|WaBb", "NOQJ", "hGWzmbCiCbiiCB", "OE0&JVkrJ", "KGQTvUU^g~m", "HNM8", "ETy?", "!h5qxOb)JHp", "IISWoRM"])

design=[ina_z,VNq_bN,LqJaK]
crossing=[ina_z,VNq_bN,LqJaK]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_3_1"))

### END
