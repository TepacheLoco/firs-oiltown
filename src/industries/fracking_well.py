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


def _reuse_oil_refinery_graphics(terrain=None, construction_state_num=None):
    return '"src/graphics/industries/oil_refinery.png"'


industry.get_graphics_file_path = _reuse_oil_refinery_graphics

industry.enable_in_economy(
    "OIL_TOWN",
    prob_in_game="6",
    prob_map_gen="8",
    prod_cargo_types_with_output_ratios=[
        ("NGAS", 40),
        ("COND", 8),
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

# pump sprites (built-in OpenTTD; mirrors oil_wells_spritelayout_pump)
sprite_ground_overlay_pump = industry.add_sprite(sprite_number=2173)
sprite_pump = industry.add_sprite(
    sprite_number="2174 + (((animation_frame % 11) < 6) ? (animation_frame % 11) : 10 - (animation_frame % 11))",
    xoffset=1,
    yoffset=2,
    xextent=15,
    yextent=14,
)

# refinery building sprites from oil_refinery.png
spriteset_ground = industry.add_spriteset(type="asphalt")
spriteset_refinery_1 = industry.add_spriteset(sprites=[(10, 10, 64, 66, -31, -35)])
spriteset_refinery_3 = industry.add_spriteset(sprites=[(150, 10, 64, 128, -31, -96)])
spriteset_refinery_4 = industry.add_spriteset(sprites=[(220, 10, 64, 128, -31, -96)])

industry.add_spritelayout(
    id="fracking_well_spritelayout_pump",
    tile="fracking_well_tile_1",
    ground_sprite=None,
    ground_overlay=sprite_ground_overlay_pump,
    building_sprites=[sprite_pump],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fracking_well_spritelayout_refinery_1",
    tile="fracking_well_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_refinery_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fracking_well_spritelayout_refinery_3",
    tile="fracking_well_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_refinery_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fracking_well_spritelayout_refinery_4",
    tile="fracking_well_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_refinery_4],
    fences=["nw", "ne", "se", "sw"],
)

# compact 2x2 layouts — all four tiles adjacent
industry.add_industry_layout(
    id="fracking_well_industry_layout_1",
    layout=[
        (1, 1, "fracking_well_spritelayout_pump"),
        (0, 1, "fracking_well_spritelayout_refinery_1"),
        (1, 0, "fracking_well_spritelayout_refinery_3"),
        (0, 0, "fracking_well_spritelayout_refinery_4"),
    ],
)
industry.add_industry_layout(
    id="fracking_well_industry_layout_2",
    layout=[
        (0, 0, "fracking_well_spritelayout_refinery_4"),
        (0, 1, "fracking_well_spritelayout_pump"),
        (1, 0, "fracking_well_spritelayout_refinery_3"),
        (1, 1, "fracking_well_spritelayout_refinery_1"),
    ],
)
