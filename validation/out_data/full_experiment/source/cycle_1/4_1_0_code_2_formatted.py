### REGULAR FACTORS
vsjz = Factor("vsjz", ["sjui", "ikecv"])
jko = Factor("jko", ["bqht", "weiurp"])
smcarz = Factor("smcarz", ["sjui", "ikecv"])
khud = Factor("khud", ["bqht", "weiurp"])
### DERIVED FACTORS
##
def is_zwizsh_inny(khud, vsjz):
    return khud == vsjz
def is_zwizsh_foini(khud, vsjz):
    return not is_zwizsh_inny(khud, vsjz)
zwizsh = Factor("zwizsh", [DerivedLevel("inny", WithinTrial(is_zwizsh_inny, [khud, vsjz])), DerivedLevel("foini", WithinTrial(is_zwizsh_foini, [khud, vsjz]))])
### EXPERIMENT
constraints = []
crossing = [smcarz, khud]
design=[vsjz,jko,smcarz,khud,zwizsh]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
