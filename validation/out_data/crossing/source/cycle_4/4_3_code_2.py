from sweetpea import *
import os
_dir=os.path.dirname(__file__)
kihdi = Factor("kihdi", ["nxhnr", "xnptz"])
gjt = Factor("gjt", ["ieifi", "yulko"])
jca = Factor("jca", ["unga", "clzmtz"])
bxffc = Factor("bxffc", ["niled", "qay"])
qtugdh = Factor("qtugdh", ["akwzp", "upz"])
cmzeth = Factor("cmzeth", ["ymyw", "hmpupn"])
zkvw = Factor("zkvw", ["rhcwe", "vltz"])
zxqj = Factor("zxqj", ["pmbbw", "njhldl"])
yodtsp = Factor("yodtsp", ["tlvh", "eev"])
npnwew = Factor("npnwew", ["urts", "fuibkx"])
gztai = Factor("gztai", ["trxsc", "loyoo"])
constraints = []
crossing = [[kihdi, gjt, jca], [bxffc, qtugdh, cmzeth, zkvw, zxqj, yodtsp, npnwew, gztai]]


design=[kihdi,gjt,jca,bxffc,qtugdh,cmzeth,zkvw,zxqj,yodtsp,npnwew,gztai]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3"))

### END