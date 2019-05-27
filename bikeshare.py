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

    valid_cities = ('chicago', 'new york city', 'washington')

    city = input("\nPlease enter the city you are interested in. It could be either Chicago, New York City or Washington.\n").lower()

    while city not in valid_cities:
        city = input("\nInvalid entry! Please enter either Chicago, New York City or Washington.\n").lower()


    # TO DO: get user input for month (all, january, february, ... , june)

    valid_months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')

    month = input("\nPlease enter the month you are interested in. It could be either January, February, March, April, May, June or all.\n").lower()

    while month not in valid_months:
        month = input("\nInvalid entry! Please enter either January, February, March, April, May, June or all.\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    valid_days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

    day = input("\nPlease enter the day of the week you are interested in. It could be either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all.\n").lower()

    while day not in valid_days:
        day = input("\nInvalid entry! Please enter either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all.\n").lower()

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

    popular_month_number = df['month'].mode()[0]

    if popular_month_number == 1:
        popular_month_name = 'January'
    elif popular_month_number == 2:
        popular_month_name = 'February'
    elif popular_month_number == 3:
        popular_month_name = 'March'
    elif popular_month_number == 4:
        popular_month_name = 'April'
    elif popular_month_number == 5:
        popular_month_name = 'May'
    elif popular_month_number == 6:
        popular_month_name = 'June'

    print('Most popular month:', popular_month_name)

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]

    print('Most popular day of the week:', popular_day)

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most popular start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]

    print('Most commonly used start station:', popular_start_station)


    # TO DO: display most commonly used end station

    popular_end_station = df['End Station'].mode()[0]

    print('Most commonly used end station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    df['Trip'] = df['Start Station'] + " to " + df['End Station']

    popular_trip = df['Trip'].mode()[0]

    print('Most popular trip goes from ', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum() //60

    print('Total travel time (in minutes):', total_travel_time)

    # TO DO: display mean travel time

    mean_travel_time = total_travel_time // len(df.index)

    print('Mean travel time (in minutes):', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender

    if city == 'washington':
        print('No information regarding gender available for city of Washington')

    else:
        gender = df['Gender'].value_counts()
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth

    if city == 'washington':
        print('No information regarding year of birth available for city of Washington')

    else:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest year of birth:', earliest_birth)
        print('Most recent year of birth:', most_recent_birth)
        print('Most common year of birth:', most_common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df, city):
    """Choose for raw data."""

    if city == 'washington':
        details = input('\nWould you like to see any raw data? Enter yes or no.\n')
        raw_subset = df[['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type']]
        i = 0
        while details.lower() != 'no':
            print(raw_subset[i:i+5])
            i += 5
            details = input('\nWould you like to see any raw data? Enter yes or no.\n')
    else:
        details = input('\nWould you like to see any raw data? Enter yes or no.\n')
        raw_subset = df[['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']]
        i = 0
        while details.lower() != 'no':
            print(raw_subset[i:i+5])
            i += 5
            details = input('\nWould you like to see any raw data? Enter yes or no.\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_raw_data(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
