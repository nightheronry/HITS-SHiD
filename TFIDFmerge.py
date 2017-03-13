# -*- coding: utf-8 -*-

from gensim import corpora, models
import ast

class TFIDF():

    def __init__(self, fileName):
        self.FileName = fileName
        self.collection = []
        self.method = ''
        pass

    def loading_document_set(self, type='', method=None):
        time_serise = []
        self.method = method
        if not type:
            raise ValueError('arg \'type\' need be input as collection or document only.')
        elif type == 'collection':
            file = 'Annotationlist/Annotationlist_'+self.FileName+'.txt'
        elif type == 'document' and method:
            file = 'Annotationlist/Merge/'+method+'/HighlightAnnotation_'+self.FileName+'_'+method+'.txt'
        else:
            raise ValueError('arg \'method\' need be input')

        read_from_annotation = open(file, 'r')
        #print(file)
        collection = []
        document = []
        time = ''
        for line in read_from_annotation:
            if ':' in line:
                if time != '':
                    #print(time)
                    time_serise.append(time)
                    collection.append(document)
                    # print(collection)
                    document = []
                    time = line.rstrip()
                else:
                    time = line.rstrip()
            elif 'PowerUser' in line or 'NormalUser' in line:
                annotation_text = read_from_annotation.readline()
                annotation_list = []
                for word_list in ast.literal_eval(annotation_text.rstrip()):
                    for tf in range(word_list[1]):
                        annotation_list.append(word_list[0])
                document.append(annotation_list)
                annotation_list = []
                read_from_annotation.readline()
                annotation_text = read_from_annotation.readline()
                for word_list in ast.literal_eval(annotation_text.rstrip()):
                    for tf in range(word_list[1]):
                        annotation_list.append(word_list[0])
                document.append(annotation_list)

        else:
            #print(time)
            time_serise.append(time)
            #print(document)
            collection.append(document)

        read_from_annotation.close()

        return collection, time_serise



    def tfidf_construct(self, corpus):
        corpus2 = []
        for document in corpus:
            document2 = []
            for graph in document:
                if len(graph)>0:
                    for word in graph:
                        document2.append(word)
            corpus2.append(document2)
        dic = corpora.Dictionary(corpus2)
        #print(dic.token2id)
        corpus = [dic.doc2bow(text) for text in corpus2]
        # print(corpus)

        tfidf_model = models.TfidfModel(corpus, wglobal=lambda *args: models.tfidfmodel.df2idf(*args, log_base=2.0, add=0.0))

        return tfidf_model, dic


    def tfidf_weighting(self, documentset=[], dic=None):
        time_seriase.reverse()
        WriteToTxt = open('Annotationlist/Merge/'+self.method+'/HighlightAnnotation_'+self.FileName+'_'+self.method+'_TFIDF.txt', 'w')
        #print(documentset)
        for document in documentset:
            document.insert(0, document[0]+document[2])
            document.insert(1, document[2]+document[4])
        #print(len(documentset))
        #print(time_seriase)
        for documents in documentset:
            # print(documents)
            flag = 0
            time = time_seriase.pop()
            WriteToTxt.writelines(time+'\n')
            for document in documents:
                # print(document)
                count = 0
                # document_list = [[d] for d in document]
                # print(document_list)
                rankList = []
                corpus = [dic.doc2bow(text) for text in [document]]
                # print(corpus)
                for i in model[corpus]:
                    # print(i)
                    for j in sorted(i, key=lambda d: d[1], reverse=True):
                        # print(j)
                        if count > 10:
                            break
                        # print(dic[j[0]])
                        # rankList.append((dic[j[0]], j[1]))
                        rankList.append(dic[j[0]])
                    if flag % 6 == 0:
                        #print('AllUser')
                        WriteToTxt.writelines('AllUser\n')
                    if flag % 6 == 2:
                        #print('PowerUser')
                        WriteToTxt.writelines('PowerUser\n')
                    if flag % 6 == 4:
                        #print('NormalUser')
                        WriteToTxt.writelines('NormalUser\n')
                    #print(rankList)
                    WriteToTxt.writelines(str(rankList))
                    #print('')
                    WriteToTxt.writelines('\n\n')
                    flag += 1
        return 0

if __name__ == '__main__':

    tfidf = TFIDF('3_05')
    collection, time = tfidf.loading_document_set(type='collection')
    model, dic = tfidf.tfidf_construct(collection)
    documentset, time_seriase = tfidf.loading_document_set(type='document', method='HITS')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    documentset, time_seriase = tfidf.loading_document_set(type='document', method='MT')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    tfidf = TFIDF('3_06')
    collection, time = tfidf.loading_document_set(type='collection')
    model, dic = tfidf.tfidf_construct(collection)
    documentset, time_seriase = tfidf.loading_document_set(type='document', method='HITS')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    documentset, time_seriase = tfidf.loading_document_set(type='document', method='MT')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    tfidf = TFIDF('7_09')
    collection, time = tfidf.loading_document_set(type='collection')
    model, dic = tfidf.tfidf_construct(collection)
    documentset, time_seriase = tfidf.loading_document_set(type='document', method='HITS')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    documentset, time_seriase = tfidf.loading_document_set(type='document', method='MT')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    tfidf = TFIDF('7_10')
    collection, time = tfidf.loading_document_set(type='collection')
    model, dic = tfidf.tfidf_construct(collection)
    documentset, time_seriase = tfidf.loading_document_set(type='document', method='HITS')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    documentset, time_seriase = tfidf.loading_document_set(type='document', method='MT')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    tfidf = TFIDF('7_13')
    collection, time = tfidf.loading_document_set(type='collection')
    model, dic = tfidf.tfidf_construct(collection)
    documentset, time_seriase = tfidf.loading_document_set(type='document', method='HITS')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    documentset, time_seriase = tfidf.loading_document_set(type='document', method='MT')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    tfidf = TFIDF('7_14')
    collection, time = tfidf.loading_document_set(type='collection')
    model, dic = tfidf.tfidf_construct(collection)
    documentset, time_seriase = tfidf.loading_document_set(type='document', method='HITS')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)

    documentset, time_seriase = tfidf.loading_document_set(type='document', method='MT')
    print(tfidf.FileName + ' ' + tfidf.method)
    print(time_seriase)
    tfidf.tfidf_weighting(documentset, dic)
