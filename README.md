# p-rotein
Building a random forest classifier model for identifying IDPs from its amino acid sequence

Here's some notes on cloning this directory: 
+ mkdir -p ~/git
+ cd ~/git
+ git clone [copied url to clone]
+ git remote add upstream [url]


Here's some notes on general git use (by Kevin Ayala - p-ai PM): 
+ to start working on an issue, use the command 
git checkout -b name_of_branch
 where the name of the branch equals the issue name. This will make a new branch, so only use it the first time
+ if you're juggling several branches, do 
git checkout branch_name
 to switch between them
+ to add changes to the "envelope", run 
 git add .
. the dot tells it to add all files, but you can also specify specific file paths if you'd like.
+ to "stamp" the envelope, use 
git commit -m "message"
 where "message" is a message describing the changes you've made
+ git push to send it up

I recommend doing a push every time you've finished a work session. Once you've finished the whole issue, push it one last time and head to the github page to start a new pull request.

To start a pull request, go to the main page of the repository, click into "branches", find yours and click into that, then push the green button to "compare and pull request". The message should include the word "resolve" followed by the issue number. Then you're done!

