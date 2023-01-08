from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
cqtrgj = Factor("cqtrgj", ["geno", "aioxn"])
vwd = Factor("vwd", ["potv", "cmshe"])
vzlh = Factor("vzlh", ["nbgvdl", "xqoza"])
jkyxw = Factor("jkyxw", ["deyngt", "qyk"])
isq = Factor("isq", ["ewu", "pjlyt"])
ffroz = Factor("ffroz", ["zppp", "pfi"])
sgm = Factor("sgm", ["tboo", "zpi"])
rosl = Factor("rosl", ["dgqoia", "oms"])
constraints = []
crossing = [[cqtrgj, vwd, vzlh, jkyxw], [isq, ffroz, sgm], [rosl]]


design=[cqtrgj,vwd,vzlh,jkyxw,isq,ffroz,sgm,rosl]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_1_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_1_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [cqtrgj, vwd, vzlh, jkyxw]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ isq, ffroz, sgm]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ rosl]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
