import os.path
from datetime import datetime, date, time
import webbrowser

class Artist():
    def __init__(self, fullname:str, practice:int, cost:int, phone:str):
        self.__fullname = fullname
        self.__practice = practice
        self.__cost = cost
        self.__phone = phone

    def get(self, key) ->  None:
        if key == 'fullname':
            value = self.__fullname
        elif key == 'practice':
            value = self.__practice
        elif key == 'cost':
            value = self.__cost
        elif key == 'phone':
            value = self.__phone
        else:
            print("Key's incorrect!")
            return
        return value
    
    def print(self):
        return(
            "{0:50} {1:10} {2:6} {3:50}".format(
                self.__fullname,
                str(self.__practice),
                str(self.__cost), 
                self.__phone
            )
        )
    
    def pars(self, row):
        try:
            row_split = row.strip().split(',')
            self.__fullname = row_split[0]
            self.__practice = int(row_split[1])
            self.__cost = int(row_split[2])
            self.__phone = row_split[3]
        except:
            print("Error pars data from file")
    
    def join(self):
        return(','.join(
            (self.__fullname,
            str(self.__practice),
            str(self.__cost), 
            self.__phone)
        )
    )

    def edit(self, key, value):
        print('!!!', key, value)
        if (key == "fullname"):
            self.__fullname = value
        if (key == "practice"):
            self.__practice = value
        if (key == "cost"):
            self.__cost = value
        if (key == "phone"):
            self.__phone = value
        print("!!! Редагування завершене успішно")

#Клас Photo() описано:
class Photo():
    def __init__(self, name:str, date: date, time: time, image:str, descr:str, autor:str):
        self.__name = name
        self.__image = image
        self.__date = date
        self.__time = time
        self.__descr = descr
        self.__autor = autor
        #keys = ['name', 'image', 'date', 'time', 'descr', 'autor']
    def get(self, key) -> None:
        if key == 'name':
            value = self.__name
        elif key == 'image':
            value = self.__image
        elif key == 'date':
            value = self.__date.strftime("%d/%m/%Y")
        elif key == 'time':
            value = self.__time.strftime("%H:%M")
        elif key == 'descr':
            value = self.__descr
        elif key == 'autor':
            value = self.__autor
        else:
            print("Parameter 'key' is incorect")
            return
        return value
    def print(self):        
        return("{0:20} {1:30} {2:15} {3:10} {4:30} {5:15}".format(
            self.__name,
            self.__image,
            self.__date.strftime("%d/%m/%Y"),
            self.__time.strftime("%H:%M"),
            self.__descr,
            self.__autor))
    def pars(self, row):
        try:
            row_split = row.strip().split(',')
            self.__name = row_split[0]
            self.__image = row_split[1]
            
            dttm = datetime.strptime(
                row_split[2] + ' ' + row_split[3], 
                "%d/%m/%Y %H:%M")
            self.__date = dttm.date()
            self.__time = dttm.time()
            
            self.__descr = row_split[4]
            self.__autor = row_split[5]
        except:
            print("Error pars data from file")
    def join(self):
        return (
            ",".join(
                (self.__name,
                self.__image,
                self.__date.strftime("%d/%m/%Y"),
                self.__time.strftime("%H:%M"),
                self.__descr,
                self.__autor)
            )
        )

    def image(self):
        self.__open_path(self.__image)        
    def description(self):
        self.__open_path(self.__descr)

    def __open_path(self, path):
        if os.path.exists(path):
            webbrowser.open_new_tab(path)
        else:
            print("File don't exist")

#Клас Masters() описано:
class Masters():
    def __init__(self):
        self.__masters = []
    
    def add(self, artist:Artist):
        self.__masters.append(artist)
    
    def select (self, value) -> None:
        for artist in self.__masters:
            if value == artist.get('fullname'):
                return artist
    
    def filter(self, key:str, value):
        self.__print_header()
        for artist in self.__masters:
            val = artist.get(key)
            if val != None:
                if (key == 'practice' or key == 'cost') and val >= int(value):
                    print(artist.print())
                elif (key == 'fullname' or key == 'phone') and value in val:
                    print(artist.print())
                    
    def read(self, fileName):
        try:
            file_reader = open (fileName, mode = 'r', encoding='utf-8')
            data_list = file_reader.read().strip().split('\n')
            for row in data_list:
                artist = Artist('',0,0,'')
                artist.pars(row)
                self.__masters.append(artist)
            file_reader.close()
            print("Read from file succesfull")
        except:
            print("Error read from file" + fileName)

    def save(self, fileName):
        try:
            file_writer = open (fileName, mode = 'w', encoding='utf-8')
            for artist in self.__masters:
                file_writer.write(artist.join() + '\n')
            file_writer.close()
        except:
            print("Error save to file" + fileName)

    def print(self):
        self.__print_header()
        for i in range(len(self.__masters)):
            print(self.__masters[i].print()+"("+str(i)+")")
    
    def __print_header(self):
        print(
            "{0:50} {1:10} {2:6} {3:50}".format('fullname', 'practice', 'cost', 'phone')
        )

    def get(self,key):
        if (key=="fullname"):
            value=self.__fullname
        elif (key=="practice"):
            value=self.__practice
        elif (key=="cost"):
            value=self.__cost
        elif (key=="phone"):
            value=self.__phone
        
        else:
            print("задано не існуюче поле")
        return value

    def get_masters(self, value): 
        for master in self.__masters:
            if(value == master.get("fullname")):
                return master
       

#Клас Album() описано:

class Album():
    def __init__(self):
        self.__album = []
    def add(self, photo):
        self.__album.append(photo)

    def filter(self, key, value):
        self.__print_header()
        for photo in self.__album:
            value = photo.get(key)
            if value != None and value in photo.get(key, value):
                    print(photo.print())
    def print(self):
        self.__print_header()
        for i in range(len(self.__album)):
            print(self.__album[i].print() + "("+str(i)+")")

    def read(self, fileName):
        try:
            file_reader = open (fileName, mode = 'r', encoding='utf-8')
            data_list = file_reader.read().strip().split('\n')
            for row in data_list:           
                photo = Photo('',0,0,'','','')
                photo.pars(row)
                self.__album.append(photo)
            file_reader.close()
            print("Read from file succesfull")
        except:
            print("Error read from file" + fileName)
        
    def save(self, fileName):
        try:
            file_writer = open (fileName, mode = 'w', encoding='utf-8')
            for photo in self.__album:
                file_writer.write(photo.join() + '\n')
            file_writer.close()
        except:
            print("Error save to file " + fileName)

    def open(self, key, index:int):
        try:
            if key == 'image':
                self.__album[index].image()
            elif key == 'description':
                self.__album[index].description()
        except:
            print("Error open file")

    def __print_header(self):
        print("{0:20} {1:30} {2:15} {3:10} {4:30} {5:15}".format('name', 'image', 'date', 'time', 'descr', 'autor'))

    def delete(self, name):
        success = False
        for i in range(len(self.__album)):
            if (self.__album[i].get("name") == name):
                self.__album.remove(self.__album[i])
                success = True
                break
        return False

    def delete(self, name):
        success = False
        for i in range(len(self.__album)):
            if (self.__album[i].get("name") == name):
                self.__album.remove(self.__album[i])
                success = True
                break
        return False
