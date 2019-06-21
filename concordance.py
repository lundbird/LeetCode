import re
from collections import defaultdict
from collections import OrderedDict
# tried to use regex didnt work
# names = "(Mr|Mrs|Ms|Dr|Jr|Sr)[.]"
# location = "(Ave|ave|Apt|apt|St|st)[.]"
# company = "(Co|Inc|Ltd)[.]"
# days = "(Sun|Mon|Tues|Wed|Thurs|Fri|Sat)[.]"
# months = "(Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[.]"
# time = "(sec|min|h|hr|wk|a.m|p.m|mo|yr|cent)[.]"
# measurement = "(in|ft|oz|t|tbsp|tsp|yd|cu|fl|lb|pt|qt|sq|mi|gal|doz)[.]"
# latin = "(i.e|p.p|e.g)[.]"
acronyms = "([A-Z][.])+"
names = ["Mr.","Mrs.","Ms.","Dr.","Jr.","Sr.","Ph.D."]
company = ["Co.","Inc.","Ltd."]
location = ["Ave.","Apt.","St."]
months = ["Jan.","Feb.","Mar.","Apr.","Jun.","Jul.","Aug.","Sep.","Sept.","Oct.","Noc.","Dec."]
days = ["Sun.","Mon.","Tues.","Wed.","Thurs.","Fri.","Sat."]
time = ["sec.","min.","h.","hr.","wk.","a.m.","p.m.","mo.","yr.","cent."]
measurement = ["in.","ft.","oz.","t.","tbsp.","tsp.","yd.","cu.","fl.","lb.","pt.","qt.","sq.","mi.","gal.","doz.",]
latin = ["i.e.","e.g.","p.p"]
numbers = "[0-9]+[.][0-9]+"
end_of_sentence = "[.!?][\" \"](?=[A-Z])" #period space Capital letter means end of sentence

def filter_text(text):
    #filters text so we can tell where sentences begin and end. Tried using regex but now using simple replace
    text = text.replace("\"","")
    total=names+company+location+months+days+time+latin+measurement
    text = re.sub(numbers,"",text) #remove decimal numbers
    text = re.sub(acronyms,"",text)
    for name in total:
        new_name = name.replace(".",'`')
        text = text.replace(name,new_name)
    return text

def generate_sorted_dictionary(conc):
    #takes concordance as input, sorts, and makes inner dictionary with key as count of indices
    sorted_list = sorted(conc.items())
    sorted_conc = OrderedDict()
    for key, indices in sorted_list:
        inner_dict = dict([(len(indices),','.join(str(i) for i in indices))])
        sorted_conc[key] = inner_dict
    return sorted_conc

def pretty_print(result):
    #print format for hackerrank
    for k,v in result.items():
        print(k+ ": ", end="")
        for k, v2 in v.items():
            print("{"+str(k)+":"+v2+"}")

def form_concordance_from_text(filtered_text):
    #takes a filtered text, splits into sentences, reforms words, and creates the concordance
    sentences = re.split(end_of_sentence, filtered_text)
    conc = defaultdict(list)
    only_letters = re.compile('[^a-zA-Z`]')
    for i, sentence in enumerate(sentences):
        for word in sentence.split():
            cleaned_word = only_letters.sub('',word).lower().replace('`','.')
            conc[cleaned_word].append(i+1)
    return conc

def generateAndPrintConcordance(inputLines):
    #Main driver function
    text = ''.join([line+' ' for line in inputLines])
    filtered_text = filter_text(text)
    conc = form_concordance_from_text(filtered_text)
    result = generate_sorted_dictionary(conc)
    pretty_print(result)


if __name__=="__main__":
    text = ["Wait a minute. Wait a minute, Doc. Are you telling me that you built a time machine out of a DeLorean?"]
    generateAndPrintConcordance(text)
