#how to run
#python clean-raw-tweet-data.py file-to-be-cleaned.txt save-result-in-this-file.txt

import sys

before_filename = str(sys.argv[1])
after_filename = str(sys.argv[2])

print(before_filename)
print(after_filename)

stopList = []
stoplistfile = open("stoplist.txt", "r")

for stopWord in stoplistfile:
    #stopWord = stopWord.replace("'", "")
    stopList.append(stopWord.replace("\n", ""))
stoplistfile.close()


beforefile = open(before_filename, "r")
afterfile = open(after_filename, "a")

for line in beforefile:
    
    items = line.split("\t")
    username = items[1]
    tweet = items[4]
    
    #tweet = tweet.replace("'", "")
    tweet = tweet.replace("?", "")
    tweet = tweet.replace(".", "")
    tweet = tweet.replace("!", "")
    tweet = tweet.replace("@", "")
    tweet = tweet.replace("$", "")
    tweet = tweet.replace("%", "")
    tweet = tweet.replace("^", "")
    tweet = tweet.replace("&", "")
    tweet = tweet.replace("*", "")
    tweet = tweet.replace("(", "")
    tweet = tweet.replace(")", "")
    tweet = tweet.replace("[", "")
    tweet = tweet.replace("]", "")
    tweet = tweet.replace("{", "")
    tweet = tweet.replace("}", "")
    tweet = tweet.replace("+", "")
    tweet = tweet.replace("=", "")
    tweet = tweet.replace("-", "")
    tweet = tweet.replace("_", "")
    tweet = tweet.replace("~", "")
    tweet = tweet.replace("`", "")
    tweet = tweet.replace("\"", "")
    tweet = tweet.replace("\\", "")
    tweet = tweet.replace("/", "")
    tweet = tweet.replace(",", "")
    tweet = tweet.replace("<3", "")
    tweet = tweet.replace(">", "")
    tweet = tweet.replace("<", "")
    tweet = tweet.replace(":", "")
    tweet = tweet.replace(";", "")
    tweet = tweet.replace("|", "")
    tweet = tweet.replace("\n", "")
    
 
    cleanTweet = ""
    

    for word in tweet.split():
        #remove word that uses # not as a hashtag
        if "#" in word:
            if word[0] != "#":
                word = word.replace("#", "")

        # remove URL
        word.strip().lower()
        isUrl = word.startswith("http")
        if word not in stopList and not isUrl:
            cleanTweet = cleanTweet + word + " "


    # remove null tweets
    if cleanTweet != "null ":        
        afterfile.write(username + "\t" + cleanTweet + "\n")
            
beforefile.close()
afterfile.close()
