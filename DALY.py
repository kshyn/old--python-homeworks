print('Введите ожидаемую продолжительность жизни')
LIFE = float(input())
print('Введите возраст, в котором произошло заражение ВИЧ')
INV = float(input())
print('Введите возраст, в котором началась антиретровирусная терапия')
MED = float(input())
print('Введите тяжесть недуга без терапии')
WEIGHT1 = float(input())
print('Введите тяжесть недуга с терапией')
WEIGHT2 = float(input())
print('Введите возраст, в котором произошла смерть')
DEATH = float(input())
YLD = (DEATH - MED) * WEIGHT2 + (MED - INV) * WEIGHT1
YLL = LIFE - DEATH
DALY = YLD + YLL
print('DALY LOST=', DALY)
