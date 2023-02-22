const formatBowSubtype = (subtype: string): string => {
    if (subtype === 'crossbow_light') {
        return 'light crossbow'
    }
    else if (subtype === 'long_bow'){
        return 'longbow'
    }
    else {
        return subtype
    }
}


export default formatBowSubtype
