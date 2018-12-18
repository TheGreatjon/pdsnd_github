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
    #I added variables such as "city_found = 0" to make my input statements work in an algebraic way.
    cities = ['chicago', 'new york city', 'washington']

    city_found = 0

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']

    month_found = 0

    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']

    day_found = 0

    print('Hello! Let\'s explore some U.S. bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city_found == 0:
        city_input = input("Would you like data for Chicago, New York City, or Washington?  Kindly pick just one: ")
        for city in cities:
             if city_input.lower() == city.lower():
                city_found = 1
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    while month_found == 0:
        month_input = input("Please type a specific month; you can type 'all' (no quotes) for all of them: ")
        for month in months:
             if month_input.lower() == month.lower():
                month_found = 1
                break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day_found == 0:
        day_input = input("And please type a day of the week; you can type 'all' here as well: ")
        for day in days:
             if day_input.lower() == day.lower():
                day_found = 1
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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month =  months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    popular_month = df['month'].mode()[0]

    print('Here\'s the most popular month:', '\n', popular_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['day'] = df['Start Time'].dt.weekday

    popular_day = df['day'].mode()[0]

    print('Here\'s the most popular weekday (in Python, Monday = 0):', '\n', popular_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]

    print('Here\'s the most frequent start hour (e.g. 0 = midnight, 12 = noon):', '\n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()

    print("Here's the most common start station: ", '\n', start_station[0])

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()

    print("Here's the most common end station: ", '\n', end_station[0])

    # TO DO: display most frequent combination of start station and end station trip
    station_combo = (df['Start Station'] + " " + "to" + " " + df['End Station']).value_counts().idxmax()

    print("And here's the most frequent combination of start station and end station trip: ", '\n', station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration, converted into minutes."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration_total = df['Trip Duration'].sum() / 60

    print("Here's the sum of travel time for all trips in minutes: ", '\n', trip_duration_total)

    # TO DO: display mean travel time
    trip_duration_mean = df['Trip Duration'].mean() / 60

    print("And here's the overall average of travel time for all trips in minutes: ", '\n', trip_duration_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users; gender and age information is not available for Washington."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("This is the breakdown of user types for your selection: ", '\n', user_types)

    # TO DO: Display a breakdown of gender type, and age information (oldest DOB, youngest DOB, and most common DOB).
    # NOTE: An "if" statement was created so that Washington would be excluded due from the dataframe search because it doesn't have gender and age data.
    
    if city != 'washington':
        user_gender = df['Gender'].value_counts()
        print("This is the breakdown of gender types for your selection: ", '\n', user_gender)
        dob_oldest = df['Birth Year'].sort_values(ascending=True).head(1)
        print("Here\'s the earliest user year of birth: ", '\n', int(dob_oldest))
        dob_youngest = df['Birth Year'].sort_values(ascending=False).head(1)
        print("Here\'s the most recent user year of birth: ", '\n', int(dob_youngest))
        dob_mode = df['Birth Year'].mode()
        print("And here\'s the most common user year of birth: ", '\n', int(dob_mode))
    else:
        print('Gender and age information are not available for Washington; our apologies!')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """This function is being used to call and display raw data for viewing at the user's request."""
    
    #I had to load the data into an array so that it could print in an intelligible form.
    np_data = np.array(df)
    
    #I am setting a data_size variable here to serve as a limit for the range of the data file in the "for" statement.
    data_size = np_data.size
    
    print ('The size of the set you are working with in rows is: ' + str(data_size))
    
    #This "for" statement below serves as a counter for the user to view the raw data.
    for d in range(0, data_size):
        if ((d % 5) == 0):
            five_more =  input("To view and keep viewing raw data five rows at a time, please type 'yes' (no quotes); to stop, type anything: ")
            if (five_more.lower() != 'yes'):
                break
            print (np_data[d])
        else:
            print (np_data[d])
             
#This is the main definition/program for the entire project.
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        #This section of code was added to the main function to prompt for raw data review; a new def for raw_data was created to make it work.       
        data_prompt = input("\nWant to see individual trip data? If so, please type 'yes' (no quotes); if not, type anything to return to restart: ")
                            
        if data_prompt.lower() == 'yes':
            raw_data(df)
        restart = input("\nWould you like to restart? If so, please type 'yes' (no quotes), otherwise, type anything to quit: ")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
