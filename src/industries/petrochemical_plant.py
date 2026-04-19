from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="petrochemical_plant",
    accept_cargos_with_input_ratios=[("NAPH", 4), ("RGAS", 2), ("CTAR", 2)],
    prod_cargo_types_with_output_ratios=[],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="64",
    colour_scheme_name="scheme_13_whitney",
    name="string(STR_IND_PETROCHEMICAL_PLANT)",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[["oil_refinery"], 96],
        same_type_distance=96,
    ),
    nearby_station_name="string(STR_STATION_PETROCHEMICAL_PLANT)",
    fund_cost_multiplier="200",
    pollution_and_squalor_factor=2,
    sprites_complete=True,
    animated_tiles_fixed=True,
)


def _reuse_copper_smelter_graphics(terrain=None, construction_state_num=None):
    return '"src/graphics/industries/copper_smelter.png"'


industry.get_graphics_file_path = _reuse_copper_smelter_graphics

industry.enable_in_economy(
    "OIL_TOWN",
    prod_cargo_types_with_output_ratios=[
        ("ETHY", 5),
        ("CHEM", 3),
    ],
)

industry.add_tile(
    id="petrochemical_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="petrochemical_plant_tile_2",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="gravel",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -31)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -26)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -31)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 128, -31, -95)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 128, -31, -95)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 128, -31, -95)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 56, -31, -26)],
    always_draw=True,
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 56, -31, -26)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 64, -31, -31)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 64, -31, -31)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(710, 10, 64, 110, -31, -61)],
)
sprite_transformer = industry.add_sprite(
    sprite_number=2054,
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=1,
    yoffset=0,
    zoffset=72,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=-12,
    yoffset=0,
    zoffset=56,
    animation_frame_offset=1,
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=0,
    zoffset=56,
    animation_frame_offset=2,
)

industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_tanks",
    tile="petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_thickening_tank",
    tile="petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_big_shed",
    tile="petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_flue_stack",
    tile="petrochemical_plant_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_ore_handling_front",
    tile="petrochemical_plant_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    smoke_sprites=[sprite_smoke_2, sprite_smoke_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_ore_handling_rear",
    tile="petrochemical_plant_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_copper_forklift",
    tile="petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=8,
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_small_shed",
    tile="petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_stack_vent_thing",
    tile="petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_ground",
    tile="petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_transformer",
    tile="petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[sprite_transformer],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=9,
)
industry.add_spritelayout(
    id="petrochemical_plant_spritelayout_empty",
    tile="petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=10,
)

industry.add_multi_tile_object(
    add_to_object_num=4,
    view_layout=[
        (0, 0, "petrochemical_plant_spritelayout_ore_handling_rear"),
        (1, 0, "petrochemical_plant_spritelayout_ore_handling_front"),
    ],
)

industry.add_industry_layout(
    id="petrochemical_plant_industry_layout_1",
    layout=[
        (0, 0, "petrochemical_plant_spritelayout_transformer"),
        (0, 1, "petrochemical_plant_spritelayout_big_shed"),
        (0, 2, "petrochemical_plant_spritelayout_big_shed"),
        (0, 3, "petrochemical_plant_spritelayout_small_shed"),
        (1, 0, "petrochemical_plant_spritelayout_ore_handling_rear"),
        (1, 1, "petrochemical_plant_spritelayout_tanks"),
        (1, 2, "petrochemical_plant_spritelayout_stack_vent_thing"),
        (1, 3, "petrochemical_plant_spritelayout_copper_forklift"),
        (2, 0, "petrochemical_plant_spritelayout_ore_handling_front"),
        (2, 1, "petrochemical_plant_spritelayout_tanks"),
        (2, 2, "petrochemical_plant_spritelayout_stack_vent_thing"),
        (2, 3, "petrochemical_plant_spritelayout_ground"),
        (3, 0, "petrochemical_plant_spritelayout_flue_stack"),
        (3, 1, "petrochemical_plant_spritelayout_thickening_tank"),
        (3, 2, "petrochemical_plant_spritelayout_thickening_tank"),
        (3, 3, "petrochemical_plant_spritelayout_ground"),
    ],
)

industry.add_industry_layout(
    id="petrochemical_plant_industry_layout_2",
    layout=[
        (0, 0, "petrochemical_plant_spritelayout_ore_handling_rear"),
        (0, 1, "petrochemical_plant_spritelayout_stack_vent_thing"),
        (0, 2, "petrochemical_plant_spritelayout_tanks"),
        (0, 3, "petrochemical_plant_spritelayout_flue_stack"),
        (0, 4, "petrochemical_plant_spritelayout_tanks"),
        (0, 5, "petrochemical_plant_spritelayout_small_shed"),
        (1, 0, "petrochemical_plant_spritelayout_ore_handling_front"),
        (1, 1, "petrochemical_plant_spritelayout_stack_vent_thing"),
        (1, 2, "petrochemical_plant_spritelayout_big_shed"),
        (1, 3, "petrochemical_plant_spritelayout_big_shed"),
        (1, 4, "petrochemical_plant_spritelayout_big_shed"),
        (1, 5, "petrochemical_plant_spritelayout_copper_forklift"),
        (2, 0, "petrochemical_plant_spritelayout_transformer"),
        (2, 1, "petrochemical_plant_spritelayout_small_shed"),
        (2, 2, "petrochemical_plant_spritelayout_thickening_tank"),
        (2, 3, "petrochemical_plant_spritelayout_thickening_tank"),
        (2, 4, "petrochemical_plant_spritelayout_ground"),
        (2, 5, "petrochemical_plant_spritelayout_ground"),
    ],
)

industry.add_industry_layout(
    id="petrochemical_plant_industry_layout_3",
    layout=[
        (0, 0, "petrochemical_plant_spritelayout_thickening_tank"),
        (0, 1, "petrochemical_plant_spritelayout_tanks"),
        (0, 2, "petrochemical_plant_spritelayout_flue_stack"),
        (0, 3, "petrochemical_plant_spritelayout_tanks"),
        (0, 4, "petrochemical_plant_spritelayout_ore_handling_rear"),
        (1, 0, "petrochemical_plant_spritelayout_thickening_tank"),
        (1, 1, "petrochemical_plant_spritelayout_big_shed"),
        (1, 2, "petrochemical_plant_spritelayout_big_shed"),
        (1, 3, "petrochemical_plant_spritelayout_big_shed"),
        (1, 4, "petrochemical_plant_spritelayout_ore_handling_front"),
        (2, 0, "petrochemical_plant_spritelayout_transformer"),
        (2, 1, "petrochemical_plant_spritelayout_big_shed"),
        (2, 2, "petrochemical_plant_spritelayout_big_shed"),
        (2, 3, "petrochemical_plant_spritelayout_big_shed"),
        (2, 4, "petrochemical_plant_spritelayout_stack_vent_thing"),
        (3, 1, "petrochemical_plant_spritelayout_copper_forklift"),
        (3, 2, "petrochemical_plant_spritelayout_small_shed"),
        (3, 3, "petrochemical_plant_spritelayout_ground"),
        (3, 4, "petrochemical_plant_spritelayout_stack_vent_thing"),
    ],
)
