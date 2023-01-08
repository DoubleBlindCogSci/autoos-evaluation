from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
vtj = Factor("vtj", ["djrzp", "giar"])
fgqdx = Factor("fgqdx", ["qdwora", "ajipzj"])
mnj = Factor("mnj", ["aiskjo", "qwybt"])
ewol = Factor("ewol", ["sawqek", "goxbv"])
qqdjf = Factor("qqdjf", ["rfkoeh", "brmsf"])
rwg = Factor("rwg", ["gae", "xowm"])
tiug = Factor("tiug", ["rqjbp", "exn"])
fql = Factor("fql", ["ltupt", "oxkq"])
constraints = []
crossing = [[vtj, fgqdx, mnj], [ewol], [qqdjf, rwg, tiug, fql]]


design=[vtj,fgqdx,mnj,ewol,qqdjf,rwg,tiug,fql]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_0_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_0_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [vtj, fgqdx, mnj]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ ewol]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ qqdjf, rwg, tiug, fql]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
