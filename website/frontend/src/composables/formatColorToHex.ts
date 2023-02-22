const formatColorToHex = (color: string): string => {
    const hexValue = color.slice(-6)
    return '#' + hexValue
}

export default formatColorToHex
