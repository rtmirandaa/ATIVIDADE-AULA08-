from abc import ABC, abstractmethod
from categoria import categoria
from produto import produto
from desktop import desktop
from notebook import notebook


PcRuim = categoria(1, 'Não guenta nada')
PcMédio = categoria(2, 'Não guenta muito')
PcBom = categoria(3, 'Guenta legal')
PCNASA = categoria(4, 'Não se preocupa com nada')


Notebook2010 = produto("Samsung RV511-S02", 1.000, "Cinza", PcMédio )
PcBarbie = produto("Xalingos(Barbie) Computer", 4.000, "Rosa", PcBom)


Notebook2010Bateria = notebook("Samsung RV511-S02", 1.000, "Cinza", PcMédio, "30h")
PcBarbiePotencia = desktop("Xalingos(Barbie) Compiuter", 4.000, "Rosa", PcBom, "7000W")



print(Notebook2010Bateria.__getInformacoes__())
print("""-----------------------------------------------------------------""")
print(PcBarbiePotencia.__getInformacoes__())