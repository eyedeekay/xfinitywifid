xfinity
=========

This script runs in the background. It pings google.com(This will be changed)
in order to test the connection. If it is successful, it simply logs that fact
and sleeps for a few seconds. I think 3 seconds is probably too few, but we'll
figure that out.

I think the top line of the next stanza of the if statement is an AppleScript
thing. Looks like it's telling the graphical shell to give a pop-up that it will
attempt the xfinitywifi-autospoofer. After it does that it makes sure that the
Captive Network Assistant is killed and runs the
kill\_captive\_network\_assistant.sh script in the background. For some reason
it printfs "Connection Failed" with no other description to stdout *after*
popping up the gui notification, but before trying to run the xfinity.py script.
After emitting to stdout, it tries the xfinity.py script, and sleeps for a
second before killing the background process started by
kill\_captive\_network\_assistant.sh and re-tests the connection. Upon success,
it pops up a notification that the connection worked and the loop re-starts.

