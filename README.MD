1.environment
    python 3.5 scrapy 1.5
2.install
    pip install scrapy
3.explain
    in fact  I dont know about spanish
    so in the csv ,I have all the column in ,
    have fun
4.usage
    cd toctoc
    scrapy crawl toctoc -o output.csv
    if you want to search something use :
        scrapy crawl toctoc -a text=thewordyouwanttosearch
    if you want to compare with the old version
        edit toctoc/settings.py    line19  COMPARE_FILE   (better absolute path)
        then run scrapy crawl toctoc -a text=thewordyouwanttosearch -o output.csv
        there will be an another file named 'update.csv' include old and new info
    -o  the file you want to output
5.params
    there are many params in the site, i can not list them all
    maybe you can find them in the chrome devtools and get the params
    then edit spiders/csvfeed.py  line 90
    to what you want
6. the params dont work ? i have a try ,but worked
    maybe when you run the crawl ,there is an another process using it
    so the change was rejected
