from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(
    id="export_terminal",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[],
    prob_in_game="2",
    prob_map_gen="4",
    map_colour="45",
    colour_scheme_name="scheme_9_shania",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=32),
    prospect_chance="0.75",
    name="string(STR_IND_EXPORT_TERMINAL)",
    nearby_station_name="string(STR_STATION_EXPORT_TERMINAL)",
    fund_cost_multiplier="180",
    override_default_construction_states=True,
    primary_production_random_factor_set="medium_range",
    sprites_complete=True,
    animated_tiles_fixed=True,
)


def _reuse_port_graphics(terrain=None, construction_state_num=None):
    if construction_state_num is not None:
        return (
            '"src/graphics/industries/port_construction_'
            + str(construction_state_num + 1)
            + '.png"'
        )
    return '"src/graphics/industries/port.png"'


industry.get_graphics_file_path = _reuse_port_graphics

industry.enable_in_economy(
    "OIL_TOWN",
    accept_cargo_types=["CHEM", "PLAS", "FERT"],
    prod_cargo_types_with_multipliers=[("FOOD", 16)],
)

industry.add_tile(
    id="export_terminal_tile_1",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="export_terminal_tile_2",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)
industry.add_tile(
    id="export_terminal_tile_3",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)

spriteset_crane_rails_nw_se = industry.add_spriteset(
    sprites=[(80, 10, 64, 39, -31, -8)],
    always_draw=True,
)
spriteset_crane_rails_ne_sw = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, -8)],
    always_draw=True,
)
spriteset_warehouse_half_nw_se = industry.add_spriteset(
    sprites=[(440, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_half_ne_sw = industry.add_spriteset(
    sprites=[(510, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_half_se_nw = industry.add_spriteset(
    sprites=[(580, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_half_sw_ne = industry.add_spriteset(
    sprites=[(650, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_full_nw_se = industry.add_spriteset(
    sprites=[(720, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_full_ne_sw = industry.add_spriteset(
    sprites=[(790, 10, 64, 84, -31, -61)],
)
spriteset_shed_half_nw_se = industry.add_spriteset(
    sprites=[(440, 210, 64, 84, -31, -61)],
)
spriteset_shed_half_ne_sw = industry.add_spriteset(
    sprites=[(510, 210, 64, 84, -31, -61)],
)
spriteset_shed_half_se_nw = industry.add_spriteset(
    sprites=[(580, 210, 64, 84, -31, -61)],
)
spriteset_shed_half_sw_ne = industry.add_spriteset(
    sprites=[(650, 210, 64, 84, -31, -61)],
)
spriteset_shed_full_nw_se = industry.add_spriteset(
    sprites=[(720, 210, 64, 84, -31, -61)],
)
spriteset_shed_full_ne_sw = industry.add_spriteset(
    sprites=[(790, 210, 64, 84, -31, -61)],
)
spriteset_tanks_sphere = industry.add_spriteset(
    sprites=[(510, 310, 64, 84, -31, -61)],
)
spriteset_silos_nw_se = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -33, -60)],
)
spriteset_silos_ne_sw = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -31, -61)],
)
spriteset_silos_se_nw = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -33, -60)],
)
spriteset_silos_sw_ne = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -33, -60)],
)
spriteset_bulk_handling_nw_se = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -61)],
)
spriteset_bulk_handling_ne_sw = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -61)],
)
spriteset_bulk_handling_se_nw = industry.add_spriteset(
    sprites=[(580, 110, 64, 84, -31, -61)],
)
spriteset_bulk_handling_sw_ne = industry.add_spriteset(
    sprites=[(650, 110, 64, 84, -31, -61)],
)
spriteset_crawler_crane_ne_sw = industry.add_spriteset(
    sprites=[(580, 310, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_crawler_crane_nw_se = industry.add_spriteset(
    sprites=[(650, 310, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_ne_sw = industry.add_spriteset(
    sprites=[(440, 410, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_nw_se = industry.add_spriteset(
    sprites=[(510, 410, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_se_nw = industry.add_spriteset(
    sprites=[(580, 410, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_sw_ne = industry.add_spriteset(
    sprites=[(650, 410, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_ship_1_ne_sw = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -40, -18)],
)
spriteset_ship_1_nw_se = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -22, -18)],
)
spriteset_ship_1_sw_ne = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -30, -22)],
)
spriteset_ship_1_se_nw = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -20)],
)
spriteset_ship_2_ne_sw = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -40, -18)],
)
spriteset_ship_2_nw_se = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -22, -18)],
)
spriteset_ship_2_sw_ne = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -30, -22)],
)
spriteset_ship_2_se_nw = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -27, -20)],
)

industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_gate_shed_coast_part",
    tile="export_terminal_tile_2",
    config={
        "building_sprites": {
            "se": [spriteset_shed_half_se_nw],
            "sw": [spriteset_shed_half_sw_ne],
            "nw": [spriteset_shed_half_nw_se],
            "ne": [spriteset_shed_half_ne_sw],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_gate_shed_sea_part",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_shed_full_nw_se],
            "sw": [spriteset_shed_full_ne_sw],
            "nw": [spriteset_shed_full_nw_se],
            "ne": [spriteset_shed_full_ne_sw],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_crane_rails_parallel",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_crane_rails_nw_se],
            "sw": [spriteset_crane_rails_ne_sw],
            "nw": [spriteset_crane_rails_nw_se],
            "ne": [spriteset_crane_rails_ne_sw],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_crane_rails_orthogonal",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_crane_rails_ne_sw],
            "sw": [spriteset_crane_rails_nw_se],
            "nw": [spriteset_crane_rails_ne_sw],
            "ne": [spriteset_crane_rails_nw_se],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_crane_parallel",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_crane_rails_nw_se, spriteset_large_crane_nw_se],
            "sw": [spriteset_crane_rails_ne_sw, spriteset_large_crane_sw_ne],
            "nw": [spriteset_crane_rails_nw_se, spriteset_large_crane_se_nw],
            "ne": [spriteset_crane_rails_ne_sw, spriteset_large_crane_ne_sw],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_crane_orthogonal",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_crane_rails_ne_sw, spriteset_large_crane_sw_ne],
            "sw": [spriteset_crane_rails_nw_se, spriteset_large_crane_se_nw],
            "nw": [spriteset_crane_rails_ne_sw, spriteset_large_crane_sw_ne],
            "ne": [spriteset_crane_rails_nw_se, spriteset_large_crane_se_nw],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_crawler_crane_orthogonal",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_crawler_crane_ne_sw],
            "sw": [spriteset_crawler_crane_nw_se],
            "nw": [spriteset_crawler_crane_ne_sw],
            "ne": [spriteset_crawler_crane_nw_se],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_tanks_sphere",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_tanks_sphere],
            "sw": [spriteset_tanks_sphere],
            "nw": [spriteset_tanks_sphere],
            "ne": [spriteset_tanks_sphere],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_silos",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_silos_nw_se],
            "sw": [spriteset_silos_ne_sw],
            "nw": [spriteset_silos_se_nw],
            "ne": [spriteset_silos_sw_ne],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_bulk_handling",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_bulk_handling_nw_se],
            "sw": [spriteset_bulk_handling_ne_sw],
            "nw": [spriteset_bulk_handling_se_nw],
            "ne": [spriteset_bulk_handling_sw_ne],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_warehouse_half_1",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_warehouse_half_nw_se],
            "sw": [spriteset_warehouse_half_ne_sw],
            "nw": [spriteset_warehouse_half_se_nw],
            "ne": [spriteset_warehouse_half_sw_ne],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_warehouse_half_2",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_warehouse_half_se_nw],
            "sw": [spriteset_warehouse_half_sw_ne],
            "nw": [spriteset_warehouse_half_nw_se],
            "ne": [spriteset_warehouse_half_ne_sw],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_warehouse_full",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_warehouse_full_nw_se],
            "sw": [spriteset_warehouse_full_ne_sw],
            "nw": [spriteset_warehouse_full_nw_se],
            "ne": [spriteset_warehouse_full_ne_sw],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_shed_half_1",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_shed_half_nw_se],
            "sw": [spriteset_shed_half_ne_sw],
            "nw": [spriteset_shed_half_se_nw],
            "ne": [spriteset_shed_half_sw_ne],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_shed_half_2",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_shed_half_se_nw],
            "sw": [spriteset_shed_half_sw_ne],
            "nw": [spriteset_shed_half_nw_se],
            "ne": [spriteset_shed_half_ne_sw],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_shed_full",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [spriteset_shed_full_nw_se],
            "sw": [spriteset_shed_full_ne_sw],
            "nw": [spriteset_shed_full_nw_se],
            "ne": [spriteset_shed_full_ne_sw],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_empty",
    tile="export_terminal_tile_1",
    config={
        "building_sprites": {
            "se": [],
            "sw": [],
            "nw": [],
            "ne": [],
        },
        "add_objects": True,
    },
)
industry.add_magic_spritelayout(
    type="water_feature_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_water_ship_1",
    tile="export_terminal_tile_3",
    config={
        "building_sprites": {
            "se": [spriteset_ship_1_nw_se],
            "sw": [spriteset_ship_1_ne_sw],
            "nw": [spriteset_ship_1_se_nw],
            "ne": [spriteset_ship_1_sw_ne],
        },
    },
)
industry.add_magic_spritelayout(
    type="water_feature_auto_orient_to_coast_direction",
    base_id="export_terminal_spritelayout_water_ship_2",
    tile="export_terminal_tile_3",
    config={
        "building_sprites": {
            "se": [spriteset_ship_2_nw_se],
            "sw": [spriteset_ship_2_ne_sw],
            "nw": [spriteset_ship_2_se_nw],
            "ne": [spriteset_ship_2_sw_ne],
        },
        "add_objects": True,
    },
)

industry.add_industry_jetty_layout(
    id="export_terminal_industry_jetty_layout_1",
    layout=[
        (0, 0, "export_terminal_spritelayout_gate_shed_coast_part"),
        (0, 1, "export_terminal_spritelayout_gate_shed_sea_part"),
        (0, 2, "export_terminal_spritelayout_warehouse_full"),
        (0, 3, "export_terminal_spritelayout_warehouse_full"),
        (0, 4, "export_terminal_spritelayout_warehouse_half_1"),
        (0, 5, "spritelayout_null_water"),
        (1, 1, "export_terminal_spritelayout_tanks_sphere"),
        (1, 2, "export_terminal_spritelayout_tanks_sphere"),
        (1, 3, "export_terminal_spritelayout_crane_rails_parallel"),
        (1, 4, "export_terminal_spritelayout_crane_parallel"),
        (1, 5, "spritelayout_null_water"),
        (2, 1, "export_terminal_spritelayout_shed_full"),
        (2, 2, "export_terminal_spritelayout_shed_half_1"),
        (2, 3, "export_terminal_spritelayout_water_ship_1"),
        (2, 4, "spritelayout_null_water"),
        (2, 5, "spritelayout_null_water"),
        (3, 1, "export_terminal_spritelayout_silos"),
        (3, 2, "export_terminal_spritelayout_silos"),
        (3, 3, "export_terminal_spritelayout_bulk_handling"),
        (3, 4, "spritelayout_null_water"),
    ],
)
industry.add_industry_jetty_layout(
    id="export_terminal_industry_jetty_layout_2",
    layout=[
        (0, 1, "export_terminal_spritelayout_warehouse_full"),
        (0, 2, "export_terminal_spritelayout_warehouse_full"),
        (0, 3, "export_terminal_spritelayout_warehouse_half_1"),
        (0, 4, "spritelayout_null_water"),
        (1, 1, "export_terminal_spritelayout_silos"),
        (1, 2, "export_terminal_spritelayout_crane_rails_parallel"),
        (1, 3, "export_terminal_spritelayout_crane_parallel"),
        (2, 1, "export_terminal_spritelayout_silos"),
        (2, 2, "export_terminal_spritelayout_water_ship_2"),
        (2, 3, "spritelayout_null_water"),
        (2, 4, "spritelayout_null_water"),
        (3, 0, "export_terminal_spritelayout_gate_shed_coast_part"),
        (3, 1, "export_terminal_spritelayout_gate_shed_sea_part"),
        (3, 2, "export_terminal_spritelayout_bulk_handling"),
        (3, 3, "export_terminal_spritelayout_tanks_sphere"),
        (3, 4, "export_terminal_spritelayout_tanks_sphere"),
        (3, 5, "spritelayout_null_water"),
        (3, 7, "spritelayout_null_water"),
    ],
)
