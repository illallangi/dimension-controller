import kopf

CRD_GROUP = "controllers.illallangi.enterprises"
CRD_VERSION = "v1"
CRD_SINGULAR = "dimension"


@kopf.index(
    group=CRD_GROUP,
    version=CRD_VERSION,
    singular=CRD_SINGULAR,
)
async def dimension_idx(
    namespace,
    body,
    **_,
):
    return {
        namespace: {k: body[k] for k in body},
    }


@kopf.on.probe(
    id=dimension_idx.__name__,
)
async def dimension_probe(
    dimension_idx: kopf.Index,
    **_,
):
    return {
        namespace: [o for o in dimension_idx[namespace]]
        for namespace in dimension_idx
    }
