##The Social Network

class User:
    def __init__(self,username):
        self.username= username
        self.firstName= ""
        self.lastName= ""
        self.bio= ""
        self.friends=[]
        self.posts=[]

    def viewFriends(self, friends):
        for people in friends:
            print(people.username)
        
    def addfirstName(self,firstName):
        self.firstName=firstName
        
    def addlastName(self,lastName):
        self.lastName=lastName
        
    def addbio(self,bio):
        self.bio=bio
        
    def addFriend(self,something):
        self.friends.append(something)
        
    def addposts(self,posts):
        self.posts.append(posts)

    def unFriend(self,yoda):
        for friend in self.friends:
            if friend.username == yoda.username:
                self.friends.remove(yoda)
                
        
    
    def viewNewsFeed(self,friends):
        for friend in self.friends:
            print(friend.posts)



if __name__ == "__main__":
     username = "WLP(L)DAvila"
    


     Fernando = User(username)
     Bob = User("BobTheBuilder")
     MrSharp = User("Genius")
     
##     print(Fernando.username)
##     print(Bob.username)
##     print(MrSharp.username)
     
     Fernando.addFriend(Bob)
     Fernando.addFriend(MrSharp)
     
     Fernando.addposts("Llama")
     MrSharp.addposts("text")
     Bob.addposts("Yes We Can!")
     
     Fernando.viewFriends(Fernando.friends)
     Fernando.viewNewsFeed(Fernando.friends)
     Fernando.unFriend(Bob)
     Fernando.viewFriends(Fernando.friends)
##     Fernando.addposts()
##     print (Fernando.posts)
##     print (MrSharp.posts)
##     print (Bob.posts)

     
