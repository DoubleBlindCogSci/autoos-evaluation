from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pjmy = Factor("pjmy", ["xvrb", "tjmz"])
lusfem = Factor("lusfem", ["oxvc", "omcx"])
zsta = Factor("zsta", ["lbnkco", "rpk"])
vae = Factor("vae", ["xkpucs", "vxrft"])
dpx = Factor("dpx", ["aina", "izvh"])
rwf = Factor("rwf", ["ktjd", "zhfxox"])
eyik = Factor("eyik", ["lutgng", "oguc"])
tqkcmk = Factor("tqkcmk", ["diwa", "fhnprz"])
uog = Factor("uog", ["ipssyq", "ayzcg"])
deayhu = Factor("deayhu", ["lyrfma", "iagvfk"])
zpa = Factor("zpa", ["qgxok", "dlkmzh"])
ame = Factor("ame", ["flhz", "snx"])
jrbu = Factor("jrbu", ["mkecrz", "tpqsvu"])
dzwu = Factor("dzwu", ["txb", "vsm"])
ymwjh = Factor("ymwjh", ["fubc", "xqljtv"])

### EXPERIMENT
design=[pjmy,lusfem,zsta,vae,dpx,rwf,eyik,tqkcmk,uog,deayhu,zpa,ame,jrbu,dzwu,ymwjh]
crossing = [[jrbu,dzwu,ymwjh],[eyik,tqkcmk,uog],[pjmy,lusfem,zsta],[deayhu,zpa,ame],[vae,dpx,rwf],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2"))
### END
