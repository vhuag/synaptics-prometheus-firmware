VENDOR=Synaptics
PROJECT_NAME=Prometheus_Config
VERSION=0009
FIRMWARE_FILE=../../binaries/prometheus-FM-03478-000_IOTA-Rev0009_prod.pkg
METAINFO_FILE=prometheus.metainfo.xml
PID=0xC2
CONFIGID=03478-000

all: $(VENDOR)-$(PROJECT_NAME)-$(VERSION)-$(CONFIGID)-$(PID).cab

clean:
	rm -f *.cab

check: $(METAINFO_FILE)
	appstream-util validate-relax $(METAINFO_FILE)

%.cab: $(FIRMWARE_FILE) $(METAINFO_FILE)
	gcab --create --nopath $@ $(FIRMWARE_FILE) $(METAINFO_FILE)
