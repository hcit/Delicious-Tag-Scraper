from mechanize import Browser, _http
from BeautifulSoup import BeautifulSoup



#Extracts links with property rel = nofollow
def extract (soup):
 links = soup.findAll('a',rel='nofollow')
 for link in links:
     print >> outfile, link['href']
 
 hits = soup.findAll('span', attrs={'class': 'delNavCount'})
 for hit in hits:
     print hit.contents


    
#File to export data to
outfile = open("albums.txt", "w")
#Browser Agent
br = Browser()    
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


#url = "http://www.delicious.com/tag/p2p"
url= "http://www.delicious.com/search?p=varun"
page = br.open(url)
html = page.read()
soup = BeautifulSoup(html)
extract(soup)

count=1
#Follows regexp match onto consecutive pages
while soup.find ('a', attrs={'class': 'pn next'}):
    print "yay"
    print count
    endOfPage = "false"
    try :
        page3 = br.follow_link(text_regex="Next")
        html3 = page3.read()
        soup3 = BeautifulSoup(html3)
        extract(soup3)
    except:
        print "End of Pages"
        endOfPage = "true"
    if valval == "true":
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

