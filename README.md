# GhostArp
A GNU/Linux Address Resolution Protocol manipulator that allows for MITM attacks and DOS attacks through Address Resolution Protocol Poisoning

The target of your attack is set through an interactive shell. All traffic flowing into the target or out of the target will be captured.
If the "DOS" variable is set to true, the traffic will not be forwarded and the attacker machine will block all traffic, effectively denial of service
attacking the target

![image](https://user-images.githubusercontent.com/55106700/204055996-642a17c8-3c1c-4fbd-abd4-a8946c4c7ef0.png)



## Installation

git clone the repo

`git clone https://github.com/Lionskey/GhostArp`

change directory to repo folder

`cd GhostArp`

run setup script to install GhostArp
(Note: Sudo is required)

`sudo python3 setup.py`

run software

`sudo ghostarp`

## Extra Notes
I am in no way liable for any damage caused by this software. This software is for educational purposes only.

