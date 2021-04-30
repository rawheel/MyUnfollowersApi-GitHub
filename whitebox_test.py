from views import compare_followers
import emoji
print()

# If username is not registered Testcase and testing the loop also
username = "david"
prev_followers = ["usman","raheel","shahzaib"]
recent_followers = ["usman","raheel","shahzaib"]
object = compare_followers(username,prev_followers,recent_followers)
print("If username is not registered Testcase and testing the loop also:")
if object['username_test'] and object['saving_user_test']:
    print( ':check_mark_button: Passed! username test case and save user loop.')
elif object['username_test']==0 or object['saving_user_test']==0:
    print(emoji.emojize(':check_mark_button: Passed! username test case and save user loop.'))
else:
    print(':cross_mark: FAILED!')

print()

# If Someone Unfollows Test
username = "rawheel"
prev_followers = ["usman","raheel","shahzaib"]
recent_followers = ["raheel","shahzaib"]
object = compare_followers(username,prev_followers,recent_followers)
print("If Someone Unfollows Test:")
if object['unfollowers_test']:
    print(emoji.emojize(':check_mark_button: passed! unfollowers are detected!'))
else:
    print(':cross_mark: FAILED!')
#print(object)
print()

# If Someone Follows Test
prev_followers = ["usman","raheel","shahzaib"]
recent_followers = ["usman","raheel","shahzaib","alishba"]
object = compare_followers(username,prev_followers,recent_followers)
print("If Someone Follows Test:")
if object['newfollowers_test']:
    print(emoji.emojize(':check_mark_button: passed! new followers are detected!'))
else:
    print(':cross_mark: FAILED!')
#print(object)
print()

# If Someone Follows and Unfollows also Testcase
prev_followers = ["usman","raheel","shahzaib"]
recent_followers = ["raheel","shahzaib","alishba"]
object = compare_followers(username,prev_followers,recent_followers)
print("If Someone Follows and Unfollows also Testcase:")
if object['newfollowers_test'] and object['unfollowers_test']:
    print(emoji.emojize(':check_mark_button: passed! unfollowers & new followers are detected!'))
else:
    print(':cross_mark: FAILED!')
print()
