import subprocess
import os

def check_existing_links():
    existing_links = set()
    if os.path.exists("artists.txt"):
        with open("artists.txt", "r") as file:
            existing_links.update(file.read().split(","))
    return existing_links

def main():
    existing_links = check_existing_links()

    download_dir = input("Enter the download directory (press Enter to skip): ")

    while True:
        artist_link = input("Enter the artist's YouTube Music playlist link (or 'n' to stop adding): ")

        if artist_link.lower() == 'n':
            add_more = input("Do you want to add more artists? n - end the script d - start download (y/n/d): ")
            if add_more.lower() == 'n':
                break
            elif add_more.lower() == 'd':
                subprocess.run(["python", "Download.py", download_dir])
            continue

        # Check if it's a valid YouTube Music playlist link
        if not artist_link.startswith("https://music.youtube.com/playlist"):
            print("Invalid link. Please provide a valid YouTube Music playlist link.")
            continue

        if artist_link in existing_links:
            print("This link has already been added.")
        else:
            existing_links.add(artist_link)
            with open("artists.txt", "a") as file:
                file.write(artist_link + ",")
                print("Artist's songs link added to artists.txt")

    if download_dir:
        with open("Download.py", "r") as file:
            script_content = file.readlines()

        updated_script_content = []
        for line in script_content:
            if line.startswith("download_directory"):
                updated_script_content.append(f'download_directory = "{download_dir}"\n')
            else:
                updated_script_content.append(line)

        with open("Download.py", "w") as file:
            file.writelines(updated_script_content)

if __name__ == "__main__":
    main()
