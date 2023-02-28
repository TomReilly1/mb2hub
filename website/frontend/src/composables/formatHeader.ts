const formatHeader = (concept: string): string => {
    let wordArr: string[] = concept.split('_')
    wordArr.forEach(word => word.slice(0,1).toUpperCase() + word.slice(1,-1))
    const formattedString: string = wordArr.join(' ')
    return formattedString
}

export default formatHeader
