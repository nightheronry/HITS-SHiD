# -*- coding: utf-8 -*-


class ExtractAnnotation:
    def __init__(self, fileName):
        self.FileName = fileName
        pass

    def ptt(self, PowerUser):
        TimeTemp = ""
        ReadFromTxt = open('WebDocuments/'+self.FileName+'.txt', 'r')
        WriteToTxt = open("Annotationlist/Annotationlist_" + self.FileName + '.txt', 'w')
        UserId = PowerUser
        if str(self.FileName).split('_')[0] == '7':  # 若為3/5, 6 改成+2, 否則+1
            shift1 = 6
            shift2 = 6
            shift3 = 1
            dicname = 'soccer'
        else:
            shift1 = 6
            shift2 = 7
            shift3 = 2
            dicname = 'baseball'
        Aselectedplayer = {}
        Aselectedterm = {}
        Pselectedplayer = {}
        Pselectedterm = {}
        Nselectedplayer = {}
        Nselectedterm = {}
        # read two dic into list[dicplayer], list[play]
        ReadFromPDic = open('Dic/'+dicname + "player.txt", 'r')
        ReadFromPDic2 = open('Dic/'+dicname + "player2.txt", 'r')

        ReadFromADic = open('Dic/'+dicname + "Term.txt", 'r')
        ReadFromADic2 = open('Dic/'+dicname + "term2.txt", 'r')
        # ReadFromADic3 = open("soccerterm3.txt", 'r')

        dicplayer = []
        dicterm = []

        for Player in ReadFromPDic:
            dicplayer.append(Player.rstrip())
        for Player in ReadFromPDic2:
            if Player.rstrip() not in dicplayer:
                dicplayer.append(Player.rstrip())
        print(dicplayer)
        for term in ReadFromADic:
            dicterm.append(term.rstrip())
        for term in ReadFromADic2:
            if term.rstrip() not in dicterm:
                dicterm.append(term.rstrip())
        # for Player in ReadFromADic3:
        #    if term.rstrip() not in dicterm:
        #        dicterm.append(Player.rstrip())
        print(dicterm)
        for Message in ReadFromTxt:

            MessageTemp = []

            MessageTemp.append(Message[len(Message) - shift1:])  # 將"回文時間“存入Messagetemp[0]#若為3/5, 6 改成-6, 否則-5
            if TimeTemp == "":
                TimeTemp = MessageTemp[0]
                # print(MessageTemp[0])
                pass
            else:
                if TimeTemp != MessageTemp[0]:  # 判斷時間

                    # 寫出上一片段資料
                    print(TimeTemp.rstrip())
                    WriteToTxt.writelines(TimeTemp.rstrip() + '\n')
                    listset = [Aselectedplayer, Aselectedterm, Pselectedplayer, Pselectedterm, Nselectedplayer, Nselectedterm]
                    count = 0
                    for selectlist in listset:
                        sort = [(p, selectlist[p]) for p in sorted(selectlist, key=selectlist.get, reverse=True)]
                        if count == 0:
                            print('AllUser:')
                            WriteToTxt.writelines('Alluser\n')
                        elif count == 2:
                            print('PowerUser:')
                            WriteToTxt.writelines('PowerUser\n')
                        elif count == 4:
                            print('NormalUser:')
                            WriteToTxt.writelines('NormalUser\n')
                        count += 1
                        print(sort)
                        WriteToTxt.writelines(str(sort) + '\n')
                        print("")
                        WriteToTxt.writelines('\n')
                    # 重置紀錄表
                    TimeTemp = MessageTemp[0]
                    Aselectedplayer.clear()
                    Aselectedterm.clear()
                    Pselectedplayer.clear()
                    Pselectedterm.clear()
                    Nselectedplayer.clear()
                    Nselectedterm.clear()

            MessageTemp.append(Message[:3])  # 將"推/噓狀態存入Messagetemp[1]
            MessageTemp.append(Message[2:Message.find(":")])  # 將"ID"存入Messagetemp[2]
            MessageTemp.append(
                Message[len(Message) - 11:len(Message) - shift2:])  # 將"日期"存入Messagetemp[3]#若為3/5, 6 改成-7, 否則-6
            MessageTemp.append(
                Message[Message.find(":") + shift3:len(Message) - 13:])  # 將"推文內容"存入Messagetemp[4]#若為3/5, 6 改成+2, 否則+1

            for player in dicplayer:
                player = player.lower()
                if player in MessageTemp[4].strip().lower():
                    count = MessageTemp[4].strip().lower().count(player)
                    if player in Aselectedplayer.keys():
                        Aselectedplayer[player] = Aselectedplayer[player] + count
                    else:
                        Aselectedplayer[player] = count
            for term in dicterm:
                term = term.lower()
                if term in MessageTemp[4].strip().lower():
                    count = MessageTemp[4].strip().lower().count(term)
                    if term in Aselectedterm.keys():
                        Aselectedterm[term] = Aselectedterm[term] + count
                    else:
                        Aselectedterm[term] = count

            if Message[2:Message.find(":")] in UserId:  # 為ＰＵ發言
                # print("PU: ", Message[2:Message.find(":"), MessageTemp[4].strip().lower(), " in "+MessageTemp[0])
                # 比對兩個詞庫 計算詞頻

                for player in dicplayer:
                    player = player.lower()
                    if player in MessageTemp[4].strip().lower():
                        count = MessageTemp[4].strip().lower().count(player)
                        if player in Pselectedplayer.keys():
                            Pselectedplayer[player] = Pselectedplayer[player] + count
                        else:
                            Pselectedplayer[player] = count
                for term in dicterm:
                    term = term.lower()
                    if term in MessageTemp[4].strip().lower():
                        count = MessageTemp[4].strip().lower().count(term)
                        if term in Pselectedterm.keys():
                            Pselectedterm[term] = Pselectedterm[term] + count
                        else:
                            Pselectedterm[term] = count
            else:
                # 不是PU發言
                # print("NU: ", Message[2:Message.find(":")], MessageTemp[4].strip().lower()+" in ", MessageTemp[0])
                # 比對兩個詞庫 計算詞頻
                for player in dicplayer:
                    player = player.lower()
                    if player in MessageTemp[4].strip().lower():
                        count = MessageTemp[4].strip().lower().count(player)
                        # print(player, ':', str(count))
                        if player in Nselectedplayer.keys():
                            Nselectedplayer[player] = Nselectedplayer[player] + count
                        else:
                            Nselectedplayer[player] = count
                for term in dicterm:
                    term = term.lower()
                    if term in MessageTemp[4].strip().lower():
                        count = MessageTemp[4].strip().lower().count(term)
                        # print(Message[2:Message.find(":")], term, ':',  str(count))
                        if term in Nselectedterm.keys():
                            Nselectedterm[term] = Nselectedterm[term] + count
                        else:
                            Nselectedterm[term] = count

        ReadFromTxt.close()
        WriteToTxt.close()
        print(self.FileName, "done!")
        return 0

    def PowerUser(self):
        fr = open("/PowerUser/PowerUser_" + self.FileName+'.txt')
        userlist = []
        for user in fr:
            userlist.append(str(user).splitlines()[0])
        return userlist


if __name__ == '__main__':

    tfidf = ExtractAnnotation('3_05')
    poweruser = tfidf.PowerUser()
    tfidf.ptt(poweruser)

    tfidf = ExtractAnnotation('3_06')
    poweruser = tfidf.PowerUser()
    tfidf.ptt(poweruser)

    tfidf = ExtractAnnotation('7_09')
    poweruser = tfidf.PowerUser()
    tfidf.ptt(poweruser)

    tfidf = ExtractAnnotation('7_10')
    poweruser = tfidf.PowerUser()
    tfidf.ptt(poweruser)

    tfidf = ExtractAnnotation('7_13')
    poweruser = tfidf.PowerUser()
    tfidf.ptt(poweruser)

    tfidf = ExtractAnnotation('7_14')
    poweruser = tfidf.PowerUser()
    tfidf.ptt(poweruser)
