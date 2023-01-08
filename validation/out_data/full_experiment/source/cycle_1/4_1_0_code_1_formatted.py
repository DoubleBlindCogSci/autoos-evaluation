### REGULAR FACTORS
vsjz = Factor("vsjz", ["sjui", "ikecv"])
jko = Factor("jko", ["bqht", "weiurp"])
smcarz = Factor("smcarz", ["sjui", "ikecv"])
khud = Factor("khud", ["bqht", "weiurp"])
### DERIVED FACTORS
##
def wdoday (khud, vsjz):
    return khud == vsjz
def xcf (khud, vsjz):
    return not wdoday(khud, vsjz)
zwizsh = Factor("zwizsh", [DerivedLevel("inny", WithinTrial(wdoday, [khud, vsjz])), DerivedLevel("foini", WithinTrial(xcf, [khud, vsjz]))])
### EXPERIMENT
design=[zwizsh,vsjz,jko,smcarz,khud]
constraints=[]
crossing=[smcarz,khud]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
