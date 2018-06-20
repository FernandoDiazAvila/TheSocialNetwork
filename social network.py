##The Social Network

class User:
    def __init__(self,username):
        self.username= username
        self.firstName= ""
        self.lastName= ""
        self.bio= ""
        self.friends=[]
        self.posts=[]
        self.userID=""
        self.createpostID=""

        

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
   

    def unFriend(self,yoda):
        for friend in self.friends:
            if friend.username == yoda.username:
                self.friends.remove(yoda)
                
        
    
    def viewNewsFeed(self,friends):
        for friend in self.friends:
            print(friend.posts)
        

##    def createPostID(self,num):
##        self.postID=len(self.posts)


    def createPost(self,content):
        mypost=post(content)
        self.posts.append(mypost)
        mypost.createPostID(len(self.posts))

    def createUserID(self,num):
        self.usersID=num




class post:
    def __init__(self,content):
        self.content=content
        self.postID=""
        self.comments=[]


    def createPostID(self,num):
        self.postID=num
        
    def createComent(self,comment):
        self.comments.append(comment)





class Network:
    def __init__(self):
        self.users=[]


    def createuser(self,username):
        myUser = User(username)
        self.users.append(myUser)
        myUser.createUserID(len(self.users))
        print ("*New User Created*")

    def getUserID(self,username):
        for b in self.users:
            if b.username == username:
                return b.userID

    def reciveOBJ(self,username):
        userID=self.getUserID(username)
        userOBJ = self.useres[userID-]
        return userOBJ

    def connect(self,user1,user2,user3):
        user1OBJ=self.getOBJ(user1)
        user2OBJ=self.getOBJ(user2)
        user3OBJ=self.getOBJ(user3)

        user1OBJ.addfriend(user2OBJ)
        user1OBJ.addfriend(user3OBJ)
        

        





if __name__ == "__main__":
    network=Network()
    network.createuser("Fernando")
    network.createuser("Bob")
    network.createuser("MrSharp")
    



     
##     Fernando.addFriend(Bob)
##     Fernando.addFriend(MrSharp)
##     
##     Fernando.createPost("Llama")
##     MrSharp.createPost("text")
##     Bob.createPost("Yes We Can!")
     
##     Fernando.viewFriends(Fernando.friends)
##     Fernando.viewNewsFeed(Fernando.friends)
##     Fernando.unFriend(Bob)
##     Fernando.viewFriends(Fernando.friends)






##     Fernando.addposts()
##     print (Fernando.posts)
##     print (MrSharp.posts)
##     print (Bob.posts)

     
