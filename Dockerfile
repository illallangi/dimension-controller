FROM ghcr.io/illallangi/nu-controller:v0.0.1

ENV CRD_GROUP="controllers.illallangi.enterprises" \
    CRD_VERSION="v1" \
    CRD_SINGULAR="dimension"

ADD templates /config/templates
