# Para importar los datos

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
htru2 = fetch_ucirepo(id=372) 
  
# data (as pandas dataframes) 
X = htru2.data.features 
y = htru2.data.targets 
  
# metadata 
print(htru2.metadata) 
  
# variable information 
print(htru2.variables) 

print(X.head())
print(y.head())
print(X.describe())