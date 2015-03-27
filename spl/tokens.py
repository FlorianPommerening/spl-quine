NEGATIVE_ADJECTIVES = [
    "bad", "cowardly", "cursed", "damned", "dirty", "disgusting", "distasteful", "dusty", "evil", "fat", "fat-kidneyed",
    "fatherless", "foul", "hairy", "half-witted", "horrible", "horrid", "infected", "lying", "miserable", "misused",
    "oozing", "rotten", "smelly", "snotty", "sorry", "stinking", "stuffed", "stupid", "vile", "villainous", "worried"]

NEUTRAL_ADJECTIVES = [
    "big", "black", "blue", "bluest", "bottomless", "furry", "green", "hard", "huge", "large", "little", "normal",
    "old", "purple", "red", "rural", "small", "tiny", "white", "yellow"]

POSITIVE_ADJECTIVES = [
    "amazing", "beautiful", "blossoming", "bold", "brave", "charming", "clearest", "cunning", "cute", "delicious",
    "embroidered", "fair", "fine", "gentle", "golden", "good", "handsome", "happy", "healthy", "honest", "lovely",
    "loving", "mighty", "noble", "peaceful", "pretty", "prompt", "proud", "reddest", "rich", "smooth", "sunny", "sweet",
    "sweetest", "trustworthy", "warm"]

ADJECTIVES = NEGATIVE_ADJECTIVES + NEUTRAL_ADJECTIVES + POSITIVE_ADJECTIVES

NEGATIVE_NOUNS = [
    "Hell", "bastard", "beggar", "blister", "codpiece", "coward", "curse", "death", "devil", "draught", "famine",
    "flirt-gill", "goat", "hate", "hog", "hound", "leech", "lie", "pig", "plague", "starvation", "toad", "war", "wolf"]

NEUTRAL_NOUNS = [
    "animal", "aunt", "brother", "cat", "chihuahua", "cousin", "cow", "daughter", "door", "face", "father", "fellow",
    "granddaughter", "grandfather", "grandmother", "grandson", "hair", "hamster", "horse", "lamp", "lantern",
    "mistletoe", "moon", "morning", "mother", "nephew", "niece", "nose", "purse", "road", "roman", "sister", "sky",
    "son", "squirrel", "stone wall", "thing", "town", "tree", "uncle", "wind"]

POSITIVE_NOUNS = [
    "Heaven", "King", "Lord", "angel", "flower", "happiness", "joy", "plum", "summer's day", "hero", "rose", "kingdom",
    "pony"]

NOUNS = NEGATIVE_NOUNS + NEUTRAL_NOUNS + POSITIVE_NOUNS

CHARACTERS = [
    "Achilles", "Adonis", "Adriana", "Aegeon", "Aemilia", "Agamemnon", "Agrippa", "Ajax", "Alonso", "Andromache",
    "Angelo", "Antiochus", "Antonio", "Arthur", "Autolycus", "Balthazar", "Banquo", "Beatrice", "Benedick", "Benvolio",
    "Bianca", "Brabantio", "Brutus", "Capulet", "Cassandra", "Cassius", "Christopher Sly", "Cicero", "Claudio",
    "Claudius", "Cleopatra", "Cordelia", "Cornelius", "Cressida", "Cymberline", "Demetrius", "Desdemona", "Dionyza",
    "Doctor Caius", "Dogberry", "Don John", "Don Pedro", "Donalbain", "Dorcas", "Duncan", "Egeus", "Emilia", "Escalus",
    "Falstaff", "Fenton", "Ferdinand", "Ford", "Fortinbras", "Francisca", "Friar John", "Friar Laurence", "Gertrude",
    "Goneril", "Hamlet", "Hecate", "Hector", "Helen", "Helena", "Hermia", "Hermonie", "Hippolyta", "Horatio", "Imogen",
    "Isabella", "John of Gaunt", "John of Lancaster", "Julia", "Juliet", "Julius Caesar", "King Henry", "King John",
    "King Lear", "King Richard", "Lady Capulet", "Lady Macbeth", "Lady Macduff", "Lady Montague", "Lennox", "Leonato",
    "Luciana", "Lucio", "Lychorida", "Lysander", "Macbeth", "Macduff", "Malcolm", "Mariana", "Mark Antony", "Mercutio",
    "Miranda", "Mistress Ford", "Mistress Overdone", "Mistress Page", "Montague", "Mopsa", "Oberon", "Octavia",
    "Octavius Caesar", "Olivia", "Ophelia", "Orlando", "Orsino", "Othello", "Page", "Pantino", "Paris", "Pericles",
    "Pinch", "Polonius", "Pompeius", "Portia", "Priam", "Prince Henry", "Prospero", "Proteus", "Publius", "Puck",
    "Queen Elinor", "Regan", "Robin", "Romeo", "Rosalind", "Sebastian", "Shallow", "Shylock", "Slender", "Solinus",
    "Stephano", "Thaisa", "The Abbot of Westminster", "The Apothecary", "The Archbishop of Canterbury",
    "The Duke of Milan", "The Duke of Venice", "The Ghost", "Theseus", "Thurio", "Timon", "Titania", "Titus", "Troilus",
    "Tybalt", "Ulysses", "Valentine", "Venus", "Vincentio", "Viola"]

ASSIGNMENT_COMMANDS = ["You are as %s as %s.", "Thou art as %s as %s."]
VALUE_TEST_COMMANDS = ["Are you as %s as %s?"]
PRINT_CHAR_COMMANDS = ["Speak your mind."]
CONDITIONAL_PROCEED_TO_SCENE_COMMANDS = ["If so, let us proceed to scene %s."]