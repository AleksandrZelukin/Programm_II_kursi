import tkinter as tk
import requests
win = tk.Tk()

def print_areas():
  url_places = 'https://www.timeapi.io/api/TimeZone/AvailableTimeZones'
  query_places = {'type': 'like'}
  res_places = requests.get(url_places, params=query_places)
  data_places = res_places.json()
  print(data_places)
print_areas()
print("\n Izvēlies atrašanās vietu atbilstoši laikazonai un ieraksti saskarnē. \n")

print("Izvēlies laikazonas starpību un ievadi saskarnē! \n")

try:
  def get_time():
    
    city = cityInput.get()
    url= 'https://www.timeapi.io/api/Time/current/zone?timeZone=America/New_York'
    query = {'type': 'like'}
    res = requests.get(url, params=query)
    data = res.json()
    print(data)
    
    title0['text'] = "Servera datums, laiks no Ņujorkas:" + f' {data["date"]} {data["time"]}'

    url= 'https://www.timeapi.io/api/Time/current/zone?timeZone=' + str(city)
    query2 = {'type': 'like'}
    res2 = requests.get(url, params=query2)
    data2 = res2.json()
    print(data2)

    title1['text'] = "Laiks ar nobīdi: " + f' {data2["date"]}, {data2["time"]}'

    if f' {data["date"]}'!= f' {data2["date"]}':
      nobide = 24 - int(f' {data["hour"]}') + int(f' {data2["hour"]}')
    else:
      if int(f' {data["hour"]}') > int(f' {data2["hour"]}'):
        nobide = int(f' {data["hour"]}') - int(f' {data2["hour"]}')
      else:
        nobide = int(f' {data2["hour"]}') - int(f' {data["hour"]}')
    title2['text'] = "Ievadītā laikazonas starpība: " + str(nobide)
except Exception as e:
  if not difference.get():
    print("Kluda, nav ievadits laiks. ", e)


win.geometry(f"600x500")
win['bg'] = 'blue'
win.title('Laika zonas')



frame1 = tk.Frame(win, bg = 'lightblue')
frame1.place(relx=0.1, rely=0.15, relwidth = 0.8, relheight=0.15)

frame2 = tk.Frame(win, bg = 'lightblue')
frame2.place(relx=0.1, rely=0.35, relwidth = 0.8, relheight=0.15)


title01 = tk.Label(frame1, text='Atrašanās vieta: ', bg = 'lightblue')
title01.place(relx=0.03, rely=0.04)

cityInput = tk.Entry(frame1, bg='white')
cityInput.place(relx=0.33, rely=0.04)


btn = tk.Button(frame1, text='Noteikt laiku un laikazonas', bg='yellow', command=get_time)
btn.place(relx=0.33, rely=0.65)


title0 = tk.Label(frame2, text='Ievadītā laikazonas starpība ', bg = 'lightblue')
title0.pack()
title1 = tk.Label(frame2, text='Datums, laiks un laikazona ', bg = 'lightblue')
title1.pack()
title2 = tk.Label(frame2, text='Nobīde ', bg = 'lightblue')
title2.pack()
win.mainloop()
