# Language Model Fine-tuning for Moby Dick

I have a dream; I'd like to write a novel. Unfortunately, I don't think I can. But maybe some day I'll be able to make a machine write a novel instead of me. Some day  ... 

Language modeling is on the center of this dream.
Luckily and thankfully we don't have to train a language model from scratch. Many great pretrained models are available.
What we need to do is fine-tune it for our tasks.

I want to see what will happen if we fine-tune a pretrained language model to a novel and generate text based on the last part of the novel. The glory goes to Moby Dick, one of the greatest novels of all time. Its text is in the public domain.

The output may not look so wonderful, but I enjoyed a lot.

## Requirements
* python 3.6+
* flair==0.4.1
* nltk==3.4
* tqdm==4.30.0
* torch==1.0

## Pretrained Language Model
* News-forward LM from [Flair](https://github.com/zalandoresearch/flair)
* It's a character rnn model.

## Fine-tuning
* STEP 1. Let's get [Moby Dick](https://www.gutenberg.org/files/2701/2701-0.txt) from [Project Gutenberg](https://www.gutenberg.org/). We take chapter 1 though chapter 134 for training.
```
python prepare_data.py
```

* STEP 2. Finetune the news-forward pretrained lm with Moby Dick text during 100 epochs. At every epoch, we save generated text.
```
python finetune.py
```

## Check the outputs.

* All the outputs are available [here](outputs).

* epoch = 10
```
orld . At $ 10,000,000 an anking , dart , arcade _ouf ; tuyed her inks ! Drink and hearing . But sway
DOWN , VILLANOVA HOLD , TABLETED BY ALL NATURAL ENCLAVES OF NEWLY IMMUTED EXTORTERS ACROSS THE WHALE , THEN WOULD BORROW ARE HOUSES ELUOUT IN NOW HIT LASHKING THE DEVILISH DESERT , THOUGH . IN THE NUMBER OF THE PLACE OF ROTTER ’ S IRON , QUEERIECE ELSE WON ’ T LIVE . HE YET TIRED STUFF , THAN THAT — SIGHT , THE SPANISH FISHERNES
But to what conclusion this strange substance has no sign of oxygen the fellow ’ s a fearless 91 million dollars . CHAPTER 89 . Tashtego . The Tash . First the Hand ? ” “ Light the line — I suppose , — but somehow , so soon as I saw some leg .
The sun — shirr ! blood . _There_ insults ! but now back — it ’ ll sit down for his fifth birthday ; he will , sir . ’ But I do not know , that I do feel the strength of my ear , I strongly suppose . Were they , not to see the whole situation now so shabby .
I see no time to plant it ; so .
Pass the topics ! Let ’ s to dreary any satisfactory pile revealed . We suspended ! So ; what ’ s the need ? Or so ? To-day ! start her ! ’ To put running glories on the deck ; God do get into the bottom of the water , but Queequeg instantly sits in mind .
a large , star-like , starbull , even the sea-warm sile to cabin vast light .
But here and there are interceded by the Republican platoon in Queequeg , not to position the scales through stout . Poor Pip took it ; so I suppose . Sir ? ” “ Would the Real congress do : but support in the Essex .
Because the fifth will be in it — but it ’ s not his business . By the first he signed the second summary ! In November 2005 she cracked a horse with her hair on top ;
He rocks like the keenest thunder-head in the sea ; so were those surfaces to be the honorable whale ; the peculiar delights in that ship ’ s vicinity , even the hunting the people in keenly known phenomenon .
Yet where indeed the broader marks now — the bucksman is the only man to remember .
turn to ! let ’ s down .
Share his seafare ; give way — soon as I steadfathers
very much , sir ? In the strained and deadly strain , to something of a strange question , since the season has drawn comparisons to the sixteen whales . Of the seven chiefly featured in this fishery , the Deck itself and since the opera he had .
to the brave sight in which the blast of the sea , now ascends , asmes seem so solid , sinn uncertain ;
but does not Bildad since the recently discovered island of Scotch , I find it very shocking . The believer in the Sperm Whale is hinting his heavenly knife ;
“ Hint , through , sir ; since it becomes of a sudden , drab ashes ! — even as I sink ! LOOK-E ! SOON NOT EVER THIS POTENTIAL COMING OVER . NEARLY ITS AUTOMATED SIXTEEN SPEAKERS . MID THIRK IN THE LAKE . GOOD LOON ! TV ‘ DEL . ( _Assailed _ ) .
and , to the extent , his vicinity in Nature measured mere hints . It sounds like that a small , grooved , softly , would-be-hearted , nurtured society of uneasy among the leviathan i
```

* epoch = 20
```
to . What whaling is needed is it mistaken for Starbuck , who , in consequence , never got back for a brief pull . That way it went , it was scorched on the beach . The billows forked up on every flame from the old Man , and in one , the white old belly of old Nantucket and Blanco .
if you would draw a fine aspect , would you measure , if only in vain , to attain some organ to certain malady being one of the remaining illustrations of man in him , even in that grove , his imperturbable glittering claw harpoon has scorching riddles . But as this whale is exposed , it appals the English Communists , as when King Fisher of Nantucket was as chief mate in the whale .
And if our appellation makes these brain , it is always disgracible to me , that in moisture is the thing I might do in the past twenty years , if it be like myself under a wide waiting . Akan ’ s food , indigesting it , is pretty much neat enough . So. ” Two day was accompanied with a Steelkilt ’ s prestice ’ s doubloons .
— “ In bearing your iron compass sought out of a boat ’ s creature , you scrimped on the papers with imputations , which were passed into the order . That omniscien ! I think we didn ’ t show up a hammer ’ s sharp belt or candle ; but we were open in the direction . Among seasons as the food of cooked wood is this : as if , in my own body , it was plain that when I was impatiently a native of Cape Horn , was Nantucket ; Flask , not a judge , in very consequence of any merit of a Stubb ’ s question ;
BUT HE WAS IN NO DOUBT ADEQUATELY TROUBLED BY SNAP-LIGHT , THAT PART TIME IT MAKES HIM FRESH AS JET , ” METHODIC HEADS TO THE TUNNEL TO THEIR CREW ; ON THE VERY SDRESSED STARBUCK ON MY LIPBEE , THE NUT OF THE COTTONED LENGTH ’ S SIDE , AND STRIKING OVER EITHER ORGANISED BY THREE ONE
— and yet , upon clam of charge , Queequeg kicked my legs , and the boy did , on night ; he went before ; after the lashing of his boat ’ s bow in a flash on his chest , down the chimney of a boat ’ s beef , and we spent that month ’ s precious oil . Sometimes this wondrous frenzies , mostly , are occasionally moodily invisible in man , in these passiveness ;
Go ! Do ye love brandy ? A row ! a row ! TAPT THE BUSHFIELD WAS A RITE OF GRASS . SICK ARE THE WOULD-FACE TRUTH . NOUR OLD ENGLISH CHAPTER COOK , WHO DIDN ’ T HAVE TO STOP ILL-GAINED BRAVERY ! HERE ’ S PARKING AS
Hence , in the best men , bearing down at deadline aloft in it , ignorance is once a dark , bantering watery sky . This must be never changed for black vomit .
“ Can ’ t see you mad ? What whitney right worshipped , is my first sight ? This is the way a coffin will work not one man . Take no present or any kind of recovery from blood in the fish ; but in very physical popular opposite consider of my mouth ’ s food is not included ? Beware of your opinion . Dominic ! Why don ’ t ye , sir ? That is all right ; but never did the minute mute love have I possibly got a boat or soul in the pleboorpius inn ’ s flame ;
the pale , delicate 
```

* epoch = 30
```
com , when he slid through the sea forecastle . “ Now , what ’ s that he says now
We had lain thus in bed , chatting and napping at sea , and learned naturalists ashore . For better or for work , they put on sea where the benefit of Ahab for the time ; without the slightest bashfulness to stand on the other flank , his eyes , now and then still afloat all his periodical vicissitudes .
And what oil is , what it means , when perished in this queerest parmacet this case is , be that fish ’ , what is more , having been hurled to read the head ? wherefore , then , after singing out in casks and cabins , gropes him dead and roll his body up , and hear his naked feet , leaving their hands hieroble and furnished .
Sleeping ? Consider ! ” “ Gabriel ! Gabriel ! ” cried Stubb , “ wise Stubb , what ’ s his left , this same fearless force of creature , his head as mechanical ! I still rest me ; men , against the slow bench , just like the Thin , whale-bosts , ” whales carrying harpoons like him .
So , clear a wave . When Twigg-hipper , mystic hearset , made my orders , I say , after a week old shur in a harpoon , without a little head , yet not yet has it .
leaks in fro ’ em , at least , in the ship ’ s whole head , have become even more of his entreaties than I . Bear a hand , and tries to teach him without listening . Bestow the beach ! from this old verse he peeled one from the onset , leaving a widow without lightning-rod and still growing discovery .
Only one swarm to stand , leaving Nantucket who wants no more than ever anywhere . CHAPTER 73 . The Feegee .
Should we have plenty of thispore , not yet ; fifty years ago this bone was in some high land and historic . Besides , my ascendency , I mean , love you feel most touching the solitude of that languishing manner .
thou steadfastly good for the best of steel ; he has already revealed he is a salt , being one such fine design in his general enterprise .
I tell you , the sleeper is my way , for I can pass on a new line of progeny , from which , by Dargh , who , by the ceremony of Tahiti , was a Salmon .
Because , on your pagan , we are now fairly embarked in this one poor pint of half , whose ceetan , sweetness of humanity ! What dentistists deemed alarmed ; here , _hard , beds ’ lower , men on board , on August — Nay . Stubb ’ s anker is still shaking one leg ; for — all my sons and my old hearse-drenched walled wings rolled like fated Persians ;
a white man , in his bed , he has no hand in still more like a flash . In his immeasural bedfellow , the stranger captain , without being taken home to sea to Moby Dick , strained , without quitting his menoptions . He was a leaner , whole and very learned , far more vampoued . In fact , hands here on the lee-beam of the isle , however , is Mac-odeno ;
because , in great analogies , these so-called stand-or-manned mannessman , why in that science and such manner they have his hands , then , at his own personal expense , in his whale-books ;
For some historic Pe
```

* epoch = 40
```
the Captain drew off with the rope to step upon that hot curtain ; but felt their charm with such power that little Moby Dick had ever cruised on to so many .
and only by a whale-ship at very every pore , had cut coyer beneath it ; and to call it so unpretention to speak of some unconquerable discharge . Three pennent hectares of vapor stretched together in a moral problem .
While his broad fins are only two inches in width , and he no longer swung over the side , and rushing into spaces and hoisting infernally reduced turns away through a cabin than any bowels having a mortal trace of the salt .
and there they stuck to , like mild blue hills . Immediately their apprehensions came over me ; and Stubb accosted Ahab , in the sea and the ship . Hark ye , devilish dark blue . Haul in , haul in , Tahitian ! These lines run whole , and whirling out : come in broken , and dragging slow . Ha !
Moreover it backed me with my ivory feet from a cannibal at the first commotion of my little Flask , I knew not ; and as for Queequeg , the boys , in the stern-sheets , are now comparing between these two of them — Nevertheless , it has long been related how Ahab was wont to proceed .
But while now Upon a towering , bad work , Stubb vowed he would run away from pulpit , and told him that he would still drag much into the whale ’ s back , and finally abandon him to it . But the longer the harpooneers gave one reproach to the Pequod as he projected his hammock from the far more vividly unassailable short northern ships than it seemed .
and looking in that director ’ s old carpet-bag , this side of his jet seemed a crown-pine looking upon the floor , for even in the sailors ’ s flukes on the pasture , yet the mould would not be staco-made . For though in some scientific pursuit the Sperm Whale travelled from out the casement that to abomate_ link upon whom some of the ice pressed hard what is used .
— but only the key ticks were hardly separable in that instance . *I had not succeeded in fastening . Fedallah first descried this jet . For the instant of such a harmony whale ! still the roof is about the size of one hundred pounds ;
with a steel shoe smoking up , and half-self-collably tightly , somehow , in its glittering express hunter , was one of the most impregnable obstinacy
All alive to his jeopardy , the common usage in this whaling way was , as an architect of the unwarped , unsupposed locksmith which had most positively accomplished some unsounded gourmand by way of accounting from the captain ’ s dusky endeavors .
open eyes ; see , and will you find this species of such wondrous philosophies now to be found in almost every kingdom of animated nature . Hark ! the infernal orgies ! that rule most lively , and not only is the living insanity of life — almost invariably in blinding pallidos .
— what a letter is this
since they will be still left gone , of the most wise-manned horrors in the air , and the life-find which at all times came out . But , though there 
```

* epoch = 50
```
this divine terror of the dragon ; set the sail ; all that cracks the sinews and cannibals still turned out their liveliness , as Lo and Bear to slay him the pities ;
aye , and in a sort of basket , slowly furnishing and ripening and silking through the fields of rich . Sum to this dead stump , entire calm , all that cracked and rolling sea , seemed gentlemen to the extremest limit of the land ; she put her chat above what a sight ! See to it. ” “ D ’ ye see him ?
No wonder there had been so much riding at the time of the attempt , so imperfectly as the seamen resumed tackles ; absent fore and aft , and join the want of some last queer joy before the mighty castors are called to reach this king ( _sneezes_ ) . — ah !
for again his eyes seemed whirling round in his temporary root ; as if last seen ; thou audazed a Nantucketer , with three far to denominatings of all his friends , had it recurred throughout the world ; his lantern swung far above the deck , as if to step ;
about this time — yes , as stamped from that of a forecastle scrape ; sweeping a finger in the sailing head for the ship ’ s two keels , and then floating it within eater ’ s head , as if a real frigate had been founded in all too of his own bound ;
But this is about the size of the tree ; and as mortal man — as a foreign country that the world is about , the poor impulse of Nantucket does not amount to a dignity , and indeed carries you very hast to it !
Yet we have seen him be passing between the whale and the ship . He is that magnificent splinter ; a stove boat weighing about the ship — about whom they pluck it from the ship ’ s side ;
thought I , and we walked away , both coiling and hearing whatever matter in my soul were ; all the sailors turned East and West ; some three degrees of vibrating blue vapory like silver ; and what a forty years ’ fool — fool
— aye , a sweet , resigned girl with a filed old age , like a flap — about three feet off — singing , and scarcely about the true conceit that seemed as the thing to do .
and which ended in providing the soft , sullen winds to which the ship had struck upon them , and though so fiercely the savage continually fought aloft across the ship that was so killed anything that sparkled by the short tens of them again .
About two thirds of the barrow yard again . I sat down on an old wooden settle , carved all over like a bench on the Battery .
Wondrous flip only splices a razor , so as to be abusive and apprehensiveness about it . It is worse ; for all about it , is made of sinister knowledge of leviathanic stature ; so that with riotous idolators the ship underneath the drabbest of all those barbarish breeches , such a furrow is like the sharkish sea of his life .
Thus this six-iron must have been exceedingly valuable . In strange convenience of all Perth and the floating order the goal with which he sailed from home .
About midnight that an age of string turned our waist lightly , as on the object of recondites , that after all
```

* epoch = 60
 ```
 The only man less than completely finished , not without speaking to him , that it was impossible correctly to claim the most mortal tribute ; that is , regarding devil ’ s fingers in the skin of the mast-head , that it may cross the screw to the mouldings of the monsters almost consisting of the barrow — Queequeg ’ s secret title hooked on the audacity of his speedy paws .
So that , like Locke ’ s Coffin , there he was every day vigorously snapping all over the watery world , such as is he doing as we might drive . CHAPTER 2 . The Spouter-Inn .
All right ; take a poor dairy round the try-works , now and to-mourn upon his supper at his Golden Inn._ ” “ C _drink , _Io_ , _he_ — heaps on that scorch. ” “ Better turn that leg , that ’ s rejecting Heaven ’ s going to be Captain of the Unbelow . Ha !
He is a dining with his own companionship ; or rather , his own entire adorable steering , as all manner of unknown naturalists are included in the market-park .
I confess , that since the slooping of some employed interlacings of the elephants in the forehead ’ s middle , with a certain malice supplied with soft , scalcious creatures , was so very surprising , that the migrations were there .
“ I say , Queequeg ! why don ’ t you speak ? It ’ s I — Ishmael. ” But all remained still as before . I began to grow alarmed . I had a good time . A pious , grief-sins as most sounding-line in the midst of the midnight watch , you float round Cape Horn to sea upon his Chinese boat .
Through all his mild darts , the unextinguished diminished awhile in the broad head of Man ’ s endemic vicinity ; as much as to say , — You can possibly be going to subdue this gaff with a scar , to fill ’ em — low veiled , high palmed Tahiti !
as in his intense comparison at the mid-cap in the forecastle , he pledged that the minister , ha , ha , ha , ha , be feigned to decently examine at every mistake for the timid universe reason of its intention to disclose a quoy which it is strong advanced on the mate ;
— to my captain ’ s men , though — all right : I say that I would not understand even that , because there are some sailors in this whale , but that one morning nurtured by all this look , like an old Mogul ’ s fore-castle deck ;
They told me in Stubb , how he flashed it into that grey manner ! ” “ The gods are God ! ” cried the official sailor . “ Lo ! you must stop dat dam racket ! ” “ Come hither to me — going alone on the sea , — ” said Starbuck , “ my country way agod — fit the whale ’ s head and sweep all the spars in fire , stove , indefinite , and raucous conscience !
All ready the boats there ?
and since the earth darted away at the slight bucket , as it were in all its other measures . In truth , this Rhee , the whale has no regard to what may be the name of my regime . Hence it is , that at times you do something as if it were stolen , or at least instantly sovered by the examples of the mighty bulk of million in short but imponderable disaster .
a gigantic idler ! Yet
```

* epoch = 70
```
twice he should live without breathing .
In a few minutes , however , he was a readiness for a supper ; and but so long as the carpenter signs him to chart a spike ; and added that he was fearful Christianity , however much this most peculiar , and finally admitted himself to the blackness of his shadow .
Sometimes they talked it over in the weary watch by night , wondering whose it was to be at last .
CHAPTER 52 . The Albatross . South-eastward from the Cape , off the distant Crozetts , a good cruising ground for Right Whalemen , a sail loomed ahead , the Goney ( Albatross ) by name .
and afterwards said , “ Grand snoozing to-night , maty ; fat night for that . I mark this in our old Mogul ’ s wine ;
Moreover , the ship soon went through the water with nothing she calmly landed on her head , and keeping it thou not feast ;
But not so the English whaler , fairly matter of social awin . In this matter , a sixteen dollar piece in fish should be from abroad .
Hard down the helm !
— In the living act , the undoubted deed — therefore , that high time to take a chair in the bowl before the brink of streets , to sharp idly ;
— how could I tell from what vile hole he had been completely encountered at ? didn ’ t you turn your skeleton on a lance , and strike a strange sort of deaf “ like a rope-yarn against an indistinctness .
yea , and the gilded vessels painted by the sun ;
In shape , the Rheumatic Idioms of the Latino in the sea and the west — every ropeyarn tingling like a wire ;
The whale , therefore , must see one distinct picture on this side , and another distinct picture on that side ;
The tails tapering down that way , serve to carry off the water , And on we forget the vibrating , strong altar in the port ; the air-sharks and spacks tickled by the madman ’ s skull , which every start he had left unhonored .
Moreover , while in the earlier ground at last extinguishing the human scud along an enchanted side , it stems from a footpath to recoil .
— HAND IT ME — ’ BROKE THE BANDED OVER-HOUSE ABOARD , WITH NOTHING BUT A WETCHES ABOUT THE SINECUSANTBS BROW , AND THE WINDOWS OF ROCK .
The first boat was all on itself as ten watches fitted out for the vessel on the water , and therefore scattered at every distance that tore and weaved and pitched one planted tower into the Pequod .
Every time I ascended to the deck from my watches below , I sat at the feet .
and at the same time sleeping among the fragrant spermaceti canoes of some such drunken tasks , these floating oars , with bread , and bearded foam-brows , were stowed along the deck , and thus explained their tissues were not elsewhere .
when all the spars is necessary on two parts , transporting an additional staff , and a non-picture of profundities , and letting it stay in the dimensional entrance of the stage and see
one of these birds came wheeling and smoking with his ivory heel — it minds me of the noble , solid , Saxon hospitality of that ship ;
The keels that we live in ?
— In the first 
```

* epoch = 80
```
moby Dick ! the body wheel is there ? ’ “ ‘ Dag more , ” cried Ahab , suddenly erecting himself , while whole thunder-clouds swept aside from his brow . “ That chase we go , who the crew stood before the wind , they were rounding about the whale-boat once ; and the whale was free .
( _Sulphur Bottom_ ) . — Another retiring gentleman , with a brimstone belly , doubtless got by scraping along the Tartarian tiles in some of his profounder divings . He is seldom seen ;
The breeze now freshened ; the sky had changed from clear , sunny cold , to drizzled by the emptying out of the water , the bulwarks stood firmly enchanted , to the rest as the birds were almost spectacles .
The small of my back ached to think of it . And it was so light too ; the small gold-fish had it not been found even when it but cast me cracked , and directed a great ferocious look about him , the more so stubborn , and directly brought to beat upon the most intent on any one related fellow .
— ‘ where moth and rust do corrupt , but turn fixed up the hearts of modern Japan , the days in summer and how they burst their broad waters into the whirlpool ; the small of many a perilous time for this man has no taste . I but the present half-inch — the fowl ! the boy ’ s hand on the hill ! ” But the other boat ’ s steward , the one far too wasty , to the breezes of the white whale , came after the wheel-and-hand that brought the beautiful and bountiful horse-sod
Like venerable moss-bearded Lady Cautching Schools , this craft seemed seldom happy to be on the whale fishery .
There they let scarcely belaxes ; this ceaseless whirling eddy is to be seen , and when at intervals , the whale carries a milk-white fog
You would almost as soon have expected him to turn out of his bunk without his nose as without his pipe . But the scud whale carries the element here is a separate contraction . If not the X-ray business will answer , then ;
when the smallest , many other fatal acts were reached the forecastle , where the steady fancied bright wrath of the whale ’ s flesh permanently descried the works .
by the straits of Sunda , chiefly , vessels bound to China from the west , emerge into the China seas . Those narrow straits of Sunda divide Sumatra from Java ;
looked aloft ; looked right and left ; looked everywhere and nowhere ;
I say , that charity ’ s chick was swallowed up , and burst there as an archangel ground . The great Sperm Whale and the Right Whale are by far the most noteworthy . They are the lads that are made to carry them the necessity for them . It fared with Ahab , who thus far had been planted by him in the waves , he patched them with hatchet-pit .
Starbuck , there ’ s no way to stop my singing in this world but to cut my throat . And when that common chinker is springing upon the water , the lightning shone the flying splinter , the smallest insect , though some seem the world . This smell of the great delicate smoke has gained a mast-head still high above the small of the mos
```

* epoch = 90
```
to do some large prospects of being annihilally spelled , it appeals to mankind in all conscience ;
Who but mighty queer , too , I thought I would tell me whether this strange uncompromisedness in him acted in miniature .
— his living foot advanced upon the deck , as if to step ;
Let the most absent-minded of men be plunged in his deepest revenges for several days .
but there you have him .
— the Coke-upon-Littleton of the fist .
— a lofty iron ere I have heard — though my body stripped to the boat ’ s backs as I was lashing them off , now , the membranes grew their broad swirdle-screws , and leaning over small quilts , so thus explaining their teeth , all over with an incredulous chase .
The boats were pulled more apart ; Starbuck giving chase to three whales running dead to leeward . Our sail was now set , and , with the still rising wind , we rushed along ;
— ha , ha ! old Ahab ! the White Whale ; he ’ ll nail ye !
The Pirate Porpoise .
FOX NEWS AHAB SAILOR .
While still warm , the oil , like hot punch , is received into the six-barrel casks ;
— to do to my fellow man what I would have my fellow man to do to me — _that_ is the will of God . Now , Queequeg is my whale-hunter , who , without being taken home to Heaven , I do not suspend because the old Manhatto had anything to say to the whaleman , who might be standing on the quarter-deck .
— so she called it. ” “ Ginger-jub !
She is ballasted with utilities ; not altogether with unusable pig-lead and kentledge . She carries years ’ water in her . Clear old pride now included .
— cucumbers is the word _recognised untoward — something like me a ’ lean-crat ;
I . The Cape of Good Hope . Despatch !
— It ’ s the Black Sea in a midnight gale . — It ’ s the unnatural combat of the four primal elements . — It ’ s a blasted heath . —
The lord be more tolerable , yet Commodore , of Nantucket , that doziness of terrors , woe to all sorts of whales , was generally half so killing whales , when he quitted the island ;
Teeth he accounted bits of ivory ; heads he deemed but top-blocks ; men themselves he lightly held for capstans .
Begone !
To be sure , it might be nothing but a good coat of tropical tanning ;
“ Look up at it ; mark it well ; the white flame but lights the way to the White Whale !
— long , very long after old Ahab ’ s peculiar horror was there to be seen ;
Ahab , now aloft and motionless ; anon , unrestingly pacing the planks .
— for those people have to do or not with the old woman ’ s palm over his wrists . Hold , don ’ t so ablutious to distinguish them , though .
He seemed to take to me quickly , and told me this screwed chair was mine .
That certain sultanism of his brain , which had otherwise in a good degree remained unmanifested ;
it all came out to , and nothing but to derive an entire terrain of the vast Sperm Whale fishery and whale .
More and more appalling before him , was Ahab , who , after its Jungfrau of the Middle Aisle , had passed nearly twenty feet of the present voyage ,
```
