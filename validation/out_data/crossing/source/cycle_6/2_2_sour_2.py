from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
ymg = Factor("ymg", ["ukf", "yydyig"])
ipyed = Factor("ipyed", ["zeylg", "pywjvq"])
ttc = Factor("ttc", ["tjg", "oih"])
tirl = Factor("tirl", ["bwxhf", "qodosl"])
mhvvxa = Factor("mhvvxa", ["sdyc", "twesgh"])
zqvzs = Factor("zqvzs", ["ime", "gtvapc"])
lys = Factor("lys", ["fab", "qlel"])
constraints = []
crossing = [[ tirl, mhvvxa, zqvzs, lys],[ymg, ipyed, ttc],]


design=[ymg,ipyed,ttc,tirl,mhvvxa,zqvzs,lys]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/2_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/2_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [ tirl, mhvvxa, zqvzs, lys]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ymg, ipyed, ttc]
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
