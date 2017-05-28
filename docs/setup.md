setup
======

This is the installer script. I'm going to replace it with a Makefile instead.

First, it makes sure the dependencies of the python script are installed. It
installs pip via easy_install, then installs a library. This library is called
[Splinter]().

Then it creates a directory under the /Applications/ folder named
xfinitywifi-autospoof and makes sure the directory is empty.

Then it copies the scripts in this folder to the newly-created
/Applications/xfinitywifi-autospoof/ folder and the geckodriver to
/usr/local/bin.


