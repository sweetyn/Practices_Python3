"""
* Please come up with Class and Data Structure Design for a "metric" system to determine the top song of a band. Two Web Service calls void
play(String bandname, String songname);
String topSong(String bandname);


// play("Lady Gaga", "Pokerface");
// play("Lady Gaga", "Pokerface");
// play("Lady Gaga", "Alejandro");
// play("Bruno Mars", "Treasure");
// topSong("Lady Gaga") -> "Pokerface" """

singers = dict()
sings = dict()

#Print the top of song by a band
def topSong(aBand):

    count =0
    theSong = ""


    for key1, val1 in singers.items():
        if val1 == aBand:
            # sings.values(key1)
            for key2, val2 in sings.items():
                if key1 == key2 and val2 > count:
                    count = val2
                    theSong = key2

    return theSong



#Store playing list
def play(aBand, aSong):

    singers[aSong] = singers.get(aSong, aBand)
    sings[aSong] = sings.get(aSong, 0)+1


play("Lady Gaga", "Pokerface")
play("Lady Gaga", "Pokerface")
play("Lady Gaga", "Alejandro")
play("Bruno Mars", "Treasure")

aBand = "Lady Gaga"

print (topSong(aBand))
