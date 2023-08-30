print('Enter life expectancy')
LIFE = float(input())
print('Enter the age at which HIV infection occurred')
INV = float(input())
print('Enter the age at which antiretroviral therapy started')
MED = float(input())
print('Enter the severity of the disease without therapy')
WEIGHT1 = float(input())
print('Enter the severity of the disease with therapy')
WEIGHT2 = float(input())
print('Enter the age at which death occurred')
DEATH = float(input())
YLD = (DEATH - MED) * WEIGHT2 + (MED - INV) * WEIGHT1
YLL = LIFE - DEATH
DALY=YLD+YLL
print('DALY LOST=', DALY)
