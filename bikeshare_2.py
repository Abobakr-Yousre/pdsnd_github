import time
import pandas as pd
import numpy as np
pd.set_option('display.expand_frame_repr', False)

CITY_DATA = {'chicago': 'F:\[Data_analysis]\Python_project\chicago.csv',
             'new york': 'F:\[Data_analysis]\Python_project\chicago.csv',
             'washington': 'F:\[Data_analysis]\Python_project\washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWould you like to see data for Chicago, New York, Washington:\n").lower()
        available_cities = ['chicago', 'new york', 'washington']
        if city.lower() in available_cities:
            break
        else:
            print(" \nOops we only have data for the cities we mentioned\n ")
    filter = input(
        "\nWould you like to filter data by month, day, or both? enter 'none' for not at all\n").lower()
    # get user input for month (all, january, february, ... , june)
    month = ""
    day = ""
    if filter == 'month':
        month = input("\nWhich month? January, February, March, April, May , and  june )\n").lower()
        day = ""
    # get user input for day of week (all, monday, tuesday, ... sunday)
    elif filter == 'day':
        day = input("\nWhich day? Monday, Tuesday, ... Sunday)\n").lower()
        month = ""
    elif filter == 'both':
        month = input("\nWhich month? January, February, March, April, May , and  june )\n").lower()
        day = input("\nWhich day? Monday, Tuesday, ... Sunday)\n").lower()

    print('-'*40)
    return city, month, day, filter


def load_data(city, month, day, filter):
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if filter == 'both':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower())+1
        df = df[df['month'] == month]
        df = df[df['day_of_week'] == day.title()]
    elif filter == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower())+1
        df = df[df['month'] == month]
    elif filter == 'day':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print("'1' = january, '2' = february,.....")
    # display the most common month
    print("most common month:\n", df['month'].mode()[0], "\n")

    # display the most common day of week
    print("most common day:\n", df['day_of_week'].mode()[0], "\n")

    # display the most common start hour
    print("most common hour:\n", df['hour'].mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most commonly Start Station:\n ", df['Start Station'].mode()[0], "\n")
    # display most commonly used end station
    print("most commonly End Station:\n ", df['End Station'].mode()[0], "\n")
    # display most frequent combination of start station and end station trip
    combination = df['combo'] = df['Start Station'] + df['End Station']
    combination = df['combo'].mode()[0]
    print("most commonly combination of trip:\n", combination, "\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total duration: \n ", df['Trip Duration'].sum(), "\n")
    # display mean travel time
    print("Average duration: \n ", df['Trip Duration'].mean(), "\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    if city.lower() != 'washington':
        print('\nCalculating User Stats...\n')
        start_time = time.time()
        # Display counts of user types
        print("Number of user:\n ", df['User Type'].value_counts(), "\n")
        # Display counts of gender
        print("Number of gender:\n", df['Gender'].value_counts(), "\n")
        # Display earliest, most recent, and most common year of birth
        print("Earliest birth day: ", int(df['Birth Year'].min()), "\n")
        print("Most recent bith day: ", int(df['Birth Year'].max()), "\n")
        print("Most common birth day", int(df['Birth Year'].mean()), "\n")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print("Sorry Washington has no user information data.")
    i = 0
    # asking the usre for individaul_data
    individaul_data = input("\nWould you like to see individual data trip?  (yes/no)\n ")
    if individaul_data.lower() == 'yes':
        while True:
            print(df.iloc[i:i+5])
            i += 5
            more_data = input("\nWould you like to see more data ? (yes/no)\n")
            if more_data.lower() != "yes":
                break


def main():
    while True:
        city, month, day, filter = get_filters()
        df = load_data(city, month, day, filter)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
