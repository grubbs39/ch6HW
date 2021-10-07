from Artist import Artist
from Artwork import Artwork

print("input the artist name: ")
user_artist_name = input()
print("input their birth year: ")
user_birth_year = int(input())
print("input their death year. If not dead put -1: ")
user_death_year = int(input())
print("input the name of the artwork: ")
user_title = input()
print("input the year it was created: ")
user_year_created = int(input())

user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

new_artwork = Artwork(user_title, user_year_created, user_artist)

new_artwork.print_info()
