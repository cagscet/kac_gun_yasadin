
from datetime import *
birth = datetime.strptime(input("Doğum tarihiniz giriniz (d.m.y):"),"%d.%m.%Y")
age = datetime.now() - birth

print("Şu kadar gün yaşadın {}".format(age.days))