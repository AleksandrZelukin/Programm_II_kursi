'''
Uzņēmumam “Help Me” ir nepieciešams izstrādāt programmsaskarni ar savu ārpakalpojuma serveri. Problēma ir pareiza laika noteikšanā. Serveris atrodas Amerikas Savienotajās Valstīs. Amerikas Savienotās Valstis atrodas citā laika zonā. Jūsu uzdevums ir izveidot vienkāršu programmsaskarni jeb API, kurš pieprasījumā atgriež tā brīža pulksteņa laiku un laika zonu, tāpat arī laika zonas starpību. Atbilde jāatgriež JSON formātā, lai abās pusēs komunikācija notiktu droši.
'''

#pievieno grafisko saskarni tkinter
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
#    difference = timeDifference.get()
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

  ### IZSKATS SASKARNEI###
#veido saskarnes logu izmērus, izskatu un nosaukumu
win.geometry(f"500x400+10+20")
win['bg'] = '#7C51A0'
win.title('Laiks, laika zonas')
win.wm_attributes('-alpha', 0.9)

#veido augšējo oranžo taisnstūri -> ietvaru 1
frame1 = tk.Frame(win, bg = 'orange')
frame1.place(relx=0.15, rely=0.15, relwidth = 0.8, relheight=0.25)
#veido apakšējo oranžo taisnstūri -> ietvaru 2
frame2 = tk.Frame(win, bg = 'orange')
frame2.place(relx=0.15, rely=0.65, relwidth = 0.8, relheight=0.15)

#veido uzrakstu Atrašanās vieta
title01 = tk.Label(frame1, text='Atrašanās vieta: ', bg = 'orange')
title01.place(relx=0.03, rely=0.04)
#veido ievades lauku pilsētai
cityInput = tk.Entry(frame1, bg='white')
cityInput.place(relx=0.33, rely=0.04)

#veido uzrakstu Laika starpība
#title02 = tk.Label(frame1, text='Laika starpība: ', bg = 'orange')
#title02.place(relx=0.03, rely=0.35)
#veido ievades lauku Laika starpībai
#timeDifference = tk.Entry(frame1, bg='white')
#timeDifference.place(relx=0.33, rely=0.35)

#veido ievades pogu
btn = tk.Button(frame1, text='Noteikt laiku un laikazonas', bg='yellow', command=get_time)
btn.place(relx=0.33, rely=0.65)

#veido uzrakstu
title0 = tk.Label(frame2, text='Ievadītā laikazonas starpība ', bg = 'orange')
title0.pack()
title1 = tk.Label(frame2, text='Datums, laiks un laikazona ', bg = 'orange')
title1.pack()
title2 = tk.Label(frame2, text='Nobīde ', bg = 'orange')
title2.pack()
win.mainloop()
