# Uasi Book Translator

### Summary
UasiBookTranslatorPython is a Python application used to translate books and various other large text files from English to Uasi. The primary goal is to translate with 100% accuracy from English to Uasi.

### About
Uasi is an artificially language created by the Hershkovitz bros. The purpose is twofold:
1) having an encrypted means of communicating to one another
2) Having fun learning an unusual language
3) Connecting with our ancient Uasin heritage

If you are not familiar with Uasi, please refer to the [Official Website](http://uasilanguage.online)

Uasi's rules are not very complex, but there are still certain principles that must be followed in order to translate accurately from English to Uasi, or vice versa. [The Guide](https://drive.google.com/file/d/1dej4qjnA0S3Yw0IpKd5oEL2YkW4-OAcd/view?usp=share_link) is the definitive source for learning the rules of this language.

What makes automating the translation process from English to Uasi difficult is the wide array of irregularities and inconsistencies contained in the English language. Thanks to the Python library, [spaCy](https://spacy.io), the task went from impossible to conceivable.

### Setup

* Install and import the [spaCy module](https://spacy.io/models) (ensure you choose the module for "accuracy")
* Run the Python program

### Input / Output
#### Book "The Godfather" by Mario Puzo, gotten from [archive.org](https://archive.org/stream/in.ernet.dli.2015.99009/2015.99009.Mario-Puzo-The-Godfather_djvu.txt)

<table>
<tr>
<th> Input </th>
<th> Output </th>
</tr>
<tr>
<td>

CHAPTER ONE 


Amerigo Bonasera sat in New York Criminal Court 
Number 3 and waited for justice; vengeance on the men who 
had so cruelly hurt his daughter, who had tried to dishonour her. 

The judge, a formidably heavy-featured man, rolled up the 
sleeves of his black robe as if to physically chastise the two 
young men standing before the bench. His face was cold with 
majestic contempt. But there was something fake in alfthis 
that Amerigo Bonasera sensed but did not yet understand. 

‘You acted like the worst kind of degenerates,* the judge 
said harshly. Yes, yes, thought Amerigo Bonasera. Animak. 
Animak. l^e two young men, glossy hair crew cut, scrubbed 
clean-cut faces composed into humble contrition, bowed their 
heads in submksion. 

^The judge went on. ‘You acted like wild beasts in a jungle 
and you are fortunate you did not sexually molest that poor 
girl or rd put you behind bars for twenty years.* The judge 
paused, his eyes beneath impressively thick brows flickered 
slyly towards the sallow-faced Amerigo Bonasera, then 
lowered to a stack of probation reports befdre him. He 
frowned and shrugged as if convinced against his own natural 
desire. He spoke again. 

‘But because of yotir youth, your dean records, because of 
your fine families, and b^use the law in its majesty does not 
seek vengeance, I hereby sentence you to three years’ con- 
finement to the penitentiary. Sentence to be suspended.* 

</td>
<td>

 cheptir uni 


 Amerigo Bonasera sotL oin New York Criminal Court 
 Number 3 upa weotL fosi jastoci; vingienci oin osi menT whu 
 hevi su craillS hart hos deaghtir, whu trSL ta doshunuar sha. 

 osi jadgi, ikaku furmodeblS hievS- fietarid men, rullL ap osi 
 slooviT uf hos bleck rubi es opho ta phSsocellS chestosi osi twu 
 Suang menT stend bifuri osi binch. hos feci baL culd woth 
 mejistoc cuntimpt. wula thiri baL sumithong feki oin elfthos 
 thet Amerigo Bonasera sinsiL wula Sit andirstendLX. 

' Sua ectL loki osi bed kond uf diginiretiT,* osi jadgi 
 seSL hershlS. Sis, Sis, thonkL Amerigo Bonasera. enomek. 
 enomek. l^i twu Suang menT, glussS heor criv cat, scrabbid 
 clien- cat feciT cumpusid ontu hambli cuntrotoun, buvL thior 
 hiedT oin sabmksoun. 

 ^thi jadgi guL oin.' Sua ectL loki wold biestT oin ikaku jangli 
 upa Sua ba furtaneti Sua sixaellS mulistLX thet paar 
 gorl ur rd pat Sua bihond berT fosi twintS SierT.* osi jadgi 
 peasiL, hos iSiT binieth omprissovilS thock bruvT flockirL 
 slSlS tuwerds osi selluv- fecid Amerigo Bonasera, thin 
 luwirL ta ikaku steck uf prubetoun ripurtT bifdri ha. ha 
 fruwnL upa shragL es opho cunvoncid egeonst hos uwn netarel 
 disori. ha spiekL egeon. 

' wula biceasi uf yotir Suath, Suar dien ricurd, biceasi uf 
 Suar foni femolST, upa b^asi osi lev oin ots mejistS 
 sookX vingienci, o hiribS sintinci Sua ta throo SierT' cun- 
 fonimint ta osi pinotintoerS. sintinci ta saspindid.* 

</td>
</tr>
</table>
