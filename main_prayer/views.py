from django.shortcuts import render
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import schedule



def main_prayer(request):
    url ='https://www.masjideumer.org.uk/'
    html = requests.get(url)
    s = BeautifulSoup(html.content, 'html.parser')

    #finding all the start times for salah
    fajr_time = s.find("td", text="Fajr").find_next_sibling("td").text
    zuhr_time = s.find("tr", id="2").find("td").find_next_sibling("td").text
    asr_time = s.find("td", text="'Asr").find_next_sibling("td").text
    maghrib_time = s.find("td", text="Maghrib").find_next_sibling("td").text
    isha_time = s.find("td", text="'Ishā'").find_next_sibling("td").text

    #finding all the congregation times for salah
    fajr_jamah = s.find("td", text="Fajr").find_next_sibling("td").find_next_sibling("td").text
    zuhr_jamah = s.find("tr", id="2").find("td").find_next_sibling("td").find_next_sibling("td").text
    asr_jamah = s.find("td", text="'Asr").find_next_sibling("td").find_next_sibling("td").text
    maghrib_jamah = s.find("td", text="Maghrib").find_next_sibling("td").find_next_sibling("td").text
    isha_jamah = s.find("td", text="'Ishā'").find_next_sibling("td").find_next_sibling("td").text


    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%H:%M", named_tuple)
    
    #time difference between isha and maghrib (how long till isha)
    t1 = datetime.strptime(isha_time, '%H:%M')
    t2 = datetime.strptime(maghrib_time, '%H:%M')
    dt = abs(t2 - t1)

    context={
        'fajr':fajr_time,
        'zuhr':zuhr_time,
        'asr':asr_time,
        'maghrib':maghrib_time,
        'isha':isha_time,
        'fajr_jamah':fajr_jamah,
        'zuhr_jamah':zuhr_jamah,
        'asr_jamah':asr_jamah,
        'maghrib_jamah':maghrib_jamah,
        'isha_jamah':isha_jamah,
        'time':time_string,
        't':dt,
    }
    
    return render(request, 'main_prayer/main.html',context)


#run the function 'main_prayer' every 6 hours to scrape new times from the website
schedule.every(360).minutes.do(main_prayer)


 


