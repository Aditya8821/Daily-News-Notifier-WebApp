from newsapi import NewsApiClient
import time
import pycountry
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *


def Check(input_countries):
    input_countries = [input_countries.strip()]

    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2

    codes = [countries.get(country.title(), 'NO')
             for country in input_countries]
    if codes[0] == "NO":
        return "Wrong Country Name: Country not found..."
    return None


def progress(): #this will display the loading gif to create an attractive interface.
    put_html("<p align=""center""><img src=""https://media0.giphy.com/media/kUTME7ABmhYg5J3psM/200.webp?cid=ecf05e47som5hu3l2owou9vmn20hue70j113dgls1ghb1909&rid=200.webp&ct=g"" width=""120px""></p>")
    time.sleep(3)
    clear()
    logo()


def logo(): #this will display the image of newspaper to create an attractive interface.
    put_html("<p align=""left""><h4><img src=""https://image.flaticon.com/icons/png/128/2965/2965879.png"" width=""28px"">NEWS</h4></p>")

#this will display as a pop up in starting.
toast('LATEST NEWS NOTIFIER PRESENTED BY ADITYA', position='center',color='#000000', duration=3, onclick=clear)
time.sleep(3)

while 1: #this will run the below code until all the news headlines are displayed successfully one by one
        clear() 
        logo()
        newsapi = NewsApiClient(api_key='d680fd29ce414518ad6c0585fb00143b') #paste your unique API id here

        input_country = input("", placeholder="Enter Country Name",required=True, validate=Check) #take name of country as an input from the user
        progress()
        input_countries = [f'{input_country.strip()}']

        countries = {}

        for country in pycountry.countries:countries[country.name] = country.alpha_2

        codes = [countries.get(country.title(), 'Unknown code')for country in input_countries]

        option = radio("Which category are you interested in?",options=['Business', 'Entertainment', 'General', 'Health','Science', 'Technology'], required=True)
        progress()
        top_headlines = newsapi.get_top_headlines(category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')

        Headlines = top_headlines['articles']
        if Headlines:
            for articles in Headlines:
                b = articles['title'][::-1].index("-")
                if "news" in (articles['title'][-b+1:]).lower():
                    popup(f"{articles['title'][-b+1:]}", [put_html("<h4>"f"{articles['title'][:-b-2]}.""</h4>"), put_buttons(['Close'], onclick=lambda _: close_popup())], implicit_close=True)
                    time.sleep(3)
                else:
                    popup(f"{articles['title'][-b+1:]} News", [put_html("<h4>"f"{articles['title'][:-b-2]}.""</h4>"), put_buttons(['Close'], onclick=lambda _: close_popup())], implicit_close=True)
                    time.sleep(3)
        else:
            put_error(f"No articles found for {input_country}, Try for others...", closable=True)
            time.sleep(3)
            clear()
        clear()
        logo()
        option = radio("Do you want to search again?",options=['Yes', 'No'], required=True)
        if option == 'Yes':
            continue
        else:
            toast("Thanks For Visiting!")
            exit()
