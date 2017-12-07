# -*- coding: utf-8 -*-

import TOBY
from TOBY.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re


cl = TOBY.LINE()
cl.login(qr=True)
cl.loginResult()

ki = TOBY.LINE()
ki.login(qr=True)
ki.loginResult()

kk = TOBY.LINE()
kk.login(qr=True)
kk.loginResult()

kc = TOBY.LINE()
kc.login(qr=True)
kc.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" Dragon BOT
]|I{•----» •㉿Continental™ «----•}I|[
=====================================
[Administrator by]
• [BLVCK DRAGON]™
• CNN/Bot Division 
• BD.CBOT-188

-㉿-  CommandMember -㉿-
-------------------------------------------
-㉿-  Say = Mengikuti Yang DiKatakan
-㉿-  Gcreator = Check Creator Grup

-㉿-  Command Creator -㉿-
-------------------------------------------
-㉿-  Admin add @ = Menambahkan Admin
-㉿-  Admin remove @ = Menghapus Admin
-㉿-  Adminlist = Cek Admin

-㉿- Command Admin -㉿-
-------------------------------------------
-㉿-  Id
-㉿-  Mid
-㉿-  Mid @
-㉿-  Me
-㉿-  K on/off
-㉿-  Gcancel:
-㉿-  Leave on/off
-㉿-  Add on/off
-㉿-  Share on/off
-㉿-  Jam on/off
-㉿-  Up 
-㉿-  Urloff
-㉿-  Urlon
-㉿-  Ginfo
-㉿-  Cancel
-㉿-  Gn
-㉿-  Out
-㉿-  Invite
-㉿-  Cn
-㉿-  Gift
-㉿-  Respon
-㉿-  Tagall
-㉿-  All join
-㉿-  Bye all
-㉿-  Glist
-㉿-  Spam
-㉿-  Check > Read
-㉿-  Steal + Mid
-㉿-  Steal @

-㉿-  Command Clone -㉿-
-------------------------------------------
-㉿-  Clone on/off
-㉿-  Clone @
-㉿-  Clone:add: @
-㉿-  Clone:del: @
-㉿-  ListTarget

-㉿-  Command Penting  -㉿-
-------------------------------------------
-㉿-  Guest On/Off
-㉿-  Mad On/Off
-㉿-  Protect On/Off
-㉿-  Ban @ 
-㉿-  Unban @
-㉿-  Kill Ban
-㉿-  Kill @
-㉿-  Nk
-㉿-  Vk @
-㉿-  Attack

============================================
Respect with our people then 
they will respect to you too, 
Enjoy and relax sir!

[Author By]
   - B L V C K  H I T T E R -
      { •㉿Continental™• }          
"""

KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["u813e54635fa8ca8c016090e933582652"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"Owner : http://line.me/ti/p/~antonlou",
    "lang":"JP",
    "comment":"Owner : http://line.me/ti/p/~antonlou",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectguest":False,
    "Protectcancel":False,
    "ProtectionOn":False,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

	if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                cl.updateGroup(X)
                Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u813e54635fa8ca8c016090e933582652":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Already on blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"I have no idea About this Apologize ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"This contact has been erase from the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        ki.sendText(msg.to,"This contact has been erase from the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        kk.sendText(msg.to,"This contact has been erase from the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        kc.sendText(msg.to,"This contact has been erase from the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"This contact is not at the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        ki.sendText(msg.to,"This contact is not at the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        kk.sendText(msg.to,"This contact is not at the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        kc.sendText(msg.to,"This contact is not at the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already on blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        ki.sendText(msg.to,"Already on blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        kk.sendText(msg.to,"Already on blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        kc.sendText(msg.to,"Already on blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"This contact has been added on blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        ki.sendText(msg.to,"This contact has been added on blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        kk.sendText(msg.to,"This contact has been added on blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        kc.sendText(msg.to,"This contact has been added on blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"This contact has been erase from the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        ki.sendText(msg.to,"This contact has been erase from the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        kk.sendText(msg.to,"This contact has been erase from the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        kc.sendText(msg.to,"This contact has been erase from the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"This contact is not at the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        ki.sendText(msg.to,"This contact is not at the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        kk.sendText(msg.to,"This contact is not at the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        kc.sendText(msg.to,"This contact is not at the blacklist by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"Success for change name group sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ.")
	    elif ("Cv1 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv1 gn ","")
						ki.updateGroup(X)
					else:
						ki.sendText(msg.to,"Success for change name group sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ.")
            elif ("Cv2 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv2 gn ","")
						kk.updateGroup(X)
					else:
						kk.sendText(msg.to,"Success for change name group sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ.")
            elif ("Cv3 gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Cv3 gn ","")
						kc.updateGroup(X)
					else:
						kc.sendText(msg.to,"Success for change name group sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ.")
            elif "Kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Kick ","")
					cl.kickoutFromGroup(msg.to,[midd])
	    elif "Cv1 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv1 kick ","")
					ki.kickoutFromGroup(msg.to,[midd])
            elif "Cv2 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv2 kick ","")
					kk.kickoutFromGroup(msg.to,[midd])
            elif "Cv3 kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv3 kick ","")
					kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Invite ","")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])
            elif "Cv1 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv1 invite ","")
					ki.findAndAddContactsByMid(midd)
					ki.inviteIntoGroup(msg.to,[midd])
            elif "Cv2 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv2 invite ","")
					kk.findAndAddContactsByMid(midd)
					kk.inviteIntoGroup(msg.to,[midd])
            elif "Cv3 invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Cv3 invite ","")
					kc.findAndAddContactsByMid(midd)
					kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': mid}
					cl.sendMessage(msg)
            elif msg.text in ["Cv1"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Amid}
					ki.sendMessage(msg)
            elif msg.text in ["Cv2"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Bmid}
					kk.sendMessage(msg)
            elif msg.text in ["gift","Gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '5'}
					msg.text = None
					cl.sendMessage(msg)
            elif msg.text in ["Cv1 Gift","Cv1 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '6'}
					msg.text = None
					ki.sendMessage(msg)
            elif msg.text in ["Cv2 Gift","Cv2 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '8'}
					msg.text = None
					kk.sendMessage(msg)
            elif msg.text in ["Cv3 Gift","Cv3 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '10'}
					msg.text = None
					kc.sendMessage(msg)
            elif msg.text in ["All Gift","All gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					kk.sendMessage(msg)
					kc.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							cl.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								ki.sendText(msg.to,"Success cancel by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                            					ki2.sendText(msg.to,"All pending members has been cancelled by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
								ki3.sendText(msg.to,"Writing to next Protocol sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
							else:
								cl.sendText(msg.to,"Cancel done ─অই͜⟦㉿ Континентальный ™ ⟧ ೋa")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"All invitation has been cancelled by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
						else:
							cl.sendText(msg.to,"Thanks, sir!")
            elif msg.text in ["Cv cancel","Bot cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						G = k3.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							k3.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								k3.sendText(msg.to,"All invitation has been cancelled by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
							else:
								k3.sendText(msg.to,"Writing to next Protocol sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
					else:
						if wait["lang"] == "JP":
							k3.sendText(msg.to,"All invitation has been cancelled by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
						else:
							k3.sendText(msg.to,"Thanks, sir!")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on","Urlon"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Url opened by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
						else:
							cl.sendText(msg.to,"Already opened by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 ourl","Cv1 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Url opened by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
						else:
							ki.sendText(msg.to,"Already opened by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 ourl","Cv2 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = False
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Url opened by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
						else:
							kk.sendText(msg.to,"Already opened by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 ourl","Cv3 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Url opened by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
						else:
							kc.sendText(msg.to,"Already opened by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off","Urloff"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Url closed by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
						else:
							cl.sendText(msg.to,"Already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 curl","Cv1 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = ki.getGroup(msg.to)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Url closed by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
						else:
							ki.sendText(msg.to,"Already closed by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
					else:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Can not be used outside the group")
						else:
							ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 curl","Cv2 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = True
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Url closed by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
						else:
							kk.sendText(msg.to,"Already closed by ─অই͜⟦㉿ Континентальный ™ ⟧ ")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 curl","Cv3 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = True
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Url closed by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
						else:
							kc.sendText(msg.to,"Already closed by ─অই͜⟦㉿ Континентальный ™ ⟧ ")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
					ki.sendText(msg.to,Amid)
					kk.sendText(msg.to,Bmid)
					kc.sendText(msg.to,Cmid)
            elif "Mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
            elif "Cv1 mid" == msg.text:
				if msg.from_ in admin:
					ki.sendText(msg.to,Amid)
            elif "Cv2 mid" == msg.text:
				if msg.from_ in admin:
					kk.sendText(msg.to,Bmid)
            elif "Cv3 mid" == msg.text:
				if msg.from_ in admin:
					kc.sendText(msg.to,Cmid)
            elif msg.text in ["Wkwkwk"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["You"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Haduh"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Please"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Wc"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Curi PP"]:
				if msg.from_ in admin:
					tl_text = msg.text.replace("TL","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cn ","")
					if len(string.decode('utf-8')) <= 20:
						profile = cl.getProfile()
						profile.displayName = string
						cl.updateProfile(profile)
						cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cv1 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = ki.getProfile()
						profile_B.displayName = string
						ki.updateProfile(profile_B)
						ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cv2 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kk.getProfile()
						profile_B.displayName = string
						kk.updateProfile(profile_B)
						kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
				if msg.from_ in admin:
					mmid = msg.text.replace("Mc ","")
					msg.contentType = 13
					msg.contentMetadata = {"mid":mmid}
					cl.sendMessage(msg)
            elif msg.text in ["Guest On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"Block invite already turned on by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"Block invite already turned on by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
            elif msg.text in ["Guest Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"Block invite already turned off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"Block invite already turned off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"URL already protected by the komite\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"URL already protected by the komite\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"Protect URL has been disabled by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"Protect URL has been disabled by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
            elif msg.text in ["K on","Contact on"]:
				if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already on")
						else:
							cl.sendText(msg.to,"Contact has been turned on by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already on")
						else:
							cl.sendText(msg.to,"Contact has been turned on by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
            elif msg.text in ["K off","Contact off"]:
				if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already off")
						else:
							cl.sendText(msg.to,"Contact has been turned off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already off")
						else:
							cl.sendText(msg.to,"Contact has been turned off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
            elif msg.text in ["Join on","Auto join:on"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already on")
						else:
							cl.sendText(msg.to,"Auto join already activated by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already on")
						else:
							cl.sendText(msg.to,"Auto join already activated by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
            elif msg.text in ["Join off","Auto join:off"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already off")
						else:
							cl.sendText(msg.to,"Auto join already disabled by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already off")
						else:
							cl.sendText(msg.to,"Auto join already disabled by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
            elif msg.text in ["Gcancel:on"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"All invitations have been refused by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    kk.sendText(msg.to,"Now We can doing bussines here sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    ki.sendText(msg.to,"Can you give me next protocol sir? ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    kk.sendText(msg.to,"Enjoy and Relax sir! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")

            elif msg.text in ["Gcancel:off"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.acceptGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"All invitations have been allowed by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    kk.sendText(msg.to,"Maybe we can show, how to hold the spoon sir! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    ki.sendText(msg.to,"Can you give me next protocol sir? ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
		    kk.sendText(msg.to,"Enjoy and Relax sir! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
			
            elif msg.text in ["Leave on","Auto leave:on"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already on")
						else:
							cl.sendText(msg.to,"Already opened by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"Already opened by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
            elif msg.text in ["Leave off","Auto leave:off"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already off")
						else:
							cl.sendText(msg.to,"Already closed by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"Already closed by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
            elif msg.text in ["Share on","Share on"]:
				if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already on")
						else:
							cl.sendText(msg.to,"Already turned on by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"Already turned on by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
            elif msg.text in ["Share off","Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already off")
						else:
							cl.sendText(msg.to,"Already turned off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"Already turned off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
            elif "album merit " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album merit ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"Ã§â€ºÂ¸Ã¥â„1¤7 Å’Ã¦Â²Â¡Ã¥Å“Â¨Ã£â‚¬â€„1¤7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "Ã¤Â»Â¥Ã¤Â¸â€¹Ã¦ËœÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡â„1¤7žÃ§â„1¤7ºÂ¸Ã¥â„1¤7 Å„1¤7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
						cl.sendText(msg.to,mg)
            elif "album " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"Ã§â€ºÂ¸Ã¥â„1¤7 Å’Ã¦Â²Â¡Ã¥Å“Â¨Ã£â‚¬â€„1¤7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "Ã¤Â»Â¥Ã¤Â¸â€¹Ã¦ËœÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡â„1¤7žÃ§â„1¤7ºÂ¸Ã¥â„1¤7 Å„1¤7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album remove ","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Deleted albums")
					else:
						cl.sendText(msg.to,str(i) + "Ã¥Ë† Ã©â„¢Â¤Ã¤Âºâ„1¤7 Ã¤Âºâ„1¤7¹Ã§Å¡â„1¤7žÃ§â„1¤7ºÂ¸Ã¥â„1¤7 Å’Ã£â‚¬â€„1¤7")
            elif msg.text in ["Group id","group¨id"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
					cl.sendText(msg.to,h)
            elif msg.text in ["Add on","Auto add:on"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already on")
						else:
							cl.sendText(msg.to,"Already turned on by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"Already turned on by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
            elif msg.text in ["Add off","Auto add:off"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already off")
						else:
							cl.sendText(msg.to,"Already turned off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"Already turned off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
            elif "Message change: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message change: ","")
					cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message changed")
					else:
						cl.sendText(msg.to,"doneÃ£â‚¬â„1¤7„1¤7")
            elif msg.text in ["Message"]:
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						cl.sendText(msg.to,"The automatic appending information is set as followsÃ£â‚¬â„1¤7š\n\n" + wait["message"])
            elif "Comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Add comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["Comment on","Comment:on"]:
				if msg.from_ in admin:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"Already turned on by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"Already turned on by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
            elif msg.text in ["Comment off","Comment off"]:
				if msg.from_ in admin:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Already turned off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
						else:
							cl.sendText(msg.to,"Already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"Already turned off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
            elif msg.text in ["Comment"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							cl.updateGroup(x)
						gurl = cl.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							ki.updateGroup(x)
						gurl = ki.reissueGroupTicket(msg.to)
						ki.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kk.updateGroup(x)
						gurl = kk.reissueGroupTicket(msg.to)
						kk.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kc.updateGroup(x)
						gurl = kc.reissueGroupTicket(msg.to)
						kc.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
				if msg.from_ in admin:
					wait["wblack"] = True
					cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
				if msg.from_ in admin:
					wait["dblack"] = True
					cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
				if msg.from_ in admin:
					if wait["commentBlack"] == {}:
						cl.sendText(msg.to,"confirmed")
					else:
						cl.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						cl.sendText(msg.to,"Already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
				if msg.from_ in admin:
					if wait["clock"] == False:
						cl.sendText(msg.to,"Already off")
					else:
						wait["clock"] = False
						cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
				if msg.from_ in admin:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						cl.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"Updated")
					else:
						cl.sendText(msg.to,"Please turn on the name clock")


            elif msg.text == "Check":
                    cl.sendText(msg.to, "Check sider"),
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「Check」you can send ♪ read point will be created ♪")
#-----------------------------------------------

#-----------------------------------------------

            elif msg.text in ["All join"]:
				if msg.from_ in admin:
                       	 		G = cl.getGroup(msg.to)
                        		ginfo = cl.getGroup(msg.to)
                        		G.preventJoinByTicket = False
                        		cl.updateGroup(G)
                        		invsend = 0
                        		Ticket = cl.reissueGroupTicket(msg.to)
                        		ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        		kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        		kc.acceptGroupInvitationByTicket(msg.to,Ticket)
					ki.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "Warmest greeting from continental, Evrything have a price Sir ! Lets agree to disagree. Evrything its just for a good bussines.\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
					kk.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "No Bussines on continental Ground. DOG BOARDNING AVAILABLE.\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
					kc.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "Perhaps Bourbon will make your good and Relax sir! .\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        		print "hitter ready"
                        		G.preventJoinByTicket = True
					cl.updateGroup(G)
            elif msg.text in ["Cv1 join"]:
				if msg.from_ in admin:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = False
					cl.updateGroup(X)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ti)
					G = kk.getGroup(msg.to)
					G.preventJoinByTicket = True
					ki.updateGroup(G)
					Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Cv2 join"]:
				if msg.from_ in admin:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = False
					cl.updateGroup(X)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					kk.acceptGroupInvitationByTicket(msg.to,Ti)
					G = ki.getGroup(msg.to)
					G.preventJoinByTicket = True
					kk.updateGroup(G)
					Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Cv3 join"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							print "kicker ok"
							G.preventJoinByTicket = True
							kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Bye all"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
 		        				ki.sendText(msg.to,"See you again soon, we always watching on you. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ \n " + "*" + str(ginfo.name) + "*")
                        				ki.leaveGroup(msg.to)
                        				kk.sendText(msg.to,"I hope next time you have a lucky day like on this day sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ \n" + "*" + str(ginfo.name) + "*")
                        				kk.leaveGroup(msg.to)
                        				kc.sendText(msg.to,"Respect with our people and then they will respect to you too. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ \n " + "*" + str(ginfo.name) + "*")
                        				kc.leaveGroup(msg.to)
							cl.sendText(msg.to,"Thanks sir")
						except:
							pass
            elif msg.text in ["Bye 1"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 2"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
						except:
							pass
				elif msg.text in ["Cv1 @bye"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Cv2 @bye"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kk.leaveGroup(msg.to)
						except:
							pass
				elif msg.text in ["Cv3 @bye"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kc.leaveGroup(msg.to)
						except:
							pass
#-----------------------------------------------
				elif msg.text in ["Tagall"]:
					if msg.from_ in admin:
						group = cl.getGroup(msg.to)
						nama = [contact.mid for contact in group.members]
						cb = ""
						cb2 = ""
						strt = int(0)
						akh = int(0)
						for md in nama:
								akh = akh + int(5)	
								cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

								strt = strt + int(6)
								akh = akh + 1
								cb2 += "@nrik\n"

						cb = (cb[:int(len(cb)-1)])
						msg.contentType = 0
						msg.text = cb2
						msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

						try:
							kk.sendMessage(msg)
						except Exception as error:
							print error							
#-----------------------------------------------
            elif msg.text in ["Kill"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kk.sendText(msg.to,"Killed by [BLVCK DRVGON]™")
							kc.sendText(msg.to,"Killed by [BLVCK DRVGON]™")
							return
						for jj in matched_list:
							try:
								klist=[ki,kk,kc]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								print (msg.to,[jj])
							except:
								print

            elif "Attack" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace("We attack as well as great damage and speed","")
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						ki.sendText(msg.to,"We have great attack and speed ratings 么")
						kk.sendText(msg.to,"We attack multiple enemies with fiery breath")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Not found.")
							kk.sendText(msg.to,"Not found.")
						else:
							for target in targets:
								try:
									klist=[ki,kk,kc]
									kicker=random.choice(klist)
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									ki.sendText(msg.to,"Group cleanse")
									kk.sendText(msg.to,"Group cleanse")
            elif "Nk " in msg.text:
				if msg.from_ in admin:
					if msg.from_ in admin:
						nk0 = msg.text.replace("Nk ","")
						nk1 = nk0.lstrip()
						nk2 = nk1.replace("@","")
						nk3 = nk2.rstrip()
						_name = nk3
						gs = cl.getGroup(msg.to)
						targets = []
						for s in gs.members:
							if _name in s.displayName:
								targets.append(s.mid)
						if targets == []:
							sendMessage(msg.to,"user does not exist")
							pass
						else:
							for target in targets:
									try:
										klist=[cl,ki,kk,kc]
										kicker=random.choice(klist)
										kicker.kickoutFromGroup(msg.to,[target])
										print (msg.to,[g.mid])
									except:
										ki.sendText(msg.to,"Succes Cv")
										kk.sendText(msg.to,"We have great attack and speed ratings"),
            elif "Blacklist @ " in msg.text:
				if msg.from_ in admin:
					_name = msg.text.replace("Blacklist @ ","")
					_kicktarget = _name.rstrip(' ')
					gs = ki.getGroup(msg.to)
					targets = []
					for g in gs.members:
						if _kicktarget == g.displayName:
							targets.append(g.mid)
							if targets == []:
								cl.sendText(msg.to,"Not found")
							else:
								for target in targets:
									try:
										wait["blacklist"][target] = True
										f=codecs.open('st2__b.json','w','utf-8')
										json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
										kc.sendText(msg.to,"Succes Cv")
									except:
										ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Ban]ok"
						_name = msg.text.replace("Ban @","")
						_nametarget = _name.rstrip('  ')
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Not Found")
						else:
							for target in targets:
								try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    					kc.sendText(msg.to,"Succesfully banned the contact sir！")
                                    					kk.sendText(msg.to,"Succesfully banned sir! Now the contact already on Continental Server targeting list, and their soul will be priceless！")
									ki.sendText(msg.to,"They will be revoke by their own Atitude！")
								except:
									ki.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban @","")
						_nametarget = _name.rstrip('  ')
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						gs = kc.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Not found")
							kk.sendText(msg.to,"Not found")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               						cl.sendText(msg.to,"Done Doing Bussines..")
                                					ki.sendText(msg.to,"Succes unbanned ser ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ.")
                                					kc.sendText(msg.to,"Anything else sir ?. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                                					kk.sendText(msg.to,"Succes Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                            					except:
                                					ki.sendText(msg.to,"Succes unban by komite Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                                					kc.sendText(msg.to,"Succesfully sir unbanned by  \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
									kk.sendText(msg.to,"Succes unbaned the Contact Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#-----------------------------------------------
            elif msg.text in ["Test"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"We attack multiple enemies with fiery breath!")
#-----------------------------------------------
            elif "Say " in msg.text:
					bctxt = msg.text.replace("Say ","")
					ki.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["Author","Creator"]:
				ki.sendText(msg.to,"line.me/ti/p/~antonlou")

#-----------------------------------------------
            elif msg.text in ["Hmm"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Batuk mas??")
            elif msg.text in ["Wkwkwk"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Gween mana ya , gw jadi kangen naena sama dia")
            elif msg.text in ["Say Gween cute"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"Gween cute 魛渷魛厰Har Har魪靠")
					kk.sendText(msg.to,"Gween cute 魛渷魛厰Har Har魪靠")
					kc.sendText(msg.to,"Gween cute 魛渷魛厰Har Har魪靠")
            elif msg.text in ["#welcome"]:
				if msg.from_ in admin:
					ki.sendText(msg.to,"This room already protected by omnious [BLVCK DRVGON]™")
					kk.sendText(msg.to,"We attack multiple enemies with fiery breath!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping","Samlekom","samlekom"]:
				ki.sendText(msg.to,"Mamen 魛渷魛厰Har Har魪靠")
				kk.sendText(msg.to,"Ngentod 魛渷魛厰Har Har魪靠")
				kc.sendText(msg.to,"Yuuk 魛渷魛厰Har Har魪靠")
#-----------------------------------------------
            elif msg.text in ["Responsename","Respon"]:
                profile = ki.getProfile()
                text = profile.displayName + "\n[ BLVCK HITTER - ORGANIZATION ]\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ"
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + "\n[ BLVCK HITTER - ORGANIZATION ]\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ"
                kk.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + "\n[ BLVCK HITTER - ORGANIZATION ]\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ"
		kc.sendText(msg.to, text)
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                		start = time.time()
                		ki.sendText(msg.to, "Writing server speed ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                		elapsed_time = time.time() - start
                		cl.sendText(msg.to, "%s second" % (elapsed_time))
				ki.sendText(msg.to, "%s second" % (elapsed_time))
				kk.sendText(msg.to, "%s second" % (elapsed_time))
				kc.sendText(msg.to, "%s second" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"send contact")					
            elif msg.text in ["Unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"send contact") 
            elif msg.text in ["Banlist"]:
				if msg.from_ in admin:
					if wait["blacklist"] == {}:
						cl.sendText(msg.to,"nothing")
					else:
						cl.sendText(msg.to,"Blacklist user")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "�" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							cl.sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
							cl.kickoutFromGroup(msg.to,[jj])
						cl.sendText(msg.to,"Bye...")
            elif msg.text in ["Clear"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.invitee]
						for _mid in gMembMids:
							cl.cancelGroupInvitation(msg.to,[_mid])
						cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "Random:" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						strnum = msg.text.replace("Random:","")
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						try:
							num = int(strnum)
							group = cl.getGroup(msg.to)
							for var in range(0,num):
								name = "".join([random.choice(source_str) for x in xrange(10)])
								time.sleep(0.01)
								group.name = name
								cl.updateGroup(group)
						except:
							cl.sendText(msg.to,"Error")
            elif "albumÃ¢â€ â„1¤7„1¤7" in msg.text:
				if msg.from_ in admin:
					try:
						albumtags = msg.text.replace("albumÃ¢â€ â„1¤7„1¤7","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
            elif "fakecÃ¢â€ â„1¤7„1¤7" in msg.text:
				if msg.from_ in admin:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecÃ¢â€ â„1¤7„1¤7","")
						cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
			for zx in range(0,20):
				hasil = cl.activity(limit=20)
				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
					try:    
						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Anton http://line.me/ti/p/~antonlou")
						kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"BLVCK DRVGON CBOT188 Enjoy and relax sir!")
						print "DiLike"
					except:
							pass
				else:
						print "Sudah DiLike"
			time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
