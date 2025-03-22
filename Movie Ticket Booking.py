global f
f = 0

# This t_movie function is used to select the movie name
def t_movie():
    global f
    f = f + 1
    print("Which movie do you want to watch?")
    print("1, Movie 1: Avengers")
    print("2, Movie 2: Spiderman")
    print("3, Movie 3: Batman")
    print("4, Movie 4: Superman")
    print("5, Movie 5: Iron Man")
    print("6, Movie 6: Captain America")
    print("7, Movie 7: Black Widow")
    print("8, Back")
    movie = int(input("Choose your movie: "))
    if movie == 8:
        # In this case, it goes to the center function and from center it goes to movie function
        # then it comes back here and goes to the theater
        center()
        return 0
    if f == 1:
        theater()

# This theater function is used to select the screen
def theater():
    print("Which screen do you want to watch the movie on?")
    print("1, SCREEN 1")
    print("2, SCREEN 2")
    print("3, SCREEN 3")
    a = int(input("Choose your screen: "))
    ticket = int(input("Number of tickets do you want?: "))
    timing(a)

# This timing function is used to select timing for the movie
def timing(a):
    time1 = {
        "1": "10:00-1:00",
        "2": "1:10-4:10",
        "3": "4:20-7:20",
        "4": "7:30-10:30"
    }
    time2 = {
        "1": "10:15-1:15",
        "2": "1:25-4:25",
        "3": "4:35-7:35",
        "4": "7:45-10:45"
    }
    time3 = {
        "1": "10:30-1:30",
        "2": "1:40-4:40",
        "3": "4:50-7:50",
        "4": "8:00-10:45"
    }
    if a == 1:
        print("Choose your time:")
        print(time1)
        t = input("Select your time: ")
        x = time1[t]
        print("Successful! Enjoy the movie at " + x)
    elif a == 2:
        print("Choose your time:")
        print(time2)
        t = input("Select your time: ")
        x = time2[t]
        print("Successful! Enjoy the movie at " + x)
    elif a == 3:
        print("Choose your time:")
        print(time3)
        t = input("Select your time: ")
        x = time3[t]
        print("Successful! Enjoy the movie at " + x)
    return 0

def movie(theater):
    if theater == 1 or theater == 2 or theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("Wrong choice")

def center():
    print("Which theater do you wish to see the movie at?")
    print("1, Inox")
    print("2, Icon")
    print("3, PVP")
    print("4, Back")
    a = int(input("Choose your option: "))
    movie(a)
    return 0

# This function is used to select the city
def city():
    print("Hi, welcome to movie ticket booking!")
    print("Where do you want to watch the movie?")
    print("1, City 1")
    print("2, City 2")
    print("3, City 3")
    place = int(input("Choose your option: "))
    if place == 1 or place == 2 or place == 3:
        center()
    else:
        print("Wrong choice")

# Start the booking process
city()  # It calls the function city
