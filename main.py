from datetime import date, time
import os

from classes import Album, Masters, Photo, Artist

album = Album()
masters = Masters()

fileNameMasters = 'masters.txt'
fileNameAlbum = 'album.txt'

def options():
    print("\n--------------ГОЛОВНЕ МЕНЮ--------------")
    print("1: Додати фотографа")
    print("2: Додати фото в альбом")

    print("3: Список фотографів повний")
    print("4: Список фотографів вибірково")

    print("5: Список фотографій в альбомі")
    
    print("6: Вивести фото")
    print("7: Вивести опис фотографії")
    
    print("8: Очистити вікно")
    print("9: Зберегти дані y файл")
    print("10: EXIT")

def getDate() -> date:
    year = int(input("  рік: "))
    while True:
        month = int(input("  місяць(1..12): "))
        if month > 0 and month < 13:
            break
    while True:
        day = int(input("  день(1..31): "))
        if day > 0 and day < 32:
            break
    return date(year, month, day)

def getTime() -> time:
    while True:
        hour = int(input("  година(0-23): "))
        if hour >= 0 and hour < 24:
            break
    while True:
        minutes = int(input("  хвилини(0..59): "))
        if minutes >= 0 and minutes < 60:
            break
    return time(hour, minutes)

masters.read(fileNameMasters)
album.read(fileNameAlbum)


os.system('cls')
options()

while True:
    option = input("--Виберіть пункт меню: ")

    if option == '1':
        # 'fullname', 'practice', 'cost', 'phone'
        print("Інформація про фоторафа")
        fullname = input("Введіть ПІП: ")
        practice = int(input("Введіть скільки років практикує: "))
        cost = int(input("Введіть вартість години роботи: "))
        phone = input("Введіть контактний номер телефону: ")
        artist = Artist(fullname, practice, cost, phone)
        masters.add(artist)
    elif option == '2':
        # 'name', 'image', 'date', 'time', 'descr', 'autor'
        nameP = input("Введіть назву фото: ")
        image = input("Задайте шлях до файлу: ")
        
        print("Вкажіть дату роботи")
        dateP = getDate()
        print("Вкажіть час роботи")
        timeP = getTime()

        descrP = input("Вкажіть шлях до файлу з описом: ")

        while True:
            fullname = input("Вкажіть ПІП автора: ")
            if masters.select(fullname) == None:
                input("Перевірте дані автора і спробуйте знову")
            else:
                photo = Photo(nameP, dateP, timeP, image, descrP, fullname)
                album.add(photo)
                break

    elif option == '3':
        masters.print()

    elif option == '4':
        print("Поля: fullname, practice, cost, phone")
        key = input("Введіть поле для пошуку: ")
        value = input("Введіть значення для пошуку: ")
        masters.filter(key, value)

    elif option == '5':
        album.print()
 

    elif option == '6':
        index = int(input("Введіть індекс фото в альбомі (0 - перший): "))
        album.open('image', index)

    elif option == '7':
        index = int(input("Введіть індекс фото в альбомі (0 - перший): "))
        album.open('description', index)
    
    elif option == '8':
                os.system('cls')
                options()

    elif option == '9':
        masters.save(fileNameMasters)
        album.save(fileNameAlbum)

    
    elif option == '10':
        break    
print("ДО ЗУСТРІЧІ!!!")
