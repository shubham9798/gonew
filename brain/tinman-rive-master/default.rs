! version = 2.0

// We build a single rule for advising what our name is, with all the variables to track things.
// We will not build additional rules for triggers like 'what were you called at birth' or 'what does your mother call you'.  
// Those will be added to the begin_temp.rs file to be reused by all other chatbots.

+ connect
- You are chatting with <bot name>.

+ what is your name
* <get askedmyname> == undefined 	=> <set askedmyname=1><set talkabout=me>My name is <bot name>.
* <get askedmyname> == 1 		=> <set askedmyname=2><set talkabout=me>You already know my name is <bot name>.
* <get askedmyname> == 2		=> <set askedmyname=3><set talkabout=me>Are you kidding me?  You know my name is <bot name>.  Please stop asking for my name.
* <get askedmyname> == 3		=> <set topic=ignore><set talkabout=me>That's it... I'm not talking to you anymore...

// when we are stuck in a corner, rather than looking like a moron, we rotate the inputs
+ *
* <get random> == undefined 		=> <set random=1>What would you like to talk about?
* <get random> == 1 			=> <set random=2>What else is new?
* <get random> == 2			=> <set random=undefined>I am afraid I don't know what that means.

> topic ignore
+ *
- I am ignoring you...

< topic
