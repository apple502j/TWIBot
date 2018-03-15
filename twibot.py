import mw_api_client as mwc
from parseMWT import parseMWT,writeMWT,WrongPageNameError
import re
import getpass
from time import sleep
from random import randint

def yesno(s):
    if s.lower()=="yes" or s.lower()=="y" or s=="1" or s.lower()=="true":
        return True
    else:
        return False

def firstup(txt):
    arr=list(txt)
    arr[0] = arr[0].upper()
    return "".join(arr)
    
INTERWIKI=['de','ja','nl','hu','id','ru','fr'] # Do not include "get" and "set" wiki.
WIKI_GET="https://en.scratch-wiki.info/w/api.php" # Where the bot gets the info of interwiki
WIKI_SET="https://test.scratch-wiki.info/w/api.php" # Where the bot puts the interwiki

USERNAME="Someone" # Change it before using!
PASSWORD=getpass.getpass() # Always asks

wGet=mwc.Wiki(WIKI_GET,"Apple_Bot (Only read!) v1.0 with python3/requests/mw-api-client")
wSet=mwc.Wiki(WIKI_SET,"Apple_Bot v1.0 with python3/requests/mw-api-client")
wSet.login(USERNAME,PASSWORD)

for page in wSet.category("Translate").categorymembers():
    contents=page.read()
    print("Working:"+page.title)
    try:
        tmp=parseMWT(contents.replace("\n",""))
        if tmp["name"].lower() != "translate":
            continue
        english=wGet.page(tmp["data"]["En"]).read()
        for lang in INTERWIKI:
            exist=re.search("\[\[" + lang + ":.*\]\]",english)
            if exist:
                pagename=exist.string[exist.start():exist.end()].replace("[["+lang+":","").replace("]]","")
                tmp["data"][firstup(lang)]=pagename
        newtmp=writeMWT(tmp,putNewline=True)
        if newtmp != contents:
            print("Interwiki Change:\nbefore\n{0}\nafter\n{1}\n".format(contents,newtmp))
            accept=yesno(input("Accept? (yes/no) >"))
            if accept:
                page.edit(newtmp,"Change Interwiki")
                print("Done!")
                sleep(randint(60,90)/10)
        else:
            print("There's no new interwiki.")
    except WrongPageNameError:
        pass
        
