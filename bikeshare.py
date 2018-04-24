import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington).
    city = ""
    month = "all"
    day = "all"
    filters = ["month","day","both","none"]
    monthlist=['january', 'february', 'march', 'april', 'may', 'june']
    daylist=["0","1","2","3","4","5","6"]
   
    while True: #Use a while loop to handle invalid inputs
        try:
            city =str(input("There are 3 cities.Please choose from Chicago,New York City,or Washington(Case-insensitive).\n").lower())
            #here you enter the city 
        except ValueError:
            print('Invalid input.')
            continue
        if city not in CITY_DATA:
            print('There is no such city.')
            continue
        else:
            try:
                filter = str(input("Would you like to filter the data by month,day,both,or not at all?Type 'NONE' for no time filter\n").lower())
            except ValueError:
                print('Invalid input.')
                continue
            
            while filter not in filters:
                filter = str(input("Would you like to filter the data by month,day,both,or not at all?Type 'NONE' for no time filter\n").lower())
            
            if filter == 'month':
                month = input("Please enter a month (January, February, March, April, May, June):").lower()
                while month not in monthlist:
                    month = input("Please enter a month (January, February, March, April, May, June):").lower()
                    
            elif filter == 'day':
                day = str(input("Please enter a day of week(The day of the week with Monday=0, Sunday=6):"))
                while day not in daylist:
                    day = str(input("Please enter a day of week(The day of the week with Monday=0, Sunday=6):"))

            elif filter == 'both':
                month = input("Please enter a month (January, February, March, April, May, June):").lower()
                while month not in monthlist:
                    month = input("Please enter a month (January, February, March, April, May, June):").lower()
                day = str(input("Please enter a day of week(The day of the week with Monday=0, Sunday=6):"))  
                while day not in daylist:
                    day = str(input("Please enter a day of week(The day of the week with Monday=0, Sunday=6):"))                 
            break

        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df =  pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['start_hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+ 1
        df = df[df['month'] == month]
      
      
    if day != 'all':
        df = df[df["day_of_week"] == int(day)]
      
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: {}".format(df['month'].mode()[0]))
    print("Noted:1 = January,2 = February,3 = March,4 = April,5 = May, 6 = June")


    # TO DO: display the most common day of week
    print("The most common day of week is: {}".format(df['day_of_week'].mode()[0]))
    print("Noted:0 = Mon.,1 = Tues.,2 = Wed.,3 = Thurs.,4 = Fri., 5 = Sat., 6 = Sun. ")


    # TO DO: display the most common start hour
    print("The most common start hour is: {}".format(df['start_hour'].mode()[0]))
    print("Noted:24-hour")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nThe most commonly used start station is: "\
          ,df['Start Station'].value_counts().idxmax(),\
          "\nCount:",\
          df['Start Station'].value_counts()[0])
    
    # TO DO: display most commonly used end station
    print("\nThe most commonly used end station is: "\
          ,df['End Station'].value_counts().idxmax(),\
          "\nCount:",\
          df['End Station'].value_counts()[0])

    # TO DO: display most frequent combination of start station and end station trip
    
    #combine the Start Station column and End Station column
    df["Start-End Station"]=df["Start Station"] + " and " + df["End Station"]
    
    print("\nThe most frequent combination of start station and end station trip is:"\
          ,df["Start-End Station"].value_counts().idxmax(),\
          "\nCount:",\
          df["Start-End Station"].value_counts()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\nThe total travel time is ",df["Trip Duration"].values.sum())

    # TO DO: display mean travel time
    print("\nThe mean travel time is ",df["Trip Duration"].values.mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    try:
        print("\ncounts of user types:\n",df["User Type"].value_counts())
    except KeyError:
        print("We don't have user types for this city.")
        

    # TO DO: Display counts of gender
    try:
        print("\ncounts of gender:\n",df["Gender"].value_counts())
    except KeyError:
        print("The Gender is not available for this city.")        

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("\nearliest year of birth:\n",df["Birth Year"].min())
        print("\nmost recent year of birth:\n",df["Birth Year"].max())
        print("\nmost common year of birth:\n",df["Birth Year"].mode()[0])
    except KeyError:
        print("The Birth Year data is not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()