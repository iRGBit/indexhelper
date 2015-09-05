# indexhelper

It was the year 2015 and still computers were maily used by humans to chit chat, make selfies and create Power Point presentations. Yet, the power of automation has not been fully exploited yet and there's still highly educated people wasting their time copy and pasting words around in their aacademic texts.

**Indexing should be easy and fun!**

This Python script is intended to eat all your written words and spit out the most common unique words in your text minus common English language wwords. Alphabetically.

**That almost sounds like an index, doesn't it?**

The human can then use this raw information, paste it into their favourite Word document and start from there.

**Usage:**

1. Create a .txt document of your writing and call it sample.txt
2. Open the terminal, navigate to the indexhelper folder and run something like

```
python indexer.py > out.txt
```
The file out.txt contains the desired list of words + count.

Enjoy

**Future improvements will include**

* Some sort of usabilty for non CLI friends
* support for writer's favourite file fomats (.docx, .odt...)
* Page numbers included for a selected set of key words to generate a final index
