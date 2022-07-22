customers = {'turtle':32, 'bobcat':33}

if 'bobcat' in customers:
    print('bobcat!')
if 'kumquat' in customers:
    print('kumquat!')
else:
    print('not here')

    print("${:,.2f}".format(1234567.89))

departments = [
    {
        "name": "kitchen & dining",
        "url_name": "kitchen-dining",
        "products": [
            {
                "id": 0,
                "product": "cookware set",
                "name": "Caraway Home Silt Green 7-Piece Non-Stick Ceramic Cookware Set",
                "price": 545.00,
                "image_loc": "store/images/caraway_cookware_set.jpg"
            },
            {
                "id": 1,
                "product": "kitchen knife set",
                "name": "Miyabi 10-Piece Knife Set",
                "price": 525.00,
                "image_loc": "store/images/miyabi_knife_set.jpg"
            },
            {
                "id": 2,
                "product": "tea kettle",
                "name": "Simplex Buckingham No. 1 Copper Rapid Boil Tea Kettle",
                "price": 399.95,
                "image_loc": "store/images/simplex_buckingham_kettle.jpg"            
            },
            {
                "id": 3,
                "product": "dinnerware set",
                "name": "Royal Albert Old Country Roses 20-Piece Dinnerware Set",
                "price": 525.00,
                "image_loc": "store/images/royal_albert_dinnerware_set.jpg"
            },
        ]
    },
    {
        "name": "furniture",
        "url_name": "furniture",
        "products": [
            {
                "id": 100,
                "product": "rocking chair",
                "name": "Hand-Crafted Walnut Rocking Chair",
                "price": 10000.00,
                "image_loc": "store/images/walnut_rocking_chair.jpg" 
            },
            {
                "id": 101,
                "product": "sofa",
                "name": "Peugeot Onyx Sofa",
                "price": 185000.00,
                "image_loc": "store/images/peugeot_onyx_sofa.jpg"

            },
            {
                "id": 102,
                "product": "coffee table",
                "name": "Boca do Lobo Lapiaz Oval Coffee Table",
                "price": 10730.00,
                "image_loc": "store/images/lapiaz-oval-center-table.png"
            },
        ],
    },
    {
        "name": "bed & bath",
        "url_name": "bed-bath",
        "products": [
            {
                "id": 200,
                "product": "bed",
                "name": "Maitland-Smith Orleans Bed",
                "price": 24747.75,
                "image_loc": "store/images/orleans_bed.jpg"
            },
            {
                "id": 201,
                "product": "chest of drawers",
                "name": "Chippendale Mahogany Chest of Drawers",
                "price": 7853.00,
                "image_loc": "store/images/chippendale_drawers.jpg"
            },
            {
                "id": 202,
                "product": "tub",
                "name": "'The Cathryn Adele68' 68-inch Cast Iron French Bateau Clawfoot Tub plus Drain",
                "price": 5195.00,
                "image_loc": "store/images/cathryn_adele_68in_clawfoot_tub.jpg"            
            },
        ],
    },
    {
        "name": "office",
        "url_name": "office",
        "products": [
            {
                "id": 300,
                "product": "desk",
                "name": "David Micahel 90-inch Executive Desk",
                "price": 52584.53,
                "image_loc": "store/images/david_michael_desk.jpg"
            },
            {
                "id": 301,
                "product": "office chair",
                "name": "Old Hickory Tannery Executive Chair",
                "price": 7560.00,
                "image_loc": "store/images/old_hickory_tannery_office_chair.jpg"
            },
            {
                "id": 302,
                "product": "desk lamp",
                "name": "Meyda Tiffany Utica 17-inch Black Lamp with USB",
                "price": 6300.00,
                "image_loc": "store/images/meyda_tiffanny_desk_lamp.jpg"            
            }
        ],
    },
    {
        "name": "baby & kids",
        "url_name": "baby-kids",
        "products": [
            {
                "id": 400,
                "product": "crib",
                "name": "Art-For-Kids Seashore Crib",
                "price": 3200.00,
                "image_loc": "store/images/ArtForKids_Seashore_Crib.jpg"
            },
            {
                "id": 401,
                "product": "playset",
                "name": "Kid’s Creations Adventure Mountain Redwood Playset",
                "price": 13999.00,
                "image_loc": "store/images/kids-creation-backyard-playset.jpeg"
            },
            {
                "id": 402,
                "product": "puppy",
                "name": "Naughty Puppy",
                "price": 0.00,
                "pretty_price": "$|_0\/3",
                "image_loc": "store/images/puppy_trouble.jpg"            
            },
        ]
    }
]

for dept in departments:
    for product in dept["products"]:
        if "pretty_price" not in product:
            product["pretty_price"] = "${:,.2f}".format(product["price"])

print(departments)        