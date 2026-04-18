from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="natural_gas_well",
    prod_cargo_types_with_multipliers=[
        ("NGAS", 20),
    ],
    prob_in_game="5",
    prob_map_gen="6",
    map_colour="168",
    colour_scheme_name="scheme_3_hendrix",
    prospect_chance="0.75",
    name="string(STR_IND_NATURAL_GAS_WELL)",
    fund_cost_multiplier="200",
    nearby_station_name="string(STR_STATION_NATURAL_GAS_WELL)",
    pollution_and_squalor_factor=1,
    provides_snow=True,
    primary_production_random_factor_set="wide_range",
    sprites_complete=False,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "OIL_TOWN",
)

industry.add_tile(
    id="natural_gas_well_tile_1",
    location_checks=TileLocationChecks(disallow_industry_adjacent=True),
    animation_length=20,
    animation_looping=True,
    animation_speed=3,
    special_flags=["INDTILE_FLAG_RANDOM_ANIMATION"],
    random_trigger="natural_gas_well_tile_1_industry_anim_control",
    custom_animation_next_frame="natural_gas_well_tile_1_anim_next_frame",
    custom_animation_control={
        "macro": "oil_wells",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_TILE_LOOP)",
    },
)
industry.add_tile(
    id="natural_gas_well_tile_2",
    location_checks=TileLocationChecks(disallow_industry_adjacent=True),
)

sprite_ground_overlay_pump = industry.add_sprite(sprite_number=2173)
sprite_pump = industry.add_sprite(
    sprite_number="2174 + (((animation_frame % 11) < 6) ? (animation_frame % 11) : 10 - (animation_frame % 11))",
    xoffset=1,
    yoffset=2,
    xextent=15,
    yextent=14,
)
sprite_ground_overlay_building = industry.add_sprite(
    sprite_number="GROUNDTILE_MUD_TRACKS",
)
spriteset_building = industry.add_spriteset(
    sprites=[(10, 10, 64, 38, -31, -9)], xoffset=1, yoffset=2, xextent=15, yextent=14
)

industry.add_spritelayout(
    id="natural_gas_well_spritelayout_pump",
    tile="natural_gas_well_tile_1",
    ground_sprite=None,
    ground_overlay=sprite_ground_overlay_pump,
    building_sprites=[sprite_pump],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="natural_gas_well_spritelayout_building",
    tile="natural_gas_well_tile_2",
    ground_sprite=None,
    ground_overlay=sprite_ground_overlay_building,
    building_sprites=[spriteset_building],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="natural_gas_well_industry_layout_1",
    layout=[
        (0, 0, "natural_gas_well_spritelayout_pump"),
        (0, 7, "natural_gas_well_spritelayout_pump"),
        (1, 4, "natural_gas_well_spritelayout_pump"),
        (2, 1, "natural_gas_well_spritelayout_pump"),
        (3, 5, "natural_gas_well_spritelayout_building"),
        (4, 8, "natural_gas_well_spritelayout_pump"),
        (5, 1, "natural_gas_well_spritelayout_pump"),
        (5, 4, "natural_gas_well_spritelayout_pump"),
    ],
)
industry.add_industry_layout(
    id="natural_gas_well_industry_layout_2",
    layout=[
        (0, 0, "natural_gas_well_spritelayout_pump"),
        (0, 4, "natural_gas_well_spritelayout_pump"),
        (1, 4, "natural_gas_well_spritelayout_pump"),
        (2, 8, "natural_gas_well_spritelayout_pump"),
        (4, 4, "natural_gas_well_spritelayout_building"),
        (4, 8, "natural_gas_well_spritelayout_pump"),
        (5, 2, "natural_gas_well_spritelayout_pump"),
        (6, 2, "natural_gas_well_spritelayout_pump"),
        (6, 4, "natural_gas_well_spritelayout_pump"),
    ],
)
industry.add_industry_layout(
    id="natural_gas_well_industry_layout_3",
    layout=[
        (0, 0, "natural_gas_well_spritelayout_pump"),
        (0, 2, "natural_gas_well_spritelayout_pump"),
        (1, 4, "natural_gas_well_spritelayout_pump"),
        (1, 6, "natural_gas_well_spritelayout_pump"),
        (2, 0, "natural_gas_well_spritelayout_building"),
        (3, 2, "natural_gas_well_spritelayout_pump"),
        (3, 4, "natural_gas_well_spritelayout_pump"),
    ],
)
