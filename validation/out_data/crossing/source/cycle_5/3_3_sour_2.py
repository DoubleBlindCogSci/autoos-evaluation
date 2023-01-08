from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
gskuwm = Factor("gskuwm", ["qjoic", "ipvoln"])
ebmpb = Factor("ebmpb", ["bmb", "mlcydz"])
tnvcy = Factor("tnvcy", ["gvjh", "mqvfml"])
tdma = Factor("tdma", ["rhqfa", "qvrmrq"])
trwhbk = Factor("trwhbk", ["gltdhi", "gnu"])
dlzigb = Factor("dlzigb", ["vfxl", "chkyme"])
lpsmn = Factor("lpsmn", ["wbxok", "rawim"])
nucsu = Factor("nucsu", ["drktpc", "humuzy"])
constraints = []
crossing = [[gskuwm, ebmpb], [tnvcy, tdma, trwhbk, dlzigb], [lpsmn, nucsu]]


design=[gskuwm,ebmpb,tnvcy,tdma,trwhbk,dlzigb,lpsmn,nucsu]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [gskuwm, ebmpb]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ tnvcy, tdma, trwhbk, dlzigb]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ lpsmn, nucsu]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
