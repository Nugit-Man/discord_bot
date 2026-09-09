#The class per person
class Person:
    def __init__(self,dump):
         self.id = int(dump[0])
         self.name = dump[1]
         self.money = int(dump[2])
         self.wordles = int(dump[3])
         self.inventory = [x for x in dump[4].split("|")]
         self.badges = [x for x in dump[5].split("|")]
         self.market = [x for x in dump[6].split("|")]
         self.case_count = int(dump[7])
         self.key_count = int(dump[8])
         self.beef_dip_count = int(dump[9])
         self.beef_dip_rank = int(dump[10])
         self.bank = [x for x in dump[11].split("|")]
         self.days_no_gamble = int(dump[12])
         self.interest = [x for x in dump[13].split("|")]
         self.case_interest = int(dump[14])
         self.blackjack = dump[15]
         self.count = int(dump[16])
         self.items_purchased = int(dump[17])
         self.commands_run = int(dump[18])
         self.cs2 = int(dump[19])
         self.achievements = [x for x in dump[20].split("|")]
         self.beer_count = int(dump[21])
         self.beer_rank = int(dump[22])
         self.money_streak = int(dump[23])
    def tostr (self):
        #only used to write to file
        return f"{self.id},{self.name},{self.money},{self.wordles},{clean_up(self.inventory)},{clean_up(self.badges)},{clean_up(self.market)},{self.case_count},{self.key_count},{self.beef_dip_count},{self.beef_dip_rank},{clean_up(self.bank)},{self.days_no_gamble},{clean_up(self.interest)},{self.case_interest},{self.blackjack},{self.count},{self.items_purchased},{self.commands_run},{self.cs2},{clean_up(self.achievements)},{self.beer_count},{self.beer_rank},{self.money_streak}"
    def blank (id,name):
        return f"{id},{name},0,0,,,,0,0,0,0,,0,,0,,0,0,0,0,,0,0,0"

    
def clean_up(text):
    """
    Cleans up the array to string text
    """
    text = str(text)[2:-2]
    text.replace(",","|")
    return text




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
    Beer Count
    Beer Prestiege
    Money Streak
"""



#Secret Achievements
#Launch Ultrakill
#Do the wordle 100 times
#Buy 100 Items from the shop