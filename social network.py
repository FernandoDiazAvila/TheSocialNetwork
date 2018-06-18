##The Social Network

class User:
    def __init__(self, firstName, lastName, username, bio, userID,):
        self.firstName= firstName
        self.lastName= lastName
        self.username= username
        self.bio= bio
        self.userID= userID
        self.friends=[]
        self.posts=[]

    def addFriend(self,username):
        self.friends.append(username)
            
##        def unFriend():
    
    def viewNewsFeed(self,friends):
        for friend in self.friends:
            print (friends.posts)



if __name__ == "__main__":
     firstName = "Fernando"
     lastName = "Diaz Avila"
     username = "WLP(L)DAvila"
     bio = "Its a Wild llama"
     userID = "3503"
     

     Fernando = User(firstName, lastName, username, bio, userID)
     Bob = User("Bob","TheBuilder","BobTheBuilder", "We Can Fix It","2222")
     MrSharp = User("Mr.Sharp","J","Genius","IDK","6243")
     print(Fernando.firstName)
     print(Bob.firstName)
     print(MrSharp.firstName)

     Fernando.addFriend("Bob")
     Fernando.addFriend("MrSharp")
     print(Fernando.friends)
     print()
     Fernando.posts.append("Llama")
     MrSharp.posts.append("text")
     Bob.posts.append("Yes We Can!")
     print (Fernando.posts)
     print (MrSharp.posts)
     print (Bob.posts)

     Fernando.viewNewsFeed(username)
