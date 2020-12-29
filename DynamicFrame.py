# First, you should install flickrapi
# pip install flickrapi

import flickrapi
import urllib.request
from PIL import Image
import pygame as pg 
from datetime import datetime
import random
import time 
import os

integers_list = ["1","2","3","4","5","6","7","8","9","0"]
NUM_IMAGES = 0

# Flickr api access key 
flickr=flickrapi.FlickrAPI('TOKEN_HERE', 'TOKEN_HERE', cache=True)

def getImage(searchquery):
    global NUM_IMAGES
    NUM_IMAGES = 0
    keyword = searchquery

    photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,           # may be you can try different numbers..
                     sort='relevance')

    urls = []
    for i, photo in enumerate(photos):
        print (i)
    
        url = photo.get('url_c')
        urls.append(url)
    
        # get 50 urls
        if i > 50:
            break

    print (urls)

   
    factor = 0
    for file in os.listdir():
        if file.endswith('.jpg'):
            os.remove(file)

    for i in range(50):
        try:
            print(i)
            urllib.request.urlretrieve(urls[i], str((i+1)-factor)+'.jpg')
            image = Image.open(str((i+1)-factor)+'.jpg') 
            image = image.resize((500, 500), Image.ANTIALIAS)
            image.save(str((i+1)-factor)+'.jpg')
            
            
        except:
            print("Error")
            factor += 1 
            print(factor)
    for file in os.listdir():
        if file.endswith('.jpg'):
            NUM_IMAGES += 1
    return factor



def startupSequence():
    characters = 0 
    screen_width = 800
    screen_height = 480
    screen = pg.display.set_mode((screen_width, screen_height)) #pg.NOFRAME
    font = pg.font.Font("slkscr.ttf", 20)
    clock = pg.time.Clock()
    input_box = pg.Rect(290, 200, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('red')
    color = color_inactive
    active = False
    text = ''
    done = False
    done2 = False
    done3 = False 



    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                done2 = True
                done3 = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        hourpick = text 
                        text = ''
                        done = True
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                        if characters != 0:
                            characters += -1
                            print(characters)
                    else:
                        if event.unicode in integers_list and characters != 2:
                            text += event.unicode
                            characters += 1
                            print(characters)
                            print(text)
    
        screen.fill((0, 0, 0))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        textsurface = font.render('Enter hour to change', True, (113, 238, 184))
        screen.blit(textsurface,((263),175))

        pg.display.flip()
        clock.tick(30)

    characters = 0 
    while not done2:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done2 = True
                done3 = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        minutepick = text 
                        text = ''
                        done2 = True
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                        if characters != 0:
                            characters += -1
                            print(characters)
                    else:
                        if event.unicode in integers_list and characters != 2:
                            text += event.unicode
                            characters += 1
                            print(characters)
                            print(text)

        
        screen.fill((0, 0, 0))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        textsurface = font.render('Enter minute to change', True, (113, 238, 184))
        screen.blit(textsurface,((263),175))

        pg.display.flip()
        clock.tick(30)

    while not done3:
        for event in pg.event.get():
            failed = getImage("beach")
            done3 = True
        
        
        screen.fill((0, 0, 0))
        textsurface = font.render("Fetching images...", True, (113, 238, 184))
        screen.blit(textsurface,((270),240))
        pg.display.flip()
        clock.tick(30)
        
    
    return hourpick, minutepick, failed 


def displayImage(numberpick):
    hourpick, minutepick, failed= startupSequence()
    print('Hourpick is', hourpick, "minute pick is", minutepick)
    #failed = getImage("beach")
    screen_width = 800
    screen_height = 480
    screen = pg.display.set_mode((screen_width,screen_height))
    font = pg.font.Font("slkscr.ttf", 20)
    clock = pg.time.Clock()
    input_box = pg.Rect(290, 440, 140, 32)
    color_inactive = pg.Color('white')
    color_active = pg.Color('red')
    color = color_inactive
    active = False
    text = ''
    done = False
    count = 0 
    while not done:
        now = datetime.now()
        hour= now.hour
        minute = now.minute
        second = now.second
        if(hour == int(hourpick) and minute == int(minutepick)):
            print("Here")
            randvalue = random.randint(1,(50-failed))
            randvalue = str(randvalue)+".jpg"
            numberpick = randvalue
            time.sleep(60)
        color = color_active if active else color_inactive
        #image = pg.image.load("9.jpg")
        #image = pg.transform.scale(image,(400,200))
        try:
            image = Image.open(numberpick)
            image = image.resize((800,480),Image.ANTIALIAS)
            image.save(numberpick)
            image = pg.image.load(numberpick)
        except FileNotFoundError:
            if count == 0:
                print("Error loading photo" + numberpick)
                count += 1 
            pass
        #screen.fill((30, 30, 30))
        #Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        #pg.display.flip()
        clock.tick(30)
        screen.blit(image,(0,0))
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        pg.display.flip()
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                done = True
            
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        searchterm = text
                        print(text)
                        #screen.fill((0, 0, 0))
                        textsurface = font.render("Fetching images...", True, (0, 0, 0))
                        screen.blit(textsurface,((270),240))
                        pg.display.flip()
                        clock.tick(30)
                        failed = getImage(searchterm)
                        text = ''
                        numberpick = "1.jpg"
                        
                        
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                
                if event.key == pg.K_RIGHT:
                    if numberpick.strip(".jpg") != str(NUM_IMAGES):
                        print(NUM_IMAGES)
                        numberpick = numberpick.strip(".jpg")
                        numberpick = int(numberpick) + 1
                        numberpick = str(numberpick)+".jpg"
                        print (numberpick)
                        count = 0
                elif event.key == pg.K_LEFT:
                    if numberpick.strip(".jpg") != "1":
                        numberpick = numberpick.strip(".jpg")
                        numberpick = int(numberpick) - 1
                        numberpick = str(numberpick)+".jpg"
                        print (numberpick)
                        count = 0
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                




#getImage("Blue")
pg.init()
pg.display.set_caption('Dynamic Frame')
#startupSequence()
displayImage("1.jpg")
pg.quit()