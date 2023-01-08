from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
vkq = Factor("vkq", ["fyiqva", "fyhezn"])
drg = Factor("drg", ["fdb", "ehn"])
fqjdvj = Factor("fqjdvj", ["sqcmmj", "lno"])
uej = Factor("uej", ["iks", "skb"])
lhbo = Factor("lhbo", ["oeqbie", "kabzup"])
tryat = Factor("tryat", ["zvlu", "wgs"])
dwqc = Factor("dwqc", ["gskzu", "traua"])
yxl = Factor("yxl", ["irk", "gzm"])
constraints = []
crossing = [[vkq, drg], [fqjdvj, uej, lhbo], [tryat, dwqc], [yxl]]


design=[vkq,drg,fqjdvj,uej,lhbo,tryat,dwqc,yxl]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [vkq, drg]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ fqjdvj, uej, lhbo]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ tryat, dwqc]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ yxl]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
