intro:
	echo ""

setup-user:
	addgroup --system xfin
	adduser --system --home /usr/share/xfinitywifid --ingroup xfin --disabled-login xfin

setup-pip:
	sudo easy_install pip

setup-deps:
	sudo -Hu xfin pip install splinter

install:
	sudo -u xfin cp run /usr/share/xfinitywifid
	sudo -u xfin cp kill_captive_network_assistant.sh /usr/share/xfinitywifid
	sudo -u xfin cp xfinity /usr/share/xfinitywifid
	sudo -u xfin cp xfinity.py /usr/share/xfinitywifid
	ln -f -s run /usr/local/bin


install-osx:
	make remove-osx
	mkdir -p /Applications/xfinitywifi-autospoof/
	cp run /Applications/xfinitywifi-autospoof
	cp kill_captive_network_assistant.sh /Applications/xfinitywifi-autospoof
	cp xfinity /Applications/xfinitywifi-autospoof
	cp xfinity.py /Applications/xfinitywifi-autospoof
	cp geckodriver /usr/local/bin

remove:
	rm -fr /usr/share/xfinitywifid
	rm -f /usr/local/bin/run

remove-osx:
	rm -fr /Applications/xfinitywifi-autospoof/
