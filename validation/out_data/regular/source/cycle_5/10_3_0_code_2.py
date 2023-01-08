from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qwe_sGXLVNkO = Factor("qwe$sGXLVNkO", ["CEr&MYm;w", "lQDXedepUvtNYe", "iZfcweVmzfJBD", "t2Gp!D<BjD7", "jt oKS%{*r", "fkonJv}maf", "KGyg7v>F|V7", "]Rned_vWIREyO", "KDlzs(xd", Level(";OzDHfctOLpB", 2)])
EUIVoenxqKf = Factor("EUIVoenxqKf", ["E:(xzKGu", "otC", "tpfjp", "jWZxl", "LAAVATb(aJdr", "QkPPBR GuIO", "pzLh", "UJlCX", "mRGAIScwbKJUzr", "iJt", Level("6Wd geXo vRDo", 4)])
sqaCFyLKi = Factor("sqaCFyLKi", ["Jdh?SGCxAyOeoL", "l9ZlGR", "YEIHwon$b", "ygK:&PMOKz", "XkJTfBHIcu", "t#TfI", "fVRly", "aRub)", "s jCRt:tEvJ$Y", "mz0tXRa", "?vJC[SH", Level(";OzDHfctOLpB", 1)])

design=[qwe_sGXLVNkO,EUIVoenxqKf,sqaCFyLKi]
crossing=[qwe_sGXLVNkO,EUIVoenxqKf,sqaCFyLKi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/10_3_0"))

### END
