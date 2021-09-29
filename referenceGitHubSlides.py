talksPath = 'c:/p/dotnetru/git/Audit_fork/db/talks/'
slidesPath = 'c:/p/dotnetru/git/AuditBlobs/slides/'
githubPrefix = 'https://github.com/DotNetRu/AuditBlobs/blob/master/slides/'

from os import listdir
from os.path import isfile, join, splitext
import xml.etree.ElementTree as ET

# Get all files with slide references
talks = [f for f in listdir(talksPath) if isfile(join(talksPath, f))]

# Get all slides
slides = [splitext(f)[0] for f in listdir(slidesPath) if isfile(join(slidesPath, f))]

for talk in talks:
    talkPath = join(talksPath, talk)
    talkName = splitext(talk)[0]

    talkDetails = ET.parse(talkPath)
    tree = talkDetails.getroot()
    slidesUrl = tree.find('.//SlidesUrl')
    if slidesUrl == None:
        continue
    
    if (talkName in slides):
        newUrl = githubPrefix + talkName + ".pdf"
        print(talkName + ": " + newUrl)
        slidesUrl.text = newUrl
        talkDetails.write(talkPath, encoding="utf-8-sig", xml_declaration=False)
    else:
        print(talkName + ": NONE")