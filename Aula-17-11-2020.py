'''import pandas as pd
dados = {'Salario':[2000, 4000, 6000, 8000, 10000, 15000],
         'Carro':[20000, 30000, 50000, 60000, 80000, 100000]}
x = pd.DataFrame(dados, columns = ['Salario', 'Carro'])
Correl = x.corr() # Correlação de Pearson
print(Correl)'''

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
data = {'Salario':[2000, 4000, 6000, 8000, 10000, 20000],
        'Carro':[20000, 30000, 50000, 60000, 80000, 120000],
        'Estudo':[8, 11, 13.5, 16, 18, 23]}
df = pd.DataFrame(data,columns = ['Salario', 'Carro', 'Estudo'])
Correl = df.corr()
print(Correl)
sn.heatmap(Correl, annot=True)
plt.show()