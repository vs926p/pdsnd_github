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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Please enter one of the three cities: chicago, new york city, washington : ').lower())
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print('Thats not a valid city, Please enter a valid city.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Please enter a valid month or "all" for all months: ').lower())
        month = month.lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print('Thats not a valid month, Please enter a valid month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Please enter a valid day of week or "all" for all days: ').lower())
        day = day.lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print('Thats not a valid day of week, Please enter a valid day')

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
    df = pd.read_csv(CITY_DATA[city])
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, hour, day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

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
    popular_month = df['month'].mode()[0]
    print('Most common month is: ', popular_month)
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week is: ', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_start_hour = df['start_hour'].mode()[0]
    print('Most common start hour is: ', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most common start station is: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most common end station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_Station'] = 'Start Station: '+ df['Start Station'] + ' and End Station: ' +  df['End Station']
    popular_comb_start_end_station = df['start_end_Station'].mode()[0]
    print('Most common trip combination is with, ', popular_comb_start_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time in days:', ((df['Trip Duration'].sum())/86400) )

    # TO DO: display mean travel time
    print('Mean total travel time in mins:', ((df['Trip Duration'].mean())/60) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of different user types: \n', df['User Type'].value_counts(), '\n')
    
    # TO DO: Display counts of gender
    try:
        print('Counts of different gender: \n', df['Gender'].value_counts(), '\n')
    except KeyError:
        print('No data is available for Gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('Earliest birth year is:', int(df['Birth Year'].min()) )
    except KeyError:
        print('No data is available for birth year')
    try:
        print('Most recent birth year is:', int(df['Birth Year'].max()) )
    except KeyError:
        print('No data is available for birth year')
    try:
        print('Most common year is:', int(df['Birth Year'].mode()) )
    except KeyError:
        print('No data is available for birth year')    
    print('-'*40)

def display_data(df):
    """
    Display the raw data to the display as requested by
    the user.
    """

    start_loc = 0
    end_loc = 5
    display_active = input("Do you want to see the raw data, yes or no?: ").lower()
    if display_active == 'yes':
        while True:
            print(df.iloc[start_loc:end_loc])
            start_loc += 5
            end_loc += 5
            end_display = input("Do you wish to continue, yes or no?: ").lower()
            if end_display == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
