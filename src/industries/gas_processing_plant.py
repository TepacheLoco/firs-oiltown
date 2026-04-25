from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="gas_processing_plant",
    accept_cargos_with_input_ratios=[
        ("NGAS", 8),
        ("RGAS", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("LNG_", 3),
        ("LPG_", 3),
        ("SULP", 2),
        ("COND", 1),
    ],
    prob_in_game="4",
    prob_map_gen="6",
    map_colour="168",
    colour_scheme_name="scheme_1_elton",
    special_flags=["IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE"],
    name="string(STR_IND_GAS_PROCESSING_PLANT)",
    nearby_station_name="string(STR_STATION_GAS_PROCESSING_PLANT)",
    fund_cost_multiplier="170",
    provides_snow=True,
    sprites_complete=False,
    animated_tiles_fixed=False,
)

industry.enable_in_economy(
    "OIL_TOWN",
    prob_in_game="2",
    prob_map_gen="3",
)

industry.add_tile(
    id="gas_processing_plant_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(500, 10, 64, 66, -31, -35)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(570, 10, 64, 66, -31, -35)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(710, 10, 64, 66, -31, -35)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(80, 10, 64, 88, -31, -58)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(150, 10, 64, 88, -31, -59)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(220, 10, 64, 88, -31, -64)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(360, 10, 64, 73, -31, -45)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(430, 10, 64, 66, -31, -38)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=1,
    yoffset=0,
    zoffset=62,
    animation_frame_offset=1,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big", xoffset=1, yoffset=-3, zoffset=62
)

industry.add_spritelayout(
    id="gas_processing_plant_spritelayout_1",
    tile="gas_processing_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_processing_plant_spritelayout_2",
    tile="gas_processing_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_processing_plant_spritelayout_3",
    tile="gas_processing_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_processing_plant_spritelayout_4",
    tile="gas_processing_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_processing_plant_spritelayout_5",
    tile="gas_processing_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_processing_plant_spritelayout_6_anim",
    tile="gas_processing_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_6],
    smoke_sprites=[sprite_smoke_2, sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_processing_plant_spritelayout_7",
    tile="gas_processing_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_processing_plant_spritelayout_8",
    tile="gas_processing_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_processing_plant_spritelayout_9",
    tile="gas_processing_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="gas_processing_plant_industry_layout_1",
    layout=[
        (0, 0, "gas_processing_plant_spritelayout_9"),
        (0, 1, "gas_processing_plant_spritelayout_2"),
        (0, 2, "gas_processing_plant_spritelayout_1"),
        (0, 3, "gas_processing_plant_spritelayout_1"),
        (1, 0, "gas_processing_plant_spritelayout_8"),
        (1, 1, "gas_processing_plant_spritelayout_4"),
        (1, 2, "gas_processing_plant_spritelayout_5"),
        (1, 3, "gas_processing_plant_spritelayout_6_anim"),
        (2, 0, "gas_processing_plant_spritelayout_7"),
        (2, 1, "gas_processing_plant_spritelayout_9"),
        (2, 2, "gas_processing_plant_spritelayout_3"),
        (2, 3, "gas_processing_plant_spritelayout_9"),
    ],
)
industry.add_industry_layout(
    id="gas_processing_plant_industry_layout_2",
    layout=[
        (0, 0, "gas_processing_plant_spritelayout_8"),
        (0, 1, "gas_processing_plant_spritelayout_4"),
        (0, 2, "gas_processing_plant_spritelayout_5"),
        (0, 3, "gas_processing_plant_spritelayout_6_anim"),
        (0, 4, "gas_processing_plant_spritelayout_9"),
        (1, 0, "gas_processing_plant_spritelayout_7"),
        (1, 1, "gas_processing_plant_spritelayout_9"),
        (1, 2, "gas_processing_plant_spritelayout_3"),
        (1, 3, "gas_processing_plant_spritelayout_9"),
        (1, 4, "gas_processing_plant_spritelayout_9"),
        (2, 0, "gas_processing_plant_spritelayout_9"),
        (2, 1, "gas_processing_plant_spritelayout_9"),
        (2, 2, "gas_processing_plant_spritelayout_1"),
        (2, 3, "gas_processing_plant_spritelayout_1"),
        (2, 4, "gas_processing_plant_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="gas_processing_plant_industry_layout_3",
    layout=[
        (0, 0, "gas_processing_plant_spritelayout_2"),
        (0, 1, "gas_processing_plant_spritelayout_2"),
        (0, 2, "gas_processing_plant_spritelayout_9"),
        (1, 0, "gas_processing_plant_spritelayout_9"),
        (1, 1, "gas_processing_plant_spritelayout_4"),
        (1, 2, "gas_processing_plant_spritelayout_3"),
        (2, 0, "gas_processing_plant_spritelayout_8"),
        (2, 1, "gas_processing_plant_spritelayout_5"),
        (2, 2, "gas_processing_plant_spritelayout_6_anim"),
        (3, 0, "gas_processing_plant_spritelayout_7"),
        (3, 1, "gas_processing_plant_spritelayout_3"),
        (3, 2, "gas_processing_plant_spritelayout_9"),
        (4, 0, "gas_processing_plant_spritelayout_9"),
        (4, 1, "gas_processing_plant_spritelayout_1"),
        (4, 2, "gas_processing_plant_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="gas_processing_plant_industry_layout_4",
    layout=[
        (0, 0, "gas_processing_plant_spritelayout_1"),
        (0, 1, "gas_processing_plant_spritelayout_9"),
        (0, 2, "gas_processing_plant_spritelayout_8"),
        (1, 0, "gas_processing_plant_spritelayout_1"),
        (1, 1, "gas_processing_plant_spritelayout_9"),
        (1, 2, "gas_processing_plant_spritelayout_7"),
        (2, 0, "gas_processing_plant_spritelayout_4"),
        (2, 1, "gas_processing_plant_spritelayout_5"),
        (2, 2, "gas_processing_plant_spritelayout_6_anim"),
        (3, 0, "gas_processing_plant_spritelayout_2"),
        (3, 1, "gas_processing_plant_spritelayout_3"),
        (3, 2, "gas_processing_plant_spritelayout_9"),
    ],
)
