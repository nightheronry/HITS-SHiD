# -*- coding: utf-8 -*-
import ast


def tuplemerge( list1=[], list2=[]):  # (B, S)
    list = []
    for item in list2:
        for item2 in list1:
            if item[0] in item2:
                list.append((item[0], item[1] + item2[1]))
                #print(item)
                list2.remove(item)
                list1.remove(item2)
                break
    return list + list2+list1

class extractHG():

    def __init__(self, fileName):
        self.FileName = fileName
        self.modetime = []
        pass



    def timeModify(self, timelist=[]):
        modetimeList = []

        #print(self.FileName)
        for time in timelist:
            templist = []
            for time2 in time:
                templist.append([int(time2 / 60), int(time2 % 60)])
            modetimeList.append(templist)
        self.modetime = modetimeList
        pass

    def extractAnnotaton(self, shift=0, exportfile=''):
        ReadFromAnnotation = open('Annotationlist/Annotationlist_'+self.FileName+'.txt', 'r')
        WriteToTxt = open('Annotationlist/Merge/'+exportfile+'/HighlightAnnotation_'+self.FileName+'_'+exportfile+'.txt', 'w')
        starttime = ReadFromAnnotation.readline().rstrip().split(':')
        starttime[0] = int(starttime[0])
        starttime[1] = int(starttime[1])
        highlighttimes = []
        for time in self.modetime:
            templist = []
            for time2 in time:
                a = str(int((time2[1]+starttime[1]) / 60+time2[0]+starttime[0]))
                b = str((time2[1]+starttime[1]) % 60)
                templist.append((a if len(a) > 1 else '0'+a)+':'+(b if len(b) > 1 else '0'+b))
            highlighttimes.append(templist)
        for highlighttime in highlighttimes:
            #print(highlighttimes)
            Alluserplayer = []
            Alluseraction = []
            Poweruserplayer = []
            Poweruseraction = []
            Normaluserplayer = []
            Normaluseraction = []
            ReadFromAnnotation.seek(0)
            for line in ReadFromAnnotation:
                # print(line)
                if line.rstrip() in highlighttime:
                    #print(line.rstrip())
                    ReadFromAnnotation.readline().rstrip()
                    Alluserplayer = tuplemerge(Alluserplayer, ast.literal_eval(ReadFromAnnotation.readline().rstrip()))#+= ast.literal_eval(ReadFromAnnotation.readline().rstrip())
                    #print(Alluserplayer)
                    ReadFromAnnotation.readline()
                    Alluseraction = tuplemerge(Alluseraction, ast.literal_eval(ReadFromAnnotation.readline().rstrip()))#+= ast.literal_eval(ReadFromAnnotation.readline().rstrip())
                    ReadFromAnnotation.readline()
                    ReadFromAnnotation.readline()
                    Poweruserplayer = tuplemerge(Poweruserplayer, ast.literal_eval(ReadFromAnnotation.readline().rstrip()))
                    ReadFromAnnotation.readline()
                    Poweruseraction = tuplemerge(Poweruseraction,  ast.literal_eval(ReadFromAnnotation.readline().rstrip()))
                    ReadFromAnnotation.readline()
                    ReadFromAnnotation.readline()
                    Normaluserplayer = tuplemerge(Normaluserplayer, ast.literal_eval(ReadFromAnnotation.readline().rstrip()))
                    ReadFromAnnotation.readline()
                    Normaluseraction = tuplemerge(Normaluseraction, ast.literal_eval(ReadFromAnnotation.readline().rstrip()))

            WriteToTxt.write(str(highlighttime)+'\n')
            #print(highlighttime)
            WriteToTxt.write('Alluser\n')
            WriteToTxt.write(str(sorted(Alluserplayer, key=lambda x: x[1], reverse=True)) + '\n')
            WriteToTxt.write('\n')
            WriteToTxt.write(str(sorted(Alluseraction, key=lambda x: x[1], reverse=True)) + '\n')
            WriteToTxt.write('\n')
            WriteToTxt.write('PowerUser\n')
            WriteToTxt.write(str(sorted(Poweruserplayer, key=lambda x: x[1], reverse=True)) + '\n')
            WriteToTxt.write('\n')
            WriteToTxt.write(str(sorted(Poweruseraction, key=lambda x: x[1], reverse=True)) + '\n')
            WriteToTxt.write('\n')
            WriteToTxt.write('NormalUser\n')
            WriteToTxt.write(
                str(sorted(Normaluserplayer, key=lambda x: x[1], reverse=True)) + '\n')
            WriteToTxt.write('\n')
            WriteToTxt.write(
                str(sorted(Normaluseraction, key=lambda x: x[1], reverse=True)) + '\n')
            WriteToTxt.write('\n')

        ReadFromAnnotation.close()
        return 0

if __name__ == '__main__':
    #  3_06
    ex = extractHG('3_06')
    #ex.timeModify([58, 62, 59, 126, 184, 135, 54, 125, 55, 49, 63])
    ex.timeModify([[58, 59], [62, 63], [126], [184], [135], [54], [125], [55], [49]])
    ex.extractAnnotaton(0, 'HITS')
    # 58->37:20
    #ex.timeModify([58, 62, 59, 48, 55, 19, 54, 49, 51, 50, 63, 13, 20, 24, 44, 52])
    ex.timeModify([[58, 59], [62, 63], [48, 49], [54, 55], [19], [50, 51, 52], [13], [20], [24], [44]])
    ex.extractAnnotaton(0, 'MT')

    #  3_05
    ex = extractHG('3_05')
    #ex.timeModify([53, 23, 75, 54, 18, 83, 74, 17, 13, 46, 11, 22, 37, 27, 67, 89, 45, 33, 40, 24, 14])
    ex.timeModify([[53, 54], [22, 23, 24], [74, 75], [17, 18], [83], [13, 14], [45, 46], [11], [37], [27], [67], [89], [33], [40]])
    ex.extractAnnotaton(0, 'HITS')

    #ex.timeModify([53, 75, 23, 83, 165, 54])
    ex.timeModify([[53, 54], [75], [23], [83], [165]])

    ex.extractAnnotaton(0, 'MT')

    # 7_09
    ex = extractHG('7_09')
    #ex.timeModify([71, 75, 70, 72, 69, 141, 76, 131, 68, 152, 57, 132])
    ex.timeModify([[68, 69, 70, 71, 72], [75, 76], [141], [131, 132], [152], [57]])

    ex.extractAnnotaton(0, 'HITS')

    #ex.timeModify([71, 70, 72, 75, 69, 57, 76, 68, 56, 73, 58, 77, 42, 63, 48, 40, 49, 17, 41, 45])
    ex.timeModify([[68, 69, 70, 71, 72], [75, 76, 77], [56, 57, 58], [73], [40, 41, 42], [63], [48, 49], [17], [45]])

    ex.extractAnnotaton(0, 'MT')

    #  7_10
    ex = extractHG('7_10')
    #ex.timeModify([133, 198, 130, 195, 199, 146, 183, 196, 149, 201, 137, 189])
    ex.timeModify([[133], [198, 199], [130], [195, 196], [146], [183], [149], [201], [137], [189]])

    ex.extractAnnotaton(0, 'HITS')

    #ex.timeModify([51, 105, 75, 71])
    ex.timeModify([[51], [105], [75], [71]])

    ex.extractAnnotaton(0, 'MT')

    #  7_13
    ex = extractHG('7_13')
    #ex.timeModify([157, 64, 50, 65, 85, 86, 51, 161, 89, 158])
    ex.timeModify([[157, 158], [64, 65], [50, 51], [85, 86], [161], [89]])

    ex.extractAnnotaton(0, 'HITS')

    #ex.timeModify([64, 65, 50, 51, 86, 85, 89, 52, 66, 87, 92, 44, 57, 88, 43, 49])
    ex.timeModify([[64, 65, 66], [49, 50, 51, 52], [85, 86, 87, 88, 89], [92], [43, 44], [57]])

    ex.extractAnnotaton(0, 'MT')

    #  7_14
    ex = extractHG('7_14')
    #ex.timeModify([63, 178, 174, 189, 80, 179, 188, 62, 109, 177, 140, 64, 175, 110])
    ex.timeModify([[62, 63, 64], [177, 178, 179], [174, 175], [188, 189], [80], [109, 110], [140]])

    ex.extractAnnotaton(0, 'HITS')

    #ex.timeModify([63, 62, 54, 64, 80, 53, 81, 79, 51, 99])
    ex.timeModify([[62, 63, 64], [53, 54], [79, 80, 81], [51], [99]])

    ex.extractAnnotaton(0, 'MT')
