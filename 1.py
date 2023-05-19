#1st question
class Circle:
  def __init__(self,radius):
    self.radius = radius
  def getArea(self):
    print("The area of circle is :",3.14*self.radius*self.radius)
  def getCircumference(self):
    print("The circumference of circle is :",2*3.14*self.radius)
radius = int(input("Enter the radius :"))
r = Circle(radius)
r.getArea()
r.getCircumference()

#2nd question
class Temperature:
  def __init__(self,temperature):
    self.temperature = temperature
  def Celcius(self):
    print("The temperature in farenheit:",((self.temperature*(9/5))+32))
  def Farenheit(self):
    print("The temperature in celcius:",((self.temperature-32)*(5/9)))
t = input("Enter the units of temperature :")
if t=="C":
  temp = int(input())
  t1=Temperature(temp)
  t1.Celcius()
else:
  temp = int(input())
  t1=Temperature(temp)
  t1.Farenheit()

#4th question
class Time:
  def __init__(self,hours,minutes):
    self.hours=hours
    self.minutes=minutes
  def displayTime(self):
    return str(self.hours)+"hr" +" "+str(self.minutes)+"mins"
  def displayMinute(self):
    return self.hours*60 + self.minutes
r1=Time(1,2)
r2=Time(2,3)
r1.displayTime()
r1.displayMinute()

#5th question
# from google.colab import files
# data = files.upload()
import pandas as pd
import scipy.stats as stats

data = pd.read_excel('employees.xls')
print(data)
data.fillna(0,inplace=True)
# print(data)
# print(data.head())
salaries = data['SALARY']
sal = list(salaries)
#zscore
z_score = stats.zscore(sal)
print(z_score)
# min-max normalization
maximum = max(sal)
minimum = min(sal)
print(sal,minimum)
min_max_n = []
a=1
b=10
for i in sal:
  c = ((i-minimum)/(maximum-minimum))*(b-a)
  min_max_n.append(c)
print(min_max_n)
#decimal normalization
dec_n=[]
x = len(str(maximum))
for i in sal:
  dec_n.append(i/(10**x))
print(*dec_n)
