from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="water_tower",
    accept_cargo_types=[],
    prod_cargo_types=[],
    prob_in_game="12",
    prob_map_gen="24",
    prod_multiplier="[0, 0]",
    map_colour="168",
    colour_scheme_name="scheme_3_hendrix",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    special_flags=["IND_FLAG_ONLY_IN_TOWNS"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_WATER_TOWER)",
    nearby_station_name="string(STR_STATION_WATER_TOWER)",
    fund_cost_multiplier="15",
    sprites_complete=True,
    animated_tiles_fixed=True,
)


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
    accept_cargo_types=["WATR"],
)

industry.add_tile(
    id="water_tower_tile_1",
    location_checks=TileLocationChecks(require_road_adjacent=True),
)

spriteset_ground = industry.add_spriteset(
    type="pavement",
)
# sphere tank from oil_trading_port spritesheet — reads like a water storage tank
spriteset_tank = industry.add_spriteset(
    sprites=[(510, 10, 64, 84, -31, -60)],
)

industry.add_spritelayout(
    id="water_tower_spritelayout",
    tile="water_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_tank],
)

industry.add_industry_layout(
    id="water_tower_industry_layout",
    layout=[(0, 0, "water_tower_spritelayout")],
)
