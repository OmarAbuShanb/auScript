import os
import sys
import threading
import time

from colorama import Fore, Style
from instaloader import instaloader

done = False
animation = "|/-\\"


def animate():
    i = 0
    while done is False:
        time.sleep(0.1)
        sys.stdout.write("\rLoading " + animation[i % len(animation)] + "*")
        sys.stdout.flush()
        i += 1


print(Fore.RED + Style.BRIGHT + "Hello I'm Omar Mustafa Script ヾ(⌐■_■)ノ♪")
username = ""
password = ""


def login():
    create = open("login.txt", "w")
    create.write("")
    passwordUser = str(input(Fore.RED + Style.BRIGHT + "Username : "))
    usernameUser = str(input(Fore.RED + Style.BRIGHT + "Password : "))
    if len(usernameUser.strip()) < 4 or len(passwordUser.strip()) < 6:
        print(Fore.RED + Style.BRIGHT + "Please enter correct information.")
        login()
    else:
        create.write(passwordUser + "\n" + usernameUser)
    create.close()


if (not os.path.exists("login.txt")) or len(open("login.txt", "r").read().strip()) == 0:
    login()
else:
    inputPress = input(Fore.RED + Style.BRIGHT + "To enter a new account, press n" + "\n" + "To continue enter")
    if inputPress == "n":
        login()
if not os.path.exists("users.txt"):
    createUsers = open("users.txt", "x")
    createUsers.close()
qq = open("users.txt", "r")
val = 0
for x in qq:
    print(Fore.GREEN + Style.BRIGHT + str(val) + " " + str(x)[13:].strip())
    val += 1

qq.close()
qqq = ""
if val == 0:
    qqq = input(Fore.RED + Style.BRIGHT + "Enter a new account : ")
else:
    qqq = input(Fore.RED + Style.BRIGHT + "Enter the account number or Create a new account : ")
id = ""
us = ""
if len(qqq) <= 2:
    val2 = 0
    xxx = open("users.txt", "r")
    for xx in xxx:
        if str(val2) == str(qqq):
            id = str(xx)[:13].strip()
            us = str(xx)[13:].strip()
        val2 += 1
    xxx.close()
loginInfo = open("login.txt", "r").readlines()
username = str(loginInfo[0]).strip()
password = str(loginInfo[1])

t = threading.Thread(target=animate)
t.start()
L = instaloader.Instaloader()
L.login(username, password)
done = True


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def saveOldFollow(user):
    profile = instaloader.Profile.from_username(L.context, user)
    # if profile.followed_by_viewer is False & profile.is_private:
    #     print('this account is private')
    if user == "omar._mustafa0":
        print('Something went wrong')
    else:
        hh = open("users.txt", "a")
        hh.write(str(profile.userid) + "     " + user.strip() + "\n")
        hh.close()
        f = open(user + "-oldFollowing.txt", "w")
        for followingList in profile.get_followees():
            f.write(str(followingList.userid) + "     " + str(followingList.username) + "\n")
        f.close()

        t = open(user + "-oldFollowers.txt", "w")
        for followersList in profile.get_followers():
            t.write(str(followersList.userid) + "     " + str(followersList.username) + "\n")
        t.close()
        print(Fore.GREEN + Style.BRIGHT + "The account has been added successfully.")


def oldAndNewFollow(user):
    oldFollowing = []
    oldFollowing2 = []
    newFollowing = []
    newFollowing2 = []

    profile = instaloader.Profile.from_id(L.context, int(id))

    for FollowingList in profile.get_followees():
        newFollowing.append(str(FollowingList.userid) + "     " + str(FollowingList.username))

    newUs = profile.username
    if newUs != us:
        replace_line('users.txt', int(qqq.strip()), id + "     " + newUs)
        os.rename(user + "-oldFollowing.txt", newUs + "-oldFollowing.txt")
        os.rename(user + "-oldFollowers.txt", newUs + "-oldFollowers.txt")
        user = profile.username

    r = open(user + "-oldFollowing.txt", "r")
    for g in r:
        oldFollowing.append(str(g).strip())
    r.close()

    for z in oldFollowing:
        oldFollowing2.append(z[13:].strip())

    for z in newFollowing:
        newFollowing2.append(z[13:].strip())

    print(Fore.RED + Style.BRIGHT + "\nUnfollowed accounts")
    for z in oldFollowing2:
        if z not in newFollowing2:
            print(Fore.BLUE + Style.BRIGHT + '@' + z)

    print(Fore.RED + Style.BRIGHT + "\nAccounts I've Followed :")
    for z in newFollowing2:
        if z not in oldFollowing2:
            print(Fore.BLUE + Style.BRIGHT + '@' + z)

    oldFollowers = []
    oldFollowers2 = []
    newFollowers = []
    newFollowers2 = []

    for FollowersList in profile.get_followers():
        newFollowers.append(str(FollowersList.userid) + "     " + str(FollowersList.username))

    r = open(user + "-oldFollowers.txt", "r")
    for g in r:
        oldFollowers.append(str(g).strip())
    r.close()

    for z in oldFollowers:
        oldFollowers2.append(z[13:].strip())

    for z in newFollowers:
        newFollowers2.append(z[13:].strip())

    print(Fore.RED + Style.BRIGHT + "\nAccounts unfollowed me :")
    for z in oldFollowers2:
        if z not in newFollowers2:
            print(Fore.BLUE + Style.BRIGHT + '@' + z)

    print(Fore.RED + Style.BRIGHT + "\nAccounts that started following :")
    for z in newFollowers2:
        if z not in oldFollowers2:
            print(Fore.BLUE + Style.BRIGHT + '@' + z)
    ##################################################
    f = open(user + "-oldFollowing.txt", "w")
    for newFollowingList in newFollowing:
        f.write(str(newFollowingList).strip() + "\n")
    f.close()

    t = open(user + "-oldFollowers.txt", "w")
    for newFollowersList in newFollowers:
        t.write(str(newFollowersList).strip() + "\n")
    t.close()


if len(qqq) <= 2:
    oldAndNewFollow(us)
elif len(qqq) > 3 & len(qqq) < 15:
    saveOldFollow(qqq)
