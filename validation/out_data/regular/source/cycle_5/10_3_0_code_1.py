from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
snJs=["CEr&MYm;w","lQDXedepUvtNYe","iZfcweVmzfJBD","t2Gp!D<BjD7",'jt oKS%{*r','fkonJv}maf',Level("KGyg7v>F|V7",2),']Rned_vWIREyO','KDlzs(xd',Level(";OzDHfctOLpB",1)]
dbTCwL=Factor('qwe$sGXLVNkO',snJs)
n03yMq='iJt'
M9RVZCyZ3JI=Factor('EUIVoenxqKf',["E:(xzKGu","otC","tpfjp",'jWZxl','LAAVATb(aJdr',Level("QkPPBR GuIO",4),'pzLh',Level('UJlCX',2),"mRGAIScwbKJUzr",n03yMq,'6Wd geXo vRDo'])
cDOU4=['eCE94WL',':hr$yBs$kOV','l9ZlGR',"wJ!hYfMXal","UGLXul5WYxA","ijrWb"]
YzWjI9t=Factor('sqaCFyLKi',['Jdh?SGCxAyOeoL',cDOU4[2],"YEIHwon$b",'ygK:&PMOKz',"XkJTfBHIcu",'t#TfI',"fVRly",'aRub)',"s jCRt:tEvJ$Y",Level('mz0tXRa',1),'?vJC[SH'])

### EXPERIMENT
design=[dbTCwL,M9RVZCyZ3JI,YzWjI9t]
crossing=[dbTCwL,M9RVZCyZ3JI,YzWjI9t]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/10_3_0"))
### END