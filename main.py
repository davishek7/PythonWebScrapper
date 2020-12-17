from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content,'lxml')
    course_cards=soup.find_all('div',class_='card')  #the '_' after class keyword used to distinguise python and html class,as class is alreday a built in keyword in python.
    for course in course_cards:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')