# 2023-02-10 ebb: This is a simple scraper that only pulls text from certain elements
# out of one page and outputs that into a single text file.
import bs4
import requests
import os

# ebb: This variable stores the website address that you want to scrape.
# archive_url = "https://www.simplyscripts.com/c.html"
# archive_url = "https://newtfire.org/courses/"
archive_url = input("http://www.textfiles.com/humor/101nos.txt")
def get_linkContents():
    # create response object
    r = requests.get(archive_url)
    print(f"{r=}")
    # create beautiful-soup object
    soup = bs4.BeautifulSoup(r.content, 'html.parser')

    # find all link text inside <a> elements and send it to the
    # download_toFile function to be output to a new file
    linkText = []
    for item in soup.findAll('a'):
        print(f"{item.text}")
        # item.text returns just the text inside the element.
        # For this, we just want to output ONE file with all the text we scraped
        # from this page, so let's accumulate all the element text in a nice Python list.
        linkText.append(item.text)
    print(linkText)
    download_toFile(linkText)
    return

def download_toFile(linkText):
    # We are just planning to output one file only here.
    file_name = "outputLinkText.txt"
    print("Downloading file: " + file_name)
    working_dir = os.getcwd()
    file_deposit = os.path.join(working_dir, file_name)
    print(file_deposit)
    # write to the file:
    with open(file_deposit, 'w') as f:
    # ebb: We just use 'w' here to write out the text we pulled, and not 'wb' which would output
    # a whole "binary object". We used the 'wb' argument to deposit a scraped document.
    # but here we have simply scraped a list of strings.
        for item in linkText:
            f.write(item + '\n')
            # the '\n' adds a return character so each piece of text goes on its own line.
            print("Downloaded " + item)
    return
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]

# ebb: Basically the line below initiates the whole program, sets it in motion.
# On the line if __name__ == "__main__": ,
# see: https://medium.com/@j.yanming/debugging-from-main-to-main-in-python-fe2a9784b36
if __name__ == "__main__":

    # getting all links to files
    get_links = get_linkContents()