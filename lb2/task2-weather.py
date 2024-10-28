import statistics as s
degrees = list(map(int, input("Введите градусы за неделю: ").split()))
minDegrees = min(degrees)
maxDegrees = max(degrees)
meanDegrees= s.mean(degrees)
print("Min degrees =", minDegrees)
print("Max degrees =", maxDegrees)
if meanDegrees < 0:
    print("Запасайтесь зимней одеждой")
elif (meanDegrees>=0) and (meanDegrees <10):
    print("Запасайтесь осенней одеждой")
elif (meanDegrees>=10) and (meanDegrees<20):
    print("Запасайтесь весенней одеждой")
elif meanDegrees>=20:
    print("Запасайтесь летней одеждой")
