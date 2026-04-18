from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="fracking_well",
    accept_cargos_with_input_ratios=[("FFLD", 8)],
    prod_cargo_types_with_output_ratios=[],
    prob_in_game="4",
    prob_map_gen="5",
    map_colour="151",
    colour_scheme_name="scheme_3_hendrix",
    name="string(STR_IND_FRACKING_WELL)",
    fund_cost_multiplier="250",
    nearby_station_name="string(STR_STATION_FRACKING_WELL)",
    pollution_and_squalor_factor=2,
    provides_snow=True,
    sprites_complete=True,
    animated_tiles_fixed=True,
)


def _reuse_oil_wells_graphics(terrain=None, construction_state_num=None):
    if terrain == "snow":
        return '"src/graphics/industries/oil_wells_snow.png"'
    return '"src/graphics/industries/oil_wells.png"'


industry.get_graphics_file_path = _reuse_oil_wells_graphics

industry.enable_in_economy(
    "OIL_TOWN",
    prod_cargo_types_with_output_ratios=[
        ("NGAS", 5),
        ("COND", 3),
    ],
)

industry.add_tile(
    id="fracking_well_tile_1",
    location_checks=TileLocationChecks(disallow_industry_adjacent=True),
    animation_length=20,
    animation_looping=True,
    animation_speed=3,
    special_flags=["INDTILE_FLAG_RANDOM_ANIMATION"],
    random_trigger="fracking_well_tile_1_industry_anim_control",
    custom_animation_next_frame="fracking_well_tile_1_anim_next_frame",
    custom_animation_control={
        "macro": "oil_wells",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_TILE_LOOP)",
    },
)
industry.add_tile(
    id="fracking_well_tile_2",
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
    id="fracking_well_spritelayout_pump",
    tile="fracking_well_tile_1",
    ground_sprite=None,
    ground_overlay=sprite_ground_overlay_pump,
    building_sprites=[sprite_pump],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fracking_well_spritelayout_building",
    tile="fracking_well_tile_2",
    ground_sprite=None,
    ground_overlay=sprite_ground_overlay_building,
    building_sprites=[spriteset_building],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="fracking_well_industry_layout_1",
    layout=[
        (0, 0, "fracking_well_spritelayout_pump"),
        (0, 4, "fracking_well_spritelayout_pump"),
        (1, 4, "fracking_well_spritelayout_pump"),
        (2, 8, "fracking_well_spritelayout_pump"),
        (4, 4, "fracking_well_spritelayout_building"),
        (4, 8, "fracking_well_spritelayout_pump"),
        (5, 2, "fracking_well_spritelayout_pump"),
        (6, 2, "fracking_well_spritelayout_pump"),
        (6, 4, "fracking_well_spritelayout_pump"),
    ],
)
industry.add_industry_layout(
    id="fracking_well_industry_layout_2",
    layout=[
        (0, 0, "fracking_well_spritelayout_pump"),
        (0, 2, "fracking_well_spritelayout_pump"),
        (1, 4, "fracking_well_spritelayout_pump"),
        (1, 6, "fracking_well_spritelayout_pump"),
        (2, 0, "fracking_well_spritelayout_building"),
        (3, 2, "fracking_well_spritelayout_pump"),
        (3, 4, "fracking_well_spritelayout_pump"),
    ],
)
