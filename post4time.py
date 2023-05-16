import os,re
from os.path import join

textsFolder = []

searchTexts = ''
countPosts2012 = 0
countPosts2013 = 0
countPosts2014 = 0
countPosts2015 = 0
countPosts2016 = 0

text2012 = open("textVK2012.txt", 'w')
text2013 = open("textVK2013.txt", 'w')
text2014 = open("textVK2014.txt", 'w')
text2015 = open("textVK2015.txt", 'w')
text2016 = open("textVK2016.txt", 'w')

for root, dirs, files in os.walk('CORPUS'):
    textsFolder.extend([join(root, file) for file in files if file.endswith('txt')])
    dirs.clear()

for file in textsFolder:
    f = open(file)
    fread = f.readlines()
    text = ''.join(fread)
    f.close()
    searchText = re.findall('(\<post\>(.|\n)*?\<\/post\>)', str(text))
    searchTexts = searchText
    for k in searchTexts:
        searchTextdate = re.findall('(\<date\>(.)*?\<\/date\>)', str(k))
        searchTexttext = re.findall('(\<text\>(.)*?\<\/text\>)', str(k))
        for i in searchTextdate:
            if "2012" in i[0]:
                datePostclear = i[0].replace('<date>','')
                datePostclear = datePostclear.replace('</date>','') 
                for j in searchTexttext:
                    textPostclear = j[0].replace('<text>','')
                    textPostclear = textPostclear.replace('</text>','')
                    text2012.write(textPostclear)
                    countPosts2012 +=1

            elif "2013" in i[0]:
                datePostclear = i[0].replace('<date>','')
                datePostclear = datePostclear.replace('</date>','') 
                for j in searchTexttext:
                    textPostclear = j[0].replace('<text>','')
                    textPostclear = textPostclear.replace('</text>','')
                    text2013.write(textPostclear)
                    countPosts2013 +=1

            elif "2014" in i[0]:
                datePostclear = i[0].replace('<date>','')
                datePostclear = datePostclear.replace('</date>','') 
                for j in searchTexttext:
                    textPostclear = j[0].replace('<text>','')
                    textPostclear = textPostclear.replace('</text>','')
                    text2014.write(textPostclear)
                    countPosts2014 +=1

            elif "2015" in i[0]:
                datePostclear = i[0].replace('<date>','')
                datePostclear = datePostclear.replace('</date>','') 
                for j in searchTexttext:
                    textPostclear = j[0].replace('<text>','')
                    textPostclear = textPostclear.replace('</text>','')
                    text2015.write(textPostclear)
                    countPosts2015 +=1

            elif "2016" in i[0]:
                datePostclear = i[0].replace('<date>','')
                datePostclear = datePostclear.replace('</date>','') 
                for j in searchTexttext:
                    textPostclear = j[0].replace('<text>','')
                    textPostclear = textPostclear.replace('</text>','')
                    text2016.write(textPostclear)
                    countPosts2016 +=1
            else:
                continue


print("############",countPosts2012,"\n",countPosts2013,"\n",countPosts2014,"\n",countPosts2015,"\n",countPosts2016)
text2012.close()
text2013.close()
text2014.close()
text2015.close()
text2016.close()
