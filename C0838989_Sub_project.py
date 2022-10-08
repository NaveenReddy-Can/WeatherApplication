
"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                SUB PROJECT-1
                      # DESCRIPTION:
                                    This is a wether displying application developed using open weather API and TKInter GUI.
                                    > Asks the user to input the any city name in the world as show here -> ENTER CITY NAME: sarnia.
###########################################################################################################################################################################                                    
                                    SAMPLE OUTPUT:-
                                    ---------------------------------------------------------------------------------------------------------------------------------------
                                    OUTPUT:-
                                           Temperature in = SARNIA 
                                           Temperature (in celsius) = 2.44
                                           Temperature (in fahrenheit) = 36.39
                                           country   = CA
                                           atmospheric pressure (in hPa unit) = 1007
                                           humidity (in percentage) = 90
                                           wind  = {'speed': 2.06, 'deg': 30}
                                           description = mist                                              
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
"""
# Naveen Reddy
# C0838989
# PYTHON SUB-PROJECT-1
"""
"""
# Import the required Libraries
# Used to design GUI and ACCESS the TIME
"""

#global variables
import tkinter as tk
import requests
from tkinter import *
import time
global string
global count

# global count variable intialized with one
count = 1

# tk inter intialization
win = tk.Tk()
# tk inter title display:
win.title('OpenWeatherApp')
# sets background color
win['background'] = '#D3AF37'

# greeting message
greetings = tk.Label(text="Welcome to Weather application",
                     foreground="white",   background="black", font='50')
# greeting alignment which does automatically
greetings.pack(fill=tk.X)

cityName = tk.StringVar()
# Enter your API key here
api_key = "24fdf55d0ba64ce8652677c1961157e0"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Initialize a Label to display the User Input
label = tk.Label(win, text="Enter a city name", font=("Courier 22 bold"))
label.pack()
# Entry for city name
entry1 = tk.Entry(win, textvariable=cityName, width=40)
string = cityName  # storing cityname in string variable
entry1.focus_set()
entry1.pack()  # alignment of entry widget.


"""
method for  finding wether and which takes event as a argument variable
"""


def FindWeather(event):
    # city_name get by method calling
    city_name = string.get()
    # complete url by putting all three variables
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
    response = requests.get(complete_url)\

# json method of response object
# convert json format data into
# python format data
    x = response.json()


# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found

    if x["cod"] != "404":
        if x["cod"] == "400":
            print("Empty string retrived")

    # store the value of "main"
    # key in variable y
        y = x["main"]
    # store the value corresponding
    # to the "temp" key of y
        current_temperature = y["temp"]
        # celsius calcuting here
        celsius = current_temperature-273.15
        # formating the celsius
        celsius_format = "{:.2f}".format(celsius)
        # calculating the fahrenheit
        fahrenheit = celsius * 9/5 + 32
        # formatting it
        fahrenheit_format = "{:.2f}".format(fahrenheit)

    # store the value corresponding
    # to the "pressure" key of y
        current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
        current_humidity = y["humidity"]

        # storing current wind in current_wind variable
        current_wind = x["wind"]

        sys = x["sys"]
        # storing country in country variable
        country = sys["country"]

    # store the value of "weather"
    # key in variable z
        z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
        weather_description = z[0]["description"]

    # print following values
        print(" Temperature in = " + (city_name).upper()
              +
              " \n Temperature (in celsius) = " +
              str(celsius_format) +
              "\n Temperature (in fahrenheit) = " +
              str(fahrenheit_format) +
              "\n country   = " +
              str(country) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidity) +
              "\n wind  = " +
              str(current_wind) +
              "\n description = " +
              str(weather_description))

        # Initialize a Label to display the User Input

        label1 = tk.Label(text="", font=("Courier 22 bold"))
        label1.pack()
        # Initialize a Label to display the User Input
        label2 = tk.Label(win, text="", font=("Courier 22 bold"))
        label2.pack()

        # Initialize a Label to display the User Input
        label3 = tk.Label(win, text="", font=("Courier 22 bold"))
        label3.pack()

        # Initialize a Label to display the User Input
        label4 = tk.Label(win, text="", font=("Courier 22 bold"))
        label4.pack()
        # Initialize a Label to display the User Input
        label5 = tk.Label(win, text="", font=("Courier 22 bold"))
        label5.pack()
        # Initialize a Label to display the User Input
        label6 = tk.Label(win, text="", font=("Courier 22 bold"))
        label6.pack()
        # Initialize a Label to display the User Input
        label7 = tk.Label(win, text="", font=("Courier 22 bold"))
        label7.pack()
        # Initialize a Label to display the User Input
        label8 = tk.Label(win, text="", font=("Courier 22 bold"))
        label8.pack()

        """
        configuring the labels and displaying the output
        the output is prints on GUI 
        TKInter is the GUI is used here
        """
        label1.configure(text="City name : " + city_name.upper())
        label2.configure(text="Celsius Temperature : " +
                         celsius_format+u"\N{DEGREE SIGN}")
        label3.configure(text="Fahrenheit Temperature : " +
                         fahrenheit_format+u"\N{DEGREE SIGN}")
        label4.configure(text="Country : " + country)
        label5.configure(text="Pressure : " + str(current_pressure))
        label6.configure(text="Humidity : " + str(current_humidity))
        label7.configure(text="Wind : " + str(current_wind))
        label8.configure(text="Weather Description : " + weather_description)

        """ 
        # destroy the previous data
        # destroying all the labels by using destroy in built method
        """
        def remove():
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            label6.destroy()
            label7.destroy()
            label8.destroy()
            entry1.delete(0, END)
            clear_screen.destroy()
        if count > 1:
            remove()
        # clears the screen after click event on clear screen button
        clear_screen = tk.Button(win, text="Clear_screen", command=remove)
        clear_screen.pack()
    else:
        # if entered city not found in Open wether api displayed this erroe message
        print(" City Not Found ")


# button for wether display by click event on it
button = tk.Button(win, text="Find Weather",
                   command=lambda: FindWeather(string))
# it displayed and aligned by pack() method auto aligns on center of the screen
button.pack()
# clock method


def clock():
    # stroing hours
    hour = time.strftime("%H")
    # storing minutes
    minute = time.strftime("%M")
    # storing seconds
    second = time.strftime("%S")
    # storing time
    day = time.strftime("%A")
    # label for displaying time
    my_label.config(text=hour+":"+minute + ":"+second)
    my_label.after(1000, clock)
    my_label2.config(text=day)


"""
labels for displaying the output
city_name and degress temperature
"""
my_label = tk.Label(win, text="", font=("Helvetica", 48),)
my_label.pack()
my_label2 = tk.Label(win, text="", font=("Helvetica", 14),)
my_label2.pack()
# method caalling
clock()

# Timer for 30 minutes


def timer30mns():
    # setting hal an hour time
    times = 18000
    while times > -1:
        minute, second = (times // 60, times % 60)
        seconds.set(second)
        minutes.set(minute)
        # Update the values
        win.update()
        # sleeps a second or pauses a second to show clock
        time.sleep(1)
        if(times == 0):
            seconds.set('00')
            minutes.set('00')
            FindWeather(string)
        times -= 1
    """
    # function calling again (recursive)   
    """
    timer30mns()


# storing in displaying minutes
minutes = tk.StringVar()
minutes.set('00')
# displying mins
mins = tk.Entry(win, textvariable=minutes, width=2, font=("bold", 20))
mins.pack()
# storing and dsiplaying minutes
seconds = tk.StringVar()
seconds.set('00')
# storing and displying seconds
sec = tk.Entry(win, textvariable=seconds, width=2, font=("bold", 20))
sec.pack()
"""
Method calling :
"""
timer30mns()

"""
Method calling :
closing loop of win Tkinter
"""
win.mainloop()

"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                  END-OF-THE-SUBPROJECT-1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
