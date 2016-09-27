 # -*- coding: utf-8 -*-

import re
import json
import codecs

#~ inFile = "../www/ressources/CV-en.json"
#~ outFile = "latex/CV-en.tex"

inFile = "../www/ressources/CV-fr.json"
outFile = "latex/CV-fr.tex"

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
f2.write("\\newcommand\Colorhref[3][blue]{\href{#2}{\small\color{#1}#3}} \n")
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
\photo[64pt][0.4pt]{images/PhotoLucasMarmiesse}                       % optional, remove / comment the line if not wanted; '64pt' is the height the picture must be resized to, 0.4pt is the thickness of the frame around it (put it to 0pt for no frame) and 'picture' is the name of the picture file
%\quote{Some quote}\n  
""")

f2.write("\\begin{document}\n")
f2.write("\makecvtitle\n")

#################################### SKILLS
skills = cv["Skills"]

f2.write("\section{"+skills["name"].encode('utf8')+"}\n")
for categ in skills["values"]:
	f2.write("\subsection{"+categ["name"]+"}\n")
	
	
	for i in range(0,len(categ["subCateg"]),2):
		
		cat1 = categ["subCateg"][i]

		if i+1<len(categ["subCateg"]):
			cat2 = categ["subCateg"][i+1]
			f2.write("\cvdoubleitem{\\textbf{"+cat1["name"].encode('utf8')+"}}{"+", ".join(cat1["values"]).encode('utf8')+"}{\\textbf{"+cat2["name"].encode('utf8')+"}}{"+", ".join(cat2["values"]).encode('utf8')+"}\n")
	
		else:
			f2.write("\cvdoubleitem{\\textbf{"+cat1["name"].encode('utf8')+"}}{"+", ".join(cat1["values"]).encode('utf8')+"}{}{}\n")
	
#################################### 


#################################### EXPERIENCES
exps = cv["Experiences"]

f2.write("\section{"+exps["name"].encode('utf8')+"}\n")
for exp in exps["values"]:
	
	supervisors = ""
	for superv in exp["supervisor"]:
		if supervisors=="":
			supervisors = superv["name"]
		else:
			supervisors += ", "+superv["name"]
	
	descr = exp["description"].encode('utf8')
	
	m = re.search('<a href="(.+)">(.+)</a>', descr)
	
	if m!=None:
		descr = descr.replace(m.group(0),"\Colorhref{"+m.group(1)+"}{"+m.group(2)+"}")
	
	
	
	
	f2.write("\cventry[1em]{"+exp["date"].encode('utf8')+"}{"+exp["name"].encode('utf8')+"}{"+exp["company"].encode('utf8')+"}{"+exp["location"].encode('utf8')+"}{}{"+descr+" \\newline{} \\textit{"+exps["supervisorWord"].encode('utf8')+": "+supervisors.encode('utf8')+"}}\n")
	
	
####################################

#################################### EDUCATION
edu = cv["Education"]

f2.write("\section{"+edu["name"].encode('utf8')+"}\n")
for ed in edu["values"]:
	f2.write("\cventry[1em]{"+ed["date"].encode('utf8')+"}{"+ed["name"].encode('utf8')+"}{"+ed["university"].encode('utf8')+"}{"+ed["location"].encode('utf8')+"}{}{"+ed["description"].encode('utf8')+"}\n")
	
	
#################################### 


#################################### PUBLICATIONS
pubs = cv["Publications"]

f2.write("\section{"+pubs["name"]+"}\n")
for pub in pubs["values"]:
	f2.write("\cventry[1em]{}{"+pub["name"].encode('utf8').replace("<i>","\\textit{").replace("</i>","}")+"}{}{}{}{"+", ".join(pub["authors"]).encode('utf8')+"\\newline{} \\textit{"+pub["journal"].encode('utf8')+"}, "+str(pub["year"]).encode('utf8')+"}\n")
	print pub["name"]
	
#################################### 

#################################### References
refs = cv["References"]

f2.write("\section{"+refs["name"].encode('utf8')+"}\n")

for i in range(0,len(refs["values"]),2):
		
	ref1 = refs["values"][i]
	
	descr1 = ref1["description"].encode('utf8')
	if ref1.has_key("mail"):
		descr1+="\\newline \emailsymbol \mbox{"+ref1["mail"].encode('utf8')+"}"
		
	if ref1.has_key("phone"):
		descr1+="\\newline \phonesymbol "+ref1["phone"].encode('utf8')
	
	if i+1<len(refs["values"]):
		ref2 = refs["values"][i+1]
		
		descr2 = ref2["description"].encode('utf8')
		if ref2.has_key("mail"):
			descr2+="\\newline \emailsymbol \mbox{"+ref2["mail"].encode('utf8')+"}"
		
		if ref2.has_key("phone"):
			descr2+="\\newline \phonesymbol "+ref2["phone"].encode('utf8')
		
		f2.write("\cvdoubleitem[1em]{\\textbf{"+ref1["name"].encode('utf8')+"}}{"+descr1+"}{\\textbf{"+ref2["name"].encode('utf8')+"}}{"+descr2+"}\n")
	else:
		f2.write("\cvdoubleitem[1em]{\\textbf{"+ref1["name"].encode('utf8')+"}}{"+descr1+"}{}{}\n")

	
#################################### 

#################################### Languages
langs = cv["Languages"]

f2.write("\section{"+langs["name"]+"}\n")

for i in range(0,len(langs["values"]),2):
		
	lang1 = langs["values"][i]

	if i+1<len(langs["values"]):
		lang2 = langs["values"][i+1]
		f2.write("\cvdoubleitem[1em]{"+lang1["name"].encode('utf8')+"}{"+lang1["level"].encode('utf8')+"}{"+lang2["name"].encode('utf8')+"}{"+lang2["level"].encode('utf8')+"}\n")
	
	else:
		f2.write("\cvdoubleitem[1em]{"+lang1["name"].encode('utf8')+"}{"+lang1["level"].encode('utf8')+"}{}{}\n")
		
#################################### 

#################################### Interests
interests = cv["Interests"]

f2.write("\section{"+interests["name"].encode('utf8')+"}\n")

for ints in interests["values"]:
	f2.write("\cventry[1em]{}{"+ints["name"].encode('utf8')+"}{}{}{}{"+ints["description"].encode('utf8')+"}\n")
	
	
	
#################################### 

f2.write("\\end{document}\n")
f.close()
f2.close()
