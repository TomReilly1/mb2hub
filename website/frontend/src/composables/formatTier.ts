const formatTier = (tier: number): string => {
    switch (tier) {
        case 1:
            return `${tier}st`
        case 2:
            return `${tier}nd`
        case 3:
            return `${tier}rd`
        default:
            return `${tier}th`
    }
}

export default formatTier 
