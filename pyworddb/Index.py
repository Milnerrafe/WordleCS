## Here we import all the Python packages that we'll need to make this code work.
import json
import random
from datetime import datetime

## Here we get the date and format it.
current_date = datetime.now()
formatted_date = current_date.strftime('%d/%m/%y')
date = formatted_date

## Here we declare the JSON data
json_data = '''
{
    "words": ["ABACK","ABASE","ABASH","ABATE","ABBEY","ABBOT","ABETS","ABHOR","ABIDE","ABLED","ABLER","ABODE","ABORT","ABOUT","ABOVE","ABUSE","ABUTS","ABUZZ","ABYSM","ABYSS","ACHED","ACHES","ACHOO","ACIDS","ACING","ACMES","ACORN","ACRES","ACRID","ACTED","ACTOR","ACUTE","ADAGE","ADAPT","ADDED","ADDER","ADDLE","ADEPT","ADIEU","ADIOS","ADMIN","ADMIT","ADOBE","ADOPT","ADORE","ADORN","ADULT","AERIE","AFFIX","AFIRE","AFOOT","AFORE","AFTER","AGAIN","AGAPE","AGAVE","AGENT","AGILE","AGING","AGLET","AGLOW","AGONY","AGREE","AHEAD","AHOLD","AIDED","AIDES","AILED","AIMED","AIRED","AISLE","ALAMO","ALARM","ALBUM","ALDER","ALERT","ALGAE","ALIAS","ALIBI","ALIEN","ALIGN","ALIKE","ALIVE","ALLAY","ALLEY","ALLOT","ALLOW","ALLOY","ALOFT","ALOHA","ALONE","ALONG","ALOOF","ALOUD","ALPHA","ALTAR","ALTER","AMASS","AMAZE","AMBER","AMBLE","AMEND","AMIGO","AMINO","AMISS","AMONG","AMORE","AMOUR","AMPED","AMPLE","AMPLY","AMUCK","AMUSE","ANGEL","ANGER","ANGLE","ANGRY","ANGST","ANIMA","ANIME","ANKLE","ANNEX","ANNOY","ANNUL","ANODE","ANTES","ANTIC","ANTSY","ANVIL","AORTA","APACE","APART","APPLE","APPLY","APRON","APTLY","ARBOR","ARDOR","AREAS","ARENA","ARGON","ARGUE","ARISE","ARMED","ARMOR","AROMA","AROSE","ARRAY","ARROW","ARSON","ARTSY","ASCOT","ASHEN","ASHES","ASIDE","ASKED","ASKEW","ASPEN","ASSAY","ASSET","ATLAS","ATOLL","ATOMS","ATONE","ATTIC","AUDIO","AUDIT","AUGER","AUGHT","AUNTS","AURAL","AVAIL","AVERT","AVIAN","AVOID","AWAIT","AWAKE","AWARD","AWARE","AWASH","AWFUL","AWOKE","AXIAL","AXIOM","AZURE","BABES","BACKS","BACON","BADGE","BADLY","BAGEL","BAGGY","BAILS","BAKED","BAKER","BAKES","BALLS","BALMY","BALSA","BANAL","BANDS","BANDY","BANES","BANGS","BANJO","BANKS","BARBS","BARED","BARGE","BARKS","BARON","BARRE","BASAL","BASED","BASES","BASIC","BASIL","BASIN","BASIS","BASKS","BASTE","BATCH","BATED","BATES","BATHE","BATHS","BATON","BATTY","BAWDY","BAYOU","BEACH","BEADS","BEADY","BEAMS","BEANS","BEARD","BEARS","BEAST","BEATS","BEEFS","BEEFY","BEEPS","BEERS","BEETS","BEFIT","BEGAN","BEGAT","BEGET","BEGIN","BEGUN","BEIGE","BEING","BELAY","BELCH","BELLE","BELLS","BELLY","BELOW","BELTS","BENCH","BENDS","BENDY","BERET","BERRY","BERTH","BESET","BESOT","BEZEL","BIBLE","BICEP","BIDET","BIGHT","BIGOT","BIKER","BIKES","BILGE","BILLS","BIMBO","BINDS","BINGE","BINGO","BIPED","BIRCH","BIRDS","BIRTH","BISON","BITCH","BITER","BITES","BITSY","BITTY","BLABS","BLACK","BLADE","BLAME","BLAND","BLANK","BLARE","BLAST","BLAZE","BLEAK","BLEED","BLEEP","BLEND","BLENT","BLESS","BLEST","BLIMP","BLIND","BLING","BLINK","BLIPS","BLISS","BLITZ","BLOAT","BLOCK","BLOKE","BLOND","BLOOD","BLOOM","BLOTS","BLOWN","BLOWS","BLUER","BLUES","BLUFF","BLUNT","BLURB","BLURT","BLUSH","BOARD","BOARS","BOAST","BOATS","BODES","BOGEY","BOGUS","BOILS","BOING","BOINK","BOLTS","BOLUS","BOMBS","BONDS","BONED","BONES","BONGO","BONUS","BOOBS","BOOKS","BOOST","BOOTH","BOOTS","BOOTY","BOOZE","BORAX","BORED","BORER","BORES","BORNE","BOSOM","BOSSY","BOTCH","BOTOX","BOUGH","BOUND","BOUTS","BOWED","BOWEL","BOWLS","BOXED","BOXER","BOXES","BOZOS","BRACE","BRAID","BRAIN","BRAKE","BRAND","BRASH","BRASS","BRATS","BRAVE","BRAVO","BRAWL","BRAWN","BRAYS","BREAD","BREAK","BREED","BREVE","BREWS","BRIAR","BRIBE","BRICK","BRIDE","BRIEF","BRIER","BRINE","BRING","BRINK","BRISK","BROAD","BROIL","BROKE","BROOD","BROOK","BROOM","BROTH","BROWN","BROWS","BRUIN","BRUNG","BRUNT","BRUSH","BRUTE","BUCKS","BUDDY","BUDGE","BUFFS","BUGGY","BUGLE","BUILD","BUILT","BULBS","BULGE","BULKY","BULLS","BULLY","BUMPS","BUMPY","BUNCH","BUNDT","BUNKS","BUNNY","BURLY","BURNS","BURNT","BURPS","BURRO","BURST","BUSES","BUSHY","BUSTS","BUSTY","BUTCH","BUTTE","BUTTS","BUXOM","BUYER","BUYIN","BUZZY","BYLAW","BYTES","BYWAY","CABAL","CABBY","CABIN","CABLE","CACHE","CACTI","CADDY","CADET","CADRE","CAGED","CAGES","CAGEY","CAJUN","CAKES","CALLS","CALMS","CALVE","CAMEL","CAMEO","CAMPS","CANAL","CANDY","CANED","CANER","CANES","CANOE","CANON","CANTO","CAPED","CAPER","CAPES","CARAT","CARBS","CARDS","CARED","CARES","CARET","CARGO","CARNY","CAROL","CARRY","CARTS","CARVE","CASED","CASES","CASTE","CASTS","CATCH","CATER","CAUSE","CAVED","CAVES","CEASE","CEDAR","CEDES","CELEB","CELLO","CELLS","CENTS","CERTS","CHAFE","CHAFF","CHAIN","CHAIR","CHALK","CHAMP","CHANT","CHAOS","CHAPS","CHARD","CHARM","CHART","CHASE","CHASM","CHATS","CHAWS","CHEAP","CHEAT","CHECK","CHEEK","CHEEP","CHEER","CHEFS","CHEMO","CHESS","CHEST","CHEWS","CHEWY","CHICK","CHIDE","CHIEF","CHILD","CHILI","CHILL","CHIME","CHIMP","CHINA","CHINK","CHINO","CHINS","CHIPS","CHIRP","CHIVE","CHOCK","CHOIR","CHOKE","CHOMP","CHOPS","CHORD","CHORE","CHOSE","CHUCK","CHUFF","CHUMP","CHUMS","CHUNK","CHURN","CHUTE","CIDER","CIGAR","CINCH","CIRCA","CITED","CIVIC","CIVIL","CLACK","CLAIM","CLAMP","CLAMS","CLANG","CLASH","CLASP","CLASS","CLAST","CLAWS","CLAYS","CLEAN","CLEAR","CLEAT","CLEFT","CLERK","CLICK","CLIFF","CLIMB","CLING","CLINK","CLIPS","CLOAK","CLOCK","CLODS","CLOGS","CLONE","CLOSE","CLOTH","CLOTS","CLOUD","CLOUT","CLOVE","CLOWN","CLUBS","CLUCK","CLUED","CLUES","CLUMP","CLUNG","CLUNK","COACH","COALS","COAST","COATS","COBRA","COCKS","COCKY","COCOA","CODED","CODES","CODEX","COEDS","COINS","COLDS","COLIC","COLON","COLOR","COMAS","COMBO","COMBS","COMES","COMET","COMFY","COMIC","COMMA","CONCH","CONDO","CONES","CONGA","CONIC","COOKS","COOLS","COOPS","COOPT","COPES","CORAL","CORDS","CORES","CORKS","CORNS","CORNY","CORPS","COSTS","COUCH","COUGH","COULD","COUNT","COUPE","COURT","COUTH","COVEN","COVER","COVET","COWED","COWER","CRABS","CRACK","CRAFT","CRAGS","CRAMP","CRANE","CRANK","CRAPS","CRASH","CRASS","CRATE","CRAVE","CRAWL","CRAZE","CRAZY","CREAK","CREAM","CREDO","CREED","CREEK","CREEP","CREME","CREPE","CREPT","CREST","CREWS","CRIBS","CRICK","CRIED","CRIER","CRIES","CRIME","CRIMP","CRISP","CROAK","CROCK","CRONE","CRONY","CROOK","CROON","CROPS","CROSS","CROUP","CROWD","CROWN","CROWS","CRUDE","CRUEL","CRUFT","CRUMB","CRUMP","CRUSH","CRUST","CRYPT","CUBAN","CUBBY","CUBED","CUBES","CUBIC","CUBIT","CUFFS","CULLS","CULTS","CUPID","CURED","CURES","CURIO","CURLS","CURLY","CURRY","CURSE","CURVE","CUSHY","CUTER","CUTIE","CYBER","CYCLE","CYNIC","DADDY","DAILY","DAIRY","DAISY","DALLY","DAMES","DANCE","DANDY","DARED","DARES","DARTS","DATED","DATER","DATES","DATUM","DAWNS","DAZED","DEALS","DEALT","DEANS","DEARS","DEATH","DEBAR","DEBIT","DEBTS","DEBUG","DEBUT","DECAF","DECAY","DECKS","DECOR","DECOY","DECRY","DEEDS","DEEMS","DEFER","DEFIB","DEIFY","DEIGN","DEISM","DEITY","DELAY","DELLS","DELTA","DELTS","DELVE","DEMIT","DEMON","DEMOS","DEMUR","DENIM","DENSE","DENTS","DEPOT","DEPTH","DERBY","DESKS","DETER","DETOX","DEUCE","DEVIL","DIALS","DIARY","DIBBS","DICED","DICEY","DICKY","DIDNT","DIETS","DIGIT","DIJON","DILLS","DILLY","DIMES","DIMLY","DINED","DINER","DINGO","DINGS","DINGY","DINKS","DINKY","DIRGE","DIRTY","DISCO","DISCS","DISKS","DITCH","DITSY","DITTO","DITTY","DITZY","DIVAN","DIVAS","DIVED","DIVER","DIVES","DIVVY","DIZZY","DOCKS","DODGE","DODGY","DOERS","DOGGY","DOGMA","DOILY","DOING","DOLLS","DOLLY","DOMED","DOMES","DONOR","DONUT","DOORS","DOOZY","DOPED","DOPES","DOPEY","DORKS","DORKY","DORMS","DOSED","DOSES","DOTER","DOTES","DOTTY","DOUBT","DOUGH","DOUSE","DOVES","DOWEL","DOWNS","DOWRY","DOZED","DOZEN","DOZER","DRAFT","DRAGS","DRAIN","DRAMA","DRANK","DRAPE","DRAWL","DRAWN","DRAWS","DREAD","DREAM","DREGS","DRESS","DRIED","DRIER","DRIES","DRIFT","DRILL","DRINK","DRIPS","DRIVE","DROID","DROLL","DRONE","DROOL","DROOP","DROPS","DROSS","DROVE","DROWN","DRUGS","DRUID","DRUMS","DRUNK","DRYER","DUCKS","DUCTS","DUDES","DUFUS","DUKES","DUMMY","DUMPS","DUNCE","DUNES","DUNKS","DUNNO","DUPED","DUPER","DUSKY","DUSTY","DUTCH","DUVET","DWARF","DWELL","DWELT","DYING","EAGER","EAGLE","EARLS","EARLY","EARNS","EARTH","EASED","EASEL","EASES","EATEN","EATER","EAVES","EBOLA","EBONY","EBOOK","EDEMA","EDGED","EDGES","EDICT","EDIFY","EDITS","EERIE","EGGED","EGRET","EIGHT","EJECT","ELATE","ELBOW","ELDER","ELECT","ELEGY","ELFIN","ELIDE","ELITE","ELOPE","ELSES","ELUDE","ELVES","EMAIL","EMBED","EMBER","EMPTY","ENACT","ENDED","ENDOW","ENEMA","ENEMY","ENJOY","ENNUI","ENSUE","ENTER","ENTRY","ENVOY","EPOCH","EPOXY","EPSOM","EQUAL","EQUIP","ERASE","ERECT","ERODE","ERRED","ERROR","ERUPT","ESSAY","ETHER","ETHIC","ETHOS","ETUDE","EVADE","EVENS","EVENT","EVERY","EVICT","EVILS","EVOKE","EXACT","EXALT","EXAMS","EXCEL","EXERT","EXILE","EXIST","EXITS","EXPEL","EXTRA","EXUDE","FABLE","FACED","FACES","FACET","FACTS","FADED","FADER","FADES","FAILS","FAINT","FAIRS","FAIRY","FAITH","FAKED","FAKER","FAKES","FALLS","FALSE","FAMED","FANCY","FANGS","FANNY","FARCE","FARED","FARES","FARMS","FARTS","FATAL","FATED","FATES","FATTY","FAULT","FAUNA","FAVOR","FAXED","FAXES","FAZED","FEARS","FEAST","FEATS","FECAL","FECES","FEEDS","FEELS","FEELY","FEIGN","FEINT","FELLA","FELON","FEMUR","FENCE","FERAL","FERNS","FERRY","FETAL","FETCH","FETID","FETUS","FEUDS","FEVER","FEWER","FIBER","FICUS","FIELD","FIEND","FIERY","FIFTH","FIFTY","FIGHT","FILCH","FILED","FILES","FILET","FILLS","FILMS","FILTH","FINAL","FINCH","FINDS","FINED","FINER","FINES","FIRED","FIRES","FIRMS","FIRST","FISHY","FISTS","FIVER","FIVES","FIXED","FIXER","FIXES","FIZZY","FJORD","FLACK","FLAGS","FLAIL","FLAIR","FLAKE","FLAKY","FLAME","FLANK","FLAPS","FLARE","FLASH","FLASK","FLATS","FLAWS","FLEAS","FLECK","FLEET","FLESH","FLICK","FLIER","FLIES","FLING","FLINT","FLIPS","FLIRT","FLOAT","FLOCK","FLOOD","FLOOR","FLOPS","FLORA","FLOSS","FLOUR","FLOUT","FLOWN","FLOWS","FLUFF","FLUID","FLUKE","FLUME","FLUNG","FLUNK","FLUSH","FLUTE","FLYER","FOAMY","FOCAL","FOCUS","FOGGY","FOLDS","FOLIO","FOLKS","FOLLY","FONDU","FOODS","FOOLS","FOOTY","FORAY","FORCE","FORGE","FORGO","FORKS","FORMS","FORTE","FORTH","FORTY","FORUM","FOUND","FOUNT","FOURS","FOXES","FOYER","FRAIL","FRAME","FRANK","FRAUD","FREAK","FREED","FREER","FREES","FREON","FRESH","FRIAR","FRIED","FRIES","FRISK","FRIZZ","FROCK","FROGS","FRONT","FROST","FROTH","FROWN","FROZE","FRUIT","FRYER","FUDGE","FUELS","FUGAL","FUGUE","FULLY","FUMES","FUNDS","FUNGI","FUNKY","FUNNY","FUROR","FURRY","FUSED","FUSES","FUSSY","FUTON","FUZZY","GAFFE","GAILY","GAINS","GALES","GAMER","GAMES","GAMEY","GAMMA","GAMUT","GANGS","GASES","GASSY","GATED","GATES","GATOR","GAUDY","GAUGE","GAUNT","GAUZE","GAVEL","GAWKY","GAZED","GEARS","GECKO","GEEKS","GEEKY","GEESE","GENES","GENIE","GENRE","GENTS","GENUS","GEODE","GERMS","GETUP","GHOST","GHOUL","GIANT","GIDDY","GIFTS","GILLS","GIMME","GIRLS","GIRLY","GIRTH","GIVEN","GIVER","GIVES","GIZMO","GLADE","GLAND","GLARE","GLASS","GLAZE","GLEAM","GLEAN","GLENS","GLIDE","GLINT","GLITZ","GLOAT","GLOBE","GLOCK","GLOOM","GLORY","GLOSS","GLOVE","GLOWS","GLOWY","GLUED","GLUES","GLUEY","GLUME","GLYPH","GNARL","GNASH","GNATS","GNOME","GOALS","GOATS","GODLY","GOERS","GOING","GONER","GONGS","GONNA","GOODS","GOODY","GOOEY","GOOFY","GOONS","GOOPY","GOOSE","GORGE","GOTHS","GOUGE","GOURD","GOWNS","GRABS","GRACE","GRADE","GRAFT","GRAIL","GRAIN","GRAMS","GRAND","GRANT","GRAPE","GRAPH","GRASP","GRASS","GRATE","GRAVE","GRAVY","GRAYS","GRAZE","GREAT","GREED","GREEK","GREEN","GREET","GRIDS","GRIEF","GRIFT","GRILL","GRIME","GRIND","GRINS","GRIPE","GRIPS","GRITS","GROAN","GRODY","GROIN","GROOM","GROPE","GROSS","GROUP","GROUT","GROVE","GROWL","GROWN","GROWS","GRUBS","GRUEL","GRUFF","GRUMP","GRUNT","GUANO","GUARD","GUESS","GUEST","GUIDE","GUILD","GUILE","GUILT","GUISE","GULAG","GULCH","GULLS","GUMBO","GUMMY","GUSHY","GUTSY","GYPSY","GYROS","HABIT","HACKS","HACKY","HADNT","HAIKU","HAILS","HAIRS","HAIRY","HAJIB","HALLS","HANDS","HANDY","HANGS","HANKY","HAPPY","HARDY","HAREM","HARMS","HARPS","HARPY","HARSH","HASNT","HASTE","HASTY","HATCH","HATED","HATER","HATES","HAULS","HAUNT","HAVEN","HAVOC","HAWKS","HAZED","HAZEL","HAZER","HEADS","HEADY","HEALS","HEAPS","HEARD","HEARS","HEART","HEATS","HEAVE","HEAVY","HECKS","HEDGE","HEELS","HEFTY","HEIRS","HEIST","HELIX","HELLO","HELLS","HELMS","HELPS","HENCE","HERBS","HERDS","HERES","HEROS","HERTZ","HEXES","HICKS","HIDES","HIGHS","HIKED","HIKER","HIKES","HILLS","HINGE","HINTS","HIPPO","HIRED","HIRES","HISSY","HITCH","HIVES","HOARD","HOBBY","HOCUS","HOIST","HOKEY","HOLDS","HOLED","HOLES","HOLEY","HOLLY","HOMER","HOMES","HOMEY","HOMIE","HONED","HONEY","HONKS","HONKY","HONOR","HOOCH","HOODS","HOOEY","HOOKS","HOOKY","HOOPS","HOPED","HOPES","HORDE","HORNS","HORNY","HORSE","HOSED","HOSES","HOSTS","HOTEL","HOUND","HOURS","HOUSE","HOVEL","HOVER","HOWDY","HOWLS","HUBBY","HUFFY","HUGGY","HUMAN","HUMID","HUMOR","HUMPS","HUMUS","HUNCH","HUNKS","HUNKY","HUNTS","HURRY","HURTS","HUSKS","HUSKY","HUTCH","HYDRO","HYMNS","HYPED","HYPER","ICING","ICONS","IDEAL","IDEAS","IDIOM","IDIOT","IDOLS","IDYLL","IGLOO","IMAGE","IMBUE","IMPEL","IMPLY","INANE","INAPT","INCUR","INDEX","INDIE","INEPT","INERT","INFER","INFIX","INKED","INLAW","INLAY","INLET","INNER","INPUT","INSET","INTEL","INTRO","INURE","IONIC","IRATE","IRKED","IRONS","IRONY","ISLET","ISSUE","ITCHY","ITEMS","IVORY","JACKS","JADED","JAGGY","JAILS","JAUNT","JAWED","JAZZY","JEANS","JEEPS","JELLY","JERKS","JERKY","JESTS","JETTY","JEWEL","JIFFY","JOINS","JOINT","JOKED","JOKER","JOKES","JOKEY","JOLLY","JOULE","JOUST","JOWLS","JUDGE","JUICE","JUICY","JUMBO","JUMPS","JUMPY","JUNKY","JUNTA","JUROR","KABOB","KAPUT","KARAT","KAYAK","KAZOO","KEBAB","KEELS","KEEPS","KEMPT","KEYED","KHAKI","KICKS","KIDDO","KIDDY","KILLS","KILOS","KINDA","KINDS","KINGS","KINKS","KINKY","KIOSK","KISSY","KITES","KITTY","KLUTZ","KNACK","KNAVE","KNEAD","KNEED","KNEEL","KNEES","KNELL","KNELT","KNICK","KNIFE","KNOBS","KNOCK","KNOLL","KNOTS","KNOWN","KNOWS","KOALA","KOOKS","KOOKY","KUDOS","LABEL","LABOR","LACED","LACES","LACKS","LADEN","LADLE","LAGER","LAITY","LAKES","LAMBS","LAMPS","LANCE","LANDS","LANES","LANKY","LAPEL","LAPSE","LARGE","LARVA","LASER","LASSO","LASTS","LATCH","LATER","LATEX","LATHE","LATTE","LAUDE","LAUGH","LAWNS","LAXLY","LAYER","LEACH","LEADS","LEAFS","LEAFY","LEAKS","LEAKY","LEANS","LEAPS","LEAPT","LEARN","LEARY","LEASE","LEASH","LEAST","LEAVE","LEDGE","LEECH","LEERY","LEFTS","LEFTY","LEGAL","LEGIT","LEMME","LEMON","LEMUR","LEPER","LETCH","LEVEE","LEVEL","LEVER","LIARS","LIBEL","LICKS","LIEGE","LIENS","LIFER","LIFTS","LIGHT","LIKED","LIKEN","LIKES","LILAC","LILLY","LIMBO","LIMBS","LIMES","LIMIT","LIMOS","LIMPS","LINED","LINEN","LINER","LINES","LINGO","LINKS","LIONS","LIPPY","LISTS","LITER","LITHE","LITRE","LIVED","LIVEN","LIVER","LIVES","LIVID","LLAMA","LOADS","LOAMY","LOANS","LOATH","LOBBY","LOBES","LOCAL","LOCKS","LOCUS","LODGE","LOFTS","LOFTY","LOGIC","LOGIN","LOGOS","LOINS","LONER","LONGS","LOOKS","LOOMS","LOONS","LOONY","LOOPS","LOOPY","LOOSE","LORDS","LORDY","LOSER","LOSES","LOTTO","LOTUS","LOUSE","LOUSY","LOVED","LOVER","LOVES","LOWER","LOWLY","LOYAL","LUCID","LUCKY","LUMEN","LUMPS","LUMPY","LUNAR","LUNCH","LUNGE","LUNGS","LUPUS","LURCH","LURED","LURES","LURID","LURKS","LUSTS","LUSTY","LYCRA","LYING","LYMPH","LYNCH","LYRIC","MACHO","MACRO","MADAM","MADLY","MAFIA","MAGIC","MAGMA","MAIDS","MAILS","MAIZE","MAJOR","MAKER","MAKES","MALES","MALLS","MAMAS","MAMBO","MANGA","MANGE","MANGO","MANIA","MANIC","MANLY","MANOR","MAPLE","MARCH","MARKS","MARRY","MARSH","MASKS","MASON","MATCH","MATED","MATES","MATEY","MATTE","MAUVE","MAVEN","MAXED","MAXIM","MAYAN","MAYBE","MAYOR","MEALS","MEALY","MEANS","MEANT","MEATS","MEATY","MECCA","MEDAL","MEDIA","MEDIC","MEETS","MELEE","MELON","MELTS","MEMES","MEMOS","MERCY","MERGE","MERIT","MERRY","MESSY","METAL","METER","METRO","MICRO","MIDST","MIGHT","MILES","MILKY","MILLS","MIMES","MIMIC","MINCE","MINDS","MINED","MINER","MINES","MINKS","MINOR","MINTS","MINTY","MINUS","MIRED","MIRES","MIRTH","MISER","MISSY","MISTY","MITES","MITRE","MIXED","MIXER","MIXES","MIXUP","MOANS","MOCHA","MOCKS","MODAL","MODEL","MODEM","MOGUL","MOIST","MOLAR","MOLDS","MOLDY","MOLES","MOMMA","MOMMY","MONEY","MONKS","MONTH","MOOCH","MOODS","MOODY","MOONS","MOORS","MOOSE","MOPED","MOPES","MOPEY","MORAL","MORON","MORPH","MORSE","MOSEY","MOTEL","MOTHS","MOTIF","MOTOR","MOTTO","MOULD","MOULT","MOUND","MOUNT","MOURN","MOUSE","MOUSY","MOUTH","MOVED","MOVER","MOVES","MOVIE","MOWED","MOWER","MOXIE","MUCUS","MUDDY","MUGGY","MULCH","MULES","MULTI","MUMMY","MUMPS","MUNCH","MUNGE","MURAL","MURKY","MUSES","MUSHY","MUSIC","MUSTY","MUTED","MYRRH","MYTHS","NABOB","NACHO","NAILS","NAIVE","NAKED","NAMED","NAMES","NANNY","NASAL","NASTY","NATAL","NATTY","NAVAL","NAVEL","NEARS","NEATO","NECKS","NEEDS","NEEDY","NEIGH","NERDS","NERDY","NERVE","NESTS","NEURO","NEVER","NEWER","NEWLY","NEXUS","NICER","NICHE","NICKS","NIECE","NIFTY","NIGHT","NINES","NINJA","NINNY","NINTH","NIPPY","NITRO","NIXED","NOBLE","NODES","NOISE","NOISY","NOMAD","NONCE","NOONE","NOOSE","NORMS","NORTH","NOSES","NOSEY","NOTCH","NOTED","NOTES","NOUNS","NOVEL","NUDES","NUDGE","NUKED","NUKES","NURSE","NUTTY","NYLON","NYMPH","OAKEN","OASIS","OATHS","OBESE","OBEYS","OBITS","OCCUR","OCEAN","OCHRE","OCTAL","OCTET","ODDLY","ODIUM","OFFER","OFTEN","OGRES","OILED","OILER","OLDER","OLDIE","OLIVE","OMEGA","OMENS","ONION","ONSET","OOMPH","OOZES","OPALS","OPENS","OPERA","OPINE","OPIUM","OPTED","OPTIC","ORATE","ORBIT","ORDER","ORGAN","OTHER","OTTER","OUGHT","OUIJA","OUNCE","OUTDO","OUTED","OUTER","OVARY","OVATE","OVENS","OVERT","OWING","OWLET","OWNED","OWNER","OXIDE","OZONE","PACED","PACER","PACES","PACKS","PAEAN","PAGAN","PAGED","PAGER","PAGES","PAINS","PAINT","PAIRS","PALER","PALES","PALMS","PALSY","PANDA","PANEL","PANES","PANGS","PANIC","PANSY","PANTS","PANTY","PAPAL","PAPER","PAPPA","PARCH","PARED","PARKA","PARKS","PARRY","PARSE","PARTS","PARTY","PASTA","PASTE","PASTS","PASTY","PATCH","PATHS","PATIO","PATSY","PATTY","PAUSE","PAVED","PAVER","PAWNS","PAYEE","PAYER","PEACE","PEACH","PEAKS","PEAKY","PEARL","PEARS","PECAN","PECKS","PEDAL","PEEKS","PEELS","PEEPS","PEERS","PEEVE","PELTS","PENAL","PENNY","PEPPY","PERCH","PERIL","PERKS","PERKY","PERPS","PERVS","PESKY","PESTO","PESTS","PETAL","PETRI","PETTY","PHASE","PHONE","PHONY","PHOTO","PHYLA","PIANO","PICKS","PICKY","PIECE","PIERS","PIETY","PIGGY","PIKED","PIKER","PILED","PILES","PILLS","PILOT","PIMPS","PINCH","PINES","PINKS","PINKY","PINOT","PINTO","PINTS","PIOUS","PIPER","PIPES","PIQUE","PISSY","PITCH","PITHY","PIVOT","PIXEL","PIXIE","PIZZA","PLACE","PLAID","PLAIN","PLAIT","PLANE","PLANK","PLANS","PLANT","PLATE","PLAYS","PLAZA","PLEAD","PLEAS","PLEAT","PLEBE","PLOTS","PLUCK","PLUGS","PLUMB","PLUME","PLUMP","PLUMS","PLUSH","PLUTO","POACH","POEMS","POETS","POINT","POISE","POKED","POKER","POKES","POKEY","POLAR","POLES","POLIO","POLKA","POLLS","POLYP","PONDS","POOCH","POOFS","POOFY","POOLS","POOPS","POOPY","POPPY","POPUP","PORCH","PORES","PORKY","PORNO","PORTS","POSED","POSER","POSES","POSIT","POSSE","POSTS","POTTY","POUCH","POUND","POURS","POUTY","POWER","PRANK","PRAWN","PRAYS","PREEN","PRESS","PRICE","PRICK","PRIDE","PRIED","PRIME","PRIMO","PRIMP","PRINT","PRIOR","PRISM","PRISS","PRIVY","PRIZE","PROBE","PRODS","PROMO","PROMS","PRONE","PRONG","PROOF","PROPS","PROSE","PROTO","PROUD","PROVE","PROWL","PROXY","PRUDE","PRUNE","PSALM","PSYCH","PUBIC","PUDGY","PUFFS","PUFFY","PUKED","PULLS","PULSE","PUMPS","PUNCH","PUNKS","PUNKY","PUPIL","PUPPY","PUREE","PURER","PURGE","PURSE","PUSHY","PUTTY","PYGMY","PYLON","QUACK","QUAIL","QUAKE","QUALM","QUARK","QUART","QUASH","QUASI","QUEEN","QUEER","QUELL","QUERY","QUEST","QUEUE","QUICK","QUIET","QUILL","QUILT","QUINE","QUIPS","QUIRK","QUITE","QUITS","QUOTA","QUOTE","RABBI","RABID","RACED","RACER","RACES","RACKS","RADAR","RADIO","RADIX","RADON","RAGED","RAGES","RAIDS","RAILS","RAINS","RAINY","RAISE","RAKED","RAKES","RALLY","RAMEN","RANCH","RANDY","RANGE","RANKS","RANTS","RAPID","RARER","RATED","RATES","RATIO","RATTY","RAVED","RAVER","RAVES","RAZOR","REACH","REACT","READS","READY","REALM","REALY","REAMS","REAPS","REARS","REAVE","REBEL","REBUT","RECAP","RECON","RECUR","REDID","REEDS","REEFS","REEKS","REELS","REFER","REGAL","REHAB","REIGN","RELAX","RELAY","RELIC","REMIT","RENEW","RENTS","REPAY","REPEL","REPLY","RERUN","RESET","RESIN","RESTS","RETCH","RETIE","RETRO","RETRY","REUSE","REVEL","RHINO","RHYME","RICER","RICKS","RIDER","RIDES","RIDGE","RIFLE","RIGHT","RIGID","RIGOR","RILED","RINDS","RINGS","RINSE","RIOTS","RIPEN","RISEN","RISER","RISES","RISKS","RISKY","RITES","RITZY","RIVAL","RIVEN","RIVER","RIVET","ROACH","ROADS","ROAST","ROBES","ROBIN","ROBOT","ROCKS","ROCKY","RODEO","ROGER","ROGUE","ROLES","ROLFS","ROLLS","ROMAN","ROOFS","ROOKS","ROOKY","ROOMS","ROOMY","ROOST","ROOTS","ROPED","ROPER","ROPES","ROSES","ROSEY","ROTOR","ROUGE","ROUGH","ROUND","ROUSE","ROUTE","ROVER","ROWDY","ROYAL","RUBES","RUDDY","RUDER","RUGBY","RUINS","RULED","RULER","RULES","RUMMY","RUMOR","RUNES","RUNIC","RUNNY","RURAL","RUSTY","RUTTY","SABER","SABLE","SACKS","SADLY","SAFER","SAFES","SAGGY","SAILS","SAINT","SAKES","SALAD","SALES","SALON","SALSA","SALTS","SALTY","SALVE","SALVO","SAMBA","SANDS","SANDY","SAPPY","SARGE","SASSY","SATAN","SATED","SATIN","SAUCE","SAUCY","SAUNA","SAUTE","SAVED","SAVER","SAVES","SAVOR","SAVVY","SAWED","SAYER","SAYSO","SCABS","SCADS","SCALD","SCALE","SCALP","SCALY","SCAMP","SCAMS","SCANS","SCANT","SCAPE","SCARE","SCARF","SCARS","SCARY","SCENE","SCENT","SCHMO","SCION","SCOFF","SCOLD","SCONE","SCOOP","SCOOT","SCOPE","SCORE","SCORN","SCOUR","SCOUT","SCOWL","SCRAM","SCRAP","SCREE","SCREW","SCRUB","SCRUM","SCUBA","SCUFF","SEALS","SEAMS","SEATS","SEDAN","SEEDS","SEEDY","SEEKS","SEEMS","SEEPS","SEERS","SEGUE","SEIZE","SELLS","SEMEN","SEMIS","SENDS","SENSE","SEPIA","SERFS","SERIF","SERUM","SERVE","SERVO","SETUP","SEVEN","SEVER","SEWED","SEWER","SEXED","SEXES","SHACK","SHADE","SHADY","SHAFT","SHAKE","SHAKY","SHALE","SHALL","SHALT","SHAME","SHANK","SHAPE","SHARD","SHARE","SHARK","SHARP","SHAVE","SHAWL","SHEAF","SHEAR","SHEDS","SHEEN","SHEEP","SHEER","SHEET","SHELF","SHELL","SHIFT","SHILL","SHINE","SHINS","SHINY","SHIPS","SHIRE","SHIRK","SHIRT","SHOAL","SHOCK","SHOES","SHONE","SHOOK","SHOOT","SHOPS","SHORE","SHORN","SHORT","SHOTS","SHOUT","SHOVE","SHOWN","SHOWS","SHOWY","SHRED","SHREW","SHRUB","SHRUG","SHUCK","SHUNT","SHUSH","SHUTS","SICKO","SIDED","SIDES","SIDLE","SIEGE","SIEVE","SIGHS","SIGHT","SIGNS","SILKS","SILKY","SILLY","SINCE","SINEW","SINGE","SINGS","SINKS","SINUS","SIRED","SIREN","SITES","SIXES","SIXTH","SIXTY","SIZED","SIZES","SKATE","SKEET","SKIDS","SKIED","SKIER","SKIES","SKIFF","SKILL","SKIMP","SKINS","SKIPS","SKIRT","SKULK","SKULL","SKUNK","SLACK","SLAIN","SLAMS","SLANG","SLANT","SLAPS","SLASH","SLATE","SLAVE","SLAYS","SLEDS","SLEEK","SLEEP","SLEET","SLEPT","SLICE","SLICK","SLIDE","SLIME","SLIMY","SLING","SLINK","SLIPS","SLOBS","SLOPE","SLOTH","SLOTS","SLOWS","SLUGS","SLUMP","SLUMS","SLUNG","SLURP","SLUSH","SMACK","SMALL","SMART","SMASH","SMEAR","SMELL","SMELT","SMILE","SMIRK","SMITE","SMITH","SMOCK","SMOKE","SMOKY","SMOTE","SMURF","SMUSH","SNACK","SNAFU","SNAIL","SNAKE","SNAPS","SNARE","SNARF","SNARK","SNARL","SNEAK","SNEER","SNIDE","SNIFF","SNIPE","SNOBS","SNOOP","SNORE","SNORT","SNOUT","SNOWS","SNOWY","SNUCK","SNUFF","SOAPS","SOAPY","SOARS","SOBER","SOCKS","SODAS","SOFAS","SOFTY","SOGGY","SOLAR","SOLES","SOLID","SOLVE","SONAR","SONGS","SONIC","SOOTY","SORES","SORRY","SORTA","SORTS","SOUGH","SOULS","SOUND","SOUPS","SOUPY","SOUSE","SOUTH","SPACE","SPADE","SPAKE","SPANK","SPANS","SPARE","SPARK","SPASM","SPATE","SPAWN","SPEAK","SPEAR","SPECK","SPECS","SPEED","SPELL","SPEND","SPENT","SPERM","SPEWS","SPICE","SPICY","SPIED","SPIEL","SPIES","SPIKE","SPIKY","SPILL","SPILT","SPINE","SPINS","SPINY","SPIRE","SPITE","SPITS","SPLAT","SPLAY","SPLIT","SPOIL","SPOKE","SPOOF","SPOOK","SPOOL","SPOON","SPORE","SPORT","SPOTS","SPOUT","SPRAY","SPREE","SPRIG","SPUDS","SPUNK","SPURN","SPURS","SPURT","SQUAB","SQUAD","SQUAT","SQUIB","SQUID","STABS","STACK","STAFF","STAGE","STAID","STAIN","STAIR","STAKE","STALE","STALK","STALL","STAMP","STAND","STANK","STARE","STARK","STARS","START","STASH","STATE","STATS","STAYS","STEAD","STEAK","STEAL","STEAM","STEED","STEEL","STEEP","STEER","STEMS","STENT","STEPS","STERN","STICK","STIFF","STILL","STILT","STING","STINK","STINT","STIRS","STOCK","STOIC","STOKE","STOLE","STOMP","STONE","STONY","STOOD","STOOL","STOOP","STOPS","STORE","STORK","STORM","STORY","STOUT","STOVE","STRAP","STRAW","STRAY","STREP","STREW","STRIP","STRUM","STRUT","STUBS","STUCK","STUDS","STUDY","STUFF","STUMP","STUNG","STUNK","STUNT","STYLE","SUAVE","SUCKS","SUCKY","SUEDE","SUGAR","SUING","SUITE","SUITS","SULKY","SUMAC","SUNNY","SUNUP","SUPER","SURFS","SURGE","SURLY","SUSHI","SWABS","SWAMI","SWAMP","SWANG","SWANK","SWANS","SWAPS","SWARM","SWATH","SWEAR","SWEAT","SWEEP","SWEET","SWELL","SWEPT","SWIFT","SWILL","SWIMS","SWINE","SWING","SWIPE","SWIRL","SWISH","SWOON","SWOOP","SWORD","SWORE","SWORN","SWUNG","SYRUP","TABBY","TABLE","TABOO","TACIT","TACKS","TACKY","TACOS","TAFFY","TAILS","TAINT","TAKEN","TAKER","TAKES","TALES","TALKS","TALKY","TALLY","TALON","TAMER","TANGO","TANGY","TANKS","TAPAS","TAPED","TAPER","TAPES","TAPPY","TARDY","TARED","TAROT","TARRY","TARTS","TASER","TASKS","TASTE","TASTY","TAUNT","TAUPE","TAWNY","TAXED","TAXES","TAXIS","TEACH","TEAMS","TEARS","TEARY","TEASE","TECHS","TEENS","TEENY","TEETH","TELLS","TEMPO","TEMPS","TEMPT","TENDS","TENET","TENOR","TENSE","TENTH","TENTS","TEPEE","TEPID","TERMS","TERRA","TERSE","TESTS","TESTY","TETRA","TEXTS","THANK","THATS","THEFT","THEIR","THEME","THERE","THESE","THICK","THIEF","THIGH","THINE","THING","THINK","THINS","THIRD","THONG","THORN","THOSE","THREE","THREW","THROB","THROW","THUGS","THUMB","THUMP","THUNK","THYME","TIARA","TIBIA","TICKS","TIDAL","TIDED","TIDES","TIGER","TIGHT","TILDE","TILES","TILLS","TIMED","TIMER","TIMES","TIMID","TINCT","TINGE","TINTS","TIPPY","TIPSY","TIRED","TIRES","TITAN","TITHE","TITLE","TITTY","TIZZY","TOADS","TOADY","TOAST","TODAY","TODDY","TOFFY","TOGAS","TOKEN","TOLLS","TOMBS","TONAL","TONED","TONER","TONES","TONGS","TONIC","TOOLS","TOONS","TOOTH","TOOTS","TOOTY","TOPAZ","TOPIC","TOPSY","TORCH","TORSO","TORUS","TOTAL","TOTEM","TOUCH","TOUGH","TOURS","TOWED","TOWEL","TOWER","TOWNS","TOXIC","TOXIN","TOYED","TRACE","TRACK","TRACT","TRADE","TRAIL","TRAIN","TRAIT","TRAMP","TRANS","TRAPS","TRASH","TRAWL","TRAYS","TREAD","TREAT","TREES","TREND","TRESS","TRIAD","TRIAL","TRIBE","TRICK","TRIED","TRIES","TRILL","TRIPE","TRIPS","TRITE","TROLL","TROOP","TROPE","TROTS","TROUT","TROVE","TRUCE","TRUCK","TRUER","TRULY","TRUMP","TRUNK","TRUSS","TRUST","TRUTH","TRYST","TUBBY","TUBER","TUBES","TULIP","TULLE","TUMID","TUMMY","TUMOR","TUNED","TUNER","TUNES","TUNIC","TURBO","TURDS","TURNS","TUSHY","TUTOR","TUXES","TWAIN","TWANG","TWEAK","TWEED","TWEEK","TWEEN","TWEET","TWERP","TWICE","TWIGS","TWILL","TWINE","TWINS","TWIRL","TWIST","TWITS","TYING","TYPED","TYPES","UDDER","ULCER","ULTRA","UMBER","UMBRA","UNCLE","UNCUT","UNDER","UNDID","UNDUE","UNFIT","UNIFY","UNION","UNITE","UNITS","UNITY","UNSET","UNTIE","UNTIL","UNWED","UNZIP","UPPED","UPPER","UPSET","URBAN","URGED","URGES","URINE","USAGE","USERS","USHER","USING","USUAL","USURP","USURY","UTTER","UVULA","VAGUE","VALET","VALID","VALOR","VALUE","VALVE","VAPID","VAPOR","VASES","VAULT","VAUNT","VEGAN","VEILS","VEINS","VEINY","VENAL","VENOM","VENTS","VENUE","VENUS","VERBS","VERGE","VERSE","VERVE","VESTS","VEXED","VIALS","VIBES","VICAR","VICES","VIDEO","VIEWS","VIGIL","VIGOR","VILLA","VINES","VINYL","VIOLA","VIPER","VIRAL","VIRUS","VISAS","VISIT","VISOR","VISTA","VITAL","VIVID","VIXEN","VOCAB","VOCAL","VODKA","VOGUE","VOICE","VOILA","VOLTS","VOMIT","VOTED","VOTER","VOTES","VOUCH","VOWED","VOWEL","VROOM","VYING","WACKO","WACKY","WADER","WAFER","WAGED","WAGER","WAGES","WAGON","WAIST","WAITS","WAIVE","WAKES","WALKS","WALLS","WALTZ","WANNA","WANTS","WARDS","WARES","WARMS","WARNS","WARTS","WASHY","WASNT","WASPS","WASTE","WATCH","WATER","WATTS","WAVED","WAVER","WAVES","WAXED","WAXES","WEARS","WEARY","WEAVE","WEDGE","WEEDS","WEEDY","WEEKS","WEENY","WEEPS","WEEPY","WEIGH","WEIRD","WELDS","WELLS","WELTS","WHACK","WHALE","WHARF","WHATS","WHEAT","WHEEL","WHELM","WHERE","WHICH","WHIFF","WHILE","WHIMS","WHINE","WHINY","WHIPS","WHIRL","WHISH","WHISK","WHITE","WHIZZ","WHOLE","WHOOP","WHOSE","WIDEN","WIDER","WIDOW","WIDTH","WIELD","WIERD","WILDS","WILES","WILEY","WILLS","WILLY","WILTS","WIMPS","WIMPY","WINCE","WINCH","WINDS","WINDY","WINES","WINGS","WINKS","WINKY","WIPED","WIPER","WIPES","WIRED","WIRES","WISER","WISHY","WITCH","WITTY","WIVES","WOMAN","WOMEN","WONKY","WOODS","WOODY","WOOED","WOOER","WOOLY","WOOPS","WOOSH","WOOZY","WORDS","WORDY","WORKS","WORLD","WORMS","WORMY","WORRY","WORSE","WORST","WORTH","WOULD","WOUND","WOVEN","WOWED","WRAPS","WRATH","WREAK","WRECK","WREST","WRING","WRIST","WRITE","WRITS","WRONG","WROTE","WRUNG","WURST","WUSSY","XANAX","XEROX","XRAYS","YACHT","YADDA","YAHOO","YANKS","YARDS","YAWNS","YEARN","YEARS","YEAST","YELLS","YIELD","YIKES","YODEL","YOKEL","YOULL","YOUNG","YOURE","YOURS","YOUTH","YOUVE","YUCKY","YUMMY","ZEBRA","ZEROS","ZESTY","ZIGGY","ZILCH","ZIPPY","ZONAL","ZONED","ZONES"]
}
'''

## Here we randomise the JSON data and declare it as a global variable.
def ranworddatamake():
    global ranworddata
    data = json.loads(json_data)
    random.shuffle(data['words'])
    ranworddata = json.dumps(data, indent=4)

## Here we check if our time database JSON file exists. If it does, then we read it and remove any excess spaces.If it doesn't exist, then we set it to a variable with no data inside, so the next piece of code will be able to create it with the correct date.
try:
    with open("datedatabase.txt", "r") as datedatabase:
        saved_date = datedatabase.read()
except FileNotFoundError:
    saved_date = ''


if saved_date != date:
    with open("datedatabase.txt", "w") as datedatabase:
        datedatabase.write(date)

    ranworddatamake()

    with open("index.json", "w") as index_file:
        index_file.write(ranworddata)


print(saved_date)
print(date)
