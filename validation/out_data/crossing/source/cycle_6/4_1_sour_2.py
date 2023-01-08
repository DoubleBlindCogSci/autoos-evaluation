from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
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
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [ qbh, vdwawv]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ izo, bygfzv]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ rvgyt]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ heunm]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [axpru]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ ojm]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = []
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
