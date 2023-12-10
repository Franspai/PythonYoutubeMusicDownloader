import subprocess
import os

download_directory = "/media/root/KingstonSSD/Music"

def read_artist_links():
    with open("artists.txt", "r") as file:
        artist_links = file.read().split(",")
    return [link for link in artist_links if link.strip()]  # Remove any empty links

def download_songs(links):
    for link in links:
        # Use yt-dlp to download songs based on the links
        subprocess.call(["yt-dlp", "-o", f"{download_directory}%(title)s.%(ext)s", "-x", "--audio-format", "mp3", "--embed-metadata", link])

def main():
    global download_directory
    download_dir = input("Enter the download directory: ")

    if os.path.isdir(download_dir):
        if not download_dir.endswith("/"):
            download_dir += "/"  # Ensure the directory path ends with a slash
        download_directory = download_dir

    artist_links = read_artist_links()
    if artist_links:
        download_songs(artist_links)
    else:
        print("No artist links found in artists.txt")

if __name__ == "__main__":
    main()
