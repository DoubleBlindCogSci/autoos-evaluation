from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eyA9cesK=Factor('yoaFxqvtb',["k8NeS",'xYTLCkuFMA(x',Level("WaPjr",1),"5ELMv^ujl^XfnQ",'mast_Q','xpAigKIpHcu'])
ESh4DLp=Factor("4ctPvTkxcwR@}Y",["L ggETb$r","XoX","iT07x",Level('n?hZi',3),Level('qfDj',1),'<jilf'])
qjVvlAWL=Factor('nvfwNpK_OB',['ZhHc|Oj%PhJxBW',"jr!MvOg",'cYGIHs',"m?X~BKgzYe",'AdzrNrKDD?5',"5W4SA"])
u6z_LnDaAH='r&sZ'
rruuo4=Factor("OA[aBte4c",['hLpIlIUs!ICYP',Level('aBrUguFn',3),'{iub',";PFkI#n2","YjP[CZyBpV4sX",'|f?',u6z_LnDaAH])

### EXPERIMENT
design=[eyA9cesK,ESh4DLp,qjVvlAWL,rruuo4]
crossing=[eyA9cesK,ESh4DLp,qjVvlAWL,rruuo4]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_4_1"))
### END