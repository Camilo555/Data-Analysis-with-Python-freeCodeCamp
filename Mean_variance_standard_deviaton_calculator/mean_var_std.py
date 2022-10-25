import numpy as np

def calculate(liste):
    
    if len(liste)<9:
        raise ValueError("List must contain nine numbers.")
    if len(liste)==9:
        

        lista = np.array(liste)
        matrix = lista.reshape(3,3)

        mean_1 = []
        mean_2 = []
        mean_f = lista.mean()

        var_1 = []
        var_2 = []
        var_f = np.var(liste)

        std_1 = []
        std_2 = []
        std_f = var_f**0.5

        max_1 = []
        max_2 = []
        max_f = lista.max()

        min_1 = []
        min_2 = []
        min_f = lista.min()

        sum_1 = []
        sum_2 = []
        sum_f = lista.sum()


        for i in range(0,3):

            # FILAS

            mean_1.append(matrix[i,:].mean())
            var_1.append(np.var(matrix[i,:]))
            std_1.append(np.var(matrix[i,:])**0.5)
            max_1.append(matrix[i,:].max())
            min_1.append(matrix[i,:].min())
            sum_1.append(matrix[i,:].sum())

            # COLUMNAS

            mean_2.append(matrix[:,i].mean())
            var_2.append(np.var(matrix[:,i]))
            std_2.append(np.var(matrix[:,i])**0.5)
            max_2.append(matrix[:,i].max())
            min_2.append(matrix[:,i].min())
            sum_2.append(matrix[:,i].sum())

        mean_t = [mean_2,mean_1,mean_f]
        var_t = [var_2,var_1,var_f]
        std_t = [std_2,std_1,std_f]
        max_t = [max_2,max_1,max_f]
        min_t = [min_2,min_1,min_f]
        sum_t = [sum_2,sum_1,sum_f]
        
        calculations = { 
                         'mean': mean_t,
                         'variance': var_t,
                         'standard deviation': std_t,
                         'max': max_t,
                         'min': min_t,
                         'sum': sum_t
                        }
    
    return calculations