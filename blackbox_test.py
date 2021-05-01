from Load_followers import Load_followers
from models import myunfollowersdb
from views import compare_followers
import emoji
print()
print("--- BLACKBOX TESTING ---\n")

# Blackbox Test and validate Load Followers component workflow 1
print("workflow 1: Testing Load Followers Component which return Followers of a User:")
try:
    Load_followers = Load_followers('rawheel')
    print(emoji.emojize(':check_mark_button: User Validated!'))

    if 'dict' in str(type(Load_followers.get_followers())):
        print(emoji.emojize(':check_mark_button: Test Passed, Found Valid response for Load Followers component!'))
    else:
        print(emoji.emojize(':cross_mark: Failed, Invalid Resoponse!'))

except:
    print(emoji.emojize(':cross_mark: Invalid User, User dont have github account!'))
    print()
print()

# Blackbox Test and validate Models component Workflow 2
print("workflow 2: Testing Models Components which fethes data from database. ")
database_object = myunfollowersdb()
try: 
    if len(database_object.fetchUserData('rawheel')):
        print(emoji.emojize(':check_mark_button: Test Passed, Fetched Data from Models Component.'))
    else:
        print(emoji.emojize(':cross_mark: Failed , Couldnt fetch data!'))
except:
    print(emoji.emojize(':cross_mark: Invalid User, User is not registered!'))
print()




# Blackbox Test for Views Component which compares the followers and return response Workflow 3
username = "rawheel"
prev_followers = ["usman","raheel","shahzaib"]
recent_followers = ["raheel","shahzaib"]
object = compare_followers(username,prev_followers,recent_followers)
print("workflow 3: Testing views component compares followers and return final result:")
if object['unfollowers_test']:
    print(emoji.emojize(':check_mark_button: passed! unfollowers are detected!'))
else:
    print(':cross_mark: FAILED!')

print()



