from views import compare_followers

username = "rawheel"
prev_followers = ["usman","raheel","shahzaib"]
recent_followers = ["raheel","shahzaib"]


# If Someone Unfollows Test
object = compare_followers(username,prev_followers,recent_followers)
print(object)

#If Someone Follows Test
prev_followers = ["usman","raheel","shahzaib"]
recent_followers = ["usman","raheel","shahzaib","alishba"]
object = compare_followers(username,prev_followers,recent_followers)
print(object)

#If Someone Follows and Unfollows also Testcase
prev_followers = ["usman","raheel","shahzaib"]
recent_followers = ["raheel","shahzaib","alishba"]
object = compare_followers(username,prev_followers,recent_followers)
print(object)