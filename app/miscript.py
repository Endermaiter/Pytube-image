from pytube import YouTube

url = input("Introduce la url de un video:")

video = YouTube(url)

# Titulo
print("Titulo: ", video.title)
# Visualizaciones
print("Views: ", video.views)
# Duracion
print("Duracion: ", video.length, " segundos")
# Descripcion
print("Descripcion: " + video.description)
# Data
print("Rating: ", video.rating)

if __name__ == '__main__':
    print("Execute Successful")
