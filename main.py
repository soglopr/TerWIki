import wikipedia
import re
import os
import config
from config import *
import colors
from colors import c, b, s

clear = lambda: os.system('clear')

def TerWiki():
    clear()
    print(s.bold + c.green + "TerWiki" + c.endc)

TerWiki()

wikipedia.set_lang(config.lang)

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ' '
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        wikitext2 = wikitext2.replace(" .", ".")
        wikitext2 = wikitext2.replace(" ,", ",")
        wikitext2 = wikitext2.replace(" ;", ";")
        wikitext2 = wikitext2.replace("  -", " -")
        wikitext2 = wikitext2.replace(" :", ":")
        wikitext2 = wikitext2.replace("  (", " (")
        wikitext2 = wikitext2.replace("  —", " —")
        return wikitext2
    except Exception as e:
        print(e)
    
while True:
    try:
        print(s.bold)
        what = input(c.yellow + f"[{config.language.get(config.lang).get('input')}]" + c.endc + " >> ")
        if what == "-help" or what == "-h":
            print(s.bold)
            print(c.yellow + f"[{config.language.get(config.lang).get('help2')}]\n" + c.endc + f"{config.language.get(config.lang).get('help')}")
        elif what == "-exit" or what == "-e":
            print()
            exit = input(s.bold + f"{config.language.get(config.lang).get('exit')} " + c.endc)
            if exit == "Д" or exit == "д" or exit == "Y" or exit == "y":
                break
            else:
                TerWiki()
                print()
                print(c.lgreen + f"{config.language.get(config.lang).get('exit_no')}" + c.endc)
        else:
            TerWiki()
            print()
            print(c.blue + "[+]" + c.endc + getwiki(what))
    except Exception as e:
        if str(e) == str('can only concatenate str (not "NoneType") to str'):
            TerWiki()
            print()
            print(s.bold + c.orange + f"[x]" + c.endc + f" {config.language.get(config.lang).get('error2')}")


