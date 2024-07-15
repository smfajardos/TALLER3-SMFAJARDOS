from models.perro import Perro
from models.boaConstructor import BoaConstructor
from models.huron import Huron


boa1 = BoaConstructor("La boa más grande del mundo", 1, 9, "Colombia", 9)
boa1.comer_ratones(2)
boa1.comer_ratones(3)

try:
    for _ in range(11):
        boa1.comer_ratones(range)
        print(f"Los ratones comidos son: {boa1.ratones}")
except ValueError as e:
    print(e)


el_huron = Huron("Huronsin", 5, 3, "Francia", 5)
print('El huron "{0}" hace {1}'.format(el_huron.get_nombre(), el_huron.hacer_sonido()))
print("El huron tiene costo de importación de: $ {0}".format(el_huron.calcular_flete()))
