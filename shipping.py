#From Shippo API Docs https://goshippo.com/docs

import shippo

shippo.config.api_key = "shippo_test_8121f1d078ea09050a0bba4b60cc2cb15d508530" #Test Key

address_from = {
    "name": "Shawn Ippotle",
    "street1": "215 Clayton St.",
    "city": "San Francisco",
    "state": "CA",
    "zip": "94117",
    "country": "US"
}

address_to = {
    "name": "Mr Hippo",
    "street1": "Broadway 1",
    "city": "New York",
    "state": "NY",
    "zip": "10007",
    "country": "US"
}

parcel = {
    "length": "5",
    "width": "5",
    "height": "5",
    "distance_unit": "in",
    "weight": "2",
    "mass_unit": "lb"
}

def create_shipment():
    shipment = shippo.Shipment.create(
        address_from = address_from,
        address_to = address_to,
        parcels = [parcel],
        async = False
    )
    print (shipment) # Potential "illegal" print statement (?)
    return shipment
