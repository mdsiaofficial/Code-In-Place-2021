"""

Title: Oxford Dictionary of English


"""
from urllib.request import urlopen
from html.parser import HTMLParser
print("oxford dictionary of english".upper().center(35),'\n\n')
#Get user's input
user_input = input()
print('You searched :'+user_input.title(),"\n")
link = urlopen("https://www.lexico.com/en/definition/"+user_input).read()
#() => print(link) source code in base64 format
link_text = str(link)
# OOP
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.p=False
        self.pbuf=[]
    def handle_starttag(self, tag, attrs):
        if(tag=="p"):
            self.p=True
            self.pbuf=[]
    def handle_endtag(self, tag):
        if(tag=="p"):
            self.p=False
            print("".join(self.pbuf),flush=1)
    def handle_data(self, data):
        if(self.p):
            data=data.replace("\\n","\n")
            data=data.replace("\\","")
            self.pbuf.append(data)


parser = MyHTMLParser()
parser.feed(link_text)

