import pandas as pd
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

# What is the average age of men?
    average_age_men = round(df[df['sex']=='Male'].age.mean(),1)

# What is the percentage of people who have a Bachelor's degree?
    value_bach = df[df['education']=='Bachelors'].count()[0]
    percentage_bachelors = round((value_bach/df.count()[0])*100,1)
# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    degrees = ['Bachelors', 'Masters', 'Doctorate']

    df_degrees = df[df['education'].isin(degrees)]
    count_degrees = df_degrees.count()[0]

    value_degree = df_degrees[df_degrees['salary']=='>50K'].count()[0]
    percentage_adv = round((value_degree/count_degrees)*100,1)

# What percentage of people without advanced education make more than 50K?

    df_notdegrees = df[~df['education'].isin(degrees)]
    count_notdegrees = df_notdegrees.count()[0]

    value_notdegree = df_notdegrees[df_notdegrees['salary']=='>50K'].count()[0]
    percentage_notadv = round((value_notdegree/count_notdegrees)*100,1)


# with and without `Bachelors`, `Masters`, or `Doctorate`


    higher_education = count_degrees
    lower_education = count_notdegrees

# percentage with salary >50K

    higher_education_rich = percentage_adv
    lower_education_rich = percentage_notadv

# What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    value_min = df[(df['hours-per-week']== 1) & (df['salary']=='>50K')].count()[0]

    num_min_workers = df[df['hours-per-week']== 1].count()[0]
    rich_percentage = round((value_min/num_min_workers)*100,1)

# What country has the highest percentage of people that earn >50K?
    df_sal = df[df['salary']=='>50K']


    df_count = df_sal['native-country'].value_counts()
    df_c = pd.Series(df['native-country'].value_counts(), name='Count tot')


    df_country = df_sal.groupby('native-country', as_index = False)['salary'].count()

    df_country['Num Country'] = (df_count/df_c)*100

    df_8 = pd.concat([df_count, df_c],axis=1)
    df_8['% Country'] = (df_8['native-country']/df_8['Count tot'])*100
    pais = df_8['% Country'].idxmax()
    percent = round(df_8['% Country'].max(),1)


    highest_earning_country = pais
    highest_earning_country_percentage = percent

# Identify the most popular occupation for those who earn >50K in India.
    df_3 = df[(df['salary']=='>50K') & (df['native-country'] =='India')]

    value = df_3['occupation'].value_counts().idxmax(axis=0)

    top_IN_occupation = value

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
