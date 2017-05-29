intro:
	echo ""

setup-user:
	addgroup --system xfin
	adduser --system --home /usr/share/xfinitywifid --ingroup xfin --disabled-login xfin
	sed -i 's|#includedir /etc/sudoers.d|includedir /etc/sudoers.d|' /etc/sudoers
	echo "Cmnd_Alias MACSPOOF_CMD = /usr/share/xfinitywifid/xfinity-spoofmac" | tee -a /etc/sudoers.d/macspoof
	echo "Defaults!MACSPOOF_CMD !requiretty" | tee -a /etc/sudoers.d/macspoof
	echo "xfin ALL = (root) NOPASSWD: MACSPOOF_CMD" | tee -a /etc/sudoers.d/macspoof


setup-pip:
	sudo easy_install pip

setup-deps:
	apt-get install python3-selenium
	sudo -Hu xfin pip install splinter

install:
	sudo -u xfin cp xfinity /usr/share/xfinitywifid
	sudo -u xfin cp xfinity.py /usr/share/xfinitywifid
	sudo cp xfinity-spoofmac /usr/share/xfinitywifid
	ln -f -s /usr/share/xfinitywifid/xfinity /usr/local/bin


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
