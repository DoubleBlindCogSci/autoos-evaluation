from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
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
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [kihdi, gjt, jca]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ bxffc, qtugdh, cmzeth, zkvw, zxqj, yodtsp, npnwew, gztai]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
