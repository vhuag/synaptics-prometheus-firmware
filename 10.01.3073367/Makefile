VENDOR=Synaptics
PROJECT_NAME=Prometheus
VERSION=10.01.3073367
FIRMWARE_FILE=prometheus-10.01.3073367_prod.pkg
METAINFO_FILE=prometheus.metainfo.xml

all: $(VENDOR)-$(PROJECT_NAME)-$(VERSION).cab

clean:
	rm -f *.cab *.dfu

check: $(METAINFO_FILE)
	appstream-util validate-relax $(METAINFO_FILE)

%.cab: $(FIRMWARE_FILE) $(METAINFO_FILE)
	gcab --create --nopath $@ $(FIRMWARE_FILE) $(METAINFO_FILE)
