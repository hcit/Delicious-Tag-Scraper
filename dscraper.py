from mechanize import Browser, _http
from BeautifulSoup import BeautifulSoup
import re 



#Extracts links with property rel = nofollow
def extract (soup):
    
    bookmarkset = soup.findAll('div', 'data')
    for bookmark in bookmarkset:
        link = bookmark.find('a',)
        vote = bookmark.find('span','delNavCount')
        try:
            print >> outfile, link['href'], " | " ,vote.contents
        except:
            print >> outfile, "[u'0']"
    #print bookmarkset

    
#File to export data to
outfile = open("output.txt", "w")

#Browser Agent
br = Browser()    
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

tagID= raw_input("Which delicious tag would you like to backup?: ")
url= "http://www.delicious.com/tag/" + tagID
print url
page = br.open(url)
html = page.read()
soup = BeautifulSoup(html)
extract(soup)

count=1
#Follows regexp match onto consecutive pages
while soup.find ('a', attrs={'class': 'pn next'}):
    print "Page:", count
    endOfPage = 0
    try :
        page3 = br.follow_link(text_regex="Next")
        html3 = page3.read()
        soup3 = BeautifulSoup(html3)
        extract(soup3)
    except:
        print "End of Pages"
        endOfPage = 1
    if endOfPage == 1:
        break
    count = count +1


#Follows regexp match onto next page
#page2 = br.follow_link(text_regex="Next")
#html2 = page2.read()
#soup2 = BeautifulSoup(html2)
#extract(soup2)
    
#debug
print "done"
outfile.close()

