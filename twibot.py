import mw_api_client as mwc
from parseMWT import parseMWT,writeMWT
import re
import getpass
from time import sleep
from random import randint

def yesno(s):
    if s.lower()=="yes" or s.lower()=="y" or s=="1" or s.lower()=="true":
        return True
    else:
        return False

INTERWIKI=['de','ja','nl','hu','id','ru','fr'] # Do not include "get" and "set" wiki.
WIKI_GET="https://en.scratch-wiki.info/w/api.php" # Where the bot gets the info of interwiki
WIKI_SET="https://test.scratch-wiki.info/w/api.php" # Where the bot puts the interwiki

USERNAME="Someone" # Change it before using!
PASSWORD=getpass.getpass() # Always asks

wGet=mwc.Wiki(WIKI_GET,"Apple_Bot (Only read!) v1.0 with python3/requests/mw-api-client")
wSet=mwc.Wiki(WIKI_SET,"Apple_Bot v1.0 with python3/requests/mw-api-client")
wSet.login(USERNAME,PASSWORD)

for page in translate=wSet.category("Translate").categorymembers()
    contents=page.read()
    try:
        tmp=parseMWT(contents)
        if tmp["name"].lower() != "translate":
            continue
        english=wGet.page(tmp["data"]["en"]).read()
        for lang in INTERWIKI:
            exist=re.search("\[\[" + lang + "\:.{1,255}\]\]",english)
            if exist:
                pagename=exist.replace("[["+lang+":","").replace("]]","")
                tmp["data"][lang]=pagename
        newtmp=writeMWT(tmp,putNewline=True)
        print("Interwiki Change:\nbefore\n{0}\nafter{1}\n".format(contents,newtmp))
        accept=yesno(input("Accept? (yes/no) >"))
        if accept:
            page.edit(newtmp,"Change Interwiki (bot)")
            print("Done!")
            sleep(randint(60,90)/10)
    except WrongPageNameError:
        pass
        
