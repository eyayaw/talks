SCHEMA = """
{
    "property_type": "str", // house, condo, apartment, land, apartment_building, warehouse, office, shop, etc.
    "property_use": "str", // commercial, residential, mixed
    "listing_type": "str", // sale, rent, lease
    "price": {
        "value": "float", // property value or rent
        "currency": "str", // ETB, USD
        "unit": "str", // total, per sqm, per month, annually, etc.
        "type": "str" // fixed, negotiable, discounted, installment, etc.
    },
    "address": {
        "original": "str", // The original address in the ad corrected for typos/mistakes
        "transliterated": "str" // Address transliterated in ASCII characters
    },
    "size": {
        "floor_area": "float", // Interior space (sqm). For land: total land area
        "plot_area": "float", // Total lot size, if applicable
        "unit": "str" // sqm, sqft
    },
    "property_condition": "str", // new, excellent, good, fair, poor, under_construction
    "bedrooms": "int",
    "bathrooms": "int",
    "floors": "int", // Total floors in building
    "floor_number": "int", // Which floor the unit is on (for apartments/condos)
    "units": "int", // For multi-unit buildings
    "year_built": "int",
    "year_renovated": "int",
    "furnishing_status": "str", // unfurnished, semi-furnished, fully-furnished
    "occupancy_status": "str", // vacant, occupied, under construction
    "rental_yield": "float", // Potential rental income estimate
    "financing_options": "str", // cash only, mortgage available, installment plan

    "structural_features": {
        "has_basement": "bool",
        "has_garage": "bool",
        "garage_spaces": "int",
        "has_parking": "bool",
        "parking_spaces": "int",
        "has_balcony": "bool",
        "has_terrace": "bool",
        "has_garden": "bool",
        "has_backyard": "bool",
        "has_elevator": "bool",
        "accessibility_features": "list[str]" // wheelchair accessible, ramp, wide doors, etc.
    },

    "interior_features": {
        "flooring_types": "list[str]", // tile, hardwood, carpet, marble, etc.
        "kitchen_type": "str", // modern, traditional, open concept, kitchenette
        "has_fireplace": "bool",
        "built_in_wardrobes": "bool",
        "air_conditioning": "str", // central, split units, window units, none
        "heating_system": "str", // central, radiator, wood stove, none
        "ceiling_height": "float", // in meters
        "storage_spaces": "list[str]" // closets, pantry, attic, etc.
    },

    "building_amenities": {
        "shared_facilities": "list[str]", // gym, pool, rooftop, community_room, etc.
        "security_features": "list[str]", // gated, doorman, cctv, alarm_system, etc.
        "maintenance_services": "list[str]", // cleaning, landscaping, concierge, etc.
        "business_facilities": "list[str]" // conference room, coworking space, etc. (for commercial/mixed)
    },

    "utilities": {
        "electricity": "str", // connected, available, not available
        "water": "str", // municipal, well, not_available
        "gas": "str", // natural_gas, propane, not_available
        "internet": "str", // fiber, broadband, limited, not available
        "sewerage": "str", // municipal, septic, not_available
        "waste_management": "str", // municipal, private, not available
        "backup_power": "bool" // generator, solar backup, etc.
    },

    "utility_costs": {
        "electricity_monthly": "float",
        "gas_monthly": "float",
        "water_monthly": "float",
        "internet_monthly": "float",
        "maintenance_fees": "float", // Monthly building/HOA fees
        "service_charges": "float" // Any additional monthly charges
    },

    "location_attributes": {
        "neighborhood": "str",
        "view": "str", // mountain, city, park, waterfront, street, courtyard
        "noise_level": "str", // quiet, moderate, busy
        "nearby_attractions": "list[str]", // schools, hospitals, malls, parks, etc.
        "transportation": {
            "walkability": "str", // excellent, good, fair, poor
            "public_transport": "list[str]", // bus, metro, taxi, etc.
            "bike_friendly": "bool",
            "parking_availability": "str" // abundant, limited, scarce
        }
    },

    "restrictions": {
        "pets_allowed": "bool",
        "smoking_allowed": "bool",
        "subletting_allowed": "bool",
        "commercial_use_allowed": "bool",
        "minimum_lease_term": "str", // 6 months, 1 year, etc.
        "maximum_occupancy": "int"
    },

    "sustainability": {
        "energy_rating": "str",
        "solar_panels": "bool",
        "ev_charging": "bool",
        "green_certifications": "list[str]",
        "water_conservation": "list[str]", // rainwater harvesting, low_flow_fixtures, etc.
        "waste_management": "list[str]" // recycling, composting, etc.
    },

    "seller": {
        "name": "str",
        "type": "str", // owner, broker, agency, developer
        "contact": {
            "phone": "str",
            "email": "str",
            "telegram": "str",
            "website": "str",
            "office_address": "str"
        },
        "commission": "float", // as percentage of property value
        "license_number": "str", // if applicable for brokers/agencies
        "languages": "list[str]" // languages spoken
    },

    "listing_metadata": {
        "posted_date": "date",
        "expires_date": "date",
        "listing_id": "str",
        "photos": "list[str]", // URLs or file paths
        "virtual_tour": "str", // URL
        "documents": "list[str]", // title deed, permits, etc.
        "verified": "bool", // Whether listing has been verified
        "featured": "bool" // Premium/featured listing
    },

    "description": "str", // Free-form description
    "remarks": "str" // Any additional relevant remarks
}
"""
