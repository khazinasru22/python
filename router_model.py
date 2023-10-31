import miniupnpc

def get_router_model():
    upnp = miniupnpc.UPnP()
    upnp.discoverdelay = 200
    upnp.discover()
    device = upnp.selectigd()

    if device:
        model_name = device.modelname
        return model_name
    else:
        return "Router not found or doesn't support UPnP."

if __name__ == "__main__":
    router_model = get_router_model()
    print("Router Model:", router_model)
