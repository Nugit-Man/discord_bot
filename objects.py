#The class per person
class Person:
    def __init__(self,dump):
         self.id = int(dump[0])
         self.name = dump[1]
         self.money = int(dump[2])
         self.wordles = int(dump[2])
         self.inventory = [int(x) for x in dump[3].split("|")]
         self.badges = [int(x) for x in dump[4].split("|")]
         self.market = [int(x) for x in dump[5].split("|")]
         self.case_count = int(dump[6])
         self.key_count = int(dump[7])
         self.beef_dip_count = int(dump[8])
         self.beef_dip_rank = int(dump[9])
         self.bank = [int(x) for x in dump[10].split("|")]
         self.days_no_gamble = int(dump[11])
         self.interest = [int(x) for x in dump[12].split("|")]
         self.case_interest = int(dump[13])
         self.blackjack = dump[14]
         self.count = int(dump[15])
         self.items_purchased = int(dump[16])
         self.commands_run = int(dump[17])
         self.CS2 = int(dump[18])
         self.Achievements = [int(x) for x in dump[19].split("|")]
         self.beer = int(dump[20])
    def tostr (self):
        #only used to write to file
        return f"{int(self.id)},{int(self.name)},"


"""
All Variables that will be used
    ID
    Name
    Money
    Wordles
    Inventory
    Badges
    Market
    Case Count
    Key Count
    Beef Dip Count
    Beef Dip Rank
    Banks
    Days no Gamble
    Interest Past 10 days
    Case Interest value
    Blackjack
    count
    Items purchased
    Commands Run
    CS2 Cases
    Achievements
    Beer Prestiege
"""



#Secret Achievements
#Launch Ultrakill
#Do the wordle 100 times
#Buy 100 Items from the shop