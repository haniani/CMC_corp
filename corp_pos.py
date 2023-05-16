import json, re, os
from pymystem3 import Mystem
from natsort import natsorted 

A = 0
ADV = 0
ADVPRO = 0
ANUM = 0
APRO = 0
COM = 0
CONJ = 0
INTJ = 0
NUM = 0
PART = 0
PR = 0
S = 0
SPRO = 0
V = 0

files_count = 0
files_count_all = 0
folders_count = 1

for path, dirs, files in os.walk('/Users/haniani/Downloads/test/'):
	sorts = natsorted(files)
	print(sorts)
	for fname in sorts:
		#act_path = os.path.join(path + fname)
		#print(act_path)
		#print(files_count)
		if fname.endswith(".xml"):
			#print(fname)
			os.chdir(path)
			file_open = open(fname, 'r')
			file_read = file_open.read()
			find_text = re.findall('\<p\>.*\<\/p\>', file_read)
			clean_text_1 = re.sub('\<p\>', '', str(find_text))
			clean_text_2 = re.sub('\<\/p\>', '', clean_text_1)

			m = Mystem()
			#lemmas = m.lemmatize(clean_text_2)

			full_info = m.analyze(clean_text_2)
			full_json = json.dumps(full_info)
			full_json_2 = json.loads(full_json)

			for item in full_json_2:
				if 'analysis' in item:
					try:
						gr_pos = item['analysis'][0]['gr']
						pos = re.search('\w{1,6}(\,|\=)', gr_pos)
						pos_edit = re.sub('\=|\,', '', pos.group(0))
						if pos_edit == 'A':
							A += 1
						elif pos_edit == 'ADV':
							ADV += 1
						elif pos_edit == 'ADVPRO':
							ADVPRO += 1
						elif pos_edit == 'ANUM':
							ANUM += 1
						elif pos_edit == 'APRO':
							APRO += 1
						elif pos_edit == 'COM':
							COM += 1
						elif pos_edit == 'CONJ':
							CONJ += 1
						elif pos_edit == 'INTJ':
							INTJ += 1
						elif pos_edit == 'NUM':
							NUM += 1
						elif pos_edit == 'PART':
							PART += 1
						elif pos_edit == 'PR':
							PR += 1
						elif pos_edit == 'S':
							S += 1
						elif pos_edit == 'SPRO':
							SPRO += 1
						elif pos_edit == 'V':
							V += 1
						else:
							print(item, pos_edit, ' Проблема')

							os.chdir('..')
					except:
						os.chdir('..')

			if files_count == 5:
				files_count = 0
				files_count += 1
				files_count_all += 1
				folders_count +=1
				os.chdir('/Users/haniani/Downloads/analysis/')
				name_folder = str(folders_count) + '_pos'
				os.makedirs('{}'.format(name_folder), exist_ok=True)
				paths = str(name_folder)
				os.chdir('/Users/haniani/Downloads/analysis/' + paths +'/')
				with open('/Users/haniani/Downloads/analysis/'+ paths +'/'+ str(files_count_all) + '.json', 'w') as file_pos:
					file_pos.write(str(full_info))
					file_pos.close()
			else:
				files_count += 1
				files_count_all += 1
				name_folder = str(folders_count) + '_pos'
				paths = str(name_folder)
				os.chdir('/Users/haniani/Downloads/analysis/' + paths+'/')
				with open('/Users/haniani/Downloads/analysis/'+ paths +'/'+ str(files_count_all) + '.json', 'w') as file_pos:
					file_pos.write(str(full_info))
					file_pos.close()

print('A', A, '\n',
'ADV', ADV, '\n',
'ADVPRO', ADVPRO, '\n',
'ANUM', ANUM, '\n',
'APRO', APRO, '\n',
'COM', COM, '\n',
'CONJ', CONJ, '\n',
'INTJ', INTJ, '\n',
'NUM', NUM, '\n',
'PART', PART, '\n',
'PR', PR, '\n',
'S', S, '\n',
'SPRO', SPRO, '\n',
'V', V, '\n')
