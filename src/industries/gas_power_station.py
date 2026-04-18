from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="gas_power_station",
    accept_cargo_types=[],
    prod_cargo_types=[],
    prob_in_game="3",
    prob_map_gen="5",
    prod_multiplier="[0, 0]",
    map_colour="168",
    colour_scheme_name="scheme_1_elton",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    town_industry_for_cargoflow=False,
    prospect_chance="0.75",
    name="string(STR_IND_GAS_POWER_STATION)",
    nearby_station_name="string(STR_STATION_POWERHUNGRY)",
    fund_cost_multiplier="15",
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "OIL_TOWN",
    accept_cargo_types=["LNG_"],
)

industry.add_tile(
    id="gas_power_station_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="gas_power_station_tile_2",
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

sprite_ground = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
sprite_1 = industry.add_sprite(sprite_number="2047")
sprite_2 = industry.add_sprite(sprite_number="2050")
sprite_3 = industry.add_sprite(sprite_number="2053")
sprite_4 = industry.add_sprite(sprite_number="2054")
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big", xoffset=3, yoffset=0, zoffset=36
)

industry.add_spritelayout(
    id="gas_power_station_spritelayout_cooling_tower",
    tile="gas_power_station_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[sprite_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_power_station_spritelayout_large_building",
    tile="gas_power_station_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[sprite_2],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_power_station_spritelayout_small_building",
    tile="gas_power_station_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[sprite_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_power_station_spritelayout_substation",
    tile="gas_power_station_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[sprite_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_power_station_spritelayout_empty",
    tile="gas_power_station_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="gas_power_station_industry_layout_1",
    layout=[
        (0, 0, "gas_power_station_spritelayout_cooling_tower"),
        (0, 1, "gas_power_station_spritelayout_small_building"),
        (1, 0, "gas_power_station_spritelayout_cooling_tower"),
        (1, 1, "gas_power_station_spritelayout_large_building"),
        (2, 0, "gas_power_station_spritelayout_cooling_tower"),
        (2, 1, "gas_power_station_spritelayout_large_building"),
        (3, 0, "gas_power_station_spritelayout_substation"),
        (3, 1, "gas_power_station_spritelayout_substation"),
    ],
)
industry.add_industry_layout(
    id="gas_power_station_industry_layout_2",
    layout=[
        (0, 1, "gas_power_station_spritelayout_cooling_tower"),
        (0, 2, "gas_power_station_spritelayout_cooling_tower"),
        (1, 0, "gas_power_station_spritelayout_large_building"),
        (1, 1, "gas_power_station_spritelayout_large_building"),
        (1, 2, "gas_power_station_spritelayout_cooling_tower"),
        (2, 0, "gas_power_station_spritelayout_small_building"),
        (2, 1, "gas_power_station_spritelayout_substation"),
        (2, 2, "gas_power_station_spritelayout_small_building"),
    ],
)
industry.add_industry_layout(
    id="gas_power_station_industry_layout_3",
    layout=[
        (0, 0, "gas_power_station_spritelayout_cooling_tower"),
        (0, 1, "gas_power_station_spritelayout_cooling_tower"),
        (1, 0, "gas_power_station_spritelayout_small_building"),
        (1, 1, "gas_power_station_spritelayout_large_building"),
        (2, 0, "gas_power_station_spritelayout_substation"),
        (2, 1, "gas_power_station_spritelayout_small_building"),
    ],
)
