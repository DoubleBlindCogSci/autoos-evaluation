from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
axm = Factor("axm", ["couero", "yfyrkr"])
frzyz = Factor("frzyz", ["sbgfa", "xyssqj"])
wmmsy = Factor("wmmsy", ["hrcoly", "fwv"])
mcdtsd = Factor("mcdtsd", ["riexm", "ytuwcr"])
prfwwr = Factor("prfwwr", ["zkw", "bfi"])
mlnqg = Factor("mlnqg", ["gtv", "neslzn"])
ejgvc = Factor("ejgvc", ["wkxi", "fbihqw"])
ouefco = Factor("ouefco", ["limde", "caim"])
vhcey = Factor("vhcey", ["spwoe", "xjnw"])
constraints = []
crossing = [[axm, frzyz], [wmmsy, mcdtsd, prfwwr, mlnqg], [ejgvc, ouefco, vhcey]]


design=[axm,frzyz,wmmsy,mcdtsd,prfwwr,mlnqg,ejgvc,ouefco,vhcey]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_0_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_0_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [axm, frzyz]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ wmmsy, mcdtsd, prfwwr, mlnqg]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ ejgvc, ouefco, vhcey]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
