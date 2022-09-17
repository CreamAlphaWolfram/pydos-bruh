#comment part! put ur words here?


#if you have no idea
true=True
false=False
null=None

#part startup words
welcomeToMinecrafftSideText=["you get no copyright strike for using this",\
    "nintendo dmca sucks",\
    "getting freaky on a friday night yeah",\
    "pixelated?",\
    "not gonna be windows 1.0 replica",\
    "PHIIIILZAAAA WAAATCH OOOOOOOOOOOOOUUUUUUUUT",\
    "also try Minecraft",\
    "also try Terraria",\
    "also follow @CreamAlphaWolfram on gj",\
    "i'm just a program without any emotion",\
    "gg ez",\
    "Technoblade Never Dies!!",\
    "show me the true Alexander the Great",\
    "without different language support",\
    "better than microsoft dos\n\tfight me Bill Gates",\
    "whatever you do don't get sussy\n\tworst mistake of my life",\
    "gotta go fast",\
    "Cream got a little Pix from Pixel",\
    "beware of the man who speaks with hands",\
    "* determination",\
    "python yyds",\
    "json yyds",\
    "why don't you try out some commands for roleplays here",\
    "json supportive",\
    "sus",\
    "get your daily dose of oxygen",\
    "when the indie cross fans see the hellclown motif\n\tin the [[bendy]] [[nightmare run]],"\
    "imdead",\
    "nice cock",\
    "don't deal with the devil",\
    "knock knock?",
    "you're driving me crazy with all your notifs Cream -Fer",\
    "no bitches?",\
    "你好中国",\
    "hello America",\
    "hello Britain",\
    "terraria forums have the best roleplay ever",\
    "E X P A N D O P O W A H",\
    "not safe for waluigi",\
    "that fushcia triangle with a piece missing",\
    "krita the best digital art maker",\
    "aseprite the best pixel art maker",\
    "dumped",\
    "go touch some grass dude",\
    "wait, you thought this is cmd.exe?",\
    "this is dos.py not cmd.exe!",\
    "technolate",\
    "slaybels? how about slayballs",\
    "it doesn't matter whether it looks good,\n\tit is excellent if you had fun making it -Cream",\
    "Sonic Origins sucks -Pixel",\
    "tiky",\
    "can someone photoshop a thing from nothing?",\
    "import os",\
    "zero divided by zero",\
    "tangent 90 degrees",\
    "nothing"]

#part start
import os
import time
import getpass
import random
import subprocess
import json
from random import seed

#part customizable exception
class cException(Exception):
    lastErrorOccured=""
    errorHistory=[]
    def __init__(self, name:str, reason:str):
        self.name=name
        if name=="invalidFunctionCall":
            self.reason="invalid call to function "+reason
        elif name == "normallyWorking":
            self.reason="don't worry much!"
        else:
            self.reason=reason
        self.lastErrorOccured=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" | "+self.name+": "+self.reason
        self.errorHistory.append(self.lastErrorOccured)
    

def lastError():
    return cException.lastErrorOccured

def clearHistory():
    cException.errorHistory=[]
#available exceptions:
# invalidFunctionCall | invalid call to a function


#part version variable
v1=0
v2=3
v3=6

#part global variable
counter=0
ended=False
command=""
user=getpass.getuser()

p=str("fat")
#part cache variable
c1=""
c2=""
c3=0
c4="main"
c5=""
help=["&msg [msg] [msg-sender afterwards] : let you send a message as someone",\
    "&clear : cleaning da screen",\
    "&quit : simply quit",\
    "&random [l.limit afterwards] [u.limit afterwards] [amount afterwards] : generate random integers",\
    "&system [command] : run a command in cmd/dos",\
    "&json : do something with that shit",\
    "&credits : view the credit list",\
    "&count : count how many commands (even those invalid one) you have input"]

#part random
seed(56260647256406015)

#part input function

def space():
    print("")

def list_input(string:str,depth:int=None):
    no_id=1
    cache=[]
    typ=""
    if depth is not None:
        sysTimeStampOut()
        print("\t"+string+": current depth: "+str(depth))
    else:
        try:
            raise cException("invalidFunctionCall","list_input(string:str,depth:int)")
        except cException as err:
            sysTimeStampErr("an error has occured!: "+cException.name+": "+cException.reason)
            print("\tthat shitty author must be using the function in a wrong way...")
        return
    while typ != "eof":
        typ=sysTimeStampIn("["+str(depth)+"] list ["+str(no_id)+"] type input (\"eof\" for ending this)(bool/int/list/dict/str/float):")
        if typ=="eof":
            break
        
        if typ=="float":
            cache.append(float(sysTimeStampIn("["+str(depth)+"] list ["+str(no_id)+"] value input:")))
        elif typ=="int":
            cache.append(int(sysTimeStampIn("["+str(depth)+"] list ["+str(no_id)+"] value input:")))
        elif typ=="bool":
            cache.append(bool(sysTimeStampIn("["+str(depth)+"] list ["+str(no_id)+"] value input:")))
        elif typ=="str":
            cache.append(str(sysTimeStampIn("["+str(depth)+"] list ["+str(no_id)+"] value input:")))
        elif typ=="list":
            cache.append(list_input(string+"\\list::"+str(no_id),depth+1))
        elif typ=="dict":
            cache.append(dict_input(string+"\\list::"+str(no_id),depth+1))
        else:
            no_id-=1
            sysTimeStampErr("it seemed invalid?")
            typ=""
            continue
        #sysTimeStampIn("list ["+str(no_id)+"] value input:")
        no_id+=1
    return cache

def dict_input(string:str,depth:int=None): #needs to be fixed
    no_id=1
    cache={}
    typ=""
    if depth is not None:
        sysTimeStampOut()
        print("\t"+string+": current depth: "+str(depth))
    else:
        try:
            raise cException("invalidFunctionCall","dict_input(string:str,depth:int)")
        except cException as err:
            sysTimeStampErr("an error has occured!: "+cException.name+": "+cException.reason)
            print("\tthat shitty author must be using the function in a wrong way...")
        return
    while typ != "eof":
        typ=sysTimeStampIn("["+str(depth)+"] dict ["+str(no_id)+"] type input (\"eof\" for ending this)(bool/int/list/dict/str/float):")
        if typ=="eof":
            break
        key=str(sysTimeStampIn("["+str(depth)+"] dict ["+str(no_id)+"] keyword input:"))
        val=""
        
        if typ=="float":
            val=sysTimeStampIn("["+str(depth)+"] dict ["+str(no_id)+"] value input:")
            cache[key]=float(val)
        elif typ=="int":
            val=sysTimeStampIn("["+str(depth)+"] dict ["+str(no_id)+"] value input:")
            cache[key]=int(val)
        elif typ=="bool":
            val=sysTimeStampIn("["+str(depth)+"] dict ["+str(no_id)+"] value input:")
            cache[key]=bool(val)
        elif typ=="str":
            val=sysTimeStampIn("["+str(depth)+"] dict ["+str(no_id)+"] value input:")
            cache[key]=str(val)
        elif typ=="list":
            cache[key]=list_input(string+"\\"+key,depth+1)
        elif typ=="dict":
            cache[key]=dict_input(string+"\\"+key,depth+1)
        else:
            no_id-=1
            sysTimeStampErr("it seemed invalid?")
            typ=""
            continue
        no_id+=1
    return cache


#part json function
st_js={}

def JS_read(location:str):
    pass

def JS_add(object:str, value:any):
    if object not in st_js:
        st_js[object]=value
    else:
        sysTimeStampErr("object "+object+" is already here! use \"&json set\" next time?")
    pass

def JS_remove(object:str):
    if object in st_js:
        st_js.pop(object)
    else:
        sysTimeStampErr("object "+object+" is already vanished! did you mean other value?")
    pass

def JS_set(object:str, value:any):
    if object in st_js:
        st_js[object]=value
        # more tba
    else:
        sysTimeStampErr("object "+object+" not existing! use \"&json add\" next time?")
    pass

def JS_fetch(object:str, __fi:list=[]):
    if object in st_js:
        if object is list or object is dict:
            pass
        else:
            return st_js[object]
        # more tba
    else:
        sysTimeStampErr("object "+object+" not existing! did you mean other value?")
        return None

def JS_print():
    print(json.dumps(st_js,sort_keys=True,indent=4,separators=(',',':')))
    pass

def JS_delete():
    st_js.clear()

#part function
def intro():
    print("\nA DOS-like shit v"+str(v1)+"."+str(v2)+"."+str(v3))
    print("by Cream Alpha Wolfram")
    print(welcomeToMinecrafftSideText[random.randint(0,len(welcomeToMinecrafftSideText)-1)])
    space()
    space()
    pass

def sysTimeStampOut():
    print("[SysOut : "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"] :")
    pass

def sysTimeStampErr(str:str):
    print("[SysErr : "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"] :")
    if str:
        print("\t"+str)
    pass

def sysTimeStampIn(str:str):
    print("[SysInReq : "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"] :\n\t"+str)
    return input("["+user+" : "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"] >> ")

def sysTerminalTSOut():
    print("[TmlCmd : "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"] :")
    pass

def sysPowerShellTSOut():
    print("[TmlPSl : "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"] :")
    pass

def fact(number:int):
    if number==1 or number==0:
        return 1
    return fact(number-1)

def space():
    print("")

def showCreditList():
    space()
    space()
    sysTimeStampOut()
    print("\tpython dos by Cream Alpha Wolfram")
    print("\tpython by Guidan Van Rossum")
    print("\tjson by Douglas Crockford")
    print("\twindows dos by Microsoft Corp. (Copyrighted - All rights reserved)")
    space()
    space()
    print("PYTHON COPYRIGHT:")
    copyright()
    space()
    space()
    pass #tba


#part intro
intro()

#part iterator variable
page=0
__iterG=0
sepEnded=False

try:
    raise cException("normallyWorking","don't worry much!")
except cException as normal:
    print("Runtime Notice: %s - %s" %(normal.name, normal.reason))
    space()
    space()
except RuntimeError:
    print("Runtime Notice: runtimeError - bruh what")
    os.system("pause>nul")
    ended=True
else:
    print("Nothing have happened... how weird.")
    space()


#part dos
while not ended:
    command = input("["+user+" : "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"] >> ")
    if len(command)<1:
        continue
    if command[0]=="&":
        counter=counter+1

        #function module
        if command[1:5]=="help":
            i=0
            gg=10
            if len(help) > 10:
                page=int(sysTimeStampIn("which page? (1~"+str(int(len(help)/10)+1)+")"))
                i=0+10*(page-1)
                gg=10+10*(page-1)
            sysTimeStampOut()
            while i<len(help) and 1<gg:
                print("\t"+help[i])
                i=i+1
        elif command[1:4]=="msg":
            c2=sysTimeStampIn("&msg - please provide message sender")
            c1=command[5:len(command)]
            sysTimeStampOut()
            print("\t<"+c2+"> "+c1)
        elif command[1:6]=="clear":
            os.system("cls")
        elif command[1:5]=="quit":
            ended=True
        elif command[1:7]=="random":
            c1=sysTimeStampIn("&random - please provide lower limit")
            c2=sysTimeStampIn("&random - please provide upper limit")
            c3=int(sysTimeStampIn("&random - please provide random integer amount"))
            sysTimeStampOut()
            __iter=1
            sepEnded=False
            try:
                while __iter<=c3:
                    print("\tgetting no-"+str(__iter)+" result:",str(random.randint(int(c1),int(c2))))
                    seed(random.randint(100000000000000,42000000000000000000)+random.randint(88,1042)*int(time.time()))
                    __iter=__iter+1
            except Exception as err:
                sysTimeStampErr()
                print("\tan error has occured!: %s" %(err))
                print("\tif it is a code error, please contact with the author with specified information.")
            #this prompt doesnt have functional effect for now
        elif command[1:6]=="count":
            sysTimeStampOut()
            print("\tRunned commands: "+str(counter))
        elif command[1:7]=="system":
            sysTerminalTSOut()
            os.system(command[8:len(command)])
        elif command[1:6]=="shell":
            try:
                sysPowerShellTSOut()
                subprocess.run(args=command[7:len(command)],shell=True)
            except Exception as err:
                sysTimeStampErr()
                print("\tan error has occured!: %s" %(err))
                print("\tif it is a code error, please contact with the author with specified information.")
        elif command[1:5]=="json":
            if command[6:len(command)]=="add":
                sysTimeStampOut()
                print("\tthere are "+str(len(st_js))+" objects in json cache:")
                for x in st_js:
                    print("\t"+x)
                c1=sysTimeStampIn("&json add - please provide object name")
                c2=sysTimeStampIn("&json add - please provide object value, can be a dict too")
                c5=sysTimeStampIn("&json add - please provide the type of the obj value (int/float/dict/list/str)")
                if c5=="int":
                    JS_add(object=c1,value=int(c2))
                elif c5=="float":
                    JS_add(object=c1,value=float(c2))
                elif c5=="dict":
                    JS_add(object=c1,value=dict_input("json object\\"+c1,1))
                elif c5=="list":
                    JS_add(object=c1,value=list_input("json object\\"+c1,1))
                elif c5=="str":
                    JS_add(object=c1,value=str(c2))
                elif c5=="bool":
                    JS_add(object=c1,value=bool(c2))
                else:
                    sysTimeStampErr("invalid value in &json get")
                #JS_add(object=c1,value=c2)
            elif command[6:len(command)]=="set":
                sysTimeStampOut()
                print("\tthere are "+str(len(st_js))+" objects in json cache:")
                for x in st_js:
                    print("\t"+x)
                c1=sysTimeStampIn("&json set - please provide object name")
                c2=sysTimeStampIn("&json - please provide object value, can be a dict too")
                c5=sysTimeStampIn("&json set - please provide the type of the obj value (int/float/dict/list/str/bool)")
                if c5=="int":
                    JS_set(object=c1,value=int(c2))
                elif c5=="float":
                    JS_set(object=c1,value=float(c2))
                elif c5=="dict":
                    JS_set(object=c1,value=dict_input("json object\\"+c1,1)) #doesn't completely work yet!
                elif c5=="list":
                    JS_set(object=c1,value=list_input("json object\\"+c1,1)) #doesn't completely work yet!
                elif c5=="str":
                    JS_set(object=c1,value=str(c2))
                elif c5=="bool":
                    JS_set(object=c1,value=bool(c2))
                else:
                    sysTimeStampErr("invalid value in &json get")
                #JS_set(object=c1,value=c2)
            elif command[6:len(command)]=="fetch":
                sysTimeStampOut()
                print("\tthere are "+str(len(st_js))+" objects in json cache:")
                for x in st_js:
                    print("\t"+x)
                    sysTimeStampOut()
                print("\tgot value: "+str(JS_fetch(object=sysTimeStampIn("&json fetch - please provide object name"))))
            elif command[6:len(command)]=="clear":
                JS_delete()
            elif command[6:len(command)]=="print":
                JS_print()
            elif command[6:len(command)]=="print":
                c1=sysTimeStampIn("&json set - please provide object name")
                JS_remove(c1)
            elif command[6:len(command)]=="read":
                c1=value=sysTimeStampIn("&json read - please provide json file location")
            elif command[6:len(command)]=="help":
                sysTimeStampOut()
                print("\tavailable sep. commands in &json: help, add, set, fetch, clear, read, print")
            else:
                sysTimeStampErr("invalid command in &json, try &json help?")
        elif command[1:8]=="credits":
            showCreditList()
        #invalid command error
        else:
            sysTimeStampErr("invalid command")
            counter = counter - 1
    else:
        sysTimeStampOut()
        print("\ttry typing &help for help?")
    print("")
else:
    os.system("cls")
    sysTimeStampOut()
    print("\tend program in any key...")
    os.system('pause>nul')


# whelp


