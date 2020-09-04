VENDOR=Synaptics
PROJECT_NAME=Prometheus
VERSION=10.01.3273255
FIRMWARE_FILE=prometheus-10.01.3273255_prod.pkg
METAINFO_FILE=prometheus.metainfo.xml
PID=0xDF

all: $(VENDOR)-$(PROJECT_NAME)-$(VERSION)-$(PID).cab

clean:
	rm -f *.cab *.dfu

check: $(METAINFO_FILE)
	appstream-util validate-relax $(METAINFO_FILE)

%.cab: $(FIRMWARE_FILE) $(METAINFO_FILE)
	gcab --create --nopath $@ $(FIRMWARE_FILE) $(METAINFO_FILE)
