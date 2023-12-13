'''
For my data analysis project, I chose to investigate electric vehicle populations and their usage in the state of Washington. I chose to explore this topic
because electric vehicles are an expanding market, as there has been a noticeable global shift towards more sustainable transportation in recent years. As a
society, we are starting to place a strong value on green technology and cleaner alternatives to products that may cause significant environmental harm. Electric
vehicles are rapidly emerging in the automotive industry due to their lack of carbon emissions and their independence from the use of fossil fuels. Along with this,
the use of an electric vehicle tends to be more cost-effective in the long run as users save on rising gas prices. The advancement of electric vehicle usage not
only lessens our environmental impact on the atmosphere but also integrates renewable energy that decreases our reliance on finite resources in a cost-effective and
convenient manner. As electric vehicle technology continues to advance, we will see that this type of automotive engineering will grow and demand and quickly become
 more common on our streets.

In this project, I am using a data set, sourced from Kaggle,  that records electric vehicle usage in the state of Washington. The data includes information on:

VIN (1-10): (first ten characters of the Vehicle Identification Number)
County of registration
City where the vehicle is located.
State where the vehicle is registered.
Postal Code of the vehicle's location.
Model Year of the vehicle model.
Make of the vehicle.
Model of the vehicle.
Electric Vehicle Type (e.g., PHEV, BEV).
CAFV (Clean Alternative Fuel Vehicle) Eligibility status.
Electric Range of the vehicle.
Base MSRP (Manufacturer's Suggested Retail Price)
Legislative District associated with the vehicle.
DOL (Department of Licensing) Vehicle ID
Geographic location of the vehicle.
Electric Utility associated with the vehicle.
2020 Census Tract information for the year 2020.

Using this data, I will be exploring the population of electric vehicles and their usage patterns in the state of Washington. Through this exploration, my goal is
to provide an in-depth and comprehensive understanding of the electric vehicle market in this population to show how this growing market is evolving the automotive
industry.

→ Understanding the Demographic ←
To explore this data,  we need to understand the demographic of people that we are observing. The total population of the state of Washington is 7,705, 281.
The median household income sits much higher than the national average of $91,306, with about 39.5% of the population holding a bachelor's degree or higher.
From this information, we can see that the overall population of Washington tends to be on the wealthier side of the class Spectrum. In association with our topic
 of electric vehicles, we can understand that a large population of people in Washington own electric vehicles due to their higher average income.

→ Questions of analysis: ←
To explore the data we need to ask questions about how certain pieces of information relate to each other. The questions I will be exploring throughout this
project are:
1. Which cities have the most electric vehicle registrations?
2. What is the average value of the electric ranges? What is the highest and lowest range, and what is the corresponding Make and Model of these values?
3. Which automotive companies make up Washington’s Electric Vehicle population?
4. How many Electric Vehicles in Washington are Clean Alternative Fuel Vehicle Eligible or Not eligible due to low battery range?
5. What percentage of electric vehicles in the dataset are eligible as Clean Alternative Fuel Vehicles?
6. What is the growth of electric vehicle populations in Washington over time?

I will be analyzing the data set and translating it into visualizations and reports in the form of graphs charts and calculations.  I will provide an answer
and a breakdown of statistical proof for each of these questions so that we can gain a comprehensive understanding of the electrical vehicle market in Washington.
'''

'''
→ Initial statements ←
This section of code is to import all of the necessary factors we need to process this data. We import the pandas package to aid in calculations, and the 
matplotlib to create data visualization such as graphs and charts. We then import the data set into this program so the code can read values from the spreadsheet
and perform analysis. 
'''
import pandas as pd
import matplotlib.pyplot as plt

dataset_path = 'Electric_Vehicle_Population_Data.csv'
df = pd.read_csv(dataset_path)

'''
→ Data cleaning ←
The first thing we do is clean up the data set a bit. As you can see In the code below, we first make a copy of our data set,  
then drop the null values of each column.  This gets rid of any data that was left empty and replaced with a zero. The next line checks if the null values 
were actually dropped. Finally, the last line of this section checks if there were any duplicates of information in the data set. This test came out negative 
so we don't have to worry about this any further
'''

df1=df
df1=df1.dropna()
df1.isnull().sum()
df1.duplicated().any()

'''
→ Establishing figure ←
This line simply establishes a figure that holds multiple plots in it. That means that multiple graphs and charts will be displayed on one window. 
'''

fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(20,7))

'''
Question 1: Which cities have the most electric vehicle registrations?

Using the code we are trying to find and output a table that displays the top 10 cities that have the highest electric vehicle registration in the left 
column and displays the exact amount of registrations in the right column. This output is generated as a simple print statement. 
The first line groups the data frame (df) by the ‘City’  column and counts the number of times this label occurs in the data set. The index that counts 
the occurrences is renamed to ‘# of Vehicles’ for the purpose of appearances. The next line sorts the data from the previous line in descending order. Finally, 
this information is printed to the output area. 

'''

vehiclesInCity = df.groupby(['City']).size().reset_index(name='# of Vehicles')
highestRegistrations = vehiclesInCity.sort_values(by='# of Vehicles', ascending=False)
print(highestRegistrations.head(10))

'''
Question 2: What is the average value of the electric ranges? What is the highest and lowest range, and what is the corresponding Make and Model of these values?

To explore this question we first need an understanding of what exactly an electric range is. 
According to Autoweek, “An electric vehicle's range refers to the number of miles an EV can travel on a fully charged battery, or a single charge. 
While an automaker may advertise—and the EPA will confirm—a certain range for a vehicle, that number represents an ideal or theoretical distance it will 
travel on a charge” 

To gain a better understanding of this data in Washington, first, I found the average range of the entire population. This was done with a simple print 
statement that took the information from the “Electric Range” column and calculated an average value. Next, I wanted to find the maximum and minimum Electric 
range values and determine the make and model of the vehicle that presented these values. To do this I used a function to find either the maximum or the minimum 
value in the column dataset. I then matched up the value that was found from the “Electric Range” column and paired it with the corresponding point of data from 
the “Make” column and the “Model” column. I printed the outputted data into two sentences that summarized the findings from this calculation. 
'''

avg_value = df['Electric Range'].mean()
print(f"Average Value of the Electric Range: {avg_value}")
topRange = df['Electric Range'].max()
topRangeMake = df.loc[df['Electric Range'] == topRange, 'Make'].values[0]
topRangeModel = df.loc[df['Electric Range'] == topRange, 'Model'].values[0]
print(f"The highest value in the Electric Range is", topRange, "and the vehicle with this value is ", topRangeMake, topRangeModel)
lowRange = df['Electric Range'].min()
lowRangeMake = df.loc[df['Electric Range'] == topRange, 'Make'].values[0]
lowRangeModel = df.loc[df['Electric Range'] == topRange, 'Model'].values[0]
print(f"The highest value in the Electric Range is", lowRange, "and the vehicle with this value is ", lowRangeMake, lowRangeModel)

'''
Question 3: Which automotive companies make up Washington’s Electic Vehicle population?
  
To find out which companies are the most popular among Washington citizens, I created a pie chart to help visualize the ratios of the data. To code this, 
I created a label for each of the companies that would appear in the data and assigned them a corresponding value to help the program discern different Makes 
and assign the data to the labels. I then established a pie chart and described its visual specifications, such as the starting angle, the font size, and an equal 
aspect ratio. The program outputs a color-coded pie chart showing the ratios of registered cars from different companies in Washinton. From this, we can see that
the top three most popular Electric vehicle companies are Volvo, Volkswagen, and Toyota.

'''

CARlabs =['Audi', 'BMW', 'Chevrolet', 'Chrysler', 'Fiat', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Lincoln', 'Mercedes-Benz', 'Mini', 'Mitsubishi', 'Nissan', 'Polestar', 'Porsche', 'Rivian', 'Smart', 'Subaru', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo' ]
CARvals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
ax1.pie(CARvals, labels = CARlabs, autopct = '%1.1f%%', startangle= 90, textprops={'fontsize':5})
ax1.axis('equal')
ax1.set_title('What are the most popular Electric Vehicle companies in Washington?')

'''
Question 4: How many Electric Vehicles in Washington are Clean Alternative Fuel Vehicle Eligible or Not eligible due to low battery range

To understand this question, we must understand what CAFV Eligibility is. According to dataWashinton.gov, “Eligibility is based on the fuel requirement 
and electric-only range requirement as outlined in RCW 82.08. 809 and RCW 82.12. 809 to be eligible for Alternative Fuel Vehicles retail sales and Washington 
State use tax exemptions” Essentially, through this data, we can determine if citizens are often able to utilize their eclectic vehicles for tax exeptions. 

For this question, I created a bar graph that consisted of three colloms, CAFV eligible, not CAFV eligible, and Eligibility was unknown due to the lack of data
on the vehicle battery range. To code this, I first counted the occurrences of each scenario from the “Clean Alternative Fuel Vehicle (CAFV) Eligibility” column
and stored the value. I created the names of the bars that this data would fill in and created a bar chart. I customized the plot and directed the corresponding 
data into the correct bar lines in the graph. The output of this code results in a bar graph with three sections that show that CAFV-eligible cars are the most 
common, non-eligible cars are the second most common, and it is most uncommon to have an unknown eligibility.

'''

cafvNUMB = df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].value_counts()
COLlabs =['CAFV eligible', 'not CAVF eligable', 'unknown battery range']
COLvals = [1, 2, 3]
cafvNUMB.plot(kind='bar', ax = ax2)
ax2.set_xlabel('What kind of Clean Alternative Fuel Vehicle (CAFV) Eligibility is Used')
ax2.set_ylabel('Frequency in Data')
ax1.set_title('What is the growth of electric vehicle populations in Washington over time?')
ax2.set_xticklabels(COLlabs, rotation = 0)
ax2.tick_params(axis = 'x', labelsize= 5)

'''
Question 5: What percentage of electric vehicles in the dataset are eligible as Clean Alternative Fuel Vehicles?

After exploring the previous question, we can see that determining CAFV eligibility can be important to Washington taxpayers and the state government. 
Uncovering the percentage of vehicles in the state that qualify for this tax exemption can prove to be very important information. The code I used to find this 
determines what vehicles are eligible by identifying which points of data in the “ “Clean Alternative Fuel Vehicle (CAFV) Eligibility” column are assigned the 
string value “ “Clean Alternative Fuel Vehicle Eligible” This determines the value of eligible vehicles, which is then used in a simple arithmetic calculation 
to fu=ind the percentage. A statement showing the results is printed 

'''

CAFVelg = df[df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'Clean Alternative Fuel Vehicle Eligible']
ratioCAFVelg = (len(CAFVelg) / len(df)) * 10
print(f"Percentage of Electric Vehicles Eligible as CAFV: {ratioCAFVelg:.2f}%")

'''
Question 6: What is the growth of electric vehicle populations in Washington over time? 

In this question, we can see how more Washinton citizens are opting for sustainable transportation as years pass. This is an important area of data 
to explore since investors, companies, and lawmakers need to see how citizens are choosing to switch from standard vehicles to electric. To code for this, 
I wanted to create a plotted line chart to show the growth of electric vehicle registrations over time. I started by listing all the years as labels and assigning
values to them to help the program create a graph. I specified the visual constraints of the plot and allowed the program to plot the values based on the data.
From the results, we can see that there is a clear linear growth of registration in electric vehicles over time.

'''

yearLABS = [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
YRvalues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
ax3.plot(yearLABS, YRvalues, marker='o', linestyle='-')
ax3.set_xlabel('What is the pattern of Electric Vehicle usage in Washington over time?')
ax3.set_xlabel('year')
ax3.set_ylabel('Frequency in data')
ax3.tick_params(labelsize= 7)

'''
→ Conclusion ←
In conclusion, this data analysis project has uncovered the electric vehicle market of Washington and has provided insight that can be used to 
influence and inform future policies and manufacturing of electric vehicles, and ultimately assist in the evolution of sustainable and eco-friendly transportation
 solutions.
 
 sources used :
 https://data.census.gov/all?q=washington
 https://www.autoweek.com/news/a37940107/ev-range-and-what-affects-it/
 https://data.wa.gov/Transportation/Electric-Vehicle-Title-and-Registration-Activity/rpr4-cgyd/data
 

'''

plt.subplots_adjust(wspace = 0.8)
plt.show()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
