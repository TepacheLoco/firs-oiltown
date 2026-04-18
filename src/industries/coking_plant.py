from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="coking_plant",
    accept_cargos_with_input_ratios=[("COAL", 8)],
    prod_cargo_types_with_output_ratios=[],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="183",
    colour_scheme_name="scheme_9_shania",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            ["coal_mine"],
            72,
        ],
        same_type_distance=72,
    ),
    name="string(STR_IND_COKING_PLANT)",
    nearby_station_name="string(STR_STATION_COKING_PLANT)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=2,
    sprites_complete=True,
    animated_tiles_fixed=True,
)


def _reuse_coke_oven_graphics(terrain=None, construction_state_num=None):
    return '"src/graphics/industries/coke_oven.png"'


industry.get_graphics_file_path = _reuse_coke_oven_graphics

industry.enable_in_economy(
    "OIL_TOWN",
    prod_cargo_types_with_output_ratios=[
        ("COKE", 6),
        ("CTAR", 1),
    ],
)

industry.add_tile(
    id="coking_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="coking_plant_tile_2",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="coking_plant_tile_3",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

sprite_ground = industry.add_spriteset(
    type="gravel",
)
spriteset_silo = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -91)],
)
spriteset_oven_battery = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -91)],
)
spriteset_oven_battery_larry_car = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -91)],
)
spriteset_pusher_rails_base = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -91)], yextent=8
)
spriteset_pusher_car = industry.add_spriteset(
    sprites=[(10, 234, 64, 64, -31, -32)], yextent=8
)
spriteset_pipe_gantry = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -91)],
)
spriteset_pipe_gantry_house = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -91)],
)
spriteset_coal_handling_front = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -91)],
)
spriteset_coal_handling_rear = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -91)],
)
spriteset_quench_tower = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -91)],
)
spriteset_gas_plant_1 = industry.add_spriteset(
    sprites=[(640, 10, 64, 122, -31, -91)],
)
spriteset_extra_pipe_huts_rear = industry.add_spriteset(
    sprites=[(710, 10, 64, 122, -31, -91)],
)
spriteset_extra_pipe_huts_front = industry.add_spriteset(
    sprites=[(780, 10, 64, 122, -31, -91)],
)
spriteset_tile_tar_tanks = industry.add_spriteset(
    sprites=[(850, 10, 64, 122, -31, -91)],
)
spriteset_pipe_gantry_angled = industry.add_spriteset(
    sprites=[(920, 10, 64, 122, -31, -91)],
)
spriteset_extra_coal_front = industry.add_spriteset(
    sprites=[(990, 10, 64, 122, -31, -91)],
)
spriteset_extra_coal_rear = industry.add_spriteset(
    sprites=[(1060, 10, 64, 122, -31, -91)],
)
spriteset_mostly_empty = industry.add_spriteset(
    sprites=[(1130, 10, 64, 122, -31, -91)],
)
sprite_smoke_big_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=8,
    yoffset=5,
    zoffset=104,
)
sprite_smoke_big_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=7,
    zoffset=76,
)
sprite_smoke_small_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=0,
    yoffset=0,
    zoffset=16,
)
sprite_smoke_small_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=0,
    yoffset=5,
    zoffset=16,
    animation_frame_offset=4,
)

industry.add_spritelayout(
    id="coking_plant_spritelayout_empty",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[],
    add_to_object_num=14,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_oven_battery_pipes_only",
    tile="coking_plant_tile_3",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_oven_battery],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_oven_battery_larry_car",
    tile="coking_plant_tile_3",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_oven_battery_larry_car],
    smoke_sprites=[sprite_smoke_small_1, sprite_smoke_small_2],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_silo",
    tile="coking_plant_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_silo],
    smoke_sprites=[sprite_smoke_big_1],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_pusher_rails_empty",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_pusher_rails_base, spriteset_pipe_gantry],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_pusher_rails_with_car",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[
        spriteset_pusher_rails_base,
        spriteset_pusher_car,
        spriteset_pipe_gantry,
    ],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_pusher_rails_with_house",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_pusher_rails_base, spriteset_pipe_gantry_house],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_quench_tower",
    tile="coking_plant_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_quench_tower],
    smoke_sprites=[sprite_smoke_big_2],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_gas_plant_1",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_gas_plant_1],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_coal_handling_front",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_coal_handling_front],
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_coal_handling_rear",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_coal_handling_rear],
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_extra_coal_front",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_coal_front],
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_extra_coal_rear",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_coal_rear],
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_extra_pipe_huts_front",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_pipe_huts_front],
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_extra_pipe_huts_rear",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_pipe_huts_rear],
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_tar_tanks",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_tile_tar_tanks],
    add_to_object_num=8,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_extra_pipe_gantry_plain",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_pipe_gantry],
    add_to_object_num=9,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_extra_pipe_gantry_fancy",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_pipe_gantry_angled],
    add_to_object_num=10,
)
industry.add_spritelayout(
    id="coking_plant_spritelayout_mostly_empty",
    tile="coking_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_mostly_empty],
    add_to_object_num=13,
)

industry.add_multi_tile_object(
    add_to_object_num=6,
    view_layout=[
        (0, 0, "coking_plant_spritelayout_coal_handling_rear"),
        (1, 0, "coking_plant_spritelayout_coal_handling_front"),
    ],
)
industry.add_multi_tile_object(
    add_to_object_num=12,
    view_layout=[
        (0, 0, "coking_plant_spritelayout_extra_coal_rear"),
        (1, 0, "coking_plant_spritelayout_extra_coal_front"),
    ],
)
industry.add_multi_tile_object(
    add_to_object_num=11,
    view_layout=[
        (0, 0, "coking_plant_spritelayout_extra_pipe_huts_rear"),
        (0, 1, "coking_plant_spritelayout_extra_pipe_huts_front"),
    ],
)

industry.add_industry_outpost_layout(
    id="coking_plant_industry_outpost_layout_1",
    layout=[
        (0, 0, "coking_plant_spritelayout_coal_handling_rear"),
        (0, 1, "coking_plant_spritelayout_gas_plant_1"),
        (1, 0, "coking_plant_spritelayout_coal_handling_front"),
        (1, 1, "coking_plant_spritelayout_tar_tanks"),
    ],
)
industry.add_industry_outpost_layout(
    id="coking_plant_industry_outpost_layout_2",
    layout=[
        (0, 0, "coking_plant_spritelayout_gas_plant_1"),
        (0, 1, "coking_plant_spritelayout_coal_handling_rear"),
        (1, 0, "coking_plant_spritelayout_tar_tanks"),
        (1, 1, "coking_plant_spritelayout_coal_handling_front"),
    ],
)
industry.add_industry_layout(
    id="coking_plant_industry_layout_1",
    layout=[
        (0, 0, "coking_plant_spritelayout_gas_plant_1"),
        (0, 1, "coking_plant_spritelayout_oven_battery_larry_car"),
        (0, 2, "coking_plant_spritelayout_pusher_rails_empty"),
        (1, 0, "coking_plant_spritelayout_mostly_empty"),
        (1, 1, "coking_plant_spritelayout_oven_battery_pipes_only"),
        (1, 2, "coking_plant_spritelayout_pusher_rails_with_house"),
        (2, 0, "coking_plant_spritelayout_tar_tanks"),
        (2, 1, "coking_plant_spritelayout_silo"),
        (2, 2, "coking_plant_spritelayout_pusher_rails_with_car"),
        (3, 0, "coking_plant_spritelayout_coal_handling_rear"),
        (3, 1, "coking_plant_spritelayout_oven_battery_pipes_only"),
        (3, 2, "coking_plant_spritelayout_pusher_rails_with_house"),
        (4, 0, "coking_plant_spritelayout_coal_handling_front"),
        (4, 1, "coking_plant_spritelayout_quench_tower"),
        (4, 2, "coking_plant_spritelayout_pusher_rails_empty"),
    ],
)
industry.add_industry_layout(
    id="coking_plant_industry_layout_2",
    layout=[
        (0, 0, "coking_plant_spritelayout_coal_handling_rear"),
        (0, 1, "coking_plant_spritelayout_oven_battery_pipes_only"),
        (0, 2, "coking_plant_spritelayout_pusher_rails_with_house"),
        (0, 3, "coking_plant_spritelayout_gas_plant_1"),
        (1, 0, "coking_plant_spritelayout_coal_handling_front"),
        (1, 1, "coking_plant_spritelayout_oven_battery_larry_car"),
        (1, 2, "coking_plant_spritelayout_pusher_rails_empty"),
        (1, 3, "coking_plant_spritelayout_tar_tanks"),
        (2, 0, "coking_plant_spritelayout_mostly_empty"),
        (2, 1, "coking_plant_spritelayout_oven_battery_pipes_only"),
        (2, 2, "coking_plant_spritelayout_pusher_rails_with_house"),
        (2, 3, "coking_plant_spritelayout_coal_handling_rear"),
        (3, 0, "coking_plant_spritelayout_quench_tower"),
        (3, 1, "coking_plant_spritelayout_silo"),
        (3, 2, "coking_plant_spritelayout_pusher_rails_with_car"),
        (3, 3, "coking_plant_spritelayout_coal_handling_front"),
    ],
)
industry.add_industry_layout(
    id="coking_plant_industry_layout_3",
    layout=[
        (0, 0, "coking_plant_spritelayout_oven_battery_larry_car"),
        (0, 1, "coking_plant_spritelayout_pusher_rails_with_house"),
        (0, 2, "coking_plant_spritelayout_quench_tower"),
        (0, 3, "coking_plant_spritelayout_gas_plant_1"),
        (0, 4, "coking_plant_spritelayout_tar_tanks"),
        (1, 0, "coking_plant_spritelayout_silo"),
        (1, 1, "coking_plant_spritelayout_pusher_rails_with_car"),
        (1, 2, "coking_plant_spritelayout_oven_battery_larry_car"),
        (1, 3, "coking_plant_spritelayout_pusher_rails_empty"),
        (1, 4, "coking_plant_spritelayout_mostly_empty"),
        (2, 0, "coking_plant_spritelayout_oven_battery_pipes_only"),
        (2, 1, "coking_plant_spritelayout_pusher_rails_empty"),
        (2, 2, "coking_plant_spritelayout_silo"),
        (2, 3, "coking_plant_spritelayout_pusher_rails_with_car"),
        (2, 4, "coking_plant_spritelayout_coal_handling_rear"),
        (3, 0, "coking_plant_spritelayout_quench_tower"),
        (3, 1, "coking_plant_spritelayout_pusher_rails_with_house"),
        (3, 2, "coking_plant_spritelayout_oven_battery_pipes_only"),
        (3, 3, "coking_plant_spritelayout_pusher_rails_empty"),
        (3, 4, "coking_plant_spritelayout_coal_handling_front"),
    ],
)
industry.add_industry_layout(
    id="coking_plant_industry_layout_4",
    layout=[
        (0, 0, "coking_plant_spritelayout_coal_handling_rear"),
        (0, 1, "coking_plant_spritelayout_oven_battery_pipes_only"),
        (0, 2, "coking_plant_spritelayout_pusher_rails_with_house"),
        (0, 3, "coking_plant_spritelayout_oven_battery_pipes_only"),
        (0, 4, "coking_plant_spritelayout_pusher_rails_with_house"),
        (1, 0, "coking_plant_spritelayout_coal_handling_front"),
        (1, 1, "coking_plant_spritelayout_silo"),
        (1, 2, "coking_plant_spritelayout_pusher_rails_empty"),
        (1, 3, "coking_plant_spritelayout_oven_battery_larry_car"),
        (1, 4, "coking_plant_spritelayout_pusher_rails_empty"),
        (2, 0, "coking_plant_spritelayout_gas_plant_1"),
        (2, 1, "coking_plant_spritelayout_oven_battery_larry_car"),
        (2, 2, "coking_plant_spritelayout_pusher_rails_with_car"),
        (2, 3, "coking_plant_spritelayout_silo"),
        (2, 4, "coking_plant_spritelayout_pusher_rails_with_car"),
        (3, 0, "coking_plant_spritelayout_tar_tanks"),
        (3, 1, "coking_plant_spritelayout_quench_tower"),
        (3, 2, "coking_plant_spritelayout_pusher_rails_empty"),
        (3, 3, "coking_plant_spritelayout_quench_tower"),
        (3, 4, "coking_plant_spritelayout_pusher_rails_empty"),
    ],
)
industry.add_industry_layout(
    id="coking_plant_industry_layout_5",
    layout=[
        (0, 0, "coking_plant_spritelayout_coal_handling_rear"),
        (0, 1, "coking_plant_spritelayout_silo"),
        (0, 2, "coking_plant_spritelayout_quench_tower"),
        (0, 3, "coking_plant_spritelayout_silo"),
        (0, 4, "coking_plant_spritelayout_gas_plant_1"),
        (1, 0, "coking_plant_spritelayout_coal_handling_front"),
        (1, 1, "coking_plant_spritelayout_oven_battery_pipes_only"),
        (1, 2, "coking_plant_spritelayout_pusher_rails_with_car"),
        (1, 3, "coking_plant_spritelayout_oven_battery_larry_car"),
        (1, 4, "coking_plant_spritelayout_pusher_rails_with_house"),
        (2, 0, "coking_plant_spritelayout_quench_tower"),
        (2, 1, "coking_plant_spritelayout_oven_battery_larry_car"),
        (2, 2, "coking_plant_spritelayout_pusher_rails_with_house"),
        (2, 3, "coking_plant_spritelayout_oven_battery_pipes_only"),
        (2, 4, "coking_plant_spritelayout_pusher_rails_with_car"),
    ],
)
