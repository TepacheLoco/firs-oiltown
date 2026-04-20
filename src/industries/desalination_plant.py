from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="desalination_plant",
    prod_cargo_types_with_multipliers=[],
    prob_in_game="4",
    prob_map_gen="5",
    map_colour="45",
    colour_scheme_name="scheme_9_shania",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=32),
    prospect_chance="0.75",
    name="string(STR_IND_DESALINATION_PLANT)",
    nearby_station_name="string(STR_STATION_DESALINATION_PLANT)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,
    primary_production_random_factor_set="medium_range",
    sprites_complete=True,
    animated_tiles_fixed=True,
)

# reuse oil_trading_port sprite sheets so we don't duplicate PNG assets
def _reuse_oil_trading_port_graphics(terrain=None, construction_state_num=None):
    if construction_state_num is not None:
        return (
            '"src/graphics/industries/oil_trading_port_construction_'
            + str(construction_state_num + 1)
            + '.png"'
        )
    return '"src/graphics/industries/oil_trading_port.png"'


industry.get_graphics_file_path = _reuse_oil_trading_port_graphics

industry.enable_in_economy(
    "OIL_TOWN",
    prod_cargo_types_with_multipliers=[("WATR", 16)],
)

industry.add_tile(
    id="desalination_plant_tile_1",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="desalination_plant_tile_2",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)
industry.add_tile(
    id="desalination_plant_tile_3",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)

spriteset_small_tanks = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_office = industry.add_spriteset(
    sprites=[(440, 10, 64, 84, -31, -43)], zoffset=18
)
spriteset_sphere_tank = industry.add_spriteset(
    sprites=[(510, 10, 64, 84, -31, -60)],
)
spriteset_large_cylinder_tank = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_barge_1_ne_sw = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -22, 0)],
)
spriteset_barge_1_nw_se = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -23, -13)],
)
spriteset_barge_1_sw_ne = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -38, -13)],
)
spriteset_barge_1_se_nw = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -47, -1)],
)
spriteset_barge_2_ne_sw = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -22, 0)],
)
spriteset_barge_2_nw_se = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -23, -13)],
)
spriteset_barge_2_sw_ne = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -38, -13)],
)
spriteset_barge_2_se_nw = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -47, -1)],
)

industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="desalination_plant_spritelayout_coast_office",
    tile="desalination_plant_tile_2",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [spriteset_office],
            "sw": [spriteset_office],
            "nw": [spriteset_office],
            "ne": [spriteset_office],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="desalination_plant_spritelayout_sphere_tank",
    tile="desalination_plant_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [spriteset_sphere_tank],
            "sw": [spriteset_sphere_tank],
            "nw": [spriteset_sphere_tank],
            "ne": [spriteset_sphere_tank],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="desalination_plant_spritelayout_small_tanks",
    tile="desalination_plant_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [spriteset_small_tanks],
            "sw": [spriteset_small_tanks],
            "nw": [spriteset_small_tanks],
            "ne": [spriteset_small_tanks],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="desalination_plant_spritelayout_large_tank",
    tile="desalination_plant_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [spriteset_large_cylinder_tank],
            "sw": [spriteset_large_cylinder_tank],
            "nw": [spriteset_large_cylinder_tank],
            "ne": [spriteset_large_cylinder_tank],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="desalination_plant_spritelayout_water_barge_1",
    tile="desalination_plant_tile_3",
    config={
        "jetty_foundations": False,
        "building_sprites": {
            "se": [spriteset_barge_1_nw_se],
            "sw": [spriteset_barge_1_ne_sw],
            "nw": [spriteset_barge_1_se_nw],
            "ne": [spriteset_barge_1_sw_ne],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="desalination_plant_spritelayout_water_barge_2",
    tile="desalination_plant_tile_3",
    config={
        "jetty_foundations": False,
        "building_sprites": {
            "se": [spriteset_barge_2_nw_se],
            "sw": [spriteset_barge_2_ne_sw],
            "nw": [spriteset_barge_2_se_nw],
            "ne": [spriteset_barge_2_sw_ne],
        },
    },
)

industry.add_industry_jetty_layout(
    id="desalination_plant_industry_layout_1",
    layout=[
        (0, 0, "desalination_plant_spritelayout_coast_office"),
        (0, 1, "desalination_plant_spritelayout_large_tank"),
        (0, 2, "desalination_plant_spritelayout_large_tank"),
        (0, 3, "desalination_plant_spritelayout_small_tanks"),
        (0, 4, "spritelayout_null_water"),
        (1, 2, "desalination_plant_spritelayout_water_barge_2"),
        (1, 3, "spritelayout_null_water"),
        (1, 4, "spritelayout_null_water"),
        (2, 0, "desalination_plant_spritelayout_large_tank"),
        (2, 1, "desalination_plant_spritelayout_large_tank"),
        (2, 2, "desalination_plant_spritelayout_small_tanks"),
        (2, 3, "desalination_plant_spritelayout_small_tanks"),
        (2, 4, "spritelayout_null_water"),
        (2, 5, "spritelayout_null_water"),
        (3, 0, "desalination_plant_spritelayout_large_tank"),
        (3, 1, "desalination_plant_spritelayout_large_tank"),
        (3, 2, "desalination_plant_spritelayout_water_barge_1"),
        (3, 3, "spritelayout_null_water"),
    ],
)

industry.add_industry_jetty_layout(
    id="desalination_plant_industry_layout_2",
    layout=[
        (0, 0, "desalination_plant_spritelayout_large_tank"),
        (0, 1, "desalination_plant_spritelayout_large_tank"),
        (1, 0, "desalination_plant_spritelayout_large_tank"),
        (1, 1, "desalination_plant_spritelayout_large_tank"),
        (1, 2, "desalination_plant_spritelayout_small_tanks"),
        (1, 3, "desalination_plant_spritelayout_small_tanks"),
        (1, 4, "spritelayout_null_water"),
        (1, 5, "spritelayout_null_water"),
        (2, 0, "desalination_plant_spritelayout_coast_office"),
        (2, 2, "desalination_plant_spritelayout_water_barge_1"),
        (2, 3, "spritelayout_null_water"),
        (2, 4, "spritelayout_null_water"),
    ],
)
