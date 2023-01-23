from reduce.armors import reduce_armors
from reduce.bows import reduce_bows
from reduce.castles import reduce_castles
from reduce.clans import reduce_clans
from reduce.cultures import reduce_cultures
from reduce.goods import reduce_goods
from reduce.kingdoms import reduce_kingdoms
from reduce.lords import reduce_lords
from reduce.mounts import reduce_mounts
from reduce.shields import reduce_shields
from reduce.towns import reduce_towns
from reduce.troops import reduce_troops
from reduce.villages import reduce_villages


def main():
    reduce_cultures()
    reduce_kingdoms()

    reduce_armors()
    reduce_bows()
    reduce_shields()
    
    reduce_lords()
    reduce_clans()

    reduce_villages()
    reduce_towns()
    reduce_castles()
    
    reduce_goods()
    reduce_mounts()
    
    reduce_troops()


if __name__ == "__main__":
    main()
