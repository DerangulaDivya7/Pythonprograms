class meta:
    def data(self):
        print("meta data.....")
class  facebook(meta):
    def profile(self):
        print("profile from facebook....")
class insta(meta):
    def reels(self):
        print("reels.....")
ob = facebook ()
ob.data()
ob.profile()                
