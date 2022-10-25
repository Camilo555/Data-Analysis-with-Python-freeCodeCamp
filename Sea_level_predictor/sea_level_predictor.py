import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure(figsize=(15, 8), dpi=100)
    ax = fig.add_subplot(111)
    plt.scatter(df.Year,df['CSIRO Adjusted Sea Level'], alpha=0.6,color = 'green', s=75)

  

    # Create first line of best fit
    slope_1, intercept_1, r_1, p_1, std_err_1 = linregress(df.Year,round(df['CSIRO Adjusted Sea Level'],7))

    anos = df.Year.copy()
    anos = anos.to_frame()
  
    a = range(2014,2051,1)
    a = list(a)
    for i in range(len(a)):
        anos = anos.append({'Year': a[i]}, ignore_index=True)

    anios = anos.Year.tolist()
    anios = list(anios)

    reg_lin = [round(((slope_1*x) + intercept_1),7) for x in anios]
    plt.plot(anios,reg_lin, label='Best Fit Line', color = 'orange', linewidth=4)

    # Create second line of best fit
    df_2 = df.copy()
    df_2 = df_2[df_2['Year']>=2000]

    slope_2, intercept_2, r_2, p_2, std_err_2 = linregress(df_2.Year,df_2['CSIRO Adjusted Sea Level'])

    anos_2 = df_2.Year.copy()
    anos_2 = anos_2.to_frame()

    for j in range(len(a)):
        anos_2 = anos_2.append({'Year': a[j]}, ignore_index=True)

    anios_2 = anos_2.Year.tolist()
    anios_2 = list(anios_2)

    reg_lin_2 = [round(((slope_2*x) + intercept_2),7) for x in anios_2]
    plt.plot(anios_2,reg_lin_2, label='Second Best Fit Line', color = 'red', linewidth=4)
  
    # Add labels and title
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()