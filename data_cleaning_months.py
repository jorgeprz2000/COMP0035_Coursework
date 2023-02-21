import pandas as pd
import os

if __name__ == '__main__':
    # Enter the desired year you wish to analyze:
    year = str(2019)
    DIRECTORY = 'DATA/' + year + '/'

    def cleaning_months():
        for folder in os.listdir(DIRECTORY):
            # We must get rid of the hidden files in Python such as .DS_Store:
            if not folder.startswith('.'):
                directory_new = DIRECTORY + str(folder)
                month = []
                for file in os.listdir(directory_new):
                    # In order for this code to be able to without having delete the output, every time it runs it will delete the previous output of month.xlsx:
                    if file.startswith('month.xlsx'):
                        os.remove(os.path.join(directory_new, file))
                    elif not file.startswith('.'):
                        filename = directory_new + '/' + file
                        df = pd.read_excel(filename, skiprows=[0])
                        # print(df.columns)
                        print(df.head())
                        df = df.drop(['Rank', 'Country of Origin', 'Distributor', 'Number of cinemas', 'Site average',
                                      '% change on last week'], errors='ignore', axis=1)
                        df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, errors='ignore', inplace=True)
                        df = df.dropna(how='all', axis='columns')
                        df.columns = df.columns.str.replace(' ', '_')
                        # Since we want to investigate how different times of the year change a movies release sucess, we will only keep those movies in each week that just released
                        df = df[df.Weeks_on_release == 1]
                        # print(df.isnull())
                        df = df.dropna()
                        month.append(df)

                month = pd.concat(month)
                directory_month = directory_new + '/month.xlsx'
                month.to_excel(directory_month, index=False)


    def number_of_movies():
        released_films = []
        average_office_sales = []
        months = []
        for folder in os.listdir(DIRECTORY):
            # We must not read hidden files such as .DS_Store:
            if not folder.startswith('.'):
                directory_new = DIRECTORY + str(folder)
                for file in os.listdir(directory_new):
                    # Only read the 'month.xlsx' files that the previous function made:
                    if file.startswith('month.xlsx'):
                        filename = directory_new + '/' + file
                        df = pd.read_excel(filename, skiprows=[1])
                        released_films.append(len(df.index))
                        months.append(str(folder))
                        average_office_sales.append(df['Weekend_Gross'].mean())
        Competition_vs_sales = pd.DataFrame({'months': months, 'released_films': released_films, 'average_office_sales': average_office_sales})
        # It is important to organize dataframe by month name. In order to do this I replace month with number month, sort, and replace back to name:
        Competition_vs_sales["months"].replace({"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}, inplace=True)
        Competition_vs_sales.sort_values(['months'], ascending=True, inplace=True)
        Competition_vs_sales["months"].replace({1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}, inplace=True)
        output_directory = 'Data_output' + '/' + year + '.xlsx'
        Competition_vs_sales.to_excel(output_directory, index=False)


cleaning_months()
number_of_movies()