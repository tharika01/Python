import pickle

"""imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the rug'),
           (2, 'psycho'),
           (3, 'Mayhem')))
          
with open("imelda.pickle","wb") as pickle_file:
          pickle.dump(imelda, pickle_file)
          
with open("imelda.pickle","rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_name = track
    print(track_number, track_name) """

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the rug'),
           (2, 'psycho'),
           (3, 'Mayhem')))
even = list(range(0,10,2))
odd = list(range(1,10,2))
with open("imelda.pickle","wb") as pickle_file:
           pickle.dump(imelda, pickle_file)
           pickle.dump(even, pickle_file)
           pickle.dump(odd, pickle_file)
           pickle.dump(2998345, pickle_file)
with open("imelda.pickle","rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)
           
print(imelda2)

album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_name = track
    print(track_number, track_name)
print()
for i in even_list:
           print(i)
print()
for i in odd_list:
           print(i)
print()
print(x)
