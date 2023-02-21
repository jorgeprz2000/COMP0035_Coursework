import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # Input year which you wish to create visualizations, summon the function(s) corresponding to them, and click run:
    year = str(2021)  # <-- input year

    filename = 'Data_output/' + year + '.xlsx'
    df = pd.read_excel(filename)

    def boxplot():
        df = pd.read_excel(filename)
        df.plot.box(['average_office_sales', 'released_films'], subplots=True)
        plt.gcf().subplots_adjust(left=0.2)
        image_name = 'Data_output/Images/bp_sales_' + year + '.png'
        plt.savefig(image_name)
        plt.show()


    def bar_chart():
        plt.bar(df['months'], df['average_office_sales'], color='purple')
        plt.xticks(rotation=90)
        plt.xlabel('Month')
        plt.ylabel('Average Box office sales (£)')
        plt.title('How do box office sales on release weekend change per month? (' + year + ')')
        plt.gcf().subplots_adjust(bottom=0.3, left=0.2)
        image_name = 'Data_output/Images/bar_chart_sales_' + year + '.png'
        plt.savefig(image_name)
        plt.show()


    def line_chart():
        plt.plot(df['months'], df['average_office_sales'], color='orange')
        plt.xticks(rotation=90)
        plt.xlabel('Month')
        plt.ylabel('Average Box office sales on release (£)')
        plt.title('How do box office sales on release weekend change per month? (' + year + ')')
        plt.gcf().subplots_adjust(bottom=0.3, left=0.2)
        image_name = 'Data_output/Images/line_chart_sales_' + year + '.png'
        plt.savefig(image_name)
        plt.show()

    def scatter_plot():
        plt.scatter(df['released_films'], df['average_office_sales'], color='green')
        plt.xlabel('number of movies being released on the same weekend')
        plt.ylabel('Average box office sales on release (£)')
        plt.title('Does competition size affect box office sales on release? (' + year + ')')
        plt.gcf().subplots_adjust(left=0.2)
        image_name = 'Data_output/Images/scatter_plot' + year + '.png'
        plt.savefig(image_name)
        plt.show()

    boxplot()
    bar_chart()
    line_chart()
    scatter_plot()





