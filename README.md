# indexhelper

It is the year 2015 and still computers are mainly used by humans to chit chat, make selfies and create Power Point presentations. Yet, the power of automation has not been fully exploited yet and there's still highly educated people wasting their time copying and pasting words around in their academic texts.

**Indexing should be easy and fun!**

This Python script is intended to eat all your written words and spit out the most common unique words in your text minus common English language words. Alphabetically.

**That almost sounds like an index, doesn't it?**

The human can then use this raw information, paste it into their favourite Word document and start from there.

**Usage:**

1. Create a .txt document of your writing

2. Open the terminal, navigate to the `indexhelper` folder and run something like
`python indexer.py <yourFile>`
If no arguments are given files/sample.txt will be used as default file.

3. `Select Language from the following: EN DE - default is EN: `

Select from the available languages, if no argument is given, English will be used.

4. `Select name of ouput text file (default is out.txt ): `

Select a name for your output text file. If none is given the file will be named `out.txt`.

The resultined file contains the desired list of words + count.

Enjoy!!!

**Example Output**
Have a look at the example folder for example file outputs, e.g. an [index of the GNU license](https://github.com/iRGBit/indexhelper/blob/master/examples/GNU_license_example_output.txt).


**Future improvements will include**

* Some sort of usabilty for non CLI friends
* support for writer's favourite file fomats (.docx, .odt...)
* Page numbers included for a selected set of key words to generate a final index
* Multiple language support (per request)
* A pony

![image alt](http://www.publicdomainpictures.net/pictures/80000/velka/a-pony-1393433833jWp.jpg "This Pony")

**Contribute**

* Feel free to contact me via hypertext ät birgitbachler dot com for feature requests
* I would be grateful if anyone wishes to contribute to the stop word text file
