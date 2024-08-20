def convert(time_str):

    time_str = time_str.strip().lower()

    if 'a.m.' in time_str or 'p.m.' in time_str:

        time_str = time_str.replace('a.m.', '').replace('p.m.', '').strip()
        hours, minutes = map(int, time_str.split(':'))

        if 'p.m.' in time_str and hours != 12:
            hours += 12

        if 'a.m.' in time_str and hours == 12:
            hours = 0

    else:

        hours, minutes = map(int, time_str.split(':'))

    return hours + minutes / 60.0

def main():

    time_input = input("What time is it?: ").strip()

    try:

        time_hours = convert(time_input)
        
    except ValueError:

        return

    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    if breakfast_start <= time_hours <= breakfast_end:

        print("breakfast time")

    elif lunch_start <= time_hours <= lunch_end:

        print("lunch time")

    elif dinner_start <= time_hours <= dinner_end:
    
        print("dinner time")

if __name__ == "__main__":
    main()
