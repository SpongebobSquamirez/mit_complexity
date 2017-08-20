#! python3

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import re
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import pickle
import os

def get_project_data(filename):
    #read in the file, while has format: id,url\n
    with open(filename, 'r') as f:
        url_list = re.split(',|\n',f.read()) #split on newlines and commas
        url_list = url_list[2:-1] #remove some useless entries from start/end
    i = 0
    ids = []
    urls = []
    while i < len(url_list)-1:
        ids.append(url_list[i])
        urls.append(url_list[i+1]+'/description')
        i=i+2
    with open('project_ids.pickle','wb+') as fileObject:
        pickle.dump(ids,fileObject)
    with open('project_urls.pickle','wb+') as f:
        pickle.dump(urls,f)
    return ids, urls

def make_description_url_pickle(filename):
    with open(filename, 'r') as f:
        modified = f.read().replace('\n','|') #split on newlines and pipes
        url_list = modified.split('|')
    i = 0
    urls = []
    while i < len(url_list)-1:
        urls.append(url_list[i])
        i=i+2
    print(urls[-1])
    with open('description_urls.pickle','wb+') as g:
        pickle.dump(urls,g)
    return

#def get_list_of_pages_with_category(category):
    
def get_category(file_string):
    """gets the top-level category of the project"""
    search = 'some_string'
    start_index = file_string.find(search)
    substring = file_string[start_index+27:start_index+45]
    category = re.split('\?|\%|/',substring)[0]#.split('?')[0]
    #category = category1.split('%')[0]
    #print(category)
    return category

def successful(parsed_html):
    """returns 1 if the label is true, and 0 otherwise"""
    success = [item['some_string'] for item in
               parsed_html.find_all(attrs={'some_string' : True})]             
    if success[0] == "successful":
        return 1
    return 0

def get_thing1(file_string):
    """returns some stuff
    takes in a string containing stuff to extract
    """
    search = 'some_string'
    start_index = file_string.find(search)
    substring = file_string[start_index:start_index+60]
    
    #splits substring and takes numerical part
    var_x_11 = substring.split('>')[1] 
    var_x_12 = var_x_11.split('<')[0]
    var_x_1 = re.sub(',','',var_x_12)#[1:]
    var_x_1 = re.sub(r'[^\d]+', '', var_x_1)
    return var_x_1

def get_name(file_string):
    """returns the name"""
    search = 'title="some_string" href="/some_string/'
    start_index = file_string.find(search)
    substring = file_string[start_index+42:start_index+71]
    var_x_3 = substring.split('/')[0]
    return var_x_3

def get_number(file_string):
    """ returns a number of things"""
    search = 'some_string'
    start = 'some_string'
    end = 'some_string"'
    start_index = file_string.find(start)
    end_index = file_string.find(end)
    var_x_2 = file_string[start_index:end_index].count(search)
    return var_x_2

def get_links(file_string):
    """return the number of links"""
    search = 'a href='
    start = 'some_string'
    end = 'some_string'
    start_index = file_string.find(start)
    end_index = file_string.find(end)
    links = file_string[start_index:end_index].count(search)
    return links

def get_yeah(file_string):
    """counts the number of individual var_x_4 on the page"""
    search = 'some_string'
    var_x_4 = file_string.count(search)
    return var_x_4

def has_var_x_7(parsed_html):
    full_text = parsed_html.find('div', attrs={'class':'formatted-lists ' \
            'some_string'}).text
    if full_text.find('patent') != -1:
        return 1
    return 0

def num_var_x_5(file_string):
    """returns the number of var_x_5
    ....function might need some refining"""
    search1 = "some_string"
    search2 = '<iframe'
    var_x_5 = file_string.count(search1) + file_string.count(search2)
    return var_x_5 - 1 #subtract 1 to normalize

def has_num_var_x_6(parsed_html):
    """returns 1 if some_string and 0 otherwise"""
    num_var_x_6 = parsed_html.find(id="some_string")
    if num_var_x_6 is None:
        return 0
    return 1

def description_length(parsed_html):
    """returns the number of human-readable (shown in the browser)
    non-space characters in the project description section"""
    #parsed_html = BeautifulSoup(file_string, "lxml")
    full_text = parsed_html.find('div', attrs={'class':'formatted-lists ' \
            'some_string'}).text
    sub_text = re.sub(' |\n','',full_text)
    return full_text, len(sub_text)

def find_people(full_text):
    tokens = nltk.word_tokenize(full_text)
    #pos_tags = nltk.pos_tag(tokens)
    return #nltk.ne_chunk(pos_tags)

def complexity_1(full_text):
    """returns the complexity.
    Accuracy depends on corpus used."""
    count = 0
    #We want all the words, including repeats (use set(words) for no repeats)
    filtered_words = []
    words = nltk.word_tokenize(full_text)
    for word in  words:
        if word not in stop_words:
            filtered_words.append(word)
    for w in filtered_words:
        if w in TechCorpus:
            count += 1
    if len(filtered_words) == 0:
        return 0
    return 100*count/len(filtered_words)

def optical_char_recognition():
    
    
def parse_project(ids, urls):
    """generator that takes in a list of projects and urls
    and yields the data for a given proejct in a format
    that can be inserted into the project database"""
    for project,url in zip(ids,urls):
        try:
            with open(project+'.html', 'r', encoding="utf8") as f:
                file_string = f.read()
                #specifer parser and parse webpage
                parsed_html = BeautifulSoup(file_string, "lxml")

                category = get_category(file_string)
                var_x_1 = get_thing1(file_string)
                var_x_2 = get_number(file_string)
                var_x_3 = get_name(file_string)
                links = get_links(file_string)
                var_x_4 = get_yeah(file_string)
                var_x_5 = num_var_x_5(file_string)
                
                full_text, description = description_length(parsed_html)
                
                num_var_x_6 = has_num_var_x_6(parsed_html)
                var_x_7 = has_var_x_7(parsed_html)
                label_1 = successful(parsed_html)
                complexity_2 = complexity_1(full_text)             
                yield [project, var_x_1, url, category, var_x_3, 
                       var_x_2, links, var_x_4, var_x_5, description, 
                       num_var_x_6, var_x_7, complexity_2, label_1]
        except Exception as e:
            print(str(e))
            print(project)
            print(ids.index(project))
            return
    

def insert_project(*args):
    query = "INSERT INTO Project(projectId, var_x_1, var_x_3, num_var_x_6, " \
                         "var_x_7, var_x_4, links, var_x_2,description, " \
                         "complexity_2, category, url, label_1, var_x_5) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    #print(query, args)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        """if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')"""
 
        conn.commit()
    except Error as error:
        print(error)
        print(args[0])
 
    finally:
        cursor.close()
        conn.close()
 
def main(*args):
    global TechCorpus
    global stop_words
    start = args[0]
    end = args[1]
    #magic file name - should be in the current directory

    with open('project_ids.pickle','rb') as g:
        ids = pickle.load(g)
    with open('description_urls.pickle','rb') as h:
        urls = pickle.load(h)
    with open('COCAacademicSci.pickle','rb') as f:
            COCAacademicSci = pickle.load(f)
            """only use the less common tech terms
            (so that more techy/designy things stand out more"""
            TechCorpus = COCAacademicSci[-600:]

    stop_words = set(stopwords.words('english'))
    
    resume_from = ids.index(start)
    go_until = ids.index(end)+1
    ids = ids[resume_from:go_until]
    urls = urls[resume_from:go_until]

    
    for [projectId, var_x_1, url, category, var_x_3, var_x_2, links, var_x_4, 
                var_x_5, description, num_var_x_6, var_x_7, 
                complexity_2, label_1] in parse_project(ids, urls):

        
        insert_project(projectId, var_x_1, var_x_3, num_var_x_6, 
            var_x_7, var_x_4, links, var_x_2,description, 
            complexity_2, category, url, label_1, var_x_5)
 
if __name__ == '__main__':
    print(os.path.basename(__file__))
    main('0','2800900900')
