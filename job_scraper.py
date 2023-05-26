import requests
from bs4 import BeautifulSoup
import os
import subprocess

#Input from the use for job role or skill keyword

job_keyword = input("Please enter a job or skill keyword :")
job_keyword=job_keyword.replace(' ','+')

# Input for Location keyword

job_location=input("Enter the preferred location :")
job_location=job_location.replace(' ','+')

# getting the html text from URL with requests

html_file = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job_keyword}&txtLocation={job_location}&cboWorkExp1=6').text

# creating the soup object

soup = BeautifulSoup(html_file,'lxml')

job_box = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

try:
    os.remove('./jobs.txt')   # removing old file called jobs.txt
except:
    pass

with open('jobs.txt','w+') as file:  # creating an new text file called jobs.txt
    file.truncate(0) 
    file.close()  


for index,item_ in enumerate(job_box):
    job_title=item_.header.h2.a.text.strip()
    job_link=item_.header.h2.a['href']
    Company =item_.header.find('h3',class_='joblist-comp-name').text.strip()
       
    print(f'{index+1}Company: {Company}')
    print(f"Job Title: {job_title} \n")

    with open('jobs.txt','a') as file:    #writing to the file
        file.write(f'{index+1}.Company: {Company} | \nJob Title: {job_title}\nJob Link: {job_link}\n\n')


subprocess.Popen(['open', './jobs.txt'])