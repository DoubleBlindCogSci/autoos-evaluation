from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
gqjsay = Factor("gqjsay", ["kgay", "vuabd"])
ylp = Factor("ylp", ["ioatiu", "imsulx"])
gmyjy = Factor("gmyjy", ["bhc", "dcz"])
wjs = Factor("wjs", ["hbi", "bhjvs"])
waezh = Factor("waezh", ["uqc", "wtz"])
aix = Factor("aix", ["cncejk", "baj"])
egmwc = Factor("egmwc", ["ifen", "vwufe"])
jmj = Factor("jmj", ["kverk", "ebnt"])
constraints = []
crossing = [[gqjsay, ylp, gmyjy], [wjs, waezh, aix, egmwc], [jmj]]


design=[gqjsay,ylp,gmyjy,wjs,waezh,aix,egmwc,jmj]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [gqjsay, ylp, gmyjy]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ wjs, waezh, aix, egmwc]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ jmj]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
