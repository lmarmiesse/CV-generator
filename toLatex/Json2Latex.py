 # -*- coding: utf-8 -*-

import json
import codecs

inFile = "../www/ressources/CV-en.json"
outFile = "latex/CV-en.tex"

f = open(inFile,"r")
f2 = open(outFile,"w")

cv = json.load(f)

cv = cv["CV"]

for a in cv:
	print a


f2.write("\documentclass[11pt,a4paper,sans]{moderncv}\n")
f2.write("\moderncvstyle{classic}\n")
f2.write("\moderncvcolor{green}\n")
f2.write("\usepackage[utf8]{inputenc} \n")
f2.write(
"""\usepackage[scale=0.80]{geometry}
\\name{"""+cv["firstname"].encode('utf8')+"""}{"""+cv["familyname"].encode('utf8')+"""}
\\title{"""+cv["title"]+"""}                               
%\\address{street and number}{postcode city}{country}% optional, remove / comment the line if not wanted; the "postcode city" and and "country" arguments can be omitted or provided empty
%\phone[mobile]{+1~(234)~567~890}                   % optional, remove / comment the line if not wanted
%\phone[fixed]{+2~(345)~678~901}                    % optional, remove / comment the line if not wanted
%\phone[fax]{+3~(456)~789~012}                      % optional, remove / comment the line if not wanted
\email{"""+cv["email"].encode('utf8')+"""}                               % optional, remove / comment the line if not wanted
\homepage{"""+cv["homepage"].encode('utf8')+"""}               % optional, remove / comment the line if not wanted
\extrainfo{\n\includegraphics[width=10px]{images/github_logo.pdf} \httplink{"""+cv["github"].encode('utf8')+"""}\n\makenewline\n\includegraphics[width=10px]{images/linkedin_logo.pdf} \httplink{"""+cv["linkedin"].encode('utf8')+"""}}           % optional, remove / comment the line if not wanted
%\photo[64pt][0.4pt]{picture}                       % optional, remove / comment the line if not wanted; '64pt' is the height the picture must be resized to, 0.4pt is the thickness of the frame around it (put it to 0pt for no frame) and 'picture' is the name of the picture file
%\quote{Some quote}\n  
""")

f2.write("\\begin{document}\n")
f2.write("\makecvtitle\n")

#################################### SKILLS
skills = cv["Skills"]

f2.write("\section{"+skills["name"]+"}\n")
for categ in skills["values"]:
	f2.write("\subsection{"+categ["name"]+"}\n")
	
	
	for i in range(0,len(categ["subCateg"]),2):
		
		cat1 = categ["subCateg"][i]

		if i+1<len(categ["subCateg"]):
			cat2 = categ["subCateg"][i+1]
			f2.write("\cvdoubleitem{"+cat1["name"]+"}{"+", ".join(cat1["values"])+"}{"+cat2["name"]+"}{"+", ".join(cat2["values"])+"}\n")
	
		else:
			f2.write("\cvdoubleitem{"+cat1["name"]+"}{"+", ".join(cat1["values"])+"}{}{}\n")
	
#################################### 


#################################### EXPERIENCES
exps = cv["Experiences"]

f2.write("\section{"+exps["name"]+"}\n")
for exp in exps["values"]:
	
	supervisors = ""
	for superv in exp["supervisor"]:
		if supervisors=="":
			supervisors = superv["name"]
		else:
			supervisors += ", "+superv["name"]
	
	
	f2.write("\cventry{"+exp["date"].encode('utf8')+"}{"+exp["name"].encode('utf8')+"}{"+exp["company"].encode('utf8')+"}{"+exp["location"].encode('utf8')+"}{}{"+exp["description"].encode('utf8')+" \\newline{} \\textit{"+exps["supervisorWord"].encode('utf8')+": "+supervisors.encode('utf8')+"}}\n")
	
	
####################################

#################################### EDUCATION
edu = cv["Education"]

f2.write("\section{"+edu["name"]+"}\n")
for ed in edu["values"]:
	f2.write("\cventry{"+ed["date"].encode('utf8')+"}{"+ed["name"].encode('utf8')+"}{"+ed["university"].encode('utf8')+"}{"+ed["location"].encode('utf8')+"}{}{"+ed["description"].encode('utf8')+"}\n")
	
	
#################################### 


#################################### PUBLICATIONS
pubs = cv["Publications"]

f2.write("\section{"+pubs["name"]+"}\n")
for pub in pubs["values"]:
	f2.write("\cventry{}{"+pub["name"].encode('utf8')+"}{}{}{}{"+", ".join(pub["authors"]).encode('utf8')+"\\newline{} \\textit{"+pub["journal"].encode('utf8')+"}, "+str(pub["year"]).encode('utf8')+"}\n")
	
	
#################################### 


#################################### Languages
langs = cv["Languages"]

f2.write("\section{"+langs["name"]+"}\n")

for i in range(0,len(categ["subCateg"]),2):
		
	lang1 = langs["values"][i]

	if i+1<len(categ["subCateg"]):
		lang2 = langs["values"][i+1]
		f2.write("\cvdoubleitem{"+lang1["name"]+"}{"+lang1["level"]+"}{"+lang2["name"]+"}{"+lang2["level"]+"}\n")
	
	else:
		f2.write("\cvdoubleitem{"+lang1["name"]+"}{"+lang1["level"]+"}{}{}\n")
		
#################################### 

#################################### PUBLICATIONS
interests = cv["Interests"]

f2.write("\section{"+interests["name"]+"}\n")
	
	
#################################### 

f2.write("\\end{document}\n")
f.close()
f2.close()
