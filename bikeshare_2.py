import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# filters city, month and day
def get_filters():
    """Asks user to specify a city, month, and day to analyze."""
    print('Hello! Let\'s explore some US bikeshare data!')
    city = get_city()
    month = get_month()
    day = get_day()

    print('-'*40)
    return city, month, day

def get_city():
    """User select a city"""
    while True:
        city = input("Enter a city (New York City, Washington or Chicago)").lower()
        if city in CITY_DATA:
            return city
        else:
            print("Invalid city. Try again")

def get_month():
    """User select a month"""
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Enter a month (january, february,... june or all): ").lower()
        if month in months:
            return month
        else:
            print("Invalid month. Try again.")

def get_day():
    """User select a day"""
    days = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday','all']
    while True:
        day = input("Enter a day(monday, tuesday,wednesday...sunday), or enter 'all' if you want all days ").lower()
        if day in days:
            return day
        else:
            print("Invalid day. Try again")


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable."""
    df = pd.read_csv(CITY_DATA[city])
    # Filter by month and day if as necessary
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    # display the most common day of week
    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # display most commonly used end station
    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


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
