from economy import Economy

economy = Economy(
    id="OIL_TOWN",
    numeric_id=6,
    cargos=[
        "coal",
        "heavy_oil",
        "light_oil",
        "lng",
        "lpg",
        "naphtha",
        "oil",
        "passengers",
        "raw_gas",
        "refinery_gas",
        "sulphur",
    ],
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [],
        "ranking_subgraphs": [],
        "clusters": [],
    },
)

economy.add_biome(
    "more_south_west",
    min_x_percent=35,
    max_x_percent=100,
    min_y_percent=0,
    max_y_percent=100,
)
economy.add_biome(
    "less_south_west",
    min_x_percent=0,
    max_x_percent=65,
    min_y_percent=0,
    max_y_percent=100,
)
