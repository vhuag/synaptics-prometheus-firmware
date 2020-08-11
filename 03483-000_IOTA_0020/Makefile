VENDOR=Synaptics
PROJECT_NAME=Prometheus_Config
VERSION=0020
FIRMWARE_FILE=prometheus-FM-03483-000_IOTA-Rev0020_prod.pkg
METAINFO_FILE=prometheus.metainfo.xml
PID=0xDF
CONFIGID=03483-000

all: $(VENDOR)-$(PROJECT_NAME)-$(VERSION)-$(CONFIGID)-$(PID).cab

clean:
	rm -f *.cab

check: $(METAINFO_FILE)
	appstream-util validate-relax $(METAINFO_FILE)

%.cab: $(FIRMWARE_FILE) $(METAINFO_FILE)
	gcab --create --nopath $@ $(FIRMWARE_FILE) $(METAINFO_FILE)
