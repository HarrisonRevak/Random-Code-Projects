class YouTubers:
    def __init__(self, n, s, g, y):
        self.name = n
        self.subscribers = s
        self.genre = g
        self.year = y

    def add_subs(self, v):
        self.subscribers += v

    def influencer(self):
        if self.subscribers > 10000:
            return ("is an influencer")
        else:
            return ("is not an influencer")

    def method(self):
        print(self.name, "has been making videos about", self.genre, "since", self.year, "and currently has", self.subscribers, "subscribers.")

mark = YouTubers("Markiplier", 36500000, "Gaming", 2012)

jack = YouTubers("Jacksepticeye", 30600000, "Gaming", 2007)

hack = YouTubers("Hacksmith", 14500000, "Entertainment", 2006)

linus = YouTubers("Linus Tech Tips", 15500000, "Informational", 2008)

mark.method()
jack.method()
hack.method()
linus.method()

mark.add_subs(3506000)
mark.method()

jack.add_subs(300500)
mark.method()

hack.add_subs(100000)
hack.method()

linus.add_subs(250000)
linus.method()


print(mark.name, "is ", mark.influencer())

print(jack.name, "is ", jack.influencer())

print(hack.name, "is ", hack.influencer())

print(linus.name, "is ", linus.influencer())
