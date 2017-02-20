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



    def timeModify(self, timelist=[], merged_bool=False):
        modetimeList = []

        print(self.FileName)

        for time in timelist:
            templist = []
            for time2 in time:
                templist.append([int(time2 / 60), int(time2 % 60)])
            modetimeList.append(templist)
        self.modetime = modetimeList
        self.merged = merged_bool
        pass

    def extractAnnotaton(self, shift=0, exportfile=''):
        print(exportfile)
        if self.merged:
            merged_directory = 'Original/'
        else:
            merged_directory = 'Merge/'


        ReadFromAnnotation = open('Annotationlist/Annotationlist_'+self.FileName+'.txt', 'r')
        WriteToTxt = open('Annotationlist/' + merged_directory+exportfile+'/HighlightAnnotation_'+self.FileName+'_'+exportfile+'.txt', 'w')
        starttime = ReadFromAnnotation.readline().rstrip().split(':')
        print(starttime)
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
        if self.merged:
            print(highlighttimes)
        for highlighttime in highlighttimes:

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
                    # print(line.rstrip())
                    ReadFromAnnotation.readline().rstrip()
                    Alluserplayer = tuplemerge(Alluserplayer, ast.literal_eval(ReadFromAnnotation.readline().rstrip()))
                    # print(Alluserplayer)
                    ReadFromAnnotation.readline()
                    Alluseraction = tuplemerge(Alluseraction, ast.literal_eval(ReadFromAnnotation.readline().rstrip()))
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
            # print(highlighttime)
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

    #  3_05
    ex = extractHG('3_05')
    ex.timeModify([[53], [75], [23], [83], [165], [54]])
    ex.extractAnnotaton(0, 'HITS')

    ex.timeModify([[53, 54], [75], [23], [83], [165]], True)
    ex.extractAnnotaton(0, 'HITS')

    ex.timeModify([[53], [23], [165], [75], [54], [18], [83], [74], [17], [13], [46], [11], [22], [37], [137]])
    ex.extractAnnotaton(0, 'MT')
    ex.timeModify([[53, 54], [22, 23], [165], [74, 75], [18], [83], [17], [13], [46], [11], [37], [137]], True)
    ex.extractAnnotaton(0, 'MT')

    #  3_06
    ex = extractHG('3_06')
    ex.timeModify([[58], [62], [59], [126], [184], [135], [54], [125], [55], [49], [63]])
    ex.extractAnnotaton(0, 'HITS')
    ex.timeModify([[58, 59], [62, 63], [125, 126], [184], [135], [54, 55], [49]], 1)
    ex.extractAnnotaton(0, 'HITS')
    # 58->37:20
    ex.timeModify([[58], [62], [59], [184], [126], [48], [55], [135], [19], [54], [49], [51], [50], [63], [182]])
    ex.extractAnnotaton(0, 'MT')
    ex.timeModify([[58, 59], [62, 63], [184], [126], [48, 49, 50, 51], [54, 55], [135], [19], [182]], True)
    ex.extractAnnotaton(0, 'MT')

    # 7_09
    ex = extractHG('7_09')
    ex.timeModify([[71], [75], [70], [72], [69], [141], [76], [131], [68], [152], [57], [132]])
    ex.extractAnnotaton(0, 'HITS')
    ex.timeModify([[68, 69, 70, 71, 72], [75, 76], [141], [131, 132], [152], [57]], True)
    ex.extractAnnotaton(0, 'HITS')

    ex.timeModify([[71], [70], [72], [75], [69], [57], [76], [68], [141], [56], [73], [131], [58], [152], [142]])
    ex.extractAnnotaton(0, 'MT')
    ex.timeModify([[68, 69, 70, 71, 72, 73], [75, 76], [56, 57, 58], [141, 142], [131], [152]], True)

    ex.extractAnnotaton(0, 'MT')

    #  7_10
    ex = extractHG('7_10')
    ex.timeModify([[133], [198], [130], [195], [199], [146], [183], [196], [149], [201], [137], [189]])
    ex.extractAnnotaton(0, 'HITS')
    ex.timeModify([[133], [198, 199], [130], [195, 196], [146], [183], [149], [201], [137], [189]], True)

    ex.extractAnnotaton(0, 'HITS')

    ex.timeModify([[133], [198], [199], [130], [195], [201], [134], [200], [196], [190], [146], [149], [51], [189], [153]])
    ex.extractAnnotaton(0, 'MT')
    ex.timeModify([[133], [198, 199, 200], [130], [195, 196], [134], [189, 190], [146], [149], [51], [153]], True)

    ex.extractAnnotaton(0, 'MT')

    #  7_13
    ex = extractHG('7_13')
    ex.timeModify([[157], [64], [50], [65], [85], [86], [51], [161], [89], [158]])
    ex.extractAnnotaton(0, 'HITS')
    ex.timeModify([[157, 158], [64, 65], [50, 51], [85, 86], [161], [89]], True)

    ex.extractAnnotaton(0, 'HITS')

    ex.timeModify([[64], [65], [50], [157], [51], [86], [85], [135], [158], [89], [161], [136], [52], [66], [162]])
    ex.extractAnnotaton(0, 'MT')
    ex.timeModify([[64, 65, 66], [50, 51, 52], [157, 158], [85, 86], [135], [89], [161, 162], [136]], True)

    ex.extractAnnotaton(0, 'MT')

    #  7_14
    ex = extractHG('7_14')
    ex.timeModify([[63], [178], [174], [189], [80], [179], [188], [62], [109], [177], [140], [64], [175], [110]])
    ex.extractAnnotaton(0, 'HITS')
    ex.timeModify([[62, 63, 64], [177, 178, 179], [174, 175], [188, 189], [80], [109, 110], [140]], True)

    ex.extractAnnotaton(0, 'HITS')

    ex.timeModify([[63], [178], [174], [179], [189], [62], [54], [64], [80], [188], [53], [110], [109], [177], [159]])
    ex.extractAnnotaton(0, 'MT')
    ex.timeModify([[62, 63, 64], [177, 178, 179], [174], [188, 189], [53, 54], [80], [109, 110], [159]], True)

    ex.extractAnnotaton(0, 'MT')
