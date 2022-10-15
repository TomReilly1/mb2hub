export interface searchObj {
    name: string,
    concept: string,
    id: string,
}

//---Tables---//
export interface armors {
    id: string,
    name: string,
    culture: string,
    weight: number,
    type: string,
    head_armor: number,
    body_armor: number,
    arm_armor: number,
    leg_armor: number,
}

export interface bows {
    id: string
    name: string
    culture: string
    weight: number
    type: string
    subtype:         string
    difficulty      :number
    speed_rating    :number
    missile_speed   :number
    accuracy        :number
    damage          :number
    fire_on_mount   :boolean
    reload_on_mount :boolean
}

export interface castles {
    id: string
    name: string
    owner_id: string
    owner_name: string
    culture: string
    x_position: number
    y_position: number
    prosperity: number
    wall_level: number
    bound_village_1: string
    bound_village_2: string
}

export interface clans {
    id: string
    name: string
    owner: string
    kingdom: string
    culture: string
    tier: number
    is_ruling_clan: boolean
}

export interface cultures {
    id: string
    name: string
    is_main_culture: boolean
    desc_text: string
}

export interface goods {
    id: string
    name: string
    plural: string
    value: number
    weight: number
    is_food: boolean
    morale_bonus: number
}

export interface kingdoms {
    id: string
    name: string
    title: string
    ruler_title: string
    culture: string
    primary_banner_color: string
    secondary_banner_color: string
    label_color: string
    color_1: string
    color_2: string
    alternative_color_1: string
    alternative_color_2: string
    desc_text: string
}

export interface lords {
    id: string
    name: string
    culture: string
    default_group: string
    age: number
    sex: string
}

export interface mounts {
    id: string
    name: string
    culture: string
    subtype: string
    difficulty: number
    is_merchandise: boolean
    maneuver: number
    speed: number
    charge_damage: number
    health: number
}

export interface towns {
    id: string
    name: string
    owner_id: string
    owner_name: string
    culture: string
    x_position: number
    y_position: number
    prosperity: number
    wall_level: number
    bound_village_1: string
    bound_village_2: string
    bound_village_3: string
    bound_village_4: string
    desc_text: string
}

export interface troops {
    id: string
    name: string
    culture: string
    default_group: string
    occupation: string
    level: number
    upgrade_target_1: string
    upgrade_target_2: string
    one_handed: number
    two_handed: number
    polearm: number
    bow: number
    crossbow: number
    throwing: number
    riding: number
    athletics: number
}

export interface villages {
    id: string
    name: string
    culture: string
    village_type: string
    x_position: number
    y_position: number
    hearth: number
    bound_settlement: string
    desc_text: string
}
