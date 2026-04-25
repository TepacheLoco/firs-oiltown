from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="chemical_plant",
    accept_cargos_with_input_ratios=[],
    prod_cargo_types_with_output_ratios=[],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="191",
    colour_scheme_name="scheme_8_haddaway",
    # it's rare to force co-location of secondaries, but this one is near port by design
    # !! this will fail if port is not available in economy
    # wharf was added to avoid pathological case in Arctic Basic where checking for only port would often fail to yield a location (for reasons I didn't fully understand eh)
    # ?? might have been due to industry ID ordering issue, but really not sure about that
    location_checks=dict(
        # near_at_least_one_of_these_keystone_industries=[["port", "wharf"], 96], # !! nerfed off for now as it's just not placing reliably - Jan 2026
        same_type_distance=128,
    ),
    name="string(STR_IND_CHEMICAL_PLANT)",
    nearby_station_name="string(STR_STATION_HEAVY_INDUSTRY_2)",
    fund_cost_multiplier="170",
    pollution_and_squalor_factor=2,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "BASIC_TROPIC",
    accept_cargos_with_input_ratios=[
        ("OIL_", 4),
        ("NITR", 4),
    ],
    prod_cargo_types_with_output_ratios=[
        ("CHEM", 8),
    ],
)

industry.enable_in_economy(
    "BASIC_ARCTIC",
    accept_cargos_with_input_ratios=[
        ("SULP", 2),
        ("PHOS", 2),
        ("NH3_", 2),
        ("POTA", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FERT", 4),
        ("BOOM", 4),
    ],
)

industry.enable_in_economy(
    "OIL_TOWN",
    prob_in_game="2",
    prob_map_gen="3",
    accept_cargos_with_input_ratios=[
        ("ETHY", 3),
        ("SULP", 3),
        ("WATR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("CHEM", 8),
    ],
    require_all_inputs_for_production=True,
)


def _reuse_gas_processing_plant_graphics(terrain=None, construction_state_num=None):
    return '"src/graphics/industries/gas_processing_plant.png"'


industry.get_graphics_file_path = _reuse_gas_processing_plant_graphics

industry.add_tile(
    id="chemical_plant_tile_1",
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
    id="chemical_plant_spritelayout_1",
    tile="chemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_2",
    tile="chemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_3",
    tile="chemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_4",
    tile="chemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_5",
    tile="chemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_6_anim",
    tile="chemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_6],
    smoke_sprites=[sprite_smoke_2, sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_7",
    tile="chemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_8",
    tile="chemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="chemical_plant_spritelayout_9",
    tile="chemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="chemical_plant_industry_layout_1",
    layout=[
        (0, 0, "chemical_plant_spritelayout_9"),
        (0, 1, "chemical_plant_spritelayout_2"),
        (0, 2, "chemical_plant_spritelayout_1"),
        (0, 3, "chemical_plant_spritelayout_1"),
        (1, 0, "chemical_plant_spritelayout_1"),
        (1, 1, "chemical_plant_spritelayout_4"),
        (1, 2, "chemical_plant_spritelayout_5"),
        (1, 3, "chemical_plant_spritelayout_6_anim"),
        (2, 0, "chemical_plant_spritelayout_1"),
        (2, 1, "chemical_plant_spritelayout_9"),
        (2, 2, "chemical_plant_spritelayout_3"),
        (2, 3, "chemical_plant_spritelayout_9"),
    ],
)
industry.add_industry_layout(
    id="chemical_plant_industry_layout_2",
    layout=[
        (0, 0, "chemical_plant_spritelayout_1"),
        (0, 1, "chemical_plant_spritelayout_4"),
        (0, 2, "chemical_plant_spritelayout_5"),
        (0, 3, "chemical_plant_spritelayout_6_anim"),
        (0, 4, "chemical_plant_spritelayout_9"),
        (1, 0, "chemical_plant_spritelayout_1"),
        (1, 1, "chemical_plant_spritelayout_9"),
        (1, 2, "chemical_plant_spritelayout_3"),
        (1, 3, "chemical_plant_spritelayout_9"),
        (1, 4, "chemical_plant_spritelayout_9"),
        (2, 0, "chemical_plant_spritelayout_9"),
        (2, 1, "chemical_plant_spritelayout_9"),
        (2, 2, "chemical_plant_spritelayout_1"),
        (2, 3, "chemical_plant_spritelayout_1"),
        (2, 4, "chemical_plant_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="chemical_plant_industry_layout_3",
    layout=[
        (0, 0, "chemical_plant_spritelayout_2"),
        (0, 1, "chemical_plant_spritelayout_2"),
        (0, 2, "chemical_plant_spritelayout_9"),
        (1, 0, "chemical_plant_spritelayout_9"),
        (1, 1, "chemical_plant_spritelayout_4"),
        (1, 2, "chemical_plant_spritelayout_3"),
        (2, 0, "chemical_plant_spritelayout_1"),
        (2, 1, "chemical_plant_spritelayout_5"),
        (2, 2, "chemical_plant_spritelayout_6_anim"),
        (3, 0, "chemical_plant_spritelayout_1"),
        (3, 1, "chemical_plant_spritelayout_3"),
        (3, 2, "chemical_plant_spritelayout_9"),
        (4, 0, "chemical_plant_spritelayout_9"),
        (4, 1, "chemical_plant_spritelayout_1"),
        (4, 2, "chemical_plant_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="chemical_plant_industry_layout_4",
    layout=[
        (0, 0, "chemical_plant_spritelayout_1"),
        (0, 1, "chemical_plant_spritelayout_9"),
        (0, 2, "chemical_plant_spritelayout_1"),
        (1, 0, "chemical_plant_spritelayout_1"),
        (1, 1, "chemical_plant_spritelayout_9"),
        (1, 2, "chemical_plant_spritelayout_1"),
        (2, 0, "chemical_plant_spritelayout_4"),
        (2, 1, "chemical_plant_spritelayout_5"),
        (2, 2, "chemical_plant_spritelayout_6_anim"),
        (3, 0, "chemical_plant_spritelayout_2"),
        (3, 1, "chemical_plant_spritelayout_3"),
        (3, 2, "chemical_plant_spritelayout_9"),
    ],
)
