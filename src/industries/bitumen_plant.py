from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="bitumen_plant",
    accept_cargos_with_input_ratios=[
        ("HOIL", 5),
        ("COKE", 3),
    ],
    prod_cargo_types_with_output_ratios=[],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="119",
    colour_scheme_name="scheme_10_wyclef",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            ["oil_refinery"],
            96,
        ],
        same_type_distance=72,
    ),
    name="string(STR_IND_BITUMEN_PLANT)",
    nearby_station_name="string(STR_STATION_BITUMEN_PLANT)",
    fund_cost_multiplier="150",
    pollution_and_squalor_factor=2,
    sprites_complete=True,
    animated_tiles_fixed=True,
)


def _reuse_lime_kiln_graphics(terrain=None, construction_state_num=None):
    return '"src/graphics/industries/lime_kiln.png"'


industry.get_graphics_file_path = _reuse_lime_kiln_graphics

industry.enable_in_economy(
    "OIL_TOWN",
    prod_cargo_types_with_output_ratios=[("BITU", 8)],
)

industry.add_tile(
    id="bitumen_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="bitumen_plant_tile_2",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="gravel",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 110, -31, -70)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 110, -31, -70)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -31)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 92, -31, -60)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -31)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=10,
    yoffset=5,
    zoffset=73,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=10,
    yoffset=10,
    zoffset=73,
    animation_frame_offset=1,
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=10,
    yoffset=15,
    zoffset=73,
)

industry.add_spritelayout(
    id="bitumen_plant_spritelayout_1",
    tile="bitumen_plant_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2, sprite_smoke_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="bitumen_plant_spritelayout_2",
    tile="bitumen_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="bitumen_plant_spritelayout_3",
    tile="bitumen_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="bitumen_plant_spritelayout_4",
    tile="bitumen_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="bitumen_plant_spritelayout_5",
    tile="bitumen_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="bitumen_plant_spritelayout_6",
    tile="bitumen_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="bitumen_plant_industry_layout_1",
    layout=[
        (0, 0, "bitumen_plant_spritelayout_2"),
        (0, 1, "bitumen_plant_spritelayout_1"),
        (0, 2, "bitumen_plant_spritelayout_6"),
        (1, 0, "bitumen_plant_spritelayout_4"),
        (1, 1, "bitumen_plant_spritelayout_5"),
        (1, 2, "bitumen_plant_spritelayout_3"),
    ],
)
industry.add_industry_layout(
    id="bitumen_plant_industry_layout_2",
    layout=[
        (0, 0, "bitumen_plant_spritelayout_2"),
        (0, 1, "bitumen_plant_spritelayout_1"),
        (1, 0, "bitumen_plant_spritelayout_4"),
        (1, 1, "bitumen_plant_spritelayout_5"),
        (2, 0, "bitumen_plant_spritelayout_6"),
        (2, 1, "bitumen_plant_spritelayout_3"),
    ],
)
industry.add_industry_layout(
    id="bitumen_plant_industry_layout_3",
    layout=[
        (0, 0, "bitumen_plant_spritelayout_2"),
        (0, 1, "bitumen_plant_spritelayout_1"),
        (0, 2, "bitumen_plant_spritelayout_6"),
        (0, 3, "bitumen_plant_spritelayout_6"),
        (1, 0, "bitumen_plant_spritelayout_4"),
        (1, 1, "bitumen_plant_spritelayout_5"),
        (1, 2, "bitumen_plant_spritelayout_3"),
        (1, 3, "bitumen_plant_spritelayout_6"),
    ],
)
