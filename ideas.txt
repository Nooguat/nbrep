Objective is to find a way to review notes using all the list entries done -> fully atomic

Self testing is the best way ; goal is to mix the != technics 
Dynamic reading ; typing some parts of the notes; 
	answering to questions generated from the note; graphing out the knowledge
How this should be setup ? 
Need streaking tools (to keep up the practise)

Review delays should be computed using this formula : `4^(level -1)`

--------

# Redefinition

## Previous implementation issues
After reflexion ; previous method would hardly work in long period of time ; some notes are too big

and all the points does not need to be reviewed at the same level (more fined-grain control)

Moreover, this solution is not portable out of the terminal; which limit the capability to 
review notes from anywhere at any time

Finally ; to only read does not have the expected effect according to experiements; if you move
one eye out of the screen; you lost control over the note understanding

## New implementation
- Implementation is based on bullet points as we done since we began to take notes. 
- The algorithm is based on note fill in the blank. The words are picked according to RAKE
evaluation of the note
- The number of missing words are increased for each level of difficulty. At level 4; only keywords
are given and the user need to remember the associated note. At level 6; the user is required to
graph the point out and find 3 links with other notes (this is in thought process; yet to determine)
- Each day, n (10?) new bullet points are added to the system. 
- Those notes can be exported to HTML view; document can be sent to other devices to work on it
- The application can also setup a webserver to do those drill on internal network

**this is still in reflexion ; need to continue to work on this**
