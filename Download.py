import subprocess
import sys

download_directory = ""

def read_artist_links():
    with open("artists.txt", "r") as file:
        artist_links = file.read().split(",")
    return [link for link in artist_links if link.strip()]  # Remove any empty links

def download_songs(links):
    for link in links:
        output_format = "{}/%(title)s.%(ext)s".format(download_directory)
        subprocess.call(["yt-dlp", "-x", "--audio-format", "mp3", "--embed-metadata", link, "-o", output_format])

def main():
    global download_directory
    download_directory = sys.argv[1] if len(sys.argv) > 1 else ""
    artist_links = read_artist_links()
    if artist_links:
        download_songs(artist_links)
    else:
        print("No artist links found in artists.txt")

if __name__ == "__main__":
    main()

