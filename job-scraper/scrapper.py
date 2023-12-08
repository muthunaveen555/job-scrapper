from bs4 import BeautifulSoup
import requests

def get_job_content(url):
    """This function will get the url as an input and return the html source

    Keyword arguments:
    argument -- url
    Return: html page of the given url
    """

    job_page_content = requests.get(url).content
    return job_page_content

def print_job_content(content):
    """This function will print the opening jobs from the given html page from the job opening website
    Keyword arguments:
    argument -- content
    Return: none
    """

    bs_object = BeautifulSoup(content, features="html.parser")
    div = bs_object.find_all("div", {"class": "posting"})
    for post in div:
        print(post.find("a", {"class": "posting-title"}).text)

if __name__ == "__main__":
    url = "https://jobs.lever.co/imbue/"
    html_content = get_job_content(url)
    print_job_content(html_content)
