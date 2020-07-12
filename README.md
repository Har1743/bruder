# bruder

This is command line based tool used to find existing/hidden web objects on any web application by brute forcing any directory based wordlist.

# How it works 

There is an inbuilt default wordlist which contains thousands of words which brute force the web content of any web application or you can also give your own wordlist in it. It searches for all the hidden web objects on any website or server by brute forcing as it gets a word from wordlist and checks the response one by one from the website and gets back a status code from the website, web objects might be .php .txt or any admin page/portal which might be malicious or vulenerable to attack.

# Arguments used 

**--url :** This argument is mandatory which takes a host or website on which you want to find brute force the web contents.<br/>
**--valid, -v :** This help you to know about all the valid responses.<br/>
**--invalid, -i :** This help you to know about all the invalid responses.<br/>
**--all, -a :** This help you to know about all the responses.<br/>
**--output :** This will save all the output to a file of your desired location.<br/>

# Usage 

**git clone https://github.com/Har1743/bruder.git** <br/>

And then just run using <br/>
**python3 bruder.py**

# Created by

[GITHUB : Har1743](https://github.com/Har1743)

